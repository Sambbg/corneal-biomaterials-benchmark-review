from pathlib import Path
import csv
from collections import Counter

INPUT = Path("screening/full_text/pubmed_balanced_final_core_records.csv")
OUTPUT = Path("screening/full_text/pubmed_balanced_full_text_retrieval_tracker.csv")
REPORT = Path("screening/full_text/pubmed_balanced_full_text_retrieval_tracker_report.md")

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

tracker_fields = list(rows[0].keys()) + [
    "full_text_status",
    "pdf_available",
    "source_checked",
    "retrieval_date",
    "retrieval_notes",
    "extraction_ready",
    "reason_not_extraction_ready"
]

out_rows = []

for r in rows:
    out = dict(r)
    out["full_text_status"] = ""
    out["pdf_available"] = ""
    out["source_checked"] = ""
    out["retrieval_date"] = ""
    out["retrieval_notes"] = ""
    out["extraction_ready"] = ""
    out["reason_not_extraction_ready"] = ""
    out_rows.append(out)

with OUTPUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=tracker_fields)
    writer.writeheader()
    writer.writerows(out_rows)

layer_counts = Counter(r.get("corneal_layer", "") for r in out_rows)
status_counts = Counter(r.get("strict_final_status", "") for r in out_rows)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# Balanced PubMed Full-Text Retrieval Tracker Report\n\n")

    f.write("## Purpose\n\n")
    f.write("This tracker records full-text retrieval status for the balanced final PubMed core records before data extraction.\n\n")

    f.write("## Counts\n\n")
    f.write(f"- Records in balanced full-text retrieval tracker: {len(out_rows)}\n\n")

    f.write("## Records by Layer\n\n")
    for k, v in layer_counts.most_common():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Core Status Counts\n\n")
    for k, v in status_counts.most_common():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Retrieval Status Labels\n\n")
    f.write("- retrieved\n")
    f.write("- open_access_available\n")
    f.write("- paywalled\n")
    f.write("- unavailable\n")
    f.write("- not_checked\n\n")

    f.write("## Extraction Ready Labels\n\n")
    f.write("- yes\n")
    f.write("- no\n")
    f.write("- maybe\n\n")

    f.write("## Output File\n\n")
    f.write(f"- `{OUTPUT}`\n")

print("Balanced full-text retrieval tracker created.")
print(f"Records in tracker: {len(out_rows)}")
print("Records by layer:")
for k, v in layer_counts.most_common():
    print(f"{k}: {v}")
