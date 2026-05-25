from pathlib import Path
import csv
from collections import Counter

INPUT = Path("screening/title_abstract/working/pubmed_screening_batch_01_FIRST_PASS.csv")
OUTPUT = Path("screening/title_abstract/working/pubmed_screening_batch_01_CORRECTED.csv")
REPORT = Path("screening/title_abstract/working/pubmed_screening_batch_01_corrected_report.md")

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
]

def infer_layer(text, sources):
    combined = f"{text} {sources}".lower()
    if "epithelial" in combined or "epithelium" in combined or "limbal" in combined or "limbus" in combined:
        if "stromal" in combined or "stroma" in combined:
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
        row["screening_notes"] = "Corrected include: title/abstract indicates corneal tissue engineering, biomaterial/scaffold, engineered construct, decellularized matrix, cell sheet, or regeneration/reconstruction relevance."
    elif has_routine_clinical:
        row["decision"] = "Exclude"
        row["exclusion_reason"] = "General ophthalmology/no engineering content"
        row["priority_level"] = ""
        row["screening_notes"] = "Corrected exclude: routine clinical/surgical keratoplasty, DMEK/DSAEK/DALK, imaging, outcome, or complication paper without clear biomaterial/scaffold/tissue-engineering construct relevance."
    elif has_background:
        row["decision"] = "Uncertain"
        row["exclusion_reason"] = ""
        row["priority_level"] = "Low"
        row["screening_notes"] = "Corrected uncertain: may support biological, optical, or mechanical benchmarking background, but not clearly a tissue-engineered material or construct."
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

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# PubMed Batch 01 Corrected Screening Report\n\n")
    f.write("## Why Correction Was Needed\n\n")
    f.write("The first-pass screening over-included routine clinical keratoplasty and DMEK/DSAEK/DALK papers because broad words such as matrix, membrane, and film produced false positives.\n\n")
    f.write("## Corrected Decision Counts\n\n")
    for k, v in counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Corrected Layer Counts\n\n")
    for k, v in layers.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Corrected Threshold\n\n")
    f.write("Include only when the title/abstract clearly indicates biomaterial, scaffold, engineered construct, cell sheet, decellularized matrix, tissue engineering, or corneal regeneration/reconstruction relevance.\n\n")
    f.write("Exclude routine clinical ophthalmology, keratoplasty, DMEK/DSAEK/DALK, imaging, outcomes, and surgical complication papers unless they clearly involve tissue engineering or biomaterial development.\n\n")
    f.write("Use Uncertain for biomechanics, collagen organization, wound healing, and model papers that may support benchmarking but are not clearly biomaterial/construct studies.\n")

print("Corrected Batch 01 screening complete.")
print("Decision counts:")
for k, v in counts.items():
    print(f"{k}: {v}")
print("Layer counts:")
for k, v in layers.items():
    print(f"{k}: {v}")
print(f"Output: {OUTPUT}")
print(f"Report: {REPORT}")
