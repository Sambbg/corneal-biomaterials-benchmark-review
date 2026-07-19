# Review Protocol v0.2

## Change Log From v0.1

- Target journal reframed from Acta Biomaterialia (Q1) to a Q2 primary/backup shortlist. Acta Biomaterialia remains a possible stretch target for a later, more exhaustive version of this work, not the current submission target.
- Single-database (PubMed) scope explicitly justified rather than left as an open gap, given the review type (critical narrative review with search transparency, not a formal systematic review).
- Added a lightweight supplementary evidence strategy (reference-list snowballing from major existing reviews + a targeted ClinicalTrials.gov pull) to replace the originally planned full Scopus/Web of Science/Embase expansion.
- Added an explicit two-tier extraction strategy to prevent effort being spread thin across all 246 core records.
- Added a required differentiation note against a closely related 2025 systematic review identified during scoping.

## Working Title

From Optical Clarity to Clinical Readiness: A Layer-Specific Benchmarking Review of Biomaterials for Corneal Tissue Engineering

## Target Journal

### Primary shortlist (Q2, realistic for current evidence base)

- Journal of Biomedical Materials Research Part B: Applied Biomaterials (Q2, IF 3.4) — closest fit; biomaterials-led, already publishes corneal-layer biomaterial studies of the type in this corpus.
- Biomedical Materials, IOP Publishing (Q2, IF 3.7) — biomaterials engineering focus, strong fit for the fabrication/benchmarking angle.

### Secondary option

- Journal of Tissue Engineering and Regenerative Medicine (Q2/Q3 across sub-categories).

### Stretch target (not current submission target)

- Acta Biomaterialia (Q1, IF 10.4) — revisit only if the evidence base is expanded to multiple databases and the manuscript demonstrates exceptional synthesis quality. Not realistic for a single-database narrative review at this stage.

## Review Type

Critical narrative review with systematic search transparency. Explicitly not a PRISMA-style systematic review or meta-analysis.

## Core Research Question

How well do currently reported biomaterials and biofabrication approaches reproduce the optical, mechanical, biological, and translational requirements of layer-specific corneal repair or replacement?

## Central Argument

Corneal tissue-engineering studies should not be judged only by novelty of biomaterial or fabrication method. They should be benchmarked against layer-specific requirements: optical clarity, biomechanics, degradation behaviour, phenotype maintenance, surgical usability, safety, and translational readiness.

## Related Work Requiring Explicit Differentiation

Anitua et al. (2025), *Advances in Corneal Tissue Engineering: Comparative Performance of Bioengineered Grafts in Animal Models* (Medicina), is a PROSPERO-registered PRISMA systematic review comparing bioengineered corneal grafts to healthy corneas across layers in animal models (PROSPERO ID CRD420250654641).

This review overlaps in subject matter but differs in framing:

- Anitua et al. benchmark engineered grafts against healthy native corneas in animal models only.
- This review benchmarks across optical, mechanical, biological, and translational/clinical-stage domains, including human first-in-human and clinical evidence where available, and is organized around a layer-specific benchmarking framework rather than an animal-model comparative performance question.

The introduction and discussion must cite and explicitly position against this paper. Failure to do so is a credible reviewer objection at any target journal.

## Databases and Search Strategy

### Primary source

PubMed / MEDLINE. Four accepted layer-specific search blocks (A3 epithelium/limbus, B3 stroma, C4 endothelium, D3 full-thickness/multilayer), 1,318 raw records, 1,082 unique after PMID deduplication. Full history in `searches/search_logs/`.

### Why single-database is defensible here

Q2 biomaterials journals routinely accept narrative/critical reviews built on one well-documented, reproducible database search, provided the search strategy, screening rules, and limitations are stated transparently. This review does not claim systematic-review exhaustiveness and should not be presented as PRISMA-compliant. The PRISMA-style summary in `reports/searches/` should be relabeled "PubMed screening flow" rather than "PRISMA-style summary" to avoid implying systematic-review-grade completeness.

### Supplementary evidence (replaces full Scopus/WoS/Embase expansion)

1. Reference-list snowball check against 5-8 major recent corneal tissue-engineering reviews (2023-2026), to catch landmark primary studies the PubMed strings missed. Two gaps already identified via a targeted Consensus search and confirmed absent from the screening corpus:
   - Puistola et al. 2024, cornea-specific adipose-stem-cell-derived ECM for stroma bioinks (ACS Applied Materials & Interfaces).
   - Ben Moussa et al. 2024, femtosecond-laser-cut lens capsule as an endothelial carrier (Bioengineering).
   Both should be added to the core candidate pool and screened using the existing inclusion/exclusion criteria.
2. Targeted ClinicalTrials.gov pull for corneal tissue-engineering/biomaterial trials, to populate the "clinical/regulatory stage" benchmark domain, which currently has no registry-level data behind it. This is a single, bounded search, not a full database expansion.

## Search Window

Primary search window: 1 January 2018 onward. Special attention: 2025-2026 literature.

## Inclusion / Exclusion Criteria

Unchanged from v0.1. See that document for full detail. Reviews remain excluded as primary evidence (this is why several 2023-2025 review papers surfaced during the Consensus gap-check, e.g. Manoochehrabadi et al. 2025 on silk biomaterials, correctly do not appear in the screening corpus — that is expected behaviour, not a search failure).

## Extraction Strategy (two-tier)

The balanced PubMed core (246 records) will not be extracted uniformly. Tiering:

### Tier 1 — full extraction (~90-120 records)

Clinical/translational studies, in vivo studies, and strong in vitro studies reporting data across most benchmark domains (optical, mechanical, biological, translational). Full extraction template completed for every field.

### Tier 2 — light-touch treatment (remaining records)

Supporting or background studies cited in prose for context but not deeply tabulated. No obligation to complete the full extraction template.

Retrieval and extraction proceed in this priority order (already established in `reports/weekly_logs/project_status_after_pubmed_balancing.md`):

1. Clinical/translational studies
2. In vivo studies
3. Ex vivo studies
4. Strong in vitro biomaterial studies
5. Supporting/background studies

## Benchmark Domains

Unchanged from v0.1: optical transparency, mechanical properties, degradation/swelling, cell viability and phenotype maintenance, in vivo/clinical performance, surgical handling, immunogenicity/safety, manufacturing and regulatory readiness.

## Planned Figures and Tables

Unchanged from v0.1, with one addition: figure and table skeletons should be drafted from the 3 completed pilot extraction rows (`extraction/pubmed_first10_pilot_extraction.csv`) before Tier 1 extraction begins at scale, so extraction effort is guided by what the benchmarking tables actually need rather than extracting all template fields uniformly.

## Current Status

Protocol revised. PubMed search, deduplication, title/abstract screening, and balanced core construction (246 records) are complete. Full-text retrieval piloted on 10 records (6 retrieved); extraction piloted and completed on 3 of those 6. Two supplementary primary studies identified for addition to the core candidate pool. Next step: retrieve and screen the 2 gap papers, then begin Tier 1 full-text retrieval in priority order.
