"""
Build the manuscript benchmarking tables (protocol v0.1/v0.2, "Planned Tables")
from the 100 valid Tier 1 primary-study extraction rows (excludes PUBMED_0672,
reclassified as a non-primary review during the 2026-07-20 QC pass).

This also functions as the gap analysis referenced in the project roadmap:
every record's optical/mechanical reporting status is normalized and split
into "genuinely not tested" (a real study limitation, not fixable by better
extraction) versus "unclear / not reported in abstract" (a candidate for the
targeted full-text upgrade pass), so the next task (targeted full-text
upgrade) has a concrete, prioritized list to work from instead of guessing.

Outputs (all in tables/):
- table1_search_strategy_summary.md
- table2_comparative_biomaterials_full.csv       (all 100 records, full data)
- table2_comparative_biomaterials_by_layer.md     (condensed, manuscript-style, grouped by layer)
- table3_cell_source_comparison.md                (aggregated by layer)
- table4_clinical_regulatory_readiness.md         (subset with animal/clinical evidence)
- gap_analysis_for_fulltext_upgrade.csv           (prioritized list for task #9)
"""
import csv
from pathlib import Path
from collections import Counter, defaultdict

EXTRACTION = Path("extraction/pubmed_balanced_core_data_extraction_template.csv")
TABLES_DIR = Path("tables")

with EXTRACTION.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

records = [
    r for r in rows
    if r["extraction_status"] == "completed" and r["screening_id"] != "PUBMED_0672"
]
assert len(records) == 100, f"expected 100 valid primary studies, got {len(records)}"

LAYER_ORDER = ["endothelium", "epithelium_limbus", "stroma", "multiple_layers"]
LAYER_LABELS = {
    "endothelium": "Endothelium",
    "epithelium_limbus": "Epithelium / Limbus",
    "stroma": "Stroma",
    "multiple_layers": "Multiple Layers / Full-Thickness",
}


def normalize_layer(raw: str) -> str:
    raw = (raw or "").strip()
    for prefix in LAYER_ORDER:
        if raw == prefix or raw.startswith(prefix + " ("):
            return prefix
    # a couple of records use "epithelium (...)" without the _limbus suffix
    if raw.startswith("epithelium"):
        return "epithelium_limbus"
    return raw or "unclassified"


def normalize_tri_state(raw: str) -> str:
    """Collapse the many free-text yes/no/partial/unclear phrasings into 4 buckets."""
    raw = (raw or "").strip().lower()
    if raw.startswith("yes"):
        return "yes"
    if raw.startswith("partial"):
        return "partial"
    if raw.startswith("unclear"):
        return "unclear_not_reported"
    if raw.startswith("no"):
        return "no_not_tested"
    return "unclear_not_reported"


for r in records:
    r["_layer"] = normalize_layer(r["target_layer_final"])
    r["_optical_state"] = normalize_tri_state(r["optical_transparency_reported"])
    r["_mechanical_state"] = normalize_tri_state(r["mechanical_testing_reported"])
    r["_biological_state"] = normalize_tri_state(r["biological_testing_reported"])
    r["_has_animal"] = r["animal_model"].strip().lower().startswith("yes")
    r["_has_clinical"] = r["clinical_evidence"].strip().lower().startswith("yes")

records.sort(key=lambda r: (LAYER_ORDER.index(r["_layer"]) if r["_layer"] in LAYER_ORDER else 99, r["screening_id"]))

