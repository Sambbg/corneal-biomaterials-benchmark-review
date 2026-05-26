from pathlib import Path
import csv
from collections import defaultdict, Counter

INPUT = Path("screening/full_text/pubmed_high_priority_include_records.csv")
OUTPUT = Path("screening/full_text/pubmed_high_priority_layer_map.md")

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

by_layer = defaultdict(list)
for r in rows:
    by_layer[r["corneal_layer"]].append(r)

layer_counts = Counter(r["corneal_layer"] for r in rows)

with OUTPUT.open("w", encoding="utf-8") as f:
    f.write("# PubMed High-Priority Include Records: Layer Map\n\n")

    f.write("## Purpose\n\n")
    f.write("This file maps high-priority PubMed Include records by corneal layer. It is intended to guide full-text retrieval, evidence mapping, and later manuscript structure.\n\n")

    f.write("## Layer Counts\n\n")
    for layer, count in layer_counts.most_common():
        f.write(f"- {layer}: {count}\n")

    for layer in sorted(by_layer.keys()):
        f.write(f"\n## {layer}\n\n")
        for r in by_layer[layer]:
            f.write(f"### {r['screening_id']} / PMID {r['pmid']}\n\n")
            f.write(f"**Title:** {r['title']}\n\n")
            f.write(f"**Year:** {r['year']}\n\n")
            f.write(f"**Journal:** {r['journal']}\n\n")
            f.write(f"**DOI:** {r['doi']}\n\n")
            f.write(f"**Sources:** {r['sources']}\n\n")
            f.write(f"**Screening note:** {r['screening_notes']}\n\n")

print("High-priority layer map created.")
print("Layer counts:")
for layer, count in layer_counts.most_common():
    print(f"{layer}: {count}")
print(f"Output: {OUTPUT}")
