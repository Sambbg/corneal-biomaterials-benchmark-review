from pathlib import Path
import csv
import argparse
from collections import Counter

parser = argparse.ArgumentParser(description="Merge corrected PubMed batch screening decisions into the master screening file.")
parser.add_argument("--batch", type=int, required=True, help="Batch number, e.g. 3 for batch 03")
args = parser.parse_args()

batch = args.batch
batch_id = f"{batch:02d}"

MASTER = Path("screening/title_abstract/pubmed_title_abstract_screening.csv")
CORRECTED = Path(f"screening/title_abstract/working/pubmed_screening_batch_{batch_id}_CORRECTED.csv")
BACKUP = Path(f"screening/title_abstract/pubmed_title_abstract_screening_before_batch{batch_id}_merge.csv")
REPORT = Path(f"screening/title_abstract/pubmed_batch{batch_id}_merge_report.md")

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
    f.write(f"# PubMed Batch {batch_id} Merge Report\n\n")
    f.write("## Merge Summary\n\n")
    f.write(f"- Corrected Batch {batch_id} records merged: {updated}\n")
    f.write(f"- Master screening file: {MASTER}\n")
    f.write(f"- Backup created: {BACKUP}\n\n")

    f.write(f"## Batch {batch_id} Decision Counts After Merge\n\n")
    for k, v in batch_decisions.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Overall Master Screening Status\n\n")
    for k, v in overall_decisions.items():
        f.write(f"- {k}: {v}\n")

print(f"Batch {batch_id} merge complete.")
print(f"Updated records: {updated}")
print(f"Batch {batch_id} decisions:")
for k, v in batch_decisions.items():
    print(f"{k}: {v}")
print("Overall master status:")
for k, v in overall_decisions.items():
    print(f"{k}: {v}")
