from pathlib import Path
import csv

INPUT = Path("screening/title_abstract/working/pubmed_screening_batch_01_FIRST_PASS.csv")
OUTPUT = Path("screening/title_abstract/working/pubmed_screening_batch_01_AUDIT_LIST.md")

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

def suspicious_include(row):
    text = f"{row['title']} {row['abstract']}".lower()

    suspicious_terms = [
        "keratoplasty",
        "dmek",
        "dalk",
        "clinical outcome",
        "visual acuity",
        "tomography",
        "topography",
        "keratoconus",
        "diagnostic",
        "surgical",
        "intraocular",
        "contact lens",
        "case report",
        "review",
    ]

    strong_engineering_terms = [
        "scaffold",
        "hydrogel",
        "biomaterial",
        "tissue engineering",
        "bioengineered",
        "engineered tissue",
        "cell sheet",
        "construct",
        "decellularized",
        "nanofiber",
        "nanofibre",
        "bioprint",
        "regeneration",
        "reconstruction",
    ]

    return (
        row["decision"] == "Include"
        and any(t in text for t in suspicious_terms)
        and not any(t in text for t in strong_engineering_terms)
    )

suspicious = [r for r in rows if suspicious_include(r)]
uncertain = [r for r in rows if r["decision"] == "Uncertain"]
excluded = [r for r in rows if r["decision"] == "Exclude"]

with OUTPUT.open("w", encoding="utf-8") as f:
    f.write("# PubMed Batch 01 First-Pass Audit List\n\n")
    f.write("## Purpose\n\n")
    f.write("This file identifies records that need manual audit before Batch 01 decisions are accepted.\n\n")

    f.write("## Summary\n\n")
    f.write(f"- Total records: {len(rows)}\n")
    f.write(f"- Suspicious Includes: {len(suspicious)}\n")
    f.write(f"- Uncertain records: {len(uncertain)}\n")
    f.write(f"- Excluded records: {len(excluded)}\n\n")

    f.write("## Suspicious Includes\n\n")
    if suspicious:
        for r in suspicious:
            f.write(f"### {r['screening_id']} / PMID {r['pmid']}\n\n")
            f.write(f"**Title:** {r['title']}\n\n")
            f.write(f"**Current decision:** {r['decision']}\n\n")
            f.write(f"**Layer:** {r['corneal_layer']}\n\n")
            f.write(f"**Abstract preview:** {r['abstract'][:900]}\n\n")
            f.write("**Audit decision:** Pending\n\n")
            f.write("**Audit rationale:** Pending\n\n")
    else:
        f.write("No suspicious includes detected by rule.\n\n")

    f.write("\n## Uncertain Records\n\n")
    for r in uncertain:
        f.write(f"### {r['screening_id']} / PMID {r['pmid']}\n\n")
        f.write(f"**Title:** {r['title']}\n\n")
        f.write(f"**Abstract preview:** {r['abstract'][:900]}\n\n")
        f.write("**Audit decision:** Pending\n\n")

print(f"Audit list written to: {OUTPUT}")
print(f"Suspicious Includes: {len(suspicious)}")
print(f"Uncertain: {len(uncertain)}")
print(f"Excluded: {len(excluded)}")
