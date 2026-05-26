from pathlib import Path
import csv
from collections import Counter

BASE_INPUT = Path("screening/full_text/pubmed_expanded_strict_final_core_records.csv")
EPI_INPUT = Path("screening/full_text/pubmed_refined_top_tier_epithelium_limbus_core_additions.csv")

OUTPUT = Path("screening/full_text/pubmed_balanced_final_core_records.csv")
EPI_ADDED_OUTPUT = Path("screening/full_text/pubmed_epithelium_limbus_records_added_to_core.csv")
REPORT = Path("screening/full_text/pubmed_balanced_final_core_report.md")

with BASE_INPUT.open(newline="", encoding="utf-8-sig") as f:
    base_rows = list(csv.DictReader(f))

with EPI_INPUT.open(newline="", encoding="utf-8-sig") as f:
    epi_rows = list(csv.DictReader(f))

base_pmids = {r["pmid"] for r in base_rows}

add_rows = []

for r in epi_rows:
    pmid = r.get("pmid", "")

    if pmid not in base_pmids:
        out = dict(r)
        out["corneal_layer"] = "epithelium_limbus"
        out["strict_final_status"] = "Added epithelium/limbus core from medium-priority screen"
        add_rows.append(out)

all_fieldnames = []

for rowset in [base_rows, add_rows]:
    for row in rowset:
        for key in row.keys():
            if key not in all_fieldnames:
                all_fieldnames.append(key)

balanced_rows = []

for r in base_rows + add_rows:
    out = {field: "" for field in all_fieldnames}
    out.update(r)
    balanced_rows.append(out)

with OUTPUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=all_fieldnames)
    writer.writeheader()
    writer.writerows(balanced_rows)

with EPI_ADDED_OUTPUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=all_fieldnames)
    writer.writeheader()
    for r in add_rows:
        out = {field: "" for field in all_fieldnames}
        out.update(r)
        writer.writerow(out)

layer_counts = Counter(r.get("corneal_layer", "") for r in balanced_rows)
status_counts = Counter(r.get("strict_final_status", "") for r in balanced_rows)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# Balanced Final PubMed Core Report\n\n")

    f.write("## Purpose\n\n")
    f.write("This report creates the balanced final PubMed core by combining the expanded strict final PubMed core with refined top-tier epithelium/limbus additions. The goal is to reduce layer imbalance before full-text retrieval and data extraction.\n\n")

    f.write("## Counts\n\n")
    f.write(f"- Expanded strict final PubMed core before epithelium/limbus expansion: {len(base_rows)}\n")
    f.write(f"- Refined epithelium/limbus records added: {len(add_rows)}\n")
    f.write(f"- Balanced final PubMed core records: {len(balanced_rows)}\n\n")

    f.write("## Balanced Final Core Records by Layer\n\n")
    for k, v in layer_counts.most_common():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Status Counts\n\n")
    for k, v in status_counts.most_common():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Epithelium/Limbus Records Added\n\n")
    for r in add_rows:
        f.write(f"- {r['screening_id']} / PMID {r['pmid']}: {r['title']}\n")

    f.write("\n## Output Files\n\n")
    f.write(f"- Balanced final PubMed core: `{OUTPUT}`\n")
    f.write(f"- Added epithelium/limbus records only: `{EPI_ADDED_OUTPUT}`\n")

print("Balanced final PubMed core created.")
print(f"Expanded strict final PubMed core before epithelium/limbus expansion: {len(base_rows)}")
print(f"Refined epithelium/limbus records added: {len(add_rows)}")
print(f"Balanced final PubMed core records: {len(balanced_rows)}")
print("Balanced final core by layer:")
for k, v in layer_counts.most_common():
    print(f"{k}: {v}")