# ---------------------------------------------------------------------------
# Table 1: search strategy / study-selection summary
# ---------------------------------------------------------------------------
t1 = TABLES_DIR / "table1_search_strategy_summary.md"
with t1.open("w", encoding="utf-8") as f:
    f.write("# Table 1. Search Strategy and Study Selection Summary\n\n")
    f.write("| Stage | Count | Notes |\n|---|---|---|\n")
    f.write("| PubMed records identified (4 layer-specific search blocks) | 1,318 | A3 epithelium/limbus, B3 stroma, C4 endothelium, D3 full-thickness/multilayer |\n")
    f.write("| Duplicate records removed (PMID) | 236 | |\n")
    f.write("| Unique records screened (title/abstract) | 1,082 | |\n")
    f.write("| Excluded at title/abstract stage | 354 | |\n")
    f.write("| Included / uncertain, carried forward | 728 | |\n")
    f.write("| Balanced final core (PubMed) | 246 | Layer-balanced after endothelium/epithelium correction; see `reports/weekly_logs/pubmed_balanced_core_checkpoint.md` |\n")
    f.write("| Additional records via Consensus reference-list snowball check | 2 | PUBMED_1083 (stroma), PUBMED_1084 (endothelium); protocol v0.2 |\n")
    f.write("| **Total core** | **248** | |\n")
    f.write("| Tier 1 - selected for full extraction | 101 | Score-based prioritization, `pubmed_tier1_tier2_extraction_plan.csv` |\n")
    f.write("| Tier 1 records reclassified as non-primary (review article) | 1 | PUBMED_0672 |\n")
    f.write("| **Tier 1 valid primary studies (this table set)** | **100** | |\n")
    f.write("| Tier 2 - light-touch / cited for context | 147 | Not deep-extracted; layer-label QC applied (15 corrected, 40 flagged) |\n")
    f.write("\nSingle-database (PubMed) scope with a targeted supplementary snowball check; see protocol v0.2 for justification given the Q2 journal target.\n")

# ---------------------------------------------------------------------------
# Table 2 (full data export)
# ---------------------------------------------------------------------------
t2_full = TABLES_DIR / "table2_comparative_biomaterials_full.csv"
export_cols = [
    "screening_id", "pmid", "year", "journal", "doi", "_layer",
    "biomaterial_category", "specific_materials", "fabrication_method",
    "cell_type_used", "cell_source",
    "optical_transparency_reported", "mechanical_testing_reported", "biological_testing_reported",
    "in_vitro_model", "ex_vivo_model", "animal_model", "clinical_evidence",
    "translational_readiness_level", "benchmarking_relevance",
    "main_outcomes", "main_limitations", "evidence_verification_level",
]
with t2_full.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=export_cols)
    w.writeheader()
    for r in records:
        w.writerow({c: r.get(c, "") for c in export_cols})

# ---------------------------------------------------------------------------
# Table 2 (condensed, manuscript-style, grouped by layer)
# ---------------------------------------------------------------------------
t2_md = TABLES_DIR / "table2_comparative_biomaterials_by_layer.md"
with t2_md.open("w", encoding="utf-8") as f:
    f.write("# Table 2. Comparative Biomaterials Extraction Table (by corneal layer)\n\n")
    f.write(
        "100 Tier 1 primary studies, grouped by target corneal layer. "
        "Identifiers use PMID/year/journal - author names are not yet captured in the "
        "extraction pipeline and must be added during reference-list compilation (task #11) "
        "before this table is submission-ready.\n\n"
        "**Evidence key:** FT = full-text verified, AF = abstract + figures reviewed, "
        "AO = abstract only (see `evidence_verification_level`).\n\n"
    )
    by_layer = defaultdict(list)
    for r in records:
        by_layer[r["_layer"]].append(r)

    for layer in LAYER_ORDER:
        recs = by_layer.get(layer, [])
        if not recs:
            continue
        f.write(f"\n## {LAYER_LABELS[layer]} (n={len(recs)})\n\n")
        f.write("| PMID / Year | Material | Fabrication | Optical | Mechanical | Model | Readiness | Ev. |\n")
        f.write("|---|---|---|---|---|---|---|---|\n")
        ev_short = {"full_text_verified": "FT", "abstract_plus_figures": "AF", "abstract_only": "AO"}
        model_short = []
        for r in recs:
            model_bits = []
            if r["_has_clinical"]:
                model_bits.append("Clinical")
            if r["_has_animal"]:
                model_bits.append("Animal")
            if r["ex_vivo_model"].strip().lower().startswith("yes"):
                model_bits.append("Ex vivo")
            if r["in_vitro_model"].strip().lower().startswith("yes") and not model_bits:
                model_bits.append("In vitro only")
            elif r["in_vitro_model"].strip().lower().startswith("yes"):
                model_bits.append("+In vitro")
            model_str = ", ".join(model_bits) if model_bits else "-"

            opt = {"yes": "Y", "partial": "partial", "no_not_tested": "-", "unclear_not_reported": "?"}[r["_optical_state"]]
            mech = {"yes": "Y", "partial": "partial", "no_not_tested": "-", "unclear_not_reported": "?"}[r["_mechanical_state"]]

            material = r["specific_materials"].strip() or r["biomaterial_category"].strip()
            if len(material) > 70:
                material = material[:67] + "..."
            fab = r["fabrication_method"].strip()
            if len(fab) > 60:
                fab = fab[:57] + "..."
            readiness = r["translational_readiness_level"].strip()
            if len(readiness) > 40:
                readiness = readiness[:37] + "..."

            f.write(
                f"| {r['pmid']} / {r['year']} | {material} | {fab} | {opt} | {mech} | "
                f"{model_str} | {readiness} | {ev_short.get(r['evidence_verification_level'], '?')} |\n"
            )

