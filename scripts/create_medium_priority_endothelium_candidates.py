from pathlib import Path
import csv
from collections import Counter

INPUT = Path("screening/full_text/pubmed_medium_priority_include_records.csv")
OUTPUT = Path("screening/full_text/pubmed_medium_priority_endothelium_candidates.csv")
REPORT = Path("screening/full_text/pubmed_medium_priority_endothelium_candidates_report.md")

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

endothelium_rows = [
    r for r in rows
    if r.get("corneal_layer") == "endothelium"
]

def score(row):
    text = f"{row.get('title','')} {row.get('abstract','')}".lower()

    terms = {
        "carrier_or_scaffold": [
            "carrier", "scaffold", "substrate", "membrane", "sheet",
            "descemet", "dmek", "dsaek", "endothelial keratoplasty"
        ],
        "cell_engineering": [
            "corneal endothelial cell", "hcec", "endothelial cells",
            "cell culture", "cultivated", "expanded", "monolayer"
        ],
        "function": [
            "na(+)/k(+)-atpase", "zo-1", "pump", "barrier",
            "hexagonal", "cell density", "transparency", "corneal thickness"
        ],
        "translation": [
            "rabbit", "monkey", "primate", "in vivo", "transplantation",
            "clinical", "surgery", "implantation"
        ]
    }

    matched_categories = []
    matched_terms = []

    for category, category_terms in terms.items():
        hits = [t for t in category_terms if t in text]
        if hits:
            matched_categories.append(category)
            matched_terms.extend(hits[:3])

    return len(matched_categories), "; ".join(matched_terms)

out_rows = []

for r in endothelium_rows:
    out = dict(r)
    s, hits = score(r)
    out["endothelium_relevance_score"] = s
    out["endothelium_relevance_terms"] = hits

    if s >= 3:
        out["recommended_action"] = "Add to core candidate"
    elif s == 2:
        out["recommended_action"] = "Manual check"
    else:
        out["recommended_action"] = "Do not add yet"

    out_rows.append(out)

out_rows.sort(key=lambda r: (-int(r["endothelium_relevance_score"]), r["screening_id"]))

with OUTPUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=out_rows[0].keys())
    writer.writeheader()
    writer.writerows(out_rows)

action_counts = Counter(r["recommended_action"] for r in out_rows)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# Medium-Priority Endothelium Candidate Report\n\n")

    f.write("## Purpose\n\n")
    f.write("This report identifies medium-priority endothelial records that may need to be added to the PubMed core pool because the strict high-priority core contains too few endothelial studies.\n\n")

    f.write("## Counts\n\n")
    f.write(f"- Medium-priority Include records checked: {len(rows)}\n")
    f.write(f"- Medium-priority endothelial records found: {len(out_rows)}\n\n")

    f.write("## Recommended Actions\n\n")
    for k, v in action_counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Candidate Records\n\n")
    for r in out_rows:
        f.write(f"### {r['screening_id']} / PMID {r['pmid']}\n\n")
        f.write(f"**Title:** {r['title']}\n\n")
        f.write(f"**Score:** {r['endothelium_relevance_score']}\n\n")
        f.write(f"**Recommended action:** {r['recommended_action']}\n\n")
        f.write(f"**Matched terms:** {r['endothelium_relevance_terms']}\n\n")

print("Medium-priority endothelium candidates created.")
print(f"Medium-priority Include records checked: {len(rows)}")
print(f"Medium-priority endothelial records found: {len(out_rows)}")
print("Recommended actions:")
for k, v in action_counts.items():
    print(f"{k}: {v}")
