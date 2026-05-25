from pathlib import Path
import csv
import math

INPUT = Path("screening/title_abstract/pubmed_title_abstract_screening.csv")
OUT_DIR = Path("screening/title_abstract/batches")
REPORT = Path("screening/title_abstract/batch_creation_report.md")

BATCH_SIZE = 100

OUT_DIR.mkdir(parents=True, exist_ok=True)

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    records = list(reader)
    fieldnames = reader.fieldnames

total = len(records)
num_batches = math.ceil(total / BATCH_SIZE)

batch_files = []

for batch_num in range(1, num_batches + 1):
    start = (batch_num - 1) * BATCH_SIZE
    end = start + BATCH_SIZE
    batch_records = records[start:end]

    batch_file = OUT_DIR / f"pubmed_screening_batch_{batch_num:02d}.csv"
    batch_files.append((batch_file, len(batch_records), batch_records[0]["screening_id"], batch_records[-1]["screening_id"]))

    with batch_file.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(batch_records)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# PubMed Title/Abstract Screening Batch Creation Report\n\n")
    f.write(f"Total records: {total}\n\n")
    f.write(f"Batch size: {BATCH_SIZE}\n\n")
    f.write(f"Number of batches: {num_batches}\n\n")
    f.write("| Batch file | Records | Screening ID range |\n")
    f.write("|---|---:|---|\n")
    for batch_file, count, first_id, last_id in batch_files:
        f.write(f"| {batch_file} | {count} | {first_id} to {last_id} |\n")

print(f"Created {num_batches} batches from {total} records.")
print(f"Report written to {REPORT}")
