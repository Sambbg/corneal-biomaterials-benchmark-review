from pathlib import Path
import csv
from collections import Counter

INPUT = Path("screening/full_text/pubmed_balanced_first_retrieval_batch.csv")
OUTPUT = Path("screening/full_text/pubmed_first_batch_retrieval_tracker.csv")
REPORT = Path("screening/full_text/pubmed_first_batch_retrieval_tracker_report.md")

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

fields_to_keep = [
    "screening_id",
    "pmid",
    "title",
    "year",
    "journal",
    "doi",
    "corneal_layer",
    "strict_retrieval_score",
    "strict_retrieval_reason",
    "strict_final_status"
]

tracker_fields = fields_to_keep + [
    "full_text_status",
    "pdf_available",
    "source_checked",
    "pdf_filename",
    "retrieval_date",
    "retrieval_notes",
    "extraction_ready",
    "reason_not_extraction_ready"
]

out_rows = []

for r in rows:
    out = {field: "" for field in tracker_fields}

    for field in fields_to_keep:
        out[field] = r.get(field, "")

    out["full_text_status"] = "not_checked"
    out["pdf_available"] = "not_checked"
    out["source_checked"] = ""
    out["pdf_filename"] = ""
    out["retrieval_date"] = ""
    out["retrieval_notes"] = ""
    out["extraction_ready"] = "not_checked"
    out["reason_not_extraction_ready"] = ""

    out_rows.append(out)

with OUTPUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=tracker_fields)
    writer.writeheader()
    writer.writerows(out_rows)

layer_counts = Counter(r.get("corneal_layer", "") for r in out_rows)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# PubMed First Batch Retrieval Tracker Report\n\n")

    f.write("## Purpose\n\n")
    f.write("This tracker is for manually recording full-text retrieval status for the balanced first PubMed retrieval batch.\n\n")

    f.write("## Counts\n\n")
    f.write(f"- First-batch records in tracker: {len(out_rows)}\n\n")

    f.write("## Records by Layer\n\n")
    for k, v in layer_counts.most_common():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Recommended Status Labels\n\n")
    f.write("### full_text_status\n\n")
    f.write("- not_checked\n")
    f.write("- retrieved\n")
    f.write("- open_access_available\n")
    f.write("- paywalled\n")
    f.write("- unavailable\n\n")

    f.write("### pdf_available\n\n")
    f.write("- not_checked\n")
    f.write("- yes\n")
    f.write("- no\n\n")

    f.write("### extraction_ready\n\n")
    f.write("- not_checked\n")
    f.write("- yes\n")
    f.write("- no\n")
    f.write("- maybe\n\n")

    f.write("## Output File\n\n")
    f.write(f"- `{OUTPUT}`\n")

print("First batch retrieval tracker created.")
print(f"First-batch records in tracker: {len(out_rows)}")
print("Records by layer:")
for k, v in layer_counts.most_common():
    print(f"{k}: {v}")
