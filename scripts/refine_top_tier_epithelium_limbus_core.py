from pathlib import Path
import csv
from collections import Counter

INPUT = Path("screening/full_text/pubmed_top_tier_epithelium_limbus_core_additions.csv")
OUTPUT = Path("screening/full_text/pubmed_refined_top_tier_epithelium_limbus_core_additions.csv")
DEMOTED_OUTPUT = Path("screening/full_text/pubmed_demoted_top_tier_epithelium_limbus_records.csv")
REPORT = Path("screening/full_text/pubmed_refined_top_tier_epithelium_limbus_core_report.md")

DEMOTE_PMIDS = {
    "32578462": "Storage-condition study; useful methods/context, but not core biomaterial benchmarking.",
    "34572321": "Cell derivation/characterization study; weak biomaterial reconstruction benchmarking.",
    "39692575": "Cryoprotectant/storage study; useful methods/context, but not core biomaterial benchmarking.",
    "40995315": "Imaging/characterization tool for epithelial products; not primary biomaterial scaffold evidence.",
    "41503585": "Clinical factor/outcome modifier study; not primary biomaterial benchmarking.",
    "39429339": "Surgical harvesting technique; useful clinical context, but not core biomaterial benchmarking."
}

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

kept_rows = []
demoted_rows = []

for r in rows:
    out = dict(r)
    pmid = r.get("pmid", "")

    if pmid in DEMOTE_PMIDS:
        out["refined_top_tier_decision"] = "Demote to supporting/context"
        out["refined_top_tier_reason"] = DEMOTE_PMIDS[pmid]
        demoted_rows.append(out)
    else:
        out["refined_top_tier_decision"] = "Keep top-tier core addition"
        out["refined_top_tier_reason"] = "Retained as strong epithelial/limbal biomaterial, scaffold, carrier, hydrogel, or cell-sheet reconstruction evidence."
        kept_rows.append(out)

def write_csv(path, rows):
    if not rows:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

write_csv(OUTPUT, kept_rows)
write_csv(DEMOTED_OUTPUT, demoted_rows)

decision_counts = Counter(r["refined_top_tier_decision"] for r in kept_rows + demoted_rows)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# Refined Top-Tier Epithelium/Limbus Core Report\n\n")

    f.write("## Purpose\n\n")
    f.write("This report applies final supervisor-level corrections to the top-tier epithelium/limbus additions before merging them into the expanded PubMed core. Records focused mainly on storage, characterization tools, clinical modifiers, or surgical technique are demoted to supporting/context.\n\n")

    f.write("## Counts\n\n")
    f.write(f"- Original top-tier epithelium/limbus records: {len(rows)}\n")
    f.write(f"- Kept as refined top-tier core additions: {len(kept_rows)}\n")
    f.write(f"- Demoted to supporting/context: {len(demoted_rows)}\n\n")

    f.write("## Decision Counts\n\n")
    for k, v in decision_counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Kept Top-Tier Core Additions\n\n")
    for r in kept_rows:
        f.write(f"- {r['screening_id']} / PMID {r['pmid']}: {r['title']}\n")

    f.write("\n## Demoted Records\n\n")
    for r in demoted_rows:
        f.write(f"- {r['screening_id']} / PMID {r['pmid']}: {r['title']} — {r['refined_top_tier_reason']}\n")

    f.write("\n## Output Files\n\n")
    f.write(f"- Refined top-tier additions: `{OUTPUT}`\n")
    f.write(f"- Demoted records: `{DEMOTED_OUTPUT}`\n")

print("Refined top-tier epithelium/limbus core created.")
print(f"Original top-tier epithelium/limbus records: {len(rows)}")
print(f"Kept as refined top-tier core additions: {len(kept_rows)}")
print(f"Demoted to supporting/context: {len(demoted_rows)}")
