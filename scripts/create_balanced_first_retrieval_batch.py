from pathlib import Path
import csv
from collections import Counter, defaultdict

INPUT = Path("screening/full_text/pubmed_strict_retrieval_shortlist.csv")
OUTPUT = Path("screening/full_text/pubmed_balanced_first_retrieval_batch.csv")
LATER_OUTPUT = Path("screening/full_text/pubmed_remaining_after_first_retrieval_batch.csv")
REPORT = Path("screening/full_text/pubmed_balanced_first_retrieval_batch_report.md")

TARGET_PER_LAYER = 20

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

rows_by_layer = defaultdict(list)

for r in rows:
    rows_by_layer[r.get("corneal_layer", "unclear")].append(r)

selected = []
remaining = []

for layer, layer_rows in rows_by_layer.items():
    layer_rows.sort(
        key=lambda r: (
            -int(r.get("strict_retrieval_score", 0)),
            r.get("screening_id", "")
        )
    )

    selected.extend(layer_rows[:TARGET_PER_LAYER])
    remaining.extend(layer_rows[TARGET_PER_LAYER:])

selected_pmids = {r["pmid"] for r in selected}

# Add any non-selected records from the original file into remaining, avoiding duplicates
for r in rows:
    if r["pmid"] not in selected_pmids and r not in remaining:
        remaining.append(r)

selected.sort(
    key=lambda r: (
        r.get("corneal_layer", ""),
        -int(r.get("strict_retrieval_score", 0)),
        r.get("screening_id", "")
    )
)

remaining.sort(
    key=lambda r: (
        r.get("corneal_layer", ""),
        -int(r.get("strict_retrieval_score", 0)),
        r.get("screening_id", "")
    )
)

def write_csv(path, data):
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

write_csv(OUTPUT, selected)
write_csv(LATER_OUTPUT, remaining)

selected_layer_counts = Counter(r.get("corneal_layer", "") for r in selected)
remaining_layer_counts = Counter(r.get("corneal_layer", "") for r in remaining)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# Balanced First Retrieval Batch Report\n\n")

    f.write("## Purpose\n\n")
    f.write("This report creates a balanced first-pass full-text retrieval batch from the strict PubMed retrieval shortlist. Instead of retrieving more than 200 papers immediately, this selects the top-scoring records within each corneal layer.\n\n")

    f.write("## Selection Rule\n\n")
    f.write(f"- Select top {TARGET_PER_LAYER} records per corneal layer based on strict retrieval score.\n")
    f.write("- This protects the layer-specific structure of the review and prevents the retrieval phase from becoming inefficient.\n\n")

    f.write("## Counts\n\n")
    f.write(f"- Records in strict retrieval shortlist: {len(rows)}\n")
    f.write(f"- Records selected for first retrieval batch: {len(selected)}\n")
    f.write(f"- Records remaining after first batch: {len(remaining)}\n\n")

    f.write("## First Retrieval Batch by Layer\n\n")
    for k, v in selected_layer_counts.most_common():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Remaining Records by Layer\n\n")
    for k, v in remaining_layer_counts.most_common():
        f.write(f"- {k}: {v}\n")

    f.write("\n## First Retrieval Batch Records\n\n")
    for r in selected:
        f.write(f"- {r['screening_id']} / PMID {r['pmid']} / score {r['strict_retrieval_score']} / {r['corneal_layer']}: {r['title']}\n")

    f.write("\n## Output Files\n\n")
    f.write(f"- First retrieval batch: `{OUTPUT}`\n")
    f.write(f"- Remaining records: `{LATER_OUTPUT}`\n")

print("Balanced first retrieval batch created.")
print(f"Records in strict retrieval shortlist: {len(rows)}")
print(f"Records selected for first retrieval batch: {len(selected)}")
print(f"Records remaining after first batch: {len(remaining)}")
print("First retrieval batch by layer:")
for k, v in selected_layer_counts.most_common():
    print(f"{k}: {v}")
