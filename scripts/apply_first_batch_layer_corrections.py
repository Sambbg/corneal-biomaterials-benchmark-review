from pathlib import Path
import csv
from collections import Counter

INPUT = Path("screening/full_text/pubmed_balanced_first_retrieval_batch.csv")
AUDIT = Path("screening/full_text/pubmed_first_batch_layer_label_audit.csv")

OUTPUT = Path("screening/full_text/pubmed_corrected_first_retrieval_batch.csv")
CORRECTIONS_OUTPUT = Path("screening/full_text/pubmed_first_batch_layer_corrections_applied.csv")
REPORT = Path("screening/full_text/pubmed_corrected_first_retrieval_batch_report.md")

# Manual supervisor-level corrections based on title/abstract audit.
# These are not blindly copied from the automated inference.
MANUAL_LAYER_CORRECTIONS = {
    "30989737": "endothelium",      # high-density human corneal endothelial equivalent
    "31751429": "endothelium",      # endothelial damage + cultured corneal endothelium
    "30339045": "endothelium",      # cultured porcine corneal endothelial cells

    "29637812": "epithelium_limbus", # cultivated oral mucosal epithelial cell sheets for LSCD
    "29978836": "multiple_layers",   # limbal reconstruction with lenticule/collagen construct
    "33542377": "multiple_layers",   # anterior corneal surface reconstruction
    "35769102": "multiple_layers",   # corneal implant/regeneration capacity

    "33603277": "stroma",           # corneal defect filler; collagen/HA matrix
    "34400306": "stroma",           # acellular porcine corneal stroma hydrogel
    "36040708": "stroma",           # hydrogel for corneal regeneration/large defects
    "36063670": "stroma",           # lamellar cornea + acellular porcine corneal stroma
    "36638943": "stroma",           # electrospun scaffold + hydrogel for wound healing
    "36844364": "stroma",           # sutureless corneal repair hydrogel
    "37019117": "stroma",           # hydrogel lenticule/refractive correction

    "29176452": "multiple_layers",  # corneal perforation sealing, not purely stromal
    "29883810": "stroma",           # corneal stroma explicitly
    "34665455": "stroma",           # GelMA for corneal tissue engineering, stromal context
    "37731910": "stroma",           # corneal stromal regeneration
    "40613723": "stroma",           # artificial cornea scaffold, stromal/artificial cornea relevance
    "41947731": "stroma",           # stromal keratocyte maintenance/repair
}

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

with AUDIT.open(newline="", encoding="utf-8-sig") as f:
    audit_rows = list(csv.DictReader(f))

audit_by_pmid = {r["pmid"]: r for r in audit_rows}

corrected_rows = []
correction_rows = []

for r in rows:
    out = dict(r)
    pmid = r.get("pmid", "")
    original_layer = r.get("corneal_layer", "")

    if pmid in MANUAL_LAYER_CORRECTIONS:
        corrected_layer = MANUAL_LAYER_CORRECTIONS[pmid]
        out["original_corneal_layer"] = original_layer
        out["corneal_layer"] = corrected_layer
        out["layer_correction_status"] = "corrected"
        out["layer_correction_basis"] = "manual correction after first-batch layer-label audit"

        audit = audit_by_pmid.get(pmid, {})
        out["audit_inferred_layer"] = audit.get("inferred_layer_from_title_abstract", "")

        correction_rows.append(out)
    else:
        out["original_corneal_layer"] = original_layer
        out["layer_correction_status"] = "unchanged"
        out["layer_correction_basis"] = ""
        out["audit_inferred_layer"] = audit_by_pmid.get(pmid, {}).get("inferred_layer_from_title_abstract", "")

    corrected_rows.append(out)

fieldnames = list(corrected_rows[0].keys())

with OUTPUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(corrected_rows)

with CORRECTIONS_OUTPUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(correction_rows)

original_counts = Counter(r.get("original_corneal_layer", "") for r in corrected_rows)
corrected_counts = Counter(r.get("corneal_layer", "") for r in corrected_rows)
status_counts = Counter(r.get("layer_correction_status", "") for r in corrected_rows)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# Corrected First PubMed Retrieval Batch Report\n\n")

    f.write("## Purpose\n\n")
    f.write("This report applies manual layer-label corrections to the first PubMed retrieval batch after the automated layer-label audit flagged possible inconsistencies.\n\n")

    f.write("## Counts\n\n")
    f.write(f"- First-batch records checked: {len(corrected_rows)}\n")
    f.write(f"- Records manually corrected: {len(correction_rows)}\n\n")

    f.write("## Correction Status Counts\n\n")
    for k, v in status_counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Original Layer Counts\n\n")
    for k, v in original_counts.most_common():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Corrected Layer Counts\n\n")
    for k, v in corrected_counts.most_common():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Corrections Applied\n\n")
    for r in correction_rows:
        f.write(
            f"- {r['screening_id']} / PMID {r['pmid']}: "
            f"{r['original_corneal_layer']} → {r['corneal_layer']} — {r['title']}\n"
        )

    f.write("\n## Output Files\n\n")
    f.write(f"- Corrected first retrieval batch: `{OUTPUT}`\n")
    f.write(f"- Corrections applied only: `{CORRECTIONS_OUTPUT}`\n")

print("Corrected first PubMed retrieval batch created.")
print(f"First-batch records checked: {len(corrected_rows)}")
print(f"Records manually corrected: {len(correction_rows)}")
print("Corrected layer counts:")
for k, v in corrected_counts.most_common():
    print(f"{k}: {v}")
