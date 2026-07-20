# Tier 1 Quality Control Pass

## Date

2026-07-20

## Purpose

After the 14-batch scheduled-task run completed all 101 Tier 1 extractions, a manual quality-control pass was run before treating this data as ready for benchmarking tables or manuscript drafting. Two questions drove this: (1) is the extracted data accurate, or did the unattended process fabricate/hallucinate anything, and (2) how much of it was verified against full article text versus abstracts only.

## Method

1. Independently re-fetched 2 of the 6 `corneal_layer`-correction records from the original source (Europe PMC REST API) and diffed the extracted `main_outcomes` text against the real abstract.
2. Ran a structural sweep across all 101 completed rows for missing required fields, suspiciously short entries, and duplicated/copy-pasted text.
3. Classified every completed record's actual evidentiary depth into a new `evidence_verification_level` column (see below), based on what was genuinely read at extraction time, not just what the batch log claimed.
4. Reviewed the one record flagged as a possible protocol violation (PUBMED_0672).

## Findings

### Accuracy spot-check: no fabrication found

- PUBMED_0151: extracted corneal-thickness figure (567 um at day ~181) matched the independently re-fetched abstract (567.33 +/- 72.77 um at day 181) exactly. The `corneal_layer` correction (stroma -> endothelium) made during extraction was independently confirmed correct - this is unambiguously an endothelium equivalent study.
- PUBMED_0690: extracted description of the CUBIC-cleared decellularized squid mantle scaffold matched the independently re-fetched abstract closely, including the rat intramuscular and rabbit inter-corneal implantation results. The `corneal_layer` correction (multiple_layers -> stroma) was independently confirmed correct.
- A third spot-check (PUBMED_1011) was attempted but blocked by the fetch tool's rate limit before completion; not a data-quality issue, just an unfinished check.
- Structural sweep: 0 rows with missing required fields, 0 suspiciously short `main_outcomes` entries (<80 characters), 0 duplicated/copy-pasted `main_outcomes` text across records.

### Evidence verification level (new column: `evidence_verification_level`)

Most Tier 1 records were extracted from PubMed/Europe PMC abstract text, not full article text, because the scheduled task's unattended runs were structurally blocked from fetching fresh full-text pages from batch 3 onward (see `tier1_extraction_progress_log.md`). This is real, author-written data - not fabricated - but it is a shallower read than the full paper, and abstracts do not always contain every quantitative value that ends up in a paper's tables and figures.

- `full_text_verified` (genuine article/PMC full text read - methods, results, discussion): **4 records** (PUBMED_0224, PUBMED_0270, PUBMED_0709, PUBMED_0821)
- `abstract_plus_figures` (PubMed/PMC abstract page read together with figure captions): **3 records** (PUBMED_0075, PUBMED_1083, PUBMED_1084)
- `abstract_only` (structured abstract text only, no figures/methods/tables seen): **94 records**

This column should be used going forward: any manuscript claim or benchmarking-table value sourced from an `abstract_only` record should be treated as author-reported-but-not-independently-verified, and ideally spot-checked against full text before being stated as a specific quantitative finding in the final manuscript. One incidental finding supports this being worth doing - PUBMED_0690 turned out to be genuinely open access (PMC10354768, CC-BY) despite being recorded as "abstract_only", meaning the true full-text-available pool is probably larger than currently reflected and a further upgrade pass would likely recover more.

### Protocol-compliance issue found and corrected: PUBMED_0672

PUBMED_0672 ("3D bioprinting as a prospective therapeutic strategy for corneal limbal epithelial stem cell deficiency") is a narrative review, not a primary experimental study. The project's own protocol (`protocol/review_protocol_v0.1.md`, Exclusion Criteria) explicitly excludes reviews as primary evidence. It had been extracted and counted as a normal Tier 1 primary study.

**Correction applied:** `include_in_final_review` changed to "no - reclassified as background citation only"; extraction_notes updated to document the reclassification. It remains in the extraction file (so the work isn't lost) but should be cited only as background/introductory context, never as a benchmarking-table entry.

**Corrected Tier 1 primary-study count: 100** (101 minus PUBMED_0672).

## Recommendation

This dataset is accurate and non-fabricated based on the spot-checks performed, and is a legitimate first pass suitable for building draft benchmarking tables and starting to write. However, given ~94% of records are abstract-level only, any specific number that will appear in a final table or be directly quoted in the manuscript should get a full-text verification pass before submission - prioritize this for whichever layer gets drafted first. The `evidence_verification_level` column exists specifically to make this triage straightforward.
