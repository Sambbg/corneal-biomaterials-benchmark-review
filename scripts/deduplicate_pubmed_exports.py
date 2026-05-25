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

def parse_pubmed_record(record):
    """
    Parses PubMed text format.

    PubMed lines look like:
    PMID- 123456
    TI  - Article title
          continued title line
    JT  - Journal Title

    Continuation lines begin with spaces.
    """
    fields = defaultdict(list)
    current_tag = None

    for line in record.splitlines():
        m = re.match(r"^([A-Z0-9]{2,4})\s*-\s*(.*)$", line)
        if m:
            current_tag = m.group(1)
            fields[current_tag].append(m.group(2).strip())
        elif current_tag and line.startswith(" "):
            continuation = line.strip()
            if continuation and fields[current_tag]:
                fields[current_tag][-1] += " " + continuation

    cleaned = {}
    for tag, values in fields.items():
        cleaned[tag] = [" ".join(v.split()) for v in values]

    return cleaned

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
        fields = parse_pubmed_record(rec)

        pmid = fields.get("PMID", [""])[0]
        if not pmid:
            continue

        sources_by_pmid[pmid].append(source)

        if pmid not in records_by_pmid:
            title = fields.get("TI", [""])[0]
            journal = fields.get("JT", [""])[0]
            dp = fields.get("DP", [""])[0]
            year_match = re.search(r"\b(19|20)\d{2}\b", dp)
            year = year_match.group(0) if year_match else ""

            doi = ""
            for aid in fields.get("AID", []):
                if "[doi]" in aid.lower():
                    doi = aid.replace("[doi]", "").strip()
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

    missing_title = sum(1 for r in unique_records if not r["title"])
    missing_year = sum(1 for r in unique_records if not r["year"])
    missing_journal = sum(1 for r in unique_records if not r["journal"])

    f.write("\n## Metadata Completeness Check\n\n")
    f.write(f"- Records missing title: {missing_title}\n")
    f.write(f"- Records missing year: {missing_year}\n")
    f.write(f"- Records missing journal: {missing_journal}\n")

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

print("\nMetadata check:")
print(f"Missing titles: {sum(1 for r in unique_records if not r['title'])}")
print(f"Missing years: {sum(1 for r in unique_records if not r['year'])}")
print(f"Missing journals: {sum(1 for r in unique_records if not r['journal'])}")
