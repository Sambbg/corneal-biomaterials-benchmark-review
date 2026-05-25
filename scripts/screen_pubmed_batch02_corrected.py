from pathlib import Path
import csv
from collections import Counter

INPUT = Path("screening/title_abstract/working/pubmed_screening_batch_02_WORKING.csv")
OUTPUT = Path("screening/title_abstract/working/pubmed_screening_batch_02_CORRECTED.csv")
REPORT = Path("screening/title_abstract/working/pubmed_screening_batch_02_corrected_report.md")

routine_clinical_terms = [
    "dmek",
    "dsaek",
    "ut-dsaek",
    "pdek",
    "dalk",
    "keratoplasty",
    "descemet membrane endothelial keratoplasty",
    "descemet stripping automated endothelial keratoplasty",
    "deep anterior lamellar keratoplasty",
    "rebubbling",
    "tamponade",
    "visual acuity",
    "clinical outcome",
    "surgical outcomes",
    "graft survival",
    "endothelial cell density",
    "corneal densitometry",
    "scheimpflug",
    "specular microscopy",
    "case series",
    "case report",
    "postoperative",
    "intraoperative",
    "cataract surgery",
    "confocal microscopy",
]

strong_include_terms = [
    "tissue engineering",
    "bioengineered",
    "biomaterial",
    "scaffold",
    "hydrogel",
    "nanofiber",
    "nanofibre",
    "cell sheet",
    "decellularized",
    "decellularised",
    "engineered corneal",
    "corneal regeneration",
    "corneal reconstruction",
    "stromal tissue construct",
    "regenerative construct",
    "bioprint",
    "chitosan",
    "silk film",
    "collagen foam",
    "poly(l-lactic acid)",
    "plla",
    "cultured oral mucosal epithelial cell sheet",
    "limbal epithelial stem cell",
    "corneal stromal stem cell",
    "keratocyte spheroid",
]

background_uncertain_terms = [
    "constitutive model",
    "biomechanical",
    "mechanical model",
    "collagen organization",
    "optical anisotropies",
    "wound healing",
    "growth factor",
    "extracellular matrix",
    "stromal repair",
    "limbal stem cell deficiency model",
    "animal model",
]

def infer_layer(text, sources):
    combined = f"{text} {sources}".lower()
    if "epithelial" in combined or "epithelium" in combined or "limbal" in combined or "limbus" in combined:
        if "stromal" in combined or "stroma" in combined or "endotheli" in combined:
            return "multiple_layers"
        return "epithelium_limbus"
    if "stroma" in combined or "stromal" in combined or "keratocyte" in combined:
        return "stroma"
    if "endotheli" in combined or "descemet" in combined:
        return "endothelium"
    if "full thickness" in combined or "full-thickness" in combined or "multilayer" in combined or "multi-layer" in combined:
        return "full_thickness_multilayer"
    if ";" in sources:
        return "multiple_layers"
    return "unclear"

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fieldnames = reader.fieldnames

for row in rows:
    text = f"{row.get('title','')} {row.get('abstract','')}".lower()
    sources = row.get("sources", "")
    row["corneal_layer"] = infer_layer(text, sources)

    has_strong_include = any(term in text for term in strong_include_terms)
    has_routine_clinical = any(term in text for term in routine_clinical_terms)
    has_background = any(term in text for term in background_uncertain_terms)

    if has_strong_include:
        row["decision"] = "Include"
        row["exclusion_reason"] = ""
        row["priority_level"] = "High" if int(row.get("source_count") or 1) >= 2 else "Medium"
        row["screening_notes"] = "Corrected include: title/abstract indicates corneal tissue engineering, biomaterial/scaffold, engineered construct, decellularized matrix, cell sheet, stem-cell construct, or regeneration/reconstruction relevance."
    elif has_routine_clinical:
        row["decision"] = "Exclude"
        row["exclusion_reason"] = "General ophthalmology/no engineering content"
        row["priority_level"] = ""
        row["screening_notes"] = "Corrected exclude: routine clinical/surgical keratoplasty, DMEK/DSAEK/DALK, imaging, outcome, or complication paper without clear biomaterial/scaffold/tissue-engineering construct relevance."
    elif has_background:
        row["decision"] = "Uncertain"
        row["exclusion_reason"] = ""
        row["priority_level"] = "Low"
        row["screening_notes"] = "Corrected uncertain: may support biological, optical, animal-model, or mechanical benchmarking background, but not clearly a tissue-engineered material or construct."
    else:
        row["decision"] = "Uncertain"
        row["exclusion_reason"] = ""
        row["priority_level"] = "Low"
        row["screening_notes"] = "Corrected uncertain: insufficient title/abstract evidence for confident inclusion or exclusion."

with OUTPUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

counts = Counter(r["decision"] for r in rows)
layers = Counter(r["corneal_layer"] for r in rows)
priorities = Counter(r["priority_level"] for r in rows if r["priority_level"])

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# PubMed Batch 02 Corrected Screening Report\n\n")
    f.write("## Method\n\n")
    f.write("Batch 02 was screened using the corrected threshold developed after Batch 01 audit.\n\n")

    f.write("## Decision Counts\n\n")
    for k, v in counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Layer Counts\n\n")
    for k, v in layers.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Priority Counts\n\n")
    for k, v in priorities.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Warning\n\n")
    f.write("This is a corrected assisted screening pass. Include and Uncertain records should still be audited before full-text retrieval.\n")

print("Batch 02 corrected screening complete.")
print("Decision counts:")
for k, v in counts.items():
    print(f"{k}: {v}")
print("Layer counts:")
for k, v in layers.items():
    print(f"{k}: {v}")
print("Priority counts:")
for k, v in priorities.items():
    print(f"{k}: {v}")
