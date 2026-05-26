from pathlib import Path
import csv
from collections import Counter

MASTER = Path("screening/title_abstract/pubmed_title_abstract_screening.csv")

OUT_DIR = Path("screening/full_text")
HIGH = OUT_DIR / "pubmed_high_priority_include_records.csv"
MEDIUM = OUT_DIR / "pubmed_medium_priority_include_records.csv"
UNCERTAIN = OUT_DIR / "pubmed_uncertain_records_for_manual_audit.csv"
REPORT = OUT_DIR / "pubmed_full_text_prioritisation_report.md"

with MASTER.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

high = [r for r in rows if r["decision"] == "Include" and r["priority_level"] == "High"]
medium = [r for r in rows if r["decision"] == "Include" and r["priority_level"] == "Medium"]
uncertain = [r for r in rows if r["decision"] == "Uncertain"]

def write_csv(path, data):
    if not data:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

write_csv(HIGH, high)
write_csv(MEDIUM, medium)
write_csv(UNCERTAIN, uncertain)

layer_high = Counter(r["corneal_layer"] for r in high)
layer_medium = Counter(r["corneal_layer"] for r in medium)
layer_uncertain = Counter(r["corneal_layer"] for r in uncertain)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# PubMed Full-Text Prioritisation Report\n\n")

    f.write("## Purpose\n\n")
    f.write("This report separates screened PubMed records into practical groups for the next review stage. High-priority Include records should be checked first for full-text retrieval and data extraction suitability.\n\n")

    f.write("## Priority Groups\n\n")
    f.write(f"- High-priority Include records: {len(high)}\n")
    f.write(f"- Medium-priority Include records: {len(medium)}\n")
    f.write(f"- Uncertain records requiring manual audit: {len(uncertain)}\n")
    f.write(f"- Total records carried forward: {len(high) + len(medium) + len(uncertain)}\n\n")

    f.write("## High-Priority Include Records by Layer\n\n")
    for k, v in layer_high.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Medium-Priority Include Records by Layer\n\n")
    for k, v in layer_medium.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Uncertain Records by Layer\n\n")
    for k, v in layer_uncertain.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Recommended Next Step\n\n")
    f.write("Start with the high-priority Include records. These are the most likely to provide extractable evidence for biomaterial/scaffold/cell-construct benchmarking. Medium-priority records should be used after the high-priority pool is mapped. Uncertain records should be audited manually before full-text retrieval.\n\n")

    f.write("## Output Files\n\n")
    f.write(f"- `{HIGH}`\n")
    f.write(f"- `{MEDIUM}`\n")
    f.write(f"- `{UNCERTAIN}`\n")

print("PubMed priority lists created.")
print(f"High-priority Include records: {len(high)}")
print(f"Medium-priority Include records: {len(medium)}")
print(f"Uncertain records requiring manual audit: {len(uncertain)}")
print(f"Total carried forward: {len(high) + len(medium) + len(uncertain)}")
