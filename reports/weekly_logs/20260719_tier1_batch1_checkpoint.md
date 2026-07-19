# Tier 1 Extraction Batch 1 Checkpoint

## Date

2026-07-19

## Purpose

First full-extraction batch under the protocol v0.2 two-tier strategy, following on from the June 2026 pilot (3 records skim-extracted).

## Attempted This Batch

6 records queued from the top of `screening/full_text/pubmed_tier1_tier2_extraction_plan.csv`:

- PUBMED_0021 (PMID 29281419, endothelium)
- PUBMED_0032 (PMID 29413615, endothelium)
- PUBMED_0075 (PMID 29998891, endothelium)
- PUBMED_0157 (PMID 31129253, endothelium)
- PUBMED_1083 (PMID 38513048, stroma) - Consensus snowball addition
- PUBMED_1084 (PMID 38534529, endothelium) - Consensus snowball addition

## Outcome

- **4 completed**: PUBMED_0075, PUBMED_0157, PUBMED_1083, PUBMED_1084. Full extraction template rows filled (`extraction/pubmed_balanced_core_data_extraction_template.csv`).
- **2 blocked**: PUBMED_0021 and PUBMED_0032 hit a reCAPTCHA challenge on pubmed.ncbi.nlm.nih.gov during automated retrieval and were not retrieved this session. Marked `full_text_status: unavailable` in the retrieval tracker with a retry note. Left `extraction_status: not_started`.

## Access Notes

- PUBMED_0075, PUBMED_1083, PUBMED_1084: open access via PMC (PMC6048920, PMC10995904, PMC10968626 respectively). Full abstract, figures, and methods reviewed.
- PUBMED_0157: Elsevier-paywalled, no PMC deposit found. Extraction is abstract-level only (marked in `extraction_notes`); flagged for manual full-text follow-up if institutional access is available. This is a real limitation of automated retrieval that will recur for other paywalled Tier 1 records - expect a mix of full PMC extractions and abstract-level extractions across the remaining 97 Tier 1 records.

## Data Quality Note

None of the completed extractions include numeric mechanical/optical values pulled from tables or supplementary data - abstracts and figure captions describe *that* transparency/mechanical testing was done, but exact numbers (transmittance %, elastic modulus, etc.) typically live in figures or tables not captured by abstract-level review. Where this matters for the benchmarking tables, these 4 records should be revisited with direct table/figure extraction before final synthesis, not just abstract text.

## Follow-Up Identified

PUBMED_1084 (Ben Moussa et al. 2024) is from a research group (Thuret/Gain, Jean Monnet University) with related tissue-engineered endothelial keratoplasty (TEEK) papers not yet checked against the corpus: Crouzet et al. 2022 (rabbit TEEK surgical procedure, PMID 34967128) and Aouimeur et al. 2025/2026 (controlled cell density TEEK, PMID 40986463). Both surfaced in the same Consensus search that found the two gap papers. Worth a targeted check during the next retrieval batch - they would add in vivo/functional-control data to strengthen the endothelium layer's translational synthesis.

## Current Extraction Status

- Tier 1 total: 101 records
- Completed: 4
- Not started: 97
- Blocked/needs retry: 2 (subset of not started)

## Next Step

Continue Tier 1 retrieval down `pubmed_tier1_tier2_extraction_plan.csv`, retrying PUBMED_0021/PUBMED_0032 individually (space out requests to avoid reCAPTCHA), and check the Crouzet/Aouimeur TEEK papers noted above.
