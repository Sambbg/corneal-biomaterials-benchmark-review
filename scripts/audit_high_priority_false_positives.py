from pathlib import Path
import csv
from collections import Counter

INPUT = Path("screening/full_text/pubmed_high_priority_include_records.csv")
AUDIT_CSV = Path("screening/full_text/pubmed_high_priority_false_positive_audit.csv")
AUDIT_MD = Path("screening/full_text/pubmed_high_priority_false_positive_audit.md")

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

false_positive_terms = [
    "neurotrophic keratitis",
    "contact lens",
    "confocal microscopy",
    "keratoplasty",
    "dmek",
    "dsaek",
    "dalk",
    "visual acuity",
    "case report",
    "case series",
    "surgical",
    "diagnostic",
    "tomography",
    "topography",
    "rna modifications",
    "molecular orchestrators",
    "intraocular pressure",
    "p-cadherin is expressed",
    "tgf-β1 promotes cell barrier",
]

strong_keep_terms = [
    "scaffold",
    "hydrogel",
    "bioink",
    "bioprint",
    "bioprinted",
    "bioprinting",
    "decellularized",
    "decellularised",
    "cell sheet",
    "tissue-engineered",
    "tissue engineered",
    "tissue engineering",
    "corneal substitute",
    "artificial cornea",
    "corneal implant",
    "corneal regeneration",
    "corneal reconstruction",
    "corneal repair",
    "construct",
    "nanofiber",
    "nanofibre",
    "electrospun",
    "gelma",
    "collagen",
    "silk fibroin",
    "chitosan",
    "polycaprolactone",
    "amniotic membrane",
    "acellular",
    "extracellular matrix",
]

audit_rows = []

for r in rows:
    text = f"{r.get('title','')} {r.get('abstract','')}".lower()

    has_false_positive_signal = any(term in text for term in false_positive_terms)
    has_strong_keep_signal = any(term in text for term in strong_keep_terms)

    audit_flag = ""
    recommended_action = ""
    rationale = ""

    if has_false_positive_signal and not has_strong_keep_signal:
        audit_flag = "Likely false positive"
        recommended_action = "Downgrade or exclude"
        rationale = "Title/abstract contains clinical/background/diagnostic signal without a strong biomaterial, scaffold, hydrogel, construct, or tissue-engineering signal."
    elif has_false_positive_signal and has_strong_keep_signal:
        audit_flag = "Needs manual check"
        recommended_action = "Manual audit"
        rationale = "Contains both possible false-positive clinical/background terms and possible tissue-engineering terms."
    else:
        continue

    out = dict(r)
    out["audit_flag"] = audit_flag
    out["recommended_action"] = recommended_action
    out["audit_rationale"] = rationale
    audit_rows.append(out)

if audit_rows:
    with AUDIT_CSV.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=audit_rows[0].keys())
        writer.writeheader()
        writer.writerows(audit_rows)

flag_counts = Counter(r["audit_flag"] for r in audit_rows)
layer_counts = Counter(r["corneal_layer"] for r in audit_rows)

with AUDIT_MD.open("w", encoding="utf-8") as f:
    f.write("# High-Priority Include False-Positive Audit\n\n")

    f.write("## Purpose\n\n")
    f.write("This audit identifies high-priority Include records that may be false positives before full-text retrieval. The aim is to avoid wasting time on clinical, diagnostic, generic wound-healing, or non-biomaterial papers.\n\n")

    f.write("## Audit Counts\n\n")
    f.write(f"- High-priority records checked: {len(rows)}\n")
    f.write(f"- Records flagged for audit: {len(audit_rows)}\n")
    for k, v in flag_counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Flagged Records by Layer\n\n")
    for k, v in layer_counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Flagged Records\n\n")
    for r in audit_rows:
        f.write(f"### {r['screening_id']} / PMID {r['pmid']}\n\n")
        f.write(f"**Title:** {r['title']}\n\n")
        f.write(f"**Layer:** {r['corneal_layer']}\n\n")
        f.write(f"**Audit flag:** {r['audit_flag']}\n\n")
        f.write(f"**Recommended action:** {r['recommended_action']}\n\n")
        f.write(f"**Rationale:** {r['audit_rationale']}\n\n")

print("High-priority false-positive audit created.")
print(f"High-priority records checked: {len(rows)}")
print(f"Records flagged for audit: {len(audit_rows)}")
for k, v in flag_counts.items():
    print(f"{k}: {v}")
print("Flagged by layer:")
for k, v in layer_counts.items():
    print(f"{k}: {v}")
