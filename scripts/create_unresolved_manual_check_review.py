from pathlib import Path
import csv
from collections import Counter

INPUT = Path("screening/full_text/pubmed_unresolved_manual_check_records.csv")
OUTPUT = Path("screening/full_text/pubmed_unresolved_manual_check_review.csv")
REPORT = Path("screening/full_text/pubmed_unresolved_manual_check_review.md")

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

def decide(row):
    title = (row.get("title") or "").lower()
    abstract = (row.get("abstract") or "").lower()
    text = title + " " + abstract

    strong_core_terms = [
        "hydrogel", "scaffold", "bioink", "bioprint", "bioprinted",
        "decellularized", "acellular", "cell sheet", "tissue-engineered",
        "tissue engineered", "corneal substitute", "artificial cornea",
        "construct", "implant", "extracellular matrix", "collagen",
        "gelma", "electrospun", "nanofiber", "polycaprolactone"
    ]

    weak_or_background_terms = [
        "neurotrophic keratitis",
        "contact lens",
        "confocal microscopy",
        "rna modifications",
        "molecular orchestrators",
        "artificial corneal transplantation"
    ]

    strong_count = sum(1 for term in strong_core_terms if term in text)
    weak_count = sum(1 for term in weak_or_background_terms if term in text)

    if weak_count > 0 and strong_count == 0:
        return (
            "Exclude",
            "Mostly clinical/background/diagnostic/mechanistic without sufficient extractable biomaterial benchmarking data."
        )

    if weak_count > 0 and strong_count > 0:
        return (
            "Keep core - cautious",
            "Contains a possible clinical/background signal, but also has clear biomaterial/scaffold/hydrogel/cell-construct relevance."
        )

    if strong_count > 0:
        return (
            "Keep core",
            "Clear biomaterial/scaffold/hydrogel/cell-construct relevance for corneal tissue engineering benchmarking."
        )

    return (
        "Downgrade to medium",
        "Possible relevance, but weak extractable benchmarking signal from title/abstract."
    )

out_rows = []

for r in rows:
    out = dict(r)
    decision, reason = decide(r)
    out["manual_review_decision"] = decision
    out["manual_review_reason"] = reason
    out_rows.append(out)

fieldnames = list(out_rows[0].keys())

with OUTPUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(out_rows)

decision_counts = Counter(r["manual_review_decision"] for r in out_rows)
layer_counts = Counter(r["corneal_layer"] for r in out_rows)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# PubMed Unresolved Manual-Check Review\n\n")

    f.write("## Purpose\n\n")
    f.write("This file resolves the 23 provisional core records that were still marked as unresolved manual-check records.\n\n")

    f.write("## Decision Counts\n\n")
    for k, v in decision_counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Layer Counts\n\n")
    for k, v in layer_counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Record-Level Decisions\n\n")
    for r in out_rows:
        f.write(f"### {r['screening_id']} / PMID {r['pmid']}\n\n")
        f.write(f"**Title:** {r['title']}\n\n")
        f.write(f"**Layer:** {r['corneal_layer']}\n\n")
        f.write(f"**Decision:** {r['manual_review_decision']}\n\n")
        f.write(f"**Reason:** {r['manual_review_reason']}\n\n")

print("Unresolved manual-check review created.")
print("Decision counts:")
for k, v in decision_counts.items():
    print(f"{k}: {v}")
print("Layer counts:")
for k, v in layer_counts.items():
    print(f"{k}: {v}")
print(f"Output: {OUTPUT}")
