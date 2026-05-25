from pathlib import Path
import csv

INPUT = Path("screening/title_abstract/working/pubmed_screening_batch_01_WORKING.csv")
OUTPUT = Path("screening/title_abstract/working/pubmed_screening_batch_01_CALIBRATION_10.csv")
REPORT = Path("screening/title_abstract/working/pubmed_screening_batch_01_calibration_notes.md")

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fieldnames = reader.fieldnames

calibration_rows = rows[:10]

with OUTPUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(calibration_rows)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# PubMed Batch 01 Calibration Notes\n\n")
    f.write("## Purpose\n\n")
    f.write("This file contains the first 10 records from PubMed Batch 01. It is used to calibrate inclusion/exclusion decisions before screening the full batch.\n\n")
    f.write("## Calibration Rule\n\n")
    f.write("Do not proceed to the full 100-record batch until these 10 records have been reviewed and the screening threshold is consistent.\n\n")
    f.write("## Records\n\n")
    for r in calibration_rows:
        f.write(f"### {r['screening_id']} / PMID {r['pmid']}\n\n")
        f.write(f"**Title:** {r['title']}\n\n")
        f.write(f"**Sources:** {r['sources']}\n\n")
        f.write("**Decision:** Pending\n\n")
        f.write("**Rationale:** Pending\n\n")

print(f"Created {OUTPUT}")
print(f"Created {REPORT}")
print(f"Records: {len(calibration_rows)}")
