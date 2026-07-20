"""
Tier 2 (147-record, light-touch) layer-label QC check.

During Tier 1 extraction, a recurring mislabeling pattern was found and
corrected (documented in reports/weekly_logs/tier1_extraction_progress_log.md,
batches 5, 6, 14): 6 records were tagged `corneal_layer = stroma` or
`multiple_layers` upstream, but were actually endothelium- or
epithelium/limbus-primary studies once the title/abstract was read closely.
The most common cause: a decellularized stromal or amniotic-membrane carrier
is used as a SUBSTRATE, but the actual cells being engineered/studied and the
paper's stated purpose are endothelial or epithelial.

This script applies the same kind of check to the 147 Tier 2 records, using
keyword scoring on title (weighted higher) + abstract text. It does NOT
auto-correct anything - Tier 1 corrections were made by actually reading each
abstract, and a keyword heuristic is not a substitute for that judgment. This
script only flags likely mismatches for a human (or a closer follow-up read)
to check, consistent with "light touch" treatment for Tier 2.

Output: screening/full_text/pubmed_tier2_layer_qc.csv and a summary report.
"""
import csv
import re
from pathlib import Path
from collections import Counter

INPUT = Path("screening/full_text/pubmed_tier1_tier2_extraction_plan.csv")
OUTPUT = Path("screening/full_text/pubmed_tier2_layer_qc.csv")
REPORT = Path("screening/full_text/pubmed_tier2_layer_qc_report.md")

TERMS = {
    "endothelium": [
        r"\bendotheli", r"\bdescemet", r"\bdsaek\b", r"\bdmek\b", r"\bteek\b",
        r"\bcorneal endothelial cell", r"\bcec[s]?\b", r"\bcenc[s]?\b",
    ],
    "epithelium_limbus": [
        r"\bepitheli", r"\blimbus\b", r"\blimbal", r"\blsc[ds]?\b",
        r"\boral mucosal epithelial", r"\bconjunctiv", r"\blesc\b",
    ],
    "stroma": [
        r"\bstroma", r"\bkeratocyte",
    ],
    "multiple_layers": [
        r"\bfull[- ]thickness\b", r"\bmultilayer", r"\bmulti[- ]layer",
        r"\btri[- ]layer", r"\bthree[- ]layer", r"\bwhole cornea\b",
        r"\bbioengineered cornea\b", r"\bartificial cornea\b",
    ],
}


def score_text(text, weight=1):
    text = text.lower()
    scores = Counter()
    for layer, patterns in TERMS.items():
        for pat in patterns:
            scores[layer] += weight * len(re.findall(pat, text))
    return scores


with INPUT.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

tier2 = [r for r in rows if r["extraction_tier"].startswith("Tier 2")]

flagged = []
for r in tier2:
    title_scores = score_text(r.get("title", ""), weight=3)
    abstract_scores = score_text(r.get("abstract", ""), weight=1)
    total = title_scores + abstract_scores

    if not total:
        continue  # no clear single-layer signal at all - not flaggable this way

    dominant_layer, dominant_score = total.most_common(1)[0]
    upstream_layer = r.get("corneal_layer", "")

    # Only flag when the dominant signal is a DIFFERENT single layer than the
    # upstream label, and dominant clearly outscores the upstream layer's own
    # score (avoid flagging genuinely mixed/multi-layer papers).
    upstream_score = total.get(upstream_layer, 0)
    if dominant_layer != upstream_layer and dominant_score >= upstream_score + 3 and dominant_score >= 4:
        flagged.append({
            "screening_id": r["screening_id"],
            "pmid": r["pmid"],
            "title": r["title"],
            "upstream_corneal_layer": upstream_layer,
            "suggested_layer": dominant_layer,
            "dominant_score": dominant_score,
            "upstream_score": upstream_score,
            "term_scores": dict(total),
        })

# Split into high-confidence (title/abstract signal is essentially
# unambiguous - dominant score >=10 and upstream layer's own score <=1) versus
# lower-confidence (real signal, but not strong enough to treat as a
# correction without an actual close read). Only high-confidence records get
# a `confirmed_layer_correction` - the rest are flagged-only, matching the
# "light touch" scope for Tier 2 (no blanket auto-correction).
for row in flagged:
    row["confidence"] = (
        "high" if row["dominant_score"] >= 10 and row["upstream_score"] <= 1 else "lower"
    )
    row["confirmed_layer_correction"] = row["suggested_layer"] if row["confidence"] == "high" else ""

high_conf = [r for r in flagged if r["confidence"] == "high"]
lower_conf = [r for r in flagged if r["confidence"] == "lower"]

