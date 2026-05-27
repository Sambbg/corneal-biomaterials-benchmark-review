from pathlib import Path
import csv
from collections import Counter

SKIM = Path("screening/full_text/pubmed_first10_retrieved_skim_checklist.csv")
MASTER_EXTRACTION = Path("extraction/pubmed_balanced_core_data_extraction_template.csv")

OUTPUT = Path("extraction/pubmed_first10_pilot_extraction.csv")
REPORT = Path("extraction/pubmed_first10_pilot_extraction_report.md")

with SKIM.open(newline="", encoding="utf-8-sig") as f:
    skim_rows = list(csv.DictReader(f))

ready_pmids = {
    r["pmid"] for r in skim_rows
    if r.get("include_for_extraction") == "yes"
}

with MASTER_EXTRACTION.open(newline="", encoding="utf-8-sig") as f:
    extraction_rows = list(csv.DictReader(f))

pilot_rows = []

for r in extraction_rows:
    if r.get("pmid") in ready_pmids:
        out = dict(r)
        out["pilot_extraction_status"] = "not_started"
        out["pilot_extraction_notes"] = ""
        pilot_rows.append(out)

if not pilot_rows:
    raise SystemExit("No pilot extraction rows found. Check PMID matching.")

fieldnames = list(pilot_rows[0].keys())

with OUTPUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(pilot_rows)

layer_counts = Counter(r.get("target_layer_final", r.get("corneal_layer", "")) for r in pilot_rows)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# First 10 PubMed Pilot Extraction Report\n\n")
    f.write("## Purpose\n\n")
    f.write("This file prepares the 6 retrieved and skim-confirmed papers from the first 10-paper retrieval test for pilot data extraction.\n\n")

    f.write("## Counts\n\n")
    f.write(f"- Papers ready for pilot extraction: {len(pilot_rows)}\n\n")

    f.write("## Layer Counts\n\n")
    for k, v in layer_counts.most_common():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Papers Included\n\n")
    for r in pilot_rows:
        f.write(f"- {r['screening_id']} / PMID {r['pmid']}: {r['title']}\n")

    f.write("\n## Output File\n\n")
    f.write(f"- `{OUTPUT}`\n")

print("Pilot extraction file created.")
print(f"Papers ready for pilot extraction: {len(pilot_rows)}")
for r in pilot_rows:
    print(f"{r['screening_id']} / PMID {r['pmid']} - {r['title']}")
