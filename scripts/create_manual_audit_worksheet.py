from pathlib import Path
import csv

INPUT = Path("screening/full_text/pubmed_core_candidate_manual_audit_records.csv")
OUTPUT = Path("screening/full_text/pubmed_manual_audit_worksheet.csv")
REPORT = Path("screening/full_text/pubmed_manual_audit_worksheet_report.md")

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

audit_fieldnames = list(rows[0].keys()) + [
    "manual_decision",
    "manual_reason",
    "final_layer",
    "final_priority",
    "full_text_needed"
]

out_rows = []
for r in rows:
    out = dict(r)
    out["manual_decision"] = ""
    out["manual_reason"] = ""
    out["final_layer"] = r.get("corneal_layer", "")
    out["final_priority"] = r.get("priority_level", "")
    out["full_text_needed"] = ""
    out_rows.append(out)

with OUTPUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=audit_fieldnames)
    writer.writeheader()
    writer.writerows(out_rows)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# PubMed Manual Audit Worksheet Report\n\n")
    f.write("## Purpose\n\n")
    f.write("This worksheet is for manually auditing high-priority records that were flagged as needing review before full-text retrieval.\n\n")

    f.write("## Records Requiring Manual Audit\n\n")
    f.write(f"- Total records in worksheet: {len(out_rows)}\n\n")

    f.write("## Manual Decision Labels\n\n")
    f.write("- Keep core\n")
    f.write("- Downgrade to medium\n")
    f.write("- Exclude\n")
    f.write("- Uncertain\n\n")

    f.write("## Full Text Needed Labels\n\n")
    f.write("- yes\n")
    f.write("- no\n")
    f.write("- maybe\n\n")

    f.write("## Output File\n\n")
    f.write(f"- `{OUTPUT}`\n")

print("Manual audit worksheet created.")
print(f"Records requiring manual audit: {len(out_rows)}")
print(f"Output: {OUTPUT}")