# ---------------------------------------------------------------------------
# Table 3: cell-source comparison (aggregated, not per-study)
# ---------------------------------------------------------------------------
t3 = TABLES_DIR / "table3_cell_source_comparison.md"
with t3.open("w", encoding="utf-8") as f:
    f.write("# Table 3. Cell-Source Comparison by Corneal Layer\n\n")
    f.write(
        "Aggregated from the `cell_source` field across the 100 Tier 1 primary studies. "
        "Categorization is keyword-based on free-text extraction values - treat as a "
        "starting point for the manuscript's cell-source discussion, not a final count.\n\n"
    )

    def bucket_cell_source(text):
        t = (text or "").lower()
        if "ipsc" in t or "induced pluripotent" in t or "hpsc" in t or "embryonic stem" in t or "esc" in t:
            return "Pluripotent stem cell-derived (iPSC/ESC)"
        if "adipose" in t:
            return "Adipose-derived stem cells"
        if "mesenchymal" in t or "wharton" in t or "msc" in t:
            return "Mesenchymal stem cells"
        if "oral mucosal" in t:
            return "Oral mucosal epithelial cells"
        if "dental pulp" in t:
            return "Dental pulp stem cells"
        if "bovine" in t or "porcine" in t or "rabbit" in t or "rat" in t or "animal" in t:
            return "Animal-derived (xenogeneic) primary cells"
        if "human" in t and ("primary" in t or "donor" in t or "cadaver" in t):
            return "Human primary/donor cells"
        if "human" in t:
            return "Human cells (source detail unspecified)"
        if "cell line" in t or "hcec-12" in t.replace(" ", "-"):
            return "Immortalized cell line"
        return "Not clearly specified"

    for layer in LAYER_ORDER:
        recs = [r for r in records if r["_layer"] == layer]
        if not recs:
            continue
        buckets = Counter(bucket_cell_source(r["cell_source"]) for r in recs)
        f.write(f"\n## {LAYER_LABELS[layer]} (n={len(recs)})\n\n")
        f.write("| Cell source category | Count | % of layer |\n|---|---|---|\n")
        for cat, count in buckets.most_common():
            f.write(f"| {cat} | {count} | {count/len(recs)*100:.0f}% |\n")

