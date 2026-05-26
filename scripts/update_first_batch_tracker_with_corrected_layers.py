from pathlib import Path
import csv
from collections import Counter

CORRECTED_BATCH = Path("screening/full_text/pubmed_corrected_first_retrieval_batch.csv")
TRACKER = Path("screening/full_text/pubmed_first_batch_retrieval_tracker.csv")
OUTPUT = Path("screening/full_text/pubmed_first_batch_retrieval_tracker_corrected_layers.csv")
REPORT = Path("screening/full_text/pubmed_first_batch_retrieval_tracker_corrected_layers_report.md")

with CORRECTED_BATCH.open(newline="", encoding="utf-8-sig") as f:
    corrected_rows = list(csv.DictReader(f))

with TRACKER.open(newline="", encoding="utf-8-sig") as f:
    tracker_rows = list(csv.DictReader(f))

corrected_by_pmid = {r["pmid"]: r for r in corrected_rows}

out_rows = []
changed = []

for r in tracker_rows:
    out = dict(r)
    pmid = r.get("pmid", "")
    corrected = corrected_by_pmid.get(pmid)

    if corrected:
        old_layer = out.get("corneal_layer", "")
        new_layer = corrected.get("corneal_layer", "")

        out["original_corneal_layer"] = corrected.get("original_corneal_layer", old_layer)
        out["corneal_layer"] = new_layer
        out["layer_correction_status"] = corrected.get("layer_correction_status", "")
        out["audit_inferred_layer"] = corrected.get("audit_inferred_layer", "")

        if old_layer != new_layer:
            changed.append(out)

    out_rows.append(out)

fieldnames = list(out_rows[0].keys())

with OUTPUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(out_rows)

layer_counts = Counter(r.get("corneal_layer", "") for r in out_rows)
status_counts = Counter(r.get("layer_correction_status", "") for r in out_rows)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# First Batch Retrieval Tracker Corrected Layers Report\n\n")

    f.write("## Purpose\n\n")
    f.write("This report creates an updated first-batch retrieval tracker using the manually corrected biological layer labels.\n\n")

    f.write("## Counts\n\n")
    f.write(f"- Tracker records updated: {len(out_rows)}\n")
    f.write(f"- Records with actual layer-label changes: {len(changed)}\n\n")

    f.write("## Corrected Layer Counts\n\n")
    for k, v in layer_counts.most_common():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Layer Correction Status Counts\n\n")
    for k, v in status_counts.most_common():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Records with Changed Layer Labels\n\n")
    for r in changed:
        f.write(
            f"- {r['screening_id']} / PMID {r['pmid']}: "
            f"{r['original_corneal_layer']} → {r['corneal_layer']} — {r['title']}\n"
        )

    f.write("\n## Output File\n\n")
    f.write(f"- `{OUTPUT}`\n")

print("Corrected-layer first batch retrieval tracker created.")
print(f"Tracker records updated: {len(out_rows)}")
print(f"Records with actual layer-label changes: {len(changed)}")
print("Corrected layer counts:")
for k, v in layer_counts.most_common():
    print(f"{k}: {v}")
