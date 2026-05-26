from pathlib import Path
import csv
from collections import Counter

HIGH_INPUT = Path("screening/full_text/pubmed_high_priority_include_records.csv")
AUDIT_INPUT = Path("screening/full_text/pubmed_high_priority_false_positive_audit.csv")

CORE_OUTPUT = Path("screening/full_text/pubmed_core_candidate_records.csv")
MANUAL_AUDIT_OUTPUT = Path("screening/full_text/pubmed_core_candidate_manual_audit_records.csv")
REMOVED_OUTPUT = Path("screening/full_text/pubmed_removed_likely_false_positives.csv")
REPORT = Path("screening/full_text/pubmed_core_candidate_report.md")

with HIGH_INPUT.open(newline="", encoding="utf-8-sig") as f:
    high_rows = list(csv.DictReader(f))

with AUDIT_INPUT.open(newline="", encoding="utf-8-sig") as f:
    audit_rows = list(csv.DictReader(f))

likely_false_positive_pmids = {
    r["pmid"] for r in audit_rows
    if r.get("audit_flag") == "Likely false positive"
}

manual_audit_pmids = {
    r["pmid"] for r in audit_rows
    if r.get("audit_flag") == "Needs manual check"
}

core_rows = [
    r for r in high_rows
    if r["pmid"] not in likely_false_positive_pmids
]

manual_audit_rows = [
    r for r in core_rows
    if r["pmid"] in manual_audit_pmids
]

removed_rows = [
    r for r in high_rows
    if r["pmid"] in likely_false_positive_pmids
]

def write_csv(path, rows):
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

write_csv(CORE_OUTPUT, core_rows)
write_csv(MANUAL_AUDIT_OUTPUT, manual_audit_rows)
write_csv(REMOVED_OUTPUT, removed_rows)

core_layer_counts = Counter(r["corneal_layer"] for r in core_rows)
manual_layer_counts = Counter(r["corneal_layer"] for r in manual_audit_rows)
removed_layer_counts = Counter(r["corneal_layer"] for r in removed_rows)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# PubMed Core Candidate Records Report\n\n")

    f.write("## Purpose\n\n")
    f.write("This report creates a cleaner core candidate set from the high-priority Include records. Only records marked as likely false positives are removed automatically. Records marked as needing manual check are retained but separated for audit.\n\n")

    f.write("## Counts\n\n")
    f.write(f"- Original high-priority Include records: {len(high_rows)}\n")
    f.write(f"- Automatically removed likely false positives: {len(removed_rows)}\n")
    f.write(f"- Core candidate records retained: {len(core_rows)}\n")
    f.write(f"- Core records requiring manual audit: {len(manual_audit_rows)}\n\n")

    f.write("## Core Candidate Records by Layer\n\n")
    for k, v in core_layer_counts.most_common():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Manual Audit Records by Layer\n\n")
    for k, v in manual_layer_counts.most_common():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Automatically Removed Records\n\n")
    if removed_rows:
        for r in removed_rows:
            f.write(f"- {r['screening_id']} / PMID {r['pmid']}: {r['title']}\n")
    else:
        f.write("- None\n")

    f.write("\n## Output Files\n\n")
    f.write(f"- Core candidate records: `{CORE_OUTPUT}`\n")
    f.write(f"- Manual audit subset: `{MANUAL_AUDIT_OUTPUT}`\n")
    f.write(f"- Removed likely false positives: `{REMOVED_OUTPUT}`\n")

print("Core candidate list created.")
print(f"Original high-priority Include records: {len(high_rows)}")
print(f"Automatically removed likely false positives: {len(removed_rows)}")
print(f"Core candidate records retained: {len(core_rows)}")
print(f"Core records requiring manual audit: {len(manual_audit_rows)}")
print("Core records by layer:")
for k, v in core_layer_counts.most_common():
    print(f"{k}: {v}")
