from pathlib import Path
import csv
from collections import Counter

INPUT = Path("screening/full_text/pubmed_balanced_final_core_records.csv")
OUTPUT = Path("screening/full_text/pubmed_strict_retrieval_shortlist.csv")
SUPPORTING_OUTPUT = Path("screening/full_text/pubmed_retrieval_later_records.csv")
REPORT = Path("screening/full_text/pubmed_strict_retrieval_shortlist_report.md")

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

def strict_score(row):
    text = f"{row.get('title','')} {row.get('abstract','')}".lower()
    layer = row.get("corneal_layer", "")

    score = 0
    reasons = []

    clinical_terms = [
        "clinical trial", "prospective clinical", "randomized",
        "first-in-human", "patients", "patient", "clinical-grade",
        "clinical application", "transplantation", "keratoplasty"
    ]

    in_vivo_terms = [
        "in vivo", "rabbit", "rat", "mouse", "porcine model",
        "dog", "cat", "primate", "non-human primate", "animal model"
    ]

    ex_vivo_terms = [
        "ex vivo", "organ culture", "cadaver", "human cornea organ culture"
    ]

    strong_material_terms = [
        "scaffold", "hydrogel", "membrane", "carrier", "substrate",
        "film", "decellularized", "collagen", "silk fibroin",
        "polycaprolactone", "electrospun", "nanofiber", "bioink",
        "bioprinting", "amniotic membrane"
    ]

    benchmark_terms = [
        "transparency", "optical", "mechanical", "tensile",
        "elastic", "modulus", "cell viability", "migration",
        "barrier", "re-epithelialization", "cell density",
        "p63", "k3", "k12", "abcg2", "zo-1", "na+/k+-atpase",
        "na(+)/k(+)-atpase"
    ]

    reconstruction_terms = [
        "regeneration", "reconstruction", "repair", "defect",
        "wound healing", "limbal stem cell deficiency",
        "endothelial dysfunction", "corneal injury",
        "corneal burn", "alkali burn"
    ]

    has_clinical = any(t in text for t in clinical_terms)
    has_in_vivo = any(t in text for t in in_vivo_terms)
    has_ex_vivo = any(t in text for t in ex_vivo_terms)
    has_material = any(t in text for t in strong_material_terms)
    has_benchmark = any(t in text for t in benchmark_terms)
    has_reconstruction = any(t in text for t in reconstruction_terms)

    if has_clinical:
        score += 5
        reasons.append("clinical/translational evidence")

    if has_in_vivo:
        score += 4
        reasons.append("in vivo evidence")

    if has_ex_vivo:
        score += 3
        reasons.append("ex vivo evidence")

    if has_material:
        score += 3
        reasons.append("clear biomaterial/scaffold/carrier signal")

    if has_benchmark:
        score += 2
        reasons.append("benchmarking metrics likely")

    if has_reconstruction:
        score += 2
        reasons.append("reconstruction/regeneration relevance")

    if layer in ["endothelium", "epithelium_limbus"]:
        score += 1
        reasons.append("layer-balancing priority")

    return score, "; ".join(reasons), {
        "has_clinical": has_clinical,
        "has_in_vivo": has_in_vivo,
        "has_ex_vivo": has_ex_vivo,
        "has_material": has_material,
        "has_benchmark": has_benchmark,
        "has_reconstruction": has_reconstruction,
    }

scored = []

for r in rows:
    out = dict(r)
    score, reasons, flags = strict_score(r)

    out["strict_retrieval_score"] = score
    out["strict_retrieval_reason"] = reasons

    for k, v in flags.items():
        out[k] = "yes" if v else "no"

    # Strict rule:
    # Priority 1 requires material evidence plus either clinical/in vivo/ex vivo evidence,
    # or material + reconstruction + benchmark signal.
    if (
        flags["has_material"]
        and (
            flags["has_clinical"]
            or flags["has_in_vivo"]
            or flags["has_ex_vivo"]
            or (flags["has_reconstruction"] and flags["has_benchmark"])
        )
        and score >= 11
    ):
        out["strict_retrieval_group"] = "Priority 1 - strict retrieval shortlist"
    elif score >= 8 and flags["has_material"]:
        out["strict_retrieval_group"] = "Priority 2 - retrieve after shortlist"
    else:
        out["strict_retrieval_group"] = "Priority 3 - retrieve later/background"

    scored.append(out)

scored.sort(
    key=lambda r: (
        r["strict_retrieval_group"],
        -int(r["strict_retrieval_score"]),
        r.get("corneal_layer", ""),
        r.get("screening_id", "")
    )
)

shortlist = [
    r for r in scored
    if r["strict_retrieval_group"] == "Priority 1 - strict retrieval shortlist"
]

later = [
    r for r in scored
    if r["strict_retrieval_group"] != "Priority 1 - strict retrieval shortlist"
]

def write_csv(path, rows_to_write):
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rows_to_write[0].keys())
        writer.writeheader()
        writer.writerows(rows_to_write)

write_csv(OUTPUT, shortlist)
write_csv(SUPPORTING_OUTPUT, later)

group_counts = Counter(r["strict_retrieval_group"] for r in scored)
shortlist_layer_counts = Counter(r["corneal_layer"] for r in shortlist)
all_layer_counts = Counter(r["corneal_layer"] for r in scored)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# Strict PubMed Retrieval Shortlist Report\n\n")

    f.write("## Purpose\n\n")
    f.write("This report creates a stricter full-text retrieval shortlist from the balanced final PubMed core. The earlier retrieval-priority script was too permissive and placed too many records into Priority 1.\n\n")

    f.write("## Counts\n\n")
    f.write(f"- Balanced final PubMed core records checked: {len(scored)}\n")
    f.write(f"- Strict Priority 1 retrieval shortlist: {len(shortlist)}\n")
    f.write(f"- Records to retrieve later/background: {len(later)}\n\n")

    f.write("## Strict Retrieval Group Counts\n\n")
    for k, v in group_counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Strict Priority 1 Shortlist by Layer\n\n")
    for k, v in shortlist_layer_counts.most_common():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Full Balanced Core by Layer\n\n")
    for k, v in all_layer_counts.most_common():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Strict Priority 1 Records\n\n")
    for r in shortlist:
        f.write(f"- {r['screening_id']} / PMID {r['pmid']} / score {r['strict_retrieval_score']} / {r['corneal_layer']}: {r['title']}\n")

    f.write("\n## Output Files\n\n")
    f.write(f"- Strict retrieval shortlist: `{OUTPUT}`\n")
    f.write(f"- Retrieve later/background records: `{SUPPORTING_OUTPUT}`\n")

print("Strict PubMed retrieval shortlist created.")
print(f"Balanced final PubMed core records checked: {len(scored)}")
print(f"Strict Priority 1 retrieval shortlist: {len(shortlist)}")
print(f"Records to retrieve later/background: {len(later)}")
print("Strict retrieval group counts:")
for k, v in group_counts.items():
    print(f"{k}: {v}")
print("Strict Priority 1 shortlist by layer:")
for k, v in shortlist_layer_counts.most_common():
    print(f"{k}: {v}")
