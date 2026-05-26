from pathlib import Path
import csv

INPUT = Path("screening/full_text/pubmed_first_batch_retrieval_tracker.csv")
OUTPUT_MD = Path("screening/full_text/pubmed_first_batch_lookup_list.md")
OUTPUT_TXT = Path("screening/full_text/pubmed_first_batch_lookup_queries.txt")

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

rows.sort(key=lambda r: (r.get("corneal_layer", ""), r.get("screening_id", "")))

with OUTPUT_MD.open("w", encoding="utf-8") as f:
    f.write("# PubMed First Batch Lookup List\n\n")
    f.write("## Purpose\n\n")
    f.write("This file lists the 80 first-batch PubMed records for quick full-text retrieval using PMID, DOI, title, and layer.\n\n")

    current_layer = None

    for r in rows:
        layer = r.get("corneal_layer", "unclear")

        if layer != current_layer:
            current_layer = layer
            f.write(f"\n## {layer}\n\n")

        f.write(f"### {r.get('screening_id', '')} / PMID {r.get('pmid', '')}\n\n")
        f.write(f"**Title:** {r.get('title', '')}\n\n")
        f.write(f"**Journal:** {r.get('journal', '')}\n\n")
        f.write(f"**Year:** {r.get('year', '')}\n\n")
        f.write(f"**DOI:** {r.get('doi', '')}\n\n")
        f.write(f"**Search query:** {r.get('title', '')} {r.get('pmid', '')}\n\n")

with OUTPUT_TXT.open("w", encoding="utf-8") as f:
    for r in rows:
        title = r.get("title", "")
        pmid = r.get("pmid", "")
        doi = r.get("doi", "")

        if doi:
            f.write(f"{doi}\n")
        f.write(f"{title} {pmid}\n\n")

print("First batch lookup files created.")
print(f"Records listed: {len(rows)}")
print(f"Markdown lookup file: {OUTPUT_MD}")
print(f"Plain-text lookup queries: {OUTPUT_TXT}")