# ---------------------------------------------------------------------------
# Table 4: clinical / regulatory readiness (subset with animal or clinical evidence)
# ---------------------------------------------------------------------------
t4 = TABLES_DIR / "table4_clinical_regulatory_readiness.md"
with t4.open("w", encoding="utf-8") as f:
    f.write("# Table 4. Clinical-Stage and Regulatory-Readiness Table\n\n")
    clinical_recs = [r for r in records if r["_has_clinical"]]
    animal_recs = [r for r in records if r["_has_animal"] and not r["_has_clinical"]]
    f.write(f"Records with genuine human clinical evidence: **{len(clinical_recs)}**. ")
    f.write(f"Additional records with an animal-model component (no clinical evidence): **{len(animal_recs)}**.\n\n")

    f.write("## Human Clinical Evidence\n\n")
    f.write("| PMID / Year | Layer | Material | Study Type | Follow-up | Readiness |\n|---|---|---|---|---|---|\n")
    for r in clinical_recs:
        f.write(
            f"| {r['pmid']} / {r['year']} | {LAYER_LABELS.get(r['_layer'], r['_layer'])} | "
            f"{(r['specific_materials'] or r['biomaterial_category'])[:50]} | {r['study_type'][:50]} | "
            f"{r['follow_up_duration'][:40]} | {r['translational_readiness_level'][:40]} |\n"
        )

    f.write("\n## Animal-Model Evidence (no clinical evidence yet)\n\n")
    f.write("| PMID / Year | Layer | Material | Animal Model | Follow-up |\n|---|---|---|---|---|\n")
    for r in animal_recs:
        f.write(
            f"| {r['pmid']} / {r['year']} | {LAYER_LABELS.get(r['_layer'], r['_layer'])} | "
            f"{(r['specific_materials'] or r['biomaterial_category'])[:50]} | "
            f"{r['main_outcomes'][:60]}... | {r['follow_up_duration'][:40]} |\n"
        )

# ---------------------------------------------------------------------------
# Gap analysis for the targeted full-text upgrade pass (task #9)
# ---------------------------------------------------------------------------
gap_csv = TABLES_DIR / "gap_analysis_for_fulltext_upgrade.csv"
gap_rows = []
for r in records:
    gaps = []
    if r["_optical_state"] == "unclear_not_reported":
        gaps.append("optical")
    if r["_mechanical_state"] == "unclear_not_reported":
        gaps.append("mechanical")
    if not gaps:
        continue
    gap_rows.append({
        "screening_id": r["screening_id"],
        "pmid": r["pmid"],
        "layer": r["_layer"],
        "benchmarking_relevance": r["benchmarking_relevance"],
        "evidence_verification_level": r["evidence_verification_level"],
        "gaps": ";".join(gaps),
        "title": r["title"],
    })

# Prioritize: high benchmarking_relevance + abstract_only + has a real gap
def priority_key(row):
    rel_rank = {"high": 0, "medium-high": 1, "medium": 2}.get(row["benchmarking_relevance"].lower(), 3)
    ev_rank = 0 if row["evidence_verification_level"] == "abstract_only" else 1
    return (rel_rank, ev_rank, -len(row["gaps"]))

gap_rows.sort(key=priority_key)

with gap_csv.open("w", newline="", encoding="utf-8") as f:
    fieldnames = ["screening_id", "pmid", "layer", "benchmarking_relevance", "evidence_verification_level", "gaps", "title"]
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(gap_rows)

# ---------------------------------------------------------------------------
# Console summary
# ---------------------------------------------------------------------------
print(f"Valid Tier 1 primary studies: {len(records)}")
print(f"Layer distribution: {dict(Counter(r['_layer'] for r in records))}")
print()
print(f"Optical reporting: {dict(Counter(r['_optical_state'] for r in records))}")
print(f"Mechanical reporting: {dict(Counter(r['_mechanical_state'] for r in records))}")
print()
print(f"Records flagged for full-text upgrade (optical and/or mechanical unclear): {len(gap_rows)}")
high_priority = [r for r in gap_rows if r["benchmarking_relevance"].lower() == "high" and r["evidence_verification_level"] == "abstract_only"]
print(f"  ...of which high-relevance + abstract-only (top upgrade priority): {len(high_priority)}")
print()
print(f"Clinical evidence records: {sum(1 for r in records if r['_has_clinical'])}")
print(f"Animal-only evidence records: {sum(1 for r in records if r['_has_animal'] and not r['_has_clinical'])}")
print()
print("Files written to tables/:")
for p in [t1, t2_full, t2_md, t3, t4, gap_csv]:
    print(" -", p)
