from pathlib import Path
import csv
from collections import Counter

CORE_INPUT = Path("screening/full_text/pubmed_core_candidate_records.csv")
PREFILL_INPUT = Path("screening/full_text/pubmed_manual_audit_worksheet_prefilled.csv")

FINAL_OUTPUT = Path("screening/full_text/pubmed_provisional_final_core_records.csv")
UNRESOLVED_OUTPUT = Path("screening/full_text/pubmed_unresolved_manual_check_records.csv")
REMOVED_OUTPUT = Path("screening/full_text/pubmed_manual_audit_removed_records.csv")
REPORT = Path("screening/full_text/pubmed_provisional_final_core_report.md")

with CORE_INPUT.open(newline="", encoding="utf-8-sig") as f:
    core_rows = list(csv.DictReader(f))

with PREFILL_INPUT.open(newline="", encoding="utf-8-sig") as f:
    prefill_rows = list(csv.DictReader(f))

prefill_by_pmid = {r["pmid"]: r for r in prefill_rows}

removed_pmids = {
    r["pmid"] for r in prefill_rows
    if r.get("manual_decision") == "Downgrade or exclude"
}

unresolved_pmids = {
    r["pmid"] for r in prefill_rows
    if r.get("manual_decision") == "Manual check"
}

final_rows = []
unresolved_rows = []
removed_rows = []

for r in core_rows:
    out = dict(r)

    if r["pmid"] in removed_pmids:
        out["final_core_status"] = "Removed after manual audit prefill"
        removed_rows.append(out)
        continue

    if r["pmid"] in unresolved_pmids:
        out["final_core_status"] = "Provisional core - unresolved manual check"
        unresolved_rows.append(out)
    else:
        out["final_core_status"] = "Provisional core"

    final_rows.append(out)

def write_csv(path, rows):
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

write_csv(FINAL_OUTPUT, final_rows)
write_csv(UNRESOLVED_OUTPUT, unresolved_rows)
write_csv(REMOVED_OUTPUT, removed_rows)

final_layer_counts = Counter(r["corneal_layer"] for r in final_rows)
unresolved_layer_counts = Counter(r["corneal_layer"] for r in unresolved_rows)
status_counts = Counter(r["final_core_status"] for r in final_rows)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# PubMed Provisional Final Core Records Report\n\n")

    f.write("## Purpose\n\n")
    f.write("This report creates the provisional final PubMed core record list for full-text retrieval and evidence extraction. Records marked as unresolved manual check are retained provisionally but require confirmation before final manuscript inclusion.\n\n")

    f.write("## Counts\n\n")
    f.write(f"- Core candidate records before manual-audit filtering: {len(core_rows)}\n")
    f.write(f"- Records removed after audit prefill: {len(removed_rows)}\n")
    f.write(f"- Provisional final core records retained: {len(final_rows)}\n")
    f.write(f"- Unresolved manual-check records retained provisionally: {len(unresolved_rows)}\n\n")

    f.write("## Final Core Status Counts\n\n")
    for k, v in status_counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Provisional Final Core Records by Layer\n\n")
    for k, v in final_layer_counts.most_common():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Unresolved Manual-Check Records by Layer\n\n")
    for k, v in unresolved_layer_counts.most_common():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Removed Records\n\n")
    if removed_rows:
        for r in removed_rows:
            f.write(f"- {r['screening_id']} / PMID {r['pmid']}: {r['title']}\n")
    else:
        f.write("- None\n")

    f.write("\n## Output Files\n\n")
    f.write(f"- Provisional final core records: `{FINAL_OUTPUT}`\n")
    f.write(f"- Unresolved manual-check records: `{UNRESOLVED_OUTPUT}`\n")
    f.write(f"- Removed records: `{REMOVED_OUTPUT}`\n")

print("Provisional final core list created.")
print(f"Core candidate records before manual-audit filtering: {len(core_rows)}")
print(f"Records removed after audit prefill: {len(removed_rows)}")
print(f"Provisional final core records retained: {len(final_rows)}")
print(f"Unresolved manual-check records retained provisionally: {len(unresolved_rows)}")
print("Final core by layer:")
for k, v in final_layer_counts.most_common():
    print(f"{k}: {v}")
