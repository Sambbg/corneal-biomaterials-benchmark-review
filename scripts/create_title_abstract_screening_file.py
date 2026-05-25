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
    f.write("## Screening Decision Options\n\n")
    f.write("- Include\n")
    f.write("- Exclude\n")
    f.write("- Uncertain\n\n")
    f.write("## Exclusion Reason Options\n\n")
    f.write("- Review/background only\n")
    f.write("- Book chapter/background clinical overview\n")
    f.write("- General ophthalmology/no engineering content\n")
    f.write("- Disease biology only\n")
    f.write("- Drug delivery only/no regenerative scaffold relevance\n")
    f.write("- Not corneal tissue engineering\n")
    f.write("- No biomaterial/scaffold/cell-engineering relevance\n")
    f.write("- Insufficient relevance from title/abstract\n\n")
    f.write("## Corneal Layer Options\n\n")
    f.write("- epithelium_limbus\n")
    f.write("- stroma\n")
    f.write("- endothelium\n")
    f.write("- full_thickness_multilayer\n")
    f.write("- multiple_layers\n")
    f.write("- unclear\n\n")
    f.write("## Priority Level Options\n\n")
    f.write("- High: likely core extraction/case-study candidate\n")
    f.write("- Medium: relevant but may support only part of the synthesis\n")
    f.write("- Low: background/supporting evidence only\n\n")
    f.write("## Methodological Note\n\n")
    f.write("Formal screening should not blindly follow AI decisions. AI may assist, but borderline records must be manually audited. The Uncertain category should be used whenever title/abstract information is insufficient.\n")

print(f"Created {OUTPUT}")
print(f"Records: {len(records)}")
