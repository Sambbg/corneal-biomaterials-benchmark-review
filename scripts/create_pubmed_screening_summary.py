from pathlib import Path
import csv
from collections import Counter

MASTER = Path("screening/title_abstract/pubmed_title_abstract_screening.csv")
SUMMARY = Path("screening/title_abstract/pubmed_title_abstract_screening_summary.md")
NEXT_STAGE = Path("screening/full_text/pubmed_include_uncertain_for_full_text_review.csv")
INCLUDE_ONLY = Path("screening/full_text/pubmed_include_only_records.csv")
EXCLUDE_ONLY = Path("screening/title_abstract/pubmed_excluded_records.csv")

with MASTER.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))
    fieldnames = f.readline()

decision_counts = Counter(r["decision"] if r["decision"] else "Unscreened" for r in rows)
layer_counts = Counter(r["corneal_layer"] if r["corneal_layer"] else "Unclear/blank" for r in rows)
priority_counts = Counter(r["priority_level"] if r["priority_level"] else "No priority" for r in rows)

include_uncertain = [r for r in rows if r["decision"] in ["Include", "Uncertain"]]
include_only = [r for r in rows if r["decision"] == "Include"]
exclude_only = [r for r in rows if r["decision"] == "Exclude"]

def write_csv(path, data):
    if not data:
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

write_csv(NEXT_STAGE, include_uncertain)
write_csv(INCLUDE_ONLY, include_only)
write_csv(EXCLUDE_ONLY, exclude_only)

with SUMMARY.open("w", encoding="utf-8") as f:
    f.write("# PubMed Title/Abstract Screening Summary\n\n")

    f.write("## Screening Completion Status\n\n")
    f.write(f"- Total unique PubMed records screened: {len(rows)}\n")
    f.write(f"- Records moved forward for full-text/manual audit: {len(include_uncertain)}\n")
    f.write(f"- Include-only records: {len(include_only)}\n")
    f.write(f"- Excluded records: {len(exclude_only)}\n\n")

    f.write("## Final Decision Counts\n\n")
    for k, v in decision_counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Corneal Layer Counts\n\n")
    for k, v in layer_counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Priority Counts\n\n")
    for k, v in priority_counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Output Files\n\n")
    f.write(f"- Include + Uncertain for full-text/manual audit: `{NEXT_STAGE}`\n")
    f.write(f"- Include-only records: `{INCLUDE_ONLY}`\n")
    f.write(f"- Excluded records: `{EXCLUDE_ONLY}`\n")

print("PubMed screening summary created.")
print("Final decision counts:")
for k, v in decision_counts.items():
    print(f"{k}: {v}")
print(f"Include + Uncertain records for next stage: {len(include_uncertain)}")
print(f"Include-only records: {len(include_only)}")
print(f"Excluded records: {len(exclude_only)}")
