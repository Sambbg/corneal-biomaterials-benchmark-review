"""
Split the balanced core into a Tier 1 (full extraction) / Tier 2 (light-touch)
plan, per protocol v0.2's two-tier extraction strategy.

Rationale: the existing retrieval_priority_score (0-18) already encodes
clinical/in-vivo/ex-vivo/biomaterial/benchmark signal from title+abstract
keyword scoring (see create_pubmed_retrieval_priority_order.py). Using the
raw 4-bucket "Priority 1" group as-is would put 194/248 records (78%) into
the top group, which defeats the purpose of tiering.

A score >= 15 cutoff was chosen because it produces a Tier 1 group of
roughly 90-120 records (the target range agreed for full extraction) while
keeping a reasonably even layer distribution, rather than being dominated by
the numerically larger multiple_layers/stroma groups.
"""
from pathlib import Path
import csv
from collections import Counter

INPUT = Path("screening/full_text/pubmed_retrieval_priority_order.csv")
OUTPUT = Path("screening/full_text/pubmed_tier1_tier2_extraction_plan.csv")
REPORT = Path("screening/full_text/pubmed_tier1_tier2_extraction_plan_report.md")

TIER1_SCORE_CUTOFF = 15

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

for r in rows:
    score = int(r["retrieval_priority_score"])
    if score >= TIER1_SCORE_CUTOFF:
        r["extraction_tier"] = "Tier 1 - full extraction"
    else:
        r["extraction_tier"] = "Tier 2 - light-touch / cited for context"

# Retrieval order within Tier 1: highest score first, then rotate layers so
# retrieval doesn't clear one entire layer before touching another.
tier1 = [r for r in rows if r["extraction_tier"].startswith("Tier 1")]
tier2 = [r for r in rows if r["extraction_tier"].startswith("Tier 2")]

layer_order = {"endothelium": 0, "epithelium_limbus": 1, "stroma": 2, "multiple_layers": 3}
tier1.sort(key=lambda r: (-int(r["retrieval_priority_score"]), layer_order.get(r.get("corneal_layer", ""), 9), r["screening_id"]))
tier2.sort(key=lambda r: (-int(r["retrieval_priority_score"]), r.get("corneal_layer", ""), r["screening_id"]))

out_rows = tier1 + tier2
fieldnames = list(out_rows[0].keys())

with OUTPUT.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(out_rows)

tier_counts = Counter(r["extraction_tier"] for r in out_rows)
tier1_layers = Counter(r["corneal_layer"] for r in tier1)
tier2_layers = Counter(r["corneal_layer"] for r in tier2)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# Tier 1 / Tier 2 Extraction Plan Report\n\n")
    f.write("## Purpose\n\n")
    f.write(
        "Splits the balanced core (protocol v0.2) into a Tier 1 group for full "
        "template extraction and a Tier 2 group cited for context only, so extraction "
        "effort concentrates on the highest-value clinical/in-vivo/ex-vivo/benchmark-rich "
        "records rather than spreading evenly across all core records.\n\n"
    )
    f.write(f"## Cutoff\n\nTier 1 = retrieval_priority_score >= {TIER1_SCORE_CUTOFF}.\n\n")
    f.write("## Counts\n\n")
    for k, v in tier_counts.items():
        f.write(f"- {k}: {v}\n")
    f.write("\n## Tier 1 Layer Distribution\n\n")
    for k, v in tier1_layers.most_common():
        f.write(f"- {k}: {v}\n")
    f.write("\n## Tier 2 Layer Distribution\n\n")
    for k, v in tier2_layers.most_common():
        f.write(f"- {k}: {v}\n")
    f.write("\n## Retrieval Order Within Tier 1\n\n")
    f.write(
        "Sorted by retrieval_priority_score descending, then rotated across layers "
        "(endothelium, epithelium_limbus, stroma, multiple_layers) so no single layer "
        "is fully cleared before another is started. This keeps benchmarking-table "
        "coverage balanced across layers even if retrieval stalls partway through.\n\n"
    )
    f.write("## First 20 Records To Retrieve\n\n")
    for r in tier1[:20]:
        f.write(f"- {r['screening_id']} / PMID {r['pmid']} / score {r['retrieval_priority_score']} / {r['corneal_layer']}: {r['title']}\n")
    f.write(f"\n## Output File\n\n- `{OUTPUT}`\n")

print("Tier 1 / Tier 2 extraction plan created.")
print(f"Tier counts: {dict(tier_counts)}")
print(f"Tier 1 layer distribution: {dict(tier1_layers)}")
print(f"Tier 2 layer distribution: {dict(tier2_layers)}")
