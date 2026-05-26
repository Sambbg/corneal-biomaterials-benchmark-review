from pathlib import Path
import csv
from collections import Counter

STRICT_CORE_INPUT = Path("screening/full_text/pubmed_strict_final_core_records.csv")
ENDOTHELIUM_INPUT = Path("screening/full_text/pubmed_strict_endothelium_additions.csv")

OUTPUT = Path("screening/full_text/pubmed_expanded_strict_final_core_records.csv")
ENDOTHELIUM_ADDED_OUTPUT = Path("screening/full_text/pubmed_endothelium_records_added_to_core.csv")
REPORT = Path("screening/full_text/pubmed_expanded_strict_final_core_report.md")

with STRICT_CORE_INPUT.open(newline="", encoding="utf-8-sig") as f:
    core_rows = list(csv.DictReader(f))

with ENDOTHELIUM_INPUT.open(newline="", encoding="utf-8-sig") as f:
    endo_rows = list(csv.DictReader(f))

core_pmids = {r["pmid"] for r in core_rows}

manual_keep_pmids = {
    "32603022"  # Designer Descemet Membranes Containing PDLLA and Functionalized Gelatins
}

add_rows = []
for r in endo_rows:
    decision = r.get("strict_endothelium_decision", "")
    pmid = r.get("pmid", "")

    if decision == "Add to endothelial core" or pmid in manual_keep_pmids:
        if pmid not in core_pmids:
            out = dict(r)
            out["corneal_layer"] = "endothelium"
            out["strict_final_status"] = "Added endothelial core from medium-priority screen"
            add_rows.append(out)

# Standardize columns across original core and added records
all_fieldnames = []
for rowset in [core_rows, add_rows]:
    for row in rowset:
        for k in row.keys():
            if k not in all_fieldnames:
                all_fieldnames.append(k)

expanded_rows = []
for r in core_rows + add_rows:
    out = {field: "" for field in all_fieldnames}
    out.update(r)
    expanded_rows.append(out)

with OUTPUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=all_fieldnames)
    writer.writeheader()
    writer.writerows(expanded_rows)

with ENDOTHELIUM_ADDED_OUTPUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=all_fieldnames)
    writer.writeheader()
    for r in add_rows:
        out = {field: "" for field in all_fieldnames}
        out.update(r)
        writer.writerow(out)

layer_counts = Counter(r.get("corneal_layer", "") for r in expanded_rows)
status_counts = Counter(r.get("strict_final_status", "") for r in expanded_rows)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# Expanded Strict Final PubMed Core Report\n\n")

    f.write("## Purpose\n\n")
    f.write("This report expands the strict final PubMed core by adding selected medium-priority endothelial biomaterial records to correct underrepresentation of the corneal endothelium layer.\n\n")

    f.write("## Counts\n\n")
    f.write(f"- Strict final PubMed core before endothelial expansion: {len(core_rows)}\n")
    f.write(f"- Endothelial records added from medium-priority screen: {len(add_rows)}\n")
    f.write(f"- Expanded strict final PubMed core records: {len(expanded_rows)}\n\n")

    f.write("## Expanded Core Records by Layer\n\n")
    for k, v in layer_counts.most_common():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Status Counts\n\n")
    for k, v in status_counts.most_common():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Endothelial Records Added\n\n")
    for r in add_rows:
        f.write(f"- {r['screening_id']} / PMID {r['pmid']}: {r['title']}\n")

    f.write("\n## Output Files\n\n")
    f.write(f"- Expanded strict final core: `{OUTPUT}`\n")
    f.write(f"- Added endothelial records only: `{ENDOTHELIUM_ADDED_OUTPUT}`\n")

print("Expanded strict final PubMed core created.")
print(f"Strict final core before endothelial expansion: {len(core_rows)}")
print(f"Endothelial records added from medium-priority screen: {len(add_rows)}")
print(f"Expanded strict final PubMed core records: {len(expanded_rows)}")
print("Expanded core by layer:")
for k, v in layer_counts.most_common():
    print(f"{k}: {v}")
