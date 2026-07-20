# Tier 1 extraction complete — checkpoint

**Date completed:** 2026-07-20
**Status:** All 101 "Tier 1 - full extraction" records in `screening/full_text/pubmed_tier1_tier2_extraction_plan.csv` now have `extraction_status = completed` in `extraction/pubmed_balanced_core_data_extraction_template.csv`.
**QC update (2026-07-20):** A manual quality-control pass (`20260720_tier1_quality_control_pass.md`) spot-checked accuracy (no fabrication found), added an `evidence_verification_level` column, and reclassified PUBMED_0672 as a non-primary-study background citation. **Corrected Tier 1 primary-study count: 100** (101 minus PUBMED_0672). See that report before treating this checkpoint's counts below as final - the layer/evidence breakdowns below were not recomputed after the QC pass.

This checkpoint file exists so future scheduled runs of this task can confirm completion quickly and no-op without re-scanning the full corpus.

## Final counts

- Tier 1 records total: 101 (100 primary studies + 1 reclassified narrative review, see QC update above)
- Tier 1 records completed: 101 (100%)
- Batches: 14 scheduled-task runs (batch 1 on 2026-07-19 through batch 14 on 2026-07-20); see `tier1_extraction_progress_log.md` in this directory for the full per-batch history.

## Target corneal layer distribution (`target_layer_final`, collapsed by primary layer)

- Endothelium: 33
- Epithelium / limbus: 33
- Stroma (including stroma-primary records with a secondary epithelialization/regeneration outcome noted): 23
- Multiple layers (full-thickness or explicit multi-layer constructs): 11
- Epithelium, ocular-surface/limbus-adjacent (non-limbal-stem-cell application): 1

A handful of `target_layer_final` values were corrected relative to the upstream `corneal_layer` column during extraction, where a record's title/abstract made the actual primary layer unambiguous (upstream `corneal_layer` was always left untouched; corrections are documented in each record's `extraction_notes` and in the relevant batch entries in `tier1_extraction_progress_log.md`). This was a recurring, actively-tracked pattern across several batches (batches 5, 6, and 14 explicitly).

## Open-access vs. abstract-only / paywalled status (from the full-text retrieval tracker)

- Confirmed or policy-based open access (`pdf_available` starts with "yes", i.e. gold-OA journal or independently confirmed article-level OA): 41 records (~41%)
- Abstract-level only, with open-access status not independently verified this run (hybrid/subscription journals, or OA not confirmed): 57 records (~56%)
- Other / not cleanly categorized in the tracker: 3 records (~3%)

All 101 records are `extraction_ready = yes` in the tracker; none required full-text access to be extraction-ready — all extractions were built from the verified abstract text captured in `screening/full_text/pubmed_tier1_tier2_extraction_plan.csv` during the original screening pass, per the retrieval-route constraint documented throughout this project (the sandboxed `web_fetch` tool's URL-provenance restriction blocked fresh Europe PMC REST API calls in every unattended scheduled run from batch 3 onward). A small number of records (e.g. PUBMED_0821, PUBMED_0224, PUBMED_0270, PUBMED_0709) did get genuine full-text pulls in earlier batches via a WebSearch-then-web_fetch route when that happened to succeed; these are noted individually in their `extraction_notes`.

## Evidence-level summary

- Records with genuine human clinical evidence: 6 (e.g. PUBMED_0646 phase I-II trial, PUBMED_0799 RCT, PUBMED_0832 RCT, PUBMED_0602 case study, PUBMED_0477 case reports with multi-year follow-up)
- Records with an animal model component: 41
- Records that are purely in vitro (no animal model, no clinical evidence): 50
- 1 record (PUBMED_0672) is a narrative review rather than a primary experimental study, extracted as a scope/synthesis record per instructions.

## Notable cross-cutting flags for the review team (see individual `extraction_notes` for full detail)

- `corneal_layer` mislabeling pattern (upstream column vs. actual paper focus): affected PUBMED_0151, PUBMED_0224, PUBMED_0270, PUBMED_0530 (labeled "stroma" but actually endothelium studies), and PUBMED_0690, PUBMED_1011 (labeled "multiple_layers" but actually stroma- and limbus-specific studies, respectively). Recommend a manual pass over the upstream `corneal_layer` column given this recurring pattern.
- A few records have abstract text truncated in the local screening corpus before the full results/discussion (e.g. PUBMED_0832, PUBMED_0867) — flagged individually as candidates for a future full-text follow-up if full-text access becomes available.
- PUBMED_0672 (narrative review) may be more appropriate as a background citation than a primary benchmarking-table entry.

## What's next

Tier 1 full extraction is done. Tier 2 ("light-touch") records in the same plan CSV were explicitly out of scope for this task per the original task instructions. Future runs of this scheduled task will find 0 remaining Tier 1 records, see this checkpoint file, and stop without further action.
