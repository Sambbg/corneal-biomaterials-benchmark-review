from pathlib import Path
import csv
from collections import Counter

INPUT = Path("screening/full_text/pubmed_medium_priority_epithelium_limbus_candidates.csv")
OUTPUT = Path("screening/full_text/pubmed_strict_epithelium_limbus_additions.csv")
REPORT = Path("screening/full_text/pubmed_strict_epithelium_limbus_additions_report.md")

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

# Strict exclusions/background based on title fit.
# These are not primary epithelial/limbal tissue-engineering biomaterial benchmarking papers.
EXCLUDE_OR_BACKGROUND = {
    "30114356": "Contact lens surface-modification study; not core corneal tissue-engineering scaffold evidence.",
    "30537839": "Contact lens surface-property study; not core tissue-engineering evidence.",
    "31375008": "General ophthalmic/contact-lens hydrogel biocompatibility; weak epithelial tissue-engineering signal.",
    "36564919": "Drug-delivery contact lens study; not epithelial/limbal tissue-engineering scaffold evidence.",
    "38258038": "Hydrogel bandage contact lens material; mainly therapeutic delivery/bandage, not tissue-engineering reconstruction.",
    "38486034": "In vitro eye irritation testing platform; not biomaterial reconstruction evidence.",
    "39657357": "Predictive gene-signature paper; not biomaterial engineering.",
    "40296952": "Post-transplant complication/IOP management; not biomaterial engineering.",
    "40689376": "Insurance/regulatory coverage paper; background only.",
    "41729365": "Macular hole closure model; not corneal epithelial/limbal reconstruction.",
    "29207049": "Molecular transdifferentiation mechanism; not scaffold/carrier benchmarking.",
    "30357138": "Dry eye hydrogel injection; not epithelial/limbal reconstruction.",
    "31161710": "Generic multilayer electrospun corneal scaffold; not clearly epithelium/limbus-specific.",
    "31397733": "Neural differentiation potential of limbal stem cells; not biomaterial reconstruction evidence.",
    "33659413": "Cell isolation/expansion protocol; not scaffold/carrier benchmarking.",
    "34033392": "General mucous membrane graft background; not primary biomaterial benchmarking.",
    "34443612": "Contact lens antimicrobial hydrogel component study; not epithelial/limbal reconstruction.",
    "34515678": "Ocular inflammation hydrogel drug-delivery study; not tissue engineering.",
    "34552942": "Clinical conjunctival sac reconstruction; relevant background but not core corneal epithelium biomaterial benchmark.",
    "34568299": "Keratocyte mechanotransduction; wrong layer for epithelium/limbus core.",
    "35019286": "Mixed retinal pigment/corneal epithelial scaffold paper; possible background, not core layer-specific evidence.",
    "35186691": "Bandage contact lens clinical comparison; not tissue engineering.",
    "35378880": "Antifungal hydrogel drug-delivery study; not epithelial reconstruction.",
    "35893466": "Nerve repair/epithelization material; background unless full text proves epithelial reconstruction.",
    "36078126": "Donor/storage effects on cultured limbal epithelial cells; not biomaterial scaffold benchmarking.",
    "37097204": "Cell differentiation induction; weak scaffold/carrier evidence.",
    "37237859": "Dry eye drug-delivery hydrogel; not tissue engineering reconstruction.",
    "37477184": "Acellular porcine cornea implantation, not epithelium/limbus-specific.",
    "38292853": "Contact lens packaging-solution study; not tissue engineering.",
    "38713471": "Clinical surgical case/procedure; not primary biomaterial engineering benchmark.",
    "39072516": "Demographic amniotic membrane use trend; background only.",
    "39522528": "First-in-human cell therapy study; translationally important but not necessarily biomaterial benchmarking unless full text provides carrier/scaffold evidence.",
    "39884436": "Dry eye hydrogel nano-enzyme therapy; not epithelial/limbal reconstruction.",
    "39951297": "Mechanistic limbal niche stiffness paper; background/mechanism, not scaffold benchmark.",
    "40759789": "Contact lens hydrogel antimicrobial study; not tissue engineering.",
    "41595971": "Bandage contact lens clinical comparison; not tissue engineering.",
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
        "hydrogel", "film", "patch", "construct", "decellularized",
        "collagen", "amniotic membrane", "nanofiber", "electrospun",
        "bioengineered", "tissue engineered", "tissue-engineered"
    ]

    epi_limbus_terms = [
        "corneal epithelial", "corneal epithelium", "limbal",
        "limbal stem", "limbal epithelial", "lsc", "lesc",
        "ocular surface reconstruction", "epithelial regeneration",
        "epithelial cell sheet"
    ]

    reconstruction_terms = [
        "transplantation", "reconstruction", "repair", "regeneration",
        "wound healing", "re-epithelialization", "limbal stem cell deficiency",
        "alkali burn", "chemical burn", "corneal defect"
    ]

    benchmark_terms = [
        "p63", "k3", "k12", "abcg2", "stratification",
        "transparency", "barrier", "cell viability", "migration",
        "in vivo", "ex vivo", "rabbit", "clinical"
    ]

    scaffold_hit = any(t in text for t in scaffold_terms)
    epi_hit = any(t in text for t in epi_limbus_terms)
    reconstruction_hit = any(t in text for t in reconstruction_terms)
    benchmark_hit = any(t in text for t in benchmark_terms)

    score = sum([scaffold_hit, epi_hit, reconstruction_hit, benchmark_hit])

    if scaffold_hit and epi_hit and reconstruction_hit and score >= 3:
        return "Add to epithelium/limbus core", "Clear epithelial/limbal tissue-engineering scaffold/carrier/cell-sheet signal with reconstruction or regeneration relevance."

    if scaffold_hit and epi_hit and score >= 3:
        return "Manual check", "Likely relevant, but reconstruction/regeneration signal is not strong enough for automatic addition."

    return "Exclude/background", "Insufficient epithelial/limbal scaffold/carrier reconstruction benchmarking signal."