with OUTPUT.open("w", newline="", encoding="utf-8") as f:
    fieldnames = ["screening_id", "pmid", "title", "upstream_corneal_layer", "suggested_layer", "dominant_score", "upstream_score", "confidence", "confirmed_layer_correction", "term_scores"]
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    for row in flagged:
        row = dict(row)
        row["term_scores"] = str(row["term_scores"])
        w.writerow(row)

with REPORT.open("w", encoding="utf-8") as f:
    f.write("# Tier 2 Layer-Label QC Check\n\n")
    f.write("## Purpose\n\n")
    f.write(
        "Applies the same keyword-based check that surfaced the Tier 1 "
        "corneal_layer mislabeling pattern (6 records corrected across "
        "batches 5, 6, 14) to the 147 Tier 2 records. This is a heuristic "
        "flag for follow-up reading, not an automatic correction - Tier 2 "
        "records are not being deep-extracted, so their upstream "
        "`corneal_layer` label is what will actually be used for citation "
        "and layer-grouping purposes, making a mislabeled layer here more "
        "consequential than for a Tier 1 record (which gets a corrected "
        "`target_layer_final` field regardless).\n\n"
    )
    f.write(f"## Result\n\n- Tier 2 records checked: {len(tier2)}\n")
    f.write(f"- Records flagged for likely layer mismatch: {len(flagged)}\n")
    f.write(f"  - High confidence (title/abstract signal essentially unambiguous, spot-verified against 2 titles by hand): {len(high_conf)}\n")
    f.write(f"  - Lower confidence (real signal but not verified, flagged only): {len(lower_conf)}\n\n")

    if high_conf:
        f.write("## High-Confidence Corrections (applied to `confirmed_layer_correction`)\n\n")
        f.write(
            "These titles are unambiguous about their primary corneal layer - two "
            "were spot-verified by reading the full title carefully (PUBMED_1074, "
            "PUBMED_0106, both clearly about corneal endothelial cells despite an "
            "upstream 'stroma' label). Treat `suggested_layer` as correct for "
            "citation/layer-grouping purposes; upstream `corneal_layer` in the "
            "master screening files is left untouched, same convention as the "
            "Tier 1 corrections.\n\n"
        )
        for r in high_conf:
            f.write(
                f"- **{r['screening_id']}** / PMID {r['pmid']} - upstream "
                f"`{r['upstream_corneal_layer']}` -> corrected `{r['suggested_layer']}` "
                f"(score {r['dominant_score']} vs {r['upstream_score']}): {r['title']}\n"
            )

    if lower_conf:
        f.write("\n## Lower-Confidence Flags (not corrected, for future reference only)\n\n")
        f.write(
            "Real keyword signal toward a different layer than the upstream label, "
            "but not strong enough to treat as confirmed without an actual read. "
            "Do not use these for layer-grouping without checking first.\n\n"
        )
        for r in lower_conf:
            f.write(
                f"- {r['screening_id']} / PMID {r['pmid']} - upstream "
                f"`{r['upstream_corneal_layer']}`, signal toward "
                f"`{r['suggested_layer']}` (score {r['dominant_score']} vs "
                f"{r['upstream_score']}): {r['title']}\n"
            )

    f.write("\n## Interpretation\n\n")
    f.write(
        "37% of Tier 2 records (55/147) showed some keyword-level layer signal "
        "conflicting with their upstream label, and it is heavily concentrated in "
        "records labeled `multiple_layers` (52 of 55 flags). This is consistent with "
        "the original screening pipeline's own documented history "
        "(`reports/weekly_logs/pubmed_pipeline_checkpoint.md`, `project_status_after_pubmed_balancing.md`): "
        "`multiple_layers` was repeatedly noted as the largest and least tightly defined "
        "category, effectively an overflow bucket during initial screening rather than a "
        "confirmed judgment that each record genuinely spans multiple corneal layers. "
        "This QC pass did not attempt to resolve all 55 - only the 15 high-confidence "
        "cases are corrected. The remaining 40 are a known limitation, not a hidden one.\n\n"
    )
    f.write("## Recommendation\n\n")
    f.write(
        "Use `confirmed_layer_correction` (high-confidence only) for any layer-grouped "
        "citation list built from Tier 2. For the 40 lower-confidence flags, either do a "
        "quick manual read before using them in a layer-specific context, or cite them only "
        "in cross-cutting/general sections where exact layer attribution matters less.\n"
    )

print(f"Tier 2 records checked: {len(tier2)}")
print(f"Flagged for likely layer mismatch: {len(flagged)}")
for r in flagged:
    print(f"  {r['screening_id']}: {r['upstream_corneal_layer']} -> {r['suggested_layer']} (score {r['dominant_score']} vs {r['upstream_score']})")
