from pathlib import Path
import csv
from collections import Counter

MASTER = Path("screening/title_abstract/pubmed_title_abstract_screening.csv")
CORRECTED = Path("screening/title_abstract/working/pubmed_screening_batch_01_CORRECTED.csv")
BACKUP = Path("screening/title_abstract/pubmed_title_abstract_screening_before_batch01_merge.csv")
REPORT = Path("screening/title_abstract/pubmed_batch01_merge_report.md")

# Backup master before merge
BACKUP.write_text(MASTER.read_text(encoding="utf-8"), encoding="utf-8")

with MASTER.open(newline="", encoding="utf-8-sig") as f:
    master_reader = csv.DictReader(f)
    master_rows = list(master_reader)
    fieldnames = master_reader.fieldnames

with CORRECTED.open(newline="", encoding="utf-8-sig") as f:
    corrected_rows = list(csv.DictReader(f))

corrected_by_id = {r["screening_id"]: r for r in corrected_rows}

updated = 0
for row in master_rows:
    sid = row["screening_id"]
    if sid in corrected_by_id:
        corrected = corrected_by_id[sid]
        for col in [
            "decision",
            "exclusion_reason",
            "corneal_layer",
            "priority_level",
            "screening_notes"
        ]:
            row[col] = corrected[col]
        updated += 1

with MASTER.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(master_rows)

batch_rows = [r for r in master_rows if r["screening_id"] in corrected_by_id]
batch_decisions = Counter(r["decision"] for r in batch_rows)
overall_decisions = Counter(r["decision"] if r["decision"] else "Unscreened" for r in master_rows)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# PubMed Batch 01 Merge Report\n\n")
    f.write("## Merge Summary\n\n")
    f.write(f"- Corrected Batch 01 records merged: {updated}\n")
    f.write(f"- Master screening file: {MASTER}\n")
    f.write(f"- Backup created: {BACKUP}\n\n")

    f.write("## Batch 01 Decision Counts After Merge\n\n")
    for k, v in batch_decisions.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Overall Master Screening Status\n\n")
    for k, v in overall_decisions.items():
        f.write(f"- {k}: {v}\n")

print("Batch 01 merge complete.")
print(f"Updated records: {updated}")
print("Batch 01 decisions:")
for k, v in batch_decisions.items():
    print(f"{k}: {v}")
print("Overall master status:")
for k, v in overall_decisions.items():
    print(f"{k}: {v}")
