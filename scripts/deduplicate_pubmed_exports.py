from pathlib import Path
import csv
import re
from collections import defaultdict

EXPORT_DIR = Path("searches/database_exports/pubmed")
OUT_DIR = Path("data/processed")
REPORT_DIR = Path("reports/searches")

OUT_DIR.mkdir(parents=True, exist_ok=True)
REPORT_DIR.mkdir(parents=True, exist_ok=True)

files = {
    "A3_epithelium_limbus": EXPORT_DIR / "pubmed_A3_epithelium_limbus.txt",
    "B3_stroma": EXPORT_DIR / "pubmed_B3_stroma.txt",
    "C4_endothelium": EXPORT_DIR / "pubmed_C4_endothelium.txt",
    "D3_full_thickness_multilayer": EXPORT_DIR / "pubmed_D3_full_thickness_multilayer.txt",
}

def split_pubmed_records(text):
    chunks = re.split(r"\n(?=PMID- )", text.strip())
    return [c.strip() for c in chunks if c.strip()]

def get_field(record, tag):
    pattern = rf"^{re.escape(tag)}- (.*?)(?=\n[A-Z0-9]{{2,4}}\s*- |\Z)"
    m = re.search(pattern, record, flags=re.M | re.S)
    if not m:
        return ""
    value = m.group(1)
    value = re.sub(r"\n\s{6}", " ", value)
    return " ".join(value.split())

def get_all_fields(record, tag):
    values = []
    for line in record.splitlines():
        if line.startswith(f"{tag}- "):
            values.append(line.split("- ", 1)[1].strip())
    return values

records_by_pmid = {}
sources_by_pmid = defaultdict(list)
raw_counts = {}

for source, path in files.items():
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")

    text = path.read_text(encoding="utf-8", errors="replace")
    records = split_pubmed_records(text)
    raw_counts[source] = len(records)

    for rec in records:
        pmid = get_field(rec, "PMID")
        if not pmid:
            continue

        sources_by_pmid[pmid].append(source)

        if pmid not in records_by_pmid:
            title = get_field(rec, "TI")
            journal = get_field(rec, "JT")
            year = get_field(rec, "DP")[:4]

            doi_values = get_all_fields(rec, "AID")
            doi = ""
            for v in doi_values:
                if "[doi]" in v.lower():
                    doi = v.replace("[doi]", "").strip()
                    break

            records_by_pmid[pmid] = {
                "pmid": pmid,
                "title": title,
                "year": year,
                "journal": journal,
                "doi": doi,
                "sources": "",
                "source_count": 0,
            }

for pmid, sources in sources_by_pmid.items():
    records_by_pmid[pmid]["sources"] = ";".join(sorted(set(sources)))
    records_by_pmid[pmid]["source_count"] = len(sorted(set(sources)))

unique_records = sorted(
    records_by_pmid.values(),
    key=lambda r: int(r["pmid"]) if r["pmid"].isdigit() else r["pmid"]
)

csv_path = OUT_DIR / "pubmed_unique_records.csv"
with csv_path.open("w", newline="", encoding="utf-8") as f:
    fieldnames = ["pmid", "title", "year", "journal", "doi", "sources", "source_count"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(unique_records)

duplicate_pmids = {
    pmid: srcs for pmid, srcs in sources_by_pmid.items()
    if len(set(srcs)) > 1
}

report_path = REPORT_DIR / "pubmed_deduplication_report.md"
with report_path.open("w", encoding="utf-8") as f:
    f.write("# PubMed Deduplication Report\n\n")

    f.write("## Raw Record Counts\n\n")
    total_raw = 0
    for source, count in raw_counts.items():
        total_raw += count
        f.write(f"- {source}: {count}\n")

    f.write(f"\n## Total Raw Records\n\n{total_raw}\n")
    f.write(f"\n## Unique PMID Records\n\n{len(unique_records)}\n")
    f.write(f"\n## Duplicate PMID Records Across Searches\n\n{len(duplicate_pmids)}\n")

    f.write("\n## Duplicate PMID List\n\n")
    if duplicate_pmids:
        f.write("| PMID | Sources |\n")
        f.write("|---|---|\n")
        for pmid, srcs in sorted(
            duplicate_pmids.items(),
            key=lambda x: int(x[0]) if x[0].isdigit() else x[0]
        ):
            f.write(f"| {pmid} | {'; '.join(sorted(set(srcs)))} |\n")
    else:
        f.write("No duplicates detected across searches.\n")

print("Deduplication complete.")
print(f"Raw total: {sum(raw_counts.values())}")
print(f"Unique records: {len(unique_records)}")
print(f"Duplicate PMIDs across searches: {len(duplicate_pmids)}")
print(f"CSV written to: {csv_path}")
print(f"Report written to: {report_path}")
