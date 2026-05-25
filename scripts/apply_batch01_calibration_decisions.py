from pathlib import Path
import csv

CSV_PATH = Path("screening/title_abstract/working/pubmed_screening_batch_01_CALIBRATION_10.csv")
NOTES_PATH = Path("screening/title_abstract/working/pubmed_screening_batch_01_calibration_notes.md")

decisions = {
    "PUBMED_0001": {
        "decision": "Uncertain",
        "exclusion_reason": "",
        "corneal_layer": "stroma",
        "priority_level": "Low",
        "screening_notes": "Human corneal fibroblast wound-healing/ECM biology model. Relevant to stromal repair biology and transparency/fibrosis background, but no clear biomaterial/scaffold/cell-construct intervention from title/abstract. Manual audit needed."
    },
    "PUBMED_0002": {
        "decision": "Include",
        "exclusion_reason": "",
        "corneal_layer": "stroma",
        "priority_level": "High",
        "screening_notes": "Direct corneal stromal tissue engineering paper. Scaffold-free stromal construct using corneal stromal stem cells; strong candidate for extraction."
    },
    "PUBMED_0003": {
        "decision": "Include",
        "exclusion_reason": "",
        "corneal_layer": "stroma",
        "priority_level": "High",
        "screening_notes": "Direct stromal tissue engineering/regeneration study using chitosan-supported keratocyte spheroids in an animal stromal defect model."
    },
    "PUBMED_0004": {
        "decision": "Include",
        "exclusion_reason": "",
        "corneal_layer": "multiple_layers",
        "priority_level": "High",
        "screening_notes": "Multi-layered silk film coculture system involving corneal epithelial and stromal stem cells. Relevant to layered corneal tissue engineering and scaffold design."
    },
    "PUBMED_0005": {
        "decision": "Exclude",
        "exclusion_reason": "Book chapter/background clinical overview",
        "corneal_layer": "unclear",
        "priority_level": "",
        "screening_notes": "Neurotrophic keratitis appears to be clinical/background overview rather than biomaterial, scaffold, cell-engineering, or regenerative construct evidence."
    },
    "PUBMED_0006": {
        "decision": "Uncertain",
        "exclusion_reason": "",
        "corneal_layer": "unclear",
        "priority_level": "Low",
        "screening_notes": "Biomechanical constitutive model of human cornea. Potentially useful for mechanical benchmarking background, but not clearly a corneal tissue engineering biomaterial/scaffold study."
    },
    "PUBMED_0007": {
        "decision": "Exclude",
        "exclusion_reason": "General ophthalmology/no engineering content",
        "corneal_layer": "stroma",
        "priority_level": "",
        "screening_notes": "Clinical/surgical prediction paper for DALK perforation risk in keratoconus. No clear biomaterial, scaffold, regenerative construct, or tissue engineering content."
    },
    "PUBMED_0008": {
        "decision": "Include",
        "exclusion_reason": "",
        "corneal_layer": "stroma",
        "priority_level": "High",
        "screening_notes": "Direct comparison of collagen foam, PLLA nanofiber mesh, and decellularized matrices for corneal regeneration. Excellent benchmarking candidate."
    },
    "PUBMED_0009": {
        "decision": "Exclude",
        "exclusion_reason": "General ophthalmology/no engineering content",
        "corneal_layer": "endothelium",
        "priority_level": "",
        "screening_notes": "Clinical DMEK tamponade comparison. Surgical management topic, not biomaterial/scaffold/cell-engineering evidence for this review."
    },
    "PUBMED_0010": {
        "decision": "Include",
        "exclusion_reason": "",
        "corneal_layer": "epithelium_limbus",
        "priority_level": "High",
        "screening_notes": "Clinical corneal reconstruction using cultured oral mucosal epithelial cell sheets. Relevant cell-sheet engineering construct even though biomaterial-free."
    },
}

with CSV_PATH.open(newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fieldnames = reader.fieldnames

for row in rows:
    sid = row["screening_id"]
    if sid in decisions:
        for key, value in decisions[sid].items():
            row[key] = value

with CSV_PATH.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

include_count = sum(1 for r in rows if r["decision"] == "Include")
exclude_count = sum(1 for r in rows if r["decision"] == "Exclude")
uncertain_count = sum(1 for r in rows if r["decision"] == "Uncertain")

with NOTES_PATH.open("w", encoding="utf-8") as f:
    f.write("# PubMed Batch 01 Calibration Notes\n\n")
    f.write("## Calibration Summary\n\n")
    f.write(f"- Total records: {len(rows)}\n")
    f.write(f"- Include: {include_count}\n")
    f.write(f"- Exclude: {exclude_count}\n")
    f.write(f"- Uncertain: {uncertain_count}\n\n")

    f.write("## Interpretation\n\n")
    f.write("The calibration threshold is intentionally conservative. Records are included when they clearly involve corneal tissue engineering, biomaterials, scaffolds, cell sheets, regenerative constructs, or direct corneal regeneration models. Records are marked uncertain when they may support benchmarking or biological context but do not clearly involve a tissue-engineered material or construct.\n\n")

    f.write("## Record-Level Decisions\n\n")
    for r in rows:
        f.write(f"### {r['screening_id']} / PMID {r['pmid']}\n\n")
        f.write(f"**Title:** {r['title']}\n\n")
        f.write(f"**Decision:** {r['decision']}\n\n")
        f.write(f"**Layer:** {r['corneal_layer']}\n\n")
        f.write(f"**Priority:** {r['priority_level']}\n\n")
        if r["exclusion_reason"]:
            f.write(f"**Exclusion reason:** {r['exclusion_reason']}\n\n")
        f.write(f"**Rationale:** {r['screening_notes']}\n\n")

print("Calibration decisions applied.")
print(f"Include: {include_count}")
print(f"Exclude: {exclude_count}")
print(f"Uncertain: {uncertain_count}")
