from pathlib import Path
import csv
from collections import Counter

INPUT = Path("screening/full_text/pubmed_strict_epithelium_limbus_additions.csv")
OUTPUT = Path("screening/full_text/pubmed_top_tier_epithelium_limbus_core_additions.csv")
SUPPORTING_OUTPUT = Path("screening/full_text/pubmed_supporting_epithelium_limbus_records.csv")
REPORT = Path("screening/full_text/pubmed_top_tier_epithelium_limbus_core_report.md")

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

candidate_rows = [
    r for r in rows
    if r.get("strict_epithelium_limbus_decision") == "Add to epithelium/limbus core"
]

def score(row):
    text = f"{row.get('title','')} {row.get('abstract','')}".lower()

    score_value = 0
    reasons = []

    strong_reconstruction_terms = [
        "limbal stem cell deficiency",
        "ocular surface reconstruction",
        "corneal reconstruction",
        "corneal epithelial reconstruction",
        "alkali burn",
        "chemical burn",
        "corneal wound healing",
        "corneal epithelial regeneration",
        "corneal damage repair"
    ]

    scaffold_terms = [
        "scaffold", "carrier", "substrate", "membrane", "hydrogel",
        "film", "decellularized", "electrospun", "nanofiber",
        "collagen", "amniotic membrane"
    ]

    cell_sheet_terms = [
        "cell sheet", "epithelial sheet", "limbal epithelial sheet",
        "oral mucosal epithelial cell sheet", "cultivated limbal epithelial"
    ]

    translational_terms = [
        "clinical trial", "prospective", "randomized", "first-in-human",
        "non-human primate", "primate", "rabbit", "in vivo",
        "transplantation"
    ]

    benchmark_terms = [
        "p63", "k3", "k12", "abcg2", "stratification",
        "transparency", "barrier", "migration", "cell viability",
        "re-epithelialization"
    ]

    if any(t in text for t in strong_reconstruction_terms):
        score_value += 3
        reasons.append("strong reconstruction/regeneration relevance")

    if any(t in text for t in scaffold_terms):
        score_value += 2
        reasons.append("scaffold/carrier/material present")

    if any(t in text for t in cell_sheet_terms):
        score_value += 2
        reasons.append("cell-sheet/cultivated epithelial construct present")

    if any(t in text for t in translational_terms):
        score_value += 2
        reasons.append("translational or in vivo evidence")

    if any(t in text for t in benchmark_terms):
        score_value += 1
        reasons.append("extractable benchmark markers likely")

    return score_value, "; ".join(reasons)

scored_rows = []

for r in candidate_rows:
    out = dict(r)
    score_value, reason = score(r)
    out["top_tier_score"] = score_value
    out["top_tier_reason"] = reason

    if score_value >= 6:
        out["top_tier_decision"] = "Top-tier core addition"
    else:
        out["top_tier_decision"] = "Supporting epithelium/limbus record"

    scored_rows.append(out)

scored_rows.sort(key=lambda r: (-int(r["top_tier_score"]), r["screening_id"]))

top_tier_rows = [
    r for r in scored_rows
    if r["top_tier_decision"] == "Top-tier core addition"
]

supporting_rows = [
    r for r in scored_rows
    if r["top_tier_decision"] == "Supporting epithelium/limbus record"
]

def write_csv(path, rows):
    if not rows:
        return

    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)

write_csv(OUTPUT, top_tier_rows)
write_csv(SUPPORTING_OUTPUT, supporting_rows)

decision_counts = Counter(r["top_tier_decision"] for r in scored_rows)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# Top-Tier Epithelium/Limbus Core Additions Report\n\n")

    f.write("## Purpose\n\n")
    f.write("This report narrows the strict epithelium/limbus additions into a smaller top-tier set for core extraction. This prevents the extraction pool from becoming too large while preserving the strongest epithelial/limbal reconstruction evidence.\n\n")

    f.write("## Counts\n\n")
    f.write(f"- Strict epithelium/limbus add candidates checked: {len(candidate_rows)}\n")
    for k, v in decision_counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Top-Tier Core Additions\n\n")
    for r in top_tier_rows:
        f.write(f"- {r['screening_id']} / PMID {r['pmid']} / score {r['top_tier_score']}: {r['title']}\n")

    f.write("\n## Supporting Epithelium/Limbus Records\n\n")
    for r in supporting_rows:
        f.write(f"- {r['screening_id']} / PMID {r['pmid']} / score {r['top_tier_score']}: {r['title']}\n")

    f.write("\n## Output Files\n\n")
    f.write(f"- Top-tier additions: `{OUTPUT}`\n")
    f.write(f"- Supporting records: `{SUPPORTING_OUTPUT}`\n")

print("Top-tier epithelium/limbus core additions created.")
print(f"Strict epithelium/limbus add candidates checked: {len(candidate_rows)}")
print("Decision counts:")
for k, v in decision_counts.items():
    print(f"{k}: {v}")
