from pathlib import Path
import csv
from collections import Counter

INPUT = Path("screening/full_text/pubmed_balanced_final_core_records.csv")
OUTPUT = Path("screening/full_text/pubmed_retrieval_priority_order.csv")
REPORT = Path("screening/full_text/pubmed_retrieval_priority_order_report.md")

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

def priority_score(row):
    text = f"{row.get('title','')} {row.get('abstract','')}".lower()

    score = 0
    reasons = []

    clinical_terms = [
        "clinical trial", "prospective", "randomized", "first-in-human",
        "patient", "patients", "clinical", "surgery", "transplantation"
    ]

    in_vivo_terms = [
        "in vivo", "rabbit", "rat", "mouse", "porcine", "dog", "cat",
        "monkey", "primate", "animal model"
    ]

    ex_vivo_terms = [
        "ex vivo", "organ culture", "cadaver", "human cornea"
    ]

    biomaterial_terms = [
        "scaffold", "hydrogel", "membrane", "carrier", "substrate",
        "film", "decellularized", "collagen", "silk fibroin",
        "polycaprolactone", "electrospun", "nanofiber", "gelatin",
        "amniotic membrane"
    ]

    benchmark_terms = [
        "transparency", "optical", "mechanical", "tensile", "elastic",
        "modulus", "cell viability", "migration", "zo-1", "p63",
        "k3", "k12", "abcg2", "na(+)/k(+)-atpase", "barrier",
        "re-epithelialization", "cell density"
    ]

    if any(t in text for t in clinical_terms):
        score += 5
        reasons.append("clinical/translational evidence")

    if any(t in text for t in in_vivo_terms):
        score += 4
        reasons.append("in vivo evidence")

    if any(t in text for t in ex_vivo_terms):
        score += 3
        reasons.append("ex vivo evidence")

    if any(t in text for t in biomaterial_terms):
        score += 3
        reasons.append("biomaterial/scaffold signal")

    if any(t in text for t in benchmark_terms):
        score += 2
        reasons.append("benchmarking metrics likely")

    layer = row.get("corneal_layer", "")

    if layer in ["endothelium", "epithelium_limbus"]:
        score += 1
        reasons.append("underrepresented layer priority")

    return score, "; ".join(reasons)

out_rows = []

for r in rows:
    out = dict(r)
    score, reason = priority_score(r)
    out["retrieval_priority_score"] = score
    out["retrieval_priority_reason"] = reason

    if score >= 11:
        out["retrieval_priority_group"] = "Priority 1 - retrieve first"
    elif score >= 8:
        out["retrieval_priority_group"] = "Priority 2 - retrieve second"
    elif score >= 5:
        out["retrieval_priority_group"] = "Priority 3 - retrieve third"
    else:
        out["retrieval_priority_group"] = "Priority 4 - retrieve later"

    out_rows.append(out)

out_rows.sort(
    key=lambda r: (
        r["retrieval_priority_group"],
        -int(r["retrieval_priority_score"]),
        r.get("corneal_layer", ""),
        r.get("screening_id", "")
    )
)

with OUTPUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=out_rows[0].keys())
    writer.writeheader()
    writer.writerows(out_rows)

group_counts = Counter(r["retrieval_priority_group"] for r in out_rows)
layer_counts = Counter(r["corneal_layer"] for r in out_rows)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# PubMed Retrieval Priority Order Report\n\n")

    f.write("## Purpose\n\n")
    f.write("This report prioritizes the balanced final PubMed core for full-text retrieval. The aim is to retrieve the highest-value clinical, in vivo, ex vivo, and benchmark-rich biomaterial papers first.\n\n")

    f.write("## Total Records Prioritized\n\n")
    f.write(f"- Records prioritized: {len(out_rows)}\n\n")

    f.write("## Priority Group Counts\n\n")
    for k, v in group_counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Layer Counts\n\n")
    for k, v in layer_counts.most_common():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Priority 1 Records\n\n")
    for r in out_rows:
        if r["retrieval_priority_group"] == "Priority 1 - retrieve first":
            f.write(f"- {r['screening_id']} / PMID {r['pmid']} / score {r['retrieval_priority_score']} / {r['corneal_layer']}: {r['title']}\n")

    f.write("\n## Output File\n\n")
    f.write(f"- `{OUTPUT}`\n")

print("PubMed retrieval priority order created.")
print(f"Records prioritized: {len(out_rows)}")
print("Priority group counts:")
for k, v in group_counts.items():
    print(f"{k}: {v}")
print("Layer counts:")
for k, v in layer_counts.most_common():
    print(f"{k}: {v}")
