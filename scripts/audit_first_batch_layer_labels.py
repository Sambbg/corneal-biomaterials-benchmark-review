from pathlib import Path
import csv
from collections import Counter

INPUT = Path("screening/full_text/pubmed_balanced_first_retrieval_batch.csv")
OUTPUT = Path("screening/full_text/pubmed_first_batch_layer_label_audit.csv")
REPORT = Path("screening/full_text/pubmed_first_batch_layer_label_audit_report.md")

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

def infer_layer(row):
    text = f"{row.get('title','')} {row.get('abstract','')}".lower()

    endothelial_terms = [
        "endothelium", "endothelial", "descemet", "dmek", "pdek",
        "endothelial keratoplasty", "corneal endothelial"
    ]

    epithelium_limbus_terms = [
        "epithelium", "epithelial", "limbal", "limbus",
        "ocular surface", "oral mucosal", "limbal stem cell"
    ]

    stroma_terms = [
        "stroma", "stromal", "keratocyte", "lamellar",
        "lenticule", "intrastromal", "stromal pocket"
    ]

    full_multilayer_terms = [
        "full-thickness", "full thickness", "bilayer", "multi-layer",
        "multilayer", "epithelium/stroma", "epithelial-stromal",
        "corneal substitute", "artificial cornea"
    ]

    hits = {
        "endothelium": any(t in text for t in endothelial_terms),
        "epithelium_limbus": any(t in text for t in epithelium_limbus_terms),
        "stroma": any(t in text for t in stroma_terms),
        "multiple_layers": any(t in text for t in full_multilayer_terms),
    }

    # Priority logic: explicit endothelium and explicit epithelium/limbus should override broad stroma labels.
    if hits["endothelium"] and not hits["epithelium_limbus"]:
        inferred = "endothelium"
    elif hits["epithelium_limbus"] and not hits["endothelium"] and not hits["stroma"]:
        inferred = "epithelium_limbus"
    elif hits["multiple_layers"]:
        inferred = "multiple_layers"
    elif hits["stroma"]:
        inferred = "stroma"
    elif hits["epithelium_limbus"]:
        inferred = "epithelium_limbus"
    elif hits["endothelium"]:
        inferred = "endothelium"
    else:
        inferred = "unclear"

    return inferred, hits

out_rows = []

for r in rows:
    out = dict(r)
    current = r.get("corneal_layer", "")
    inferred, hits = infer_layer(r)

    out["inferred_layer_from_title_abstract"] = inferred
    out["layer_label_audit_decision"] = "label_ok" if inferred == current else "manual_check"
    out["has_endothelium_terms"] = "yes" if hits["endothelium"] else "no"
    out["has_epithelium_limbus_terms"] = "yes" if hits["epithelium_limbus"] else "no"
    out["has_stroma_terms"] = "yes" if hits["stroma"] else "no"
    out["has_multiple_layer_terms"] = "yes" if hits["multiple_layers"] else "no"
    out_rows.append(out)

with OUTPUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=out_rows[0].keys())
    writer.writeheader()
    writer.writerows(out_rows)

audit_counts = Counter(r["layer_label_audit_decision"] for r in out_rows)
current_layer_counts = Counter(r.get("corneal_layer", "") for r in out_rows)
inferred_layer_counts = Counter(r.get("inferred_layer_from_title_abstract", "") for r in out_rows)

manual_checks = [r for r in out_rows if r["layer_label_audit_decision"] == "manual_check"]

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# First Batch Layer Label Audit Report\n\n")

    f.write("## Purpose\n\n")
    f.write("This audit checks whether the assigned corneal layer labels in the first retrieval batch appear consistent with title/abstract terminology. This is important because the review is explicitly layer-specific.\n\n")

    f.write("## Counts\n\n")
    f.write(f"- First-batch records audited: {len(out_rows)}\n")
    for k, v in audit_counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Current Layer Counts\n\n")
    for k, v in current_layer_counts.most_common():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Inferred Layer Counts\n\n")
    for k, v in inferred_layer_counts.most_common():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Records Requiring Manual Layer Check\n\n")
    for r in manual_checks:
        f.write(
            f"- {r['screening_id']} / PMID {r['pmid']}: "
            f"current={r['corneal_layer']} / inferred={r['inferred_layer_from_title_abstract']} — {r['title']}\n"
        )

    f.write("\n## Output File\n\n")
    f.write(f"- `{OUTPUT}`\n")

print("First batch layer label audit created.")
print(f"First-batch records audited: {len(out_rows)}")
print("Audit counts:")
for k, v in audit_counts.items():
    print(f"{k}: {v}")
print("Inferred layer counts:")
for k, v in inferred_layer_counts.most_common():
    print(f"{k}: {v}")
