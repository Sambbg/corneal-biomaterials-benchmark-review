from pathlib import Path
import csv
from collections import Counter

INPUT = Path("screening/full_text/pubmed_manual_audit_worksheet.csv")
OUTPUT = Path("screening/full_text/pubmed_manual_audit_reading_file.md")

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

def classify_pressure(row):
    title = row.get("title", "").lower()
    abstract = row.get("abstract", "").lower()
    text = title + " " + abstract

    weak_terms = [
        "contact lens",
        "confocal microscopy",
        "rna modifications",
        "molecular orchestrators",
        "p-cadherin is expressed",
        "tgf-β1 promotes cell barrier",
        "intraocular pressure",
        "neurotrophic keratitis",
        "artificial corneal transplantation"
    ]

    strong_terms = [
        "scaffold",
        "hydrogel",
        "bioink",
        "bioprint",
        "decellularized",
        "acellular",
        "cell sheet",
        "tissue-engineered",
        "tissue engineered",
        "corneal substitute",
        "artificial cornea",
        "construct",
        "electrospun",
        "nanofiber",
        "gelma",
        "collagen",
        "silk fibroin",
        "polycaprolactone"
    ]

    has_weak = any(t in text for t in weak_terms)
    strong_count = sum(1 for t in strong_terms if t in text)

    if has_weak and strong_count == 0:
        return "Likely downgrade/exclude"
    if has_weak and strong_count > 0:
        return "Needs close audit"
    return "Likely keep core"

for r in rows:
    r["audit_pressure"] = classify_pressure(r)

pressure_counts = Counter(r["audit_pressure"] for r in rows)
layer_counts = Counter(r["corneal_layer"] for r in rows)

with OUTPUT.open("w", encoding="utf-8") as f:
    f.write("# PubMed Manual Audit Reading File\n\n")

    f.write("## Purpose\n\n")
    f.write("This file presents the 64 manually flagged core candidate records in a readable format. Use it to decide whether each paper should remain in the core set, be downgraded to medium priority, excluded, or left uncertain.\n\n")

    f.write("## Audit Pressure Counts\n\n")
    for k, v in pressure_counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Layer Counts\n\n")
    for k, v in layer_counts.items():
        f.write(f"- {k}: {v}\n")

    for pressure in ["Likely downgrade/exclude", "Needs close audit", "Likely keep core"]:
        selected = [r for r in rows if r["audit_pressure"] == pressure]
        if not selected:
            continue

        f.write(f"\n# {pressure}\n\n")

        for r in selected:
            f.write(f"## {r['screening_id']} / PMID {r['pmid']}\n\n")
            f.write(f"**Title:** {r['title']}\n\n")
            f.write(f"**Year:** {r['year']}\n\n")
            f.write(f"**Journal:** {r['journal']}\n\n")
            f.write(f"**Layer:** {r['corneal_layer']}\n\n")
            f.write(f"**Priority:** {r['priority_level']}\n\n")
            f.write(f"**DOI:** {r['doi']}\n\n")
            f.write(f"**Abstract:** {r['abstract']}\n\n")
            f.write("**Manual decision:** \n\n")
            f.write("**Manual reason:** \n\n")
            f.write("---\n\n")

print("Manual audit reading file created.")
print("Audit pressure counts:")
for k, v in pressure_counts.items():
    print(f"{k}: {v}")
print(f"Output: {OUTPUT}")
