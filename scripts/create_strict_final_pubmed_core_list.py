from pathlib import Path
import csv
from collections import Counter

CORE_INPUT = Path("screening/full_text/pubmed_provisional_final_core_records.csv")
STRICT_INPUT = Path("screening/full_text/pubmed_unresolved_manual_check_review_strict.csv")

FINAL_OUTPUT = Path("screening/full_text/pubmed_strict_final_core_records.csv")
BACKGROUND_OUTPUT = Path("screening/full_text/pubmed_background_context_records.csv")
EXCLUDED_OUTPUT = Path("screening/full_text/pubmed_strict_excluded_from_core_records.csv")
REPORT = Path("screening/full_text/pubmed_strict_final_core_report.md")

with CORE_INPUT.open(newline="", encoding="utf-8-sig") as f:
    core_rows = list(csv.DictReader(f))

with STRICT_INPUT.open(newline="", encoding="utf-8-sig") as f:
    strict_rows = list(csv.DictReader(f))

strict_by_pmid = {r["pmid"]: r for r in strict_rows}

background_pmids = {
    r["pmid"] for r in strict_rows
    if r.get("strict_manual_decision") == "Downgrade to background"
}

excluded_pmids = {
    r["pmid"] for r in strict_rows
    if r.get("strict_manual_decision") == "Exclude from core"
}

final_rows = []
background_rows = []
excluded_rows = []

for r in core_rows:
    pmid = r["pmid"]
    out = dict(r)

    if pmid in background_pmids:
        out["strict_final_status"] = "Background/context only"
        background_rows.append(out)
        continue

    if pmid in excluded_pmids:
        out["strict_final_status"] = "Excluded from core"
        excluded_rows.append(out)
        continue

    if pmid in strict_by_pmid:
        decision = strict_by_pmid[pmid].get("strict_manual_decision", "")
        out["strict_final_status"] = decision
    else:
        out["strict_final_status"] = "Final core"

    final_rows.append(out)

def write_csv(path, rows):
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

write_csv(FINAL_OUTPUT, final_rows)
write_csv(BACKGROUND_OUTPUT, background_rows)
write_csv(EXCLUDED_OUTPUT, excluded_rows)

final_layer_counts = Counter(r["corneal_layer"] for r in final_rows)
status_counts = Counter(r["strict_final_status"] for r in final_rows)
background_layer_counts = Counter(r["corneal_layer"] for r in background_rows)
excluded_layer_counts = Counter(r["corneal_layer"] for r in excluded_rows)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# Strict Final PubMed Core Records Report\n\n")

    f.write("## Purpose\n\n")
    f.write("This report applies strict manual override decisions to the provisional final PubMed core list.\n\n")

    f.write("## Counts\n\n")
    f.write(f"- Provisional final core records before strict filtering: {len(core_rows)}\n")
    f.write(f"- Records downgraded to background/context only: {len(background_rows)}\n")
    f.write(f"- Records excluded from core: {len(excluded_rows)}\n")
    f.write(f"- Strict final PubMed core records retained: {len(final_rows)}\n\n")

    f.write("## Strict Final Status Counts\n\n")
    for k, v in status_counts.most_common():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Strict Final Core Records by Layer\n\n")
    for k, v in final_layer_counts.most_common():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Background/Context Records by Layer\n\n")
    if background_rows:
        for k, v in background_layer_counts.most_common():
            f.write(f"- {k}: {v}\n")
    else:
        f.write("- None\n")

    f.write("\n## Excluded Records by Layer\n\n")
    if excluded_rows:
        for k, v in excluded_layer_counts.most_common():
            f.write(f"- {k}: {v}\n")
    else:
        f.write("- None\n")

    f.write("\n## Background/Context Records\n\n")
    if background_rows:
        for r in background_rows:
            f.write(f"- {r['screening_id']} / PMID {r['pmid']}: {r['title']}\n")
    else:
        f.write("- None\n")

    f.write("\n## Excluded Records\n\n")
    if excluded_rows:
        for r in excluded_rows:
            f.write(f"- {r['screening_id']} / PMID {r['pmid']}: {r['title']}\n")
    else:
        f.write("- None\n")

    f.write("\n## Output Files\n\n")
    f.write(f"- Strict final core records: `{FINAL_OUTPUT}`\n")
    f.write(f"- Background/context records: `{BACKGROUND_OUTPUT}`\n")
    f.write(f"- Excluded records: `{EXCLUDED_OUTPUT}`\n")

print("Strict final PubMed core list created.")
print(f"Provisional final core before strict filtering: {len(core_rows)}")
print(f"Downgraded to background/context only: {len(background_rows)}")
print(f"Excluded from core: {len(excluded_rows)}")
print(f"Strict final PubMed core retained: {len(final_rows)}")
print("Final core by layer:")
for k, v in final_layer_counts.most_common():
    print(f"{k}: {v}")
