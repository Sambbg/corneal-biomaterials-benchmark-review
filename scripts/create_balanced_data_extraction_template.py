from pathlib import Path
import csv
from collections import Counter

INPUT = Path("screening/full_text/pubmed_balanced_final_core_records.csv")
OUTPUT = Path("extraction/pubmed_balanced_core_data_extraction_template.csv")
REPORT = Path("extraction/pubmed_balanced_core_data_extraction_template_report.md")

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

base_fields = [
    "screening_id",
    "pmid",
    "title",
    "year",
    "journal",
    "doi",
    "corneal_layer",
    "priority_level",
    "strict_final_status"
]

extraction_fields = [
    "extraction_status",
    "study_type",
    "target_layer_final",
    "biomaterial_category",
    "specific_materials",
    "fabrication_method",
    "scaffold_architecture",
    "cell_type_used",
    "cell_source",
    "growth_factors_or_bioactive_agents",
    "optical_transparency_reported",
    "optical_metric_details",
    "mechanical_testing_reported",
    "mechanical_metric_details",
    "biological_testing_reported",
    "biological_metric_details",
    "in_vitro_model",
    "ex_vivo_model",
    "animal_model",
    "clinical_evidence",
    "follow_up_duration",
    "main_outcomes",
    "main_limitations",
    "translational_readiness_level",
    "benchmarking_relevance",
    "include_in_final_review",
    "extraction_notes"
]

fieldnames = base_fields + extraction_fields

out_rows = []

for r in rows:
    out = {field: "" for field in fieldnames}

    for field in base_fields:
        out[field] = r.get(field, "")

    out["extraction_status"] = "not_started"
    out_rows.append(out)

with OUTPUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(out_rows)

layer_counts = Counter(r.get("corneal_layer", "") for r in rows)
status_counts = Counter(r.get("strict_final_status", "") for r in rows)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# Balanced PubMed Core Data Extraction Template Report\n\n")

    f.write("## Purpose\n\n")
    f.write("This extraction template is designed for the balanced final PubMed core. It captures layer-specific biomaterial, optical, mechanical, biological, and translational evidence for corneal tissue engineering.\n\n")

    f.write("## Records Included\n\n")
    f.write(f"- Records prepared for extraction: {len(out_rows)}\n\n")

    f.write("## Records by Layer\n\n")
    for k, v in layer_counts.most_common():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Core Status Counts\n\n")
    for k, v in status_counts.most_common():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Key Benchmarking Domains\n\n")
    f.write("- Optical performance\n")
    f.write("- Mechanical performance\n")
    f.write("- Biological/cytocompatibility performance\n")
    f.write("- In vitro, ex vivo, animal, or clinical performance\n")
    f.write("- Translational readiness\n")
    f.write("- Layer-specific relevance\n\n")

    f.write("## Output File\n\n")
    f.write(f"- `{OUTPUT}`\n")

print("Balanced data extraction template created.")
print(f"Records prepared for extraction: {len(out_rows)}")
print("Records by layer:")
for k, v in layer_counts.most_common():
    print(f"{k}: {v}")
