from pathlib import Path
import csv
from collections import Counter

INPUT = Path("screening/full_text/pubmed_unresolved_manual_check_review.csv")
OUTPUT = Path("screening/full_text/pubmed_unresolved_manual_check_review_strict.csv")
REPORT = Path("screening/full_text/pubmed_unresolved_manual_check_review_strict.md")

# Strict supervisor-level overrides based on title/abstract fit.
# These are not core extraction papers because they are mainly clinical/background/diagnostic/mechanistic.
OVERRIDES = {
    "28613758": (
        "Downgrade to background",
        "General clinical/background article on neurotrophic keratitis. Useful for context, but not a primary biomaterial benchmarking study."
    ),
    "31009395": (
        "Exclude from core",
        "Contact lens/confocal microscopy study. It does not provide primary corneal tissue-engineering biomaterial evidence."
    ),
    "33760451": (
        "Downgrade to background",
        "Broad artificial corneal transplantation overview. Useful for introduction/context, but not a primary extractable biomaterial study."
    ),
    "41878560": (
        "Downgrade to background",
        "Broad RNA modification/wound-healing review with only partial corneal relevance. Not a primary biomaterial benchmarking study."
    ),
}

with INPUT.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

out_rows = []

for r in rows:
    out = dict(r)
    pmid = r["pmid"]

    if pmid in OVERRIDES:
        decision, reason = OVERRIDES[pmid]
        out["strict_manual_decision"] = decision
        out["strict_manual_reason"] = reason
    else:
        previous = r.get("manual_review_decision", "")
        if previous in ["Keep core", "Keep core - cautious"]:
            out["strict_manual_decision"] = previous
            out["strict_manual_reason"] = r.get("manual_review_reason", "")
        else:
            out["strict_manual_decision"] = previous
            out["strict_manual_reason"] = r.get("manual_review_reason", "")

    out_rows.append(out)

fieldnames = list(out_rows[0].keys())

with OUTPUT.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(out_rows)

decision_counts = Counter(r["strict_manual_decision"] for r in out_rows)
layer_counts = Counter(r["corneal_layer"] for r in out_rows)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# Strict Manual Override Review\n\n")

    f.write("## Purpose\n\n")
    f.write("This file applies stricter supervisor-level corrections to the unresolved manual-check review. The previous automated review over-kept some records because it treated any mention of hydrogel/scaffold/construct as sufficient for core inclusion.\n\n")

    f.write("## Strict Decision Counts\n\n")
    for k, v in decision_counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Layer Counts\n\n")
    for k, v in layer_counts.items():
        f.write(f"- {k}: {v}\n")

    f.write("\n## Strict Overrides Applied\n\n")
    for pmid, (decision, reason) in OVERRIDES.items():
        match = next((r for r in out_rows if r["pmid"] == pmid), None)
        if match:
            f.write(f"### {match['screening_id']} / PMID {pmid}\n\n")
            f.write(f"**Title:** {match['title']}\n\n")
            f.write(f"**Strict decision:** {decision}\n\n")
            f.write(f"**Reason:** {reason}\n\n")

print("Strict manual overrides applied.")
print("Strict decision counts:")
for k, v in decision_counts.items():
    print(f"{k}: {v}")
print("Overrides applied:", len(OVERRIDES))
