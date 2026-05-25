from pathlib import Path
import csv
from collections import Counter

INPUT = Path("screening/title_abstract/working/pubmed_screening_batch_01_WORKING.csv")
OUTPUT = Path("screening/title_abstract/working/pubmed_screening_batch_01_FIRST_PASS.csv")
REPORT = Path("screening/title_abstract/working/pubmed_screening_batch_01_first_pass_report.md")

include_terms = [
    "tissue engineering", "engineered", "bioengineered", "biomaterial",
    "scaffold", "hydrogel", "nanofiber", "nanofibre", "film", "membrane",
    "decellularized", "decellularised", "matrix", "construct", "cell sheet",
    "stromal tissue", "corneal regeneration", "corneal reconstruction",
    "regenerative", "bioprint", "collagen foam", "chitosan", "silk"
]

exclude_terms = [
    "dmek", "descemet membrane endothelial keratoplasty",
    "deep anterior lamellar keratoplasty", "dalk",
    "keratoconus", "tamponade", "clinical outcomes",
    "visual acuity", "case report", "surgical", "diagnostic",
    "tomography", "topography", "intraocular", "contact lens"
]

background_terms = [
    "biomechanical", "mechanical model", "constitutive model",
    "wound healing", "fibrosis", "growth factor", "migration",
    "extracellular matrix"
]

def infer_layer(text, sources):
    combined = f"{text} {sources}".lower()
    if "endotheli" in combined or "descemet" in combined:
        return "endothelium"
    if "stroma" in combined or "stromal" in combined or "keratocyte" in combined:
        return "stroma"
    if "epithelial" in combined or "epithelium" in combined or "limbal" in combined or "limbus" in combined:
        return "epithelium_limbus"
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

    include_hit = any(term in text for term in include_terms)
    exclude_hit = any(term in text for term in exclude_terms)
    background_hit = any(term in text for term in background_terms)

    if include_hit:
        row["decision"] = "Include"
        row["exclusion_reason"] = ""
        row["priority_level"] = "High" if row["source_count"] and int(row["source_count"]) >= 2 else "Medium"
        row["screening_notes"] = "First-pass include: title/abstract indicates corneal tissue engineering, biomaterial/scaffold, engineered construct, regeneration model, or cell-based reconstruction. Requires manual audit."
    elif exclude_hit and not include_hit:
        row["decision"] = "Exclude"
        row["exclusion_reason"] = "General ophthalmology/no engineering content"
        row["priority_level"] = ""
        row["screening_notes"] = "First-pass exclude: appears primarily clinical/surgical/diagnostic with no clear biomaterial, scaffold, regenerative construct, or tissue-engineering content. Requires audit if borderline."
    elif background_hit:
        row["decision"] = "Uncertain"
        row["exclusion_reason"] = ""
        row["priority_level"] = "Low"
        row["screening_notes"] = "First-pass uncertain: relevant to corneal biology/mechanics/wound-healing background, but tissue-engineering material or construct relevance is not clear enough from title/abstract."
    else:
        row["decision"] = "Uncertain"
        row["exclusion_reason"] = ""
        row["priority_level"] = "Low"
        row["screening_notes"] = "First-pass uncertain: insufficient evidence from title/abstract to confidently include or exclude."

with OUTPUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

counts = Counter(r["decision"] for r in rows)
layer_counts = Counter(r["corneal_layer"] for r in rows)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# PubMed Batch 01 First-Pass Screening Report\n\n")
    f.write("## Important Methodological Warning\n\n")
    f.write("This is a first-pass assisted screen, not the final screening decision set. All Include and Uncertain records should be manually audited before merging into the master screening file.\n\n")

    f.write("## Decision Counts\n\n")
    for k, v in counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Layer Counts\n\n")
    for k, v in layer_counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Screening Threshold Used\n\n")
    f.write("Include when title/abstract clearly indicates corneal tissue engineering, biomaterial/scaffold, regenerative construct, cell sheet, engineered corneal tissue, or corneal regeneration model.\n\n")
    f.write("Exclude when title/abstract clearly indicates general ophthalmology, clinical surgery, diagnosis, imaging, or management without engineering relevance.\n\n")
    f.write("Uncertain when the record may support biological/mechanical benchmarking but does not clearly involve a tissue-engineered material or construct.\n")

print("First-pass screening complete.")
print("Decision counts:")
for k, v in counts.items():
    print(f"{k}: {v}")
print("Layer counts:")
for k, v in layer_counts.items():
    print(f"{k}: {v}")
print(f"Output: {OUTPUT}")
print(f"Report: {REPORT}")
