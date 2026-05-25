from pathlib import Path
import csv

INPUT = Path("data/processed/pubmed_unique_records.csv")
OUTPUT = Path("screening/title_abstract/pubmed_title_abstract_screening.csv")
REPORT = Path("screening/title_abstract/pubmed_title_abstract_screening_setup.md")

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    records = list(reader)

fieldnames = [
    "screening_id",
    "pmid",
    "title",
    "abstract",
    "year",
    "journal",
    "doi",
    "sources",
    "source_count",
    "decision",
    "exclusion_reason",
    "corneal_layer",
    "priority_level",
    "screening_notes"
]

rows = []
for i, r in enumerate(records, start=1):
    rows.append({
        "screening_id": f"PUBMED_{i:04d}",
        "pmid": r.get("pmid", ""),
        "title": r.get("title", ""),
        "abstract": r.get("abstract", ""),
        "year": r.get("year", ""),
        "journal": r.get("journal", ""),
        "doi": r.get("doi", ""),
        "sources": r.get("sources", ""),
        "source_count": r.get("source_count", ""),
        "decision": "",
        "exclusion_reason": "",
        "corneal_layer": "",
        "priority_level": "",
        "screening_notes": ""
    })

with OUTPUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# PubMed Title/Abstract Screening Setup\n\n")
    f.write("## Source File\n\n")
    f.write("data/processed/pubmed_unique_records.csv\n\n")
    f.write("## Output Screening File\n\n")
    f.write("screening/title_abstract/pubmed_title_abstract_screening.csv\n\n")
    f.write("## Number of Unique PubMed Records\n\n")
    f.write(f"{len(records)}\n\n")
    f.write("## Important Note\n\n")
    f.write("This screening file includes both title and abstract fields. Screening decisions should be based on both fields where abstracts are available.\n")

print(f"Created {OUTPUT}")
print(f"Records: {len(records)}")
