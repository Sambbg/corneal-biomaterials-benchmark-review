from pathlib import Path
import csv
from collections import Counter

INPUT = Path("screening/full_text/pubmed_manual_audit_worksheet.csv")
OUTPUT = Path("screening/full_text/pubmed_manual_audit_worksheet_prefilled.csv")
REPORT = Path("screening/full_text/pubmed_manual_audit_prefill_report.md")

def classify_pressure(row):
    title = row.get("title", "").lower()
    abstract = row.get("abstract", "").lower()
    text = title + " " + abstract

    weak_terms = [
        "contact lens",
        "confocal microscopy",
        "rna modifications",
        "molecular orchestrators",
        "p-cadherin is expressed",
        "tgf-β1 promotes cell barrier",
        "intraocular pressure",
        "neurotrophic keratitis",
        "artificial corneal transplantation"
    ]

    strong_terms = [
        "scaffold",
        "hydrogel",
        "bioink",
        "bioprint",
        "decellularized",
        "acellular",
        "cell sheet",
        "tissue-engineered",
        "tissue engineered",
        "corneal substitute",
        "artificial cornea",
        "construct",
        "electrospun",
        "nanofiber",
        "gelma",
        "collagen",
        "silk fibroin",
        "polycaprolactone"
    ]

    has_weak = any(t in text for t in weak_terms)
    strong_count = sum(1 for t in strong_terms if t in text)

    if has_weak and strong_count == 0:
        return "Likely downgrade/exclude"
    if has_weak and strong_count > 0:
        return "Needs close audit"
    return "Likely keep core"

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

out_rows = []
for r in rows:
    pressure = classify_pressure(r)
    out = dict(r)
    out["audit_pressure"] = pressure

    if pressure == "Likely keep core":
        out["manual_decision"] = "Keep core"
        out["manual_reason"] = "Strong biomaterial/scaffold/hydrogel/cell-construct signal; relevant to corneal tissue engineering benchmarking."
        out["full_text_needed"] = "yes"
    elif pressure == "Needs close audit":
        out["manual_decision"] = "Manual check"
        out["manual_reason"] = "Contains both tissue-engineering signal and possible clinical/background/therapy signal; requires manual confirmation before final core inclusion."
        out["full_text_needed"] = "maybe"
    else:
        out["manual_decision"] = "Downgrade or exclude"
        out["manual_reason"] = "Weak fit for biomaterial benchmarking based on title/abstract; likely background, clinical, diagnostic, or mechanistic-only paper."
        out["full_text_needed"] = "no"

    out_rows.append(out)

fieldnames = list(out_rows[0].keys())

with OUTPUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(out_rows)

decision_counts = Counter(r["manual_decision"] for r in out_rows)
pressure_counts = Counter(r["audit_pressure"] for r in out_rows)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# PubMed Manual Audit Prefill Report\n\n")

    f.write("## Purpose\n\n")
    f.write("This file pre-fills manual audit decisions using conservative rules. It does not replace human judgement. Records marked Manual check still require explicit review before final core inclusion.\n\n")

    f.write("## Prefilled Decision Counts\n\n")
    for k, v in decision_counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Audit Pressure Counts\n\n")
    for k, v in pressure_counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Output File\n\n")
    f.write(f"- `{OUTPUT}`\n")

print("Manual audit decisions prefilled.")
print("Prefilled decision counts:")
for k, v in decision_counts.items():
    print(f"{k}: {v}")
print("Audit pressure counts:")
for k, v in pressure_counts.items():
    print(f"{k}: {v}")