out_rows = []

for r in rows:
    out = dict(r)
    decision, reason = strict_decision(r)
    out["strict_epithelium_limbus_decision"] = decision
    out["strict_epithelium_limbus_reason"] = reason
    out_rows.append(out)

with OUTPUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=out_rows[0].keys())
    writer.writeheader()
    writer.writerows(out_rows)

decision_counts = Counter(r["strict_epithelium_limbus_decision"] for r in out_rows)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# Strict Medium-Priority Epithelium/Limbus Additions Report\n\n")

    f.write("## Purpose\n\n")
    f.write("This report applies stricter rules to medium-priority epithelium/limbus records before adding them to the PubMed core pool. The goal is to strengthen the epithelial/limbal layer without contaminating the extraction set with contact lens, dry-eye drug-delivery, generic cell-biology, or weakly relevant surgical/background papers.\n\n")

    f.write("## Strict Decision Counts\n\n")
    for k, v in decision_counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Records Recommended for Epithelium/Limbus Core Addition\n\n")
    for r in out_rows:
        if r["strict_epithelium_limbus_decision"] == "Add to epithelium/limbus core":
            f.write(f"- {r['screening_id']} / PMID {r['pmid']}: {r['title']}\n")

    f.write("\n## Manual Check Records\n\n")
    for r in out_rows:
        if r["strict_epithelium_limbus_decision"] == "Manual check":
            f.write(f"- {r['screening_id']} / PMID {r['pmid']}: {r['title']}\n")

    f.write("\n## Exclude/Background Records\n\n")
    for r in out_rows:
        if r["strict_epithelium_limbus_decision"] == "Exclude/background":
            f.write(f"- {r['screening_id']} / PMID {r['pmid']}: {r['title']} — {r['strict_epithelium_limbus_reason']}\n")

print("Strict epithelium/limbus additions file created.")
print("Strict decision counts:")
for k, v in decision_counts.items():
    print(f"{k}: {v}")
