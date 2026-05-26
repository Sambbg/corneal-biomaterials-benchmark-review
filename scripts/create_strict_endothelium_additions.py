from pathlib import Path
import csv
from collections import Counter

INPUT = Path("screening/full_text/pubmed_medium_priority_endothelium_candidates.csv")
OUTPUT = Path("screening/full_text/pubmed_strict_endothelium_additions.csv")
REPORT = Path("screening/full_text/pubmed_strict_endothelium_additions_report.md")

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

# Strict exclusions/background based on title fit.
# These are useful context/methodology papers, but not core biomaterial benchmarking papers.
EXCLUDE_OR_BACKGROUND = {
    "33072921": "Culture approach only; weak biomaterial/scaffold benchmarking signal.",
    "33259606": "Disease/mechanistic collagen-remodeling paper; not a primary biomaterial engineering study.",
    "38247948": "Software/cell counting method for cellular therapy; not a biomaterial benchmarking study.",
    "41356124": "Mechanistic ECM stiffness/barrier paper; not clearly a corneal biomaterial scaffold/implant study.",
    "30319302": "Soft contact lens morphology study; not tissue engineering biomaterial evidence.",
    "37951740": "Contact lens wear/ocular surface study; not corneal tissue engineering.",
    "40038090": "Drug-delivery safety study; not corneal endothelial tissue-engineering scaffold evidence.",
    "40383650": "Soft contact lens endothelial-characteristics study; not tissue engineering.",
    "29680447": "Basic cultivation of sheep endothelial cells; weak scaffold/biomaterial benchmarking signal."
}

def strict_decision(row):
    pmid = row.get("pmid", "")

    if pmid in EXCLUDE_OR_BACKGROUND:
        return "Exclude/background", EXCLUDE_OR_BACKGROUND[pmid]

    title = (row.get("title") or "").lower()
    abstract = (row.get("abstract") or "").lower()
    text = title + " " + abstract

    scaffold_terms = [
        "scaffold", "carrier", "substrate", "membrane", "sheet",
        "graft", "implant", "descemet", "hydrogel", "vitrigel",
        "silk fibroin", "collagen", "polycaprolactone", "agarose",
        "amniotic membrane", "extracellular matrix"
    ]

    endothelial_terms = [
        "corneal endothelial", "endothelium", "endothelial cell",
        "hcec", "endothelial keratoplasty", "dmek", "dsaek"
    ]

    functional_terms = [
        "zo-1", "na(+)/k(+)-atpase", "pump", "barrier",
        "hexagonal", "cell density", "transparency", "corneal thickness",
        "monolayer"
    ]

    translational_terms = [
        "rabbit", "monkey", "primate", "in vivo", "ex vivo",
        "transplantation", "keratoplasty", "clinical", "surgery",
        "implantation"
    ]

    scaffold_hit = any(t in text for t in scaffold_terms)
    endothelial_hit = any(t in text for t in endothelial_terms)
    functional_hit = any(t in text for t in functional_terms)
    translational_hit = any(t in text for t in translational_terms)

    score = sum([scaffold_hit, endothelial_hit, functional_hit, translational_hit])

    if scaffold_hit and endothelial_hit and score >= 3:
        return "Add to endothelial core", "Clear endothelial tissue-engineering biomaterial/carrier/scaffold signal with functional or translational relevance."

    if scaffold_hit and endothelial_hit:
        return "Manual check", "Likely relevant, but title/abstract signal is not strong enough for automatic core addition."

    return "Exclude/background", "Insufficient scaffold/carrier/endothelial tissue-engineering benchmarking signal."

out_rows = []

for r in rows:
    out = dict(r)
    decision, reason = strict_decision(r)
    out["strict_endothelium_decision"] = decision
    out["strict_endothelium_reason"] = reason
    out_rows.append(out)

with OUTPUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=out_rows[0].keys())
    writer.writeheader()
    writer.writerows(out_rows)

decision_counts = Counter(r["strict_endothelium_decision"] for r in out_rows)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# Strict Medium-Priority Endothelium Additions Report\n\n")

    f.write("## Purpose\n\n")
    f.write("This report applies stricter rules to medium-priority endothelial records before adding them to the PubMed core pool. The goal is to strengthen the underrepresented endothelial layer without contaminating the core extraction set with contact lens, software, disease-mechanism, or generic culture-method papers.\n\n")

    f.write("## Strict Decision Counts\n\n")
    for k, v in decision_counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Records Recommended for Endothelial Core Addition\n\n")
    for r in out_rows:
        if r["strict_endothelium_decision"] == "Add to endothelial core":
            f.write(f"- {r['screening_id']} / PMID {r['pmid']}: {r['title']}\n")

    f.write("\n## Manual Check Records\n\n")
    for r in out_rows:
        if r["strict_endothelium_decision"] == "Manual check":
            f.write(f"- {r['screening_id']} / PMID {r['pmid']}: {r['title']}\n")

    f.write("\n## Exclude/Background Records\n\n")
    for r in out_rows:
        if r["strict_endothelium_decision"] == "Exclude/background":
            f.write(f"- {r['screening_id']} / PMID {r['pmid']}: {r['title']} — {r['strict_endothelium_reason']}\n")

print("Strict endothelium additions file created.")
print("Strict decision counts:")
for k, v in decision_counts.items():
    print(f"{k}: {v}")
