from pathlib import Path
import csv
from collections import Counter

INPUT = Path("screening/title_abstract/working/pubmed_screening_batch_01_CORRECTED.csv")
OUTPUT = Path("screening/title_abstract/working/pubmed_screening_batch_01_corrected_audit_summary.md")

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

decision_counts = Counter(r["decision"] for r in rows)
layer_counts = Counter(r["corneal_layer"] for r in rows)
priority_counts = Counter(r["priority_level"] for r in rows if r["priority_level"])

includes = [r for r in rows if r["decision"] == "Include"]
uncertain = [r for r in rows if r["decision"] == "Uncertain"]
excluded = [r for r in rows if r["decision"] == "Exclude"]

with OUTPUT.open("w", encoding="utf-8") as f:
    f.write("# Corrected PubMed Batch 01 Audit Summary\n\n")

    f.write("## Decision Counts\n\n")
    for k, v in decision_counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Layer Counts\n\n")
    for k, v in layer_counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Priority Counts\n\n")
    for k, v in priority_counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Included Records\n\n")
    for r in includes:
        f.write(f"- {r['screening_id']} / PMID {r['pmid']} — {r['title']} [{r['corneal_layer']}, {r['priority_level']}]\n")

    f.write("\n## Uncertain Records Requiring Manual Review\n\n")
    for r in uncertain:
        f.write(f"- {r['screening_id']} / PMID {r['pmid']} — {r['title']} [{r['corneal_layer']}, {r['priority_level']}]\n")

    f.write("\n## Excluded Records\n\n")
    for r in excluded:
        f.write(f"- {r['screening_id']} / PMID {r['pmid']} — {r['title']} | Reason: {r['exclusion_reason']}\n")

print("Corrected Batch 01 audit summary created.")
print("Decision counts:")
for k, v in decision_counts.items():
    print(f"{k}: {v}")
print("Output:", OUTPUT)
