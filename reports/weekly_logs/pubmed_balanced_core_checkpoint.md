# PubMed Balanced Core Checkpoint

## Project Title

From Optical Clarity to Clinical Readiness: A Layer-Specific Benchmarking Review of Biomaterials for Corneal Tissue Engineering

## Purpose of This Checkpoint

This checkpoint documents the transition from the initial PubMed screening pool to the balanced final PubMed core used for full-text retrieval and data extraction.

The goal was not simply to maximize the number of included papers. The goal was to create a defensible, layer-specific core set suitable for benchmarking corneal tissue-engineering biomaterials across optical, mechanical, biological, and translational criteria.

## PubMed Search and Screening Summary

- Raw PubMed records identified: 1,318
- Unique PubMed records after PMID deduplication: 1,082
- Title/abstract records screened: 1,082
- Title/abstract Include records: 541
- Title/abstract Uncertain records: 187
- Title/abstract Exclude records: 354
- Include + Uncertain records carried forward: 728

## Initial High-Priority Core

The first high-priority PubMed core contained 187 records.

However, manual audit identified that a small number of records were not suitable for core extraction because they were mainly clinical background, contact-lens/diagnostic, or broad mechanistic papers rather than primary biomaterial benchmarking studies.

After strict manual correction:

- Provisional final high-priority core: 185
- Strict final high-priority core: 181
- Downgraded to background/context: 3
- Excluded from core: 1

## Layer Imbalance Problem

The strict high-priority core was methodologically cleaner but layer-imbalanced:

- multiple_layers: 104
- stroma: 56
- epithelium_limbus: 15
- endothelium: 6

The endothelial and epithelial/limbal layers were underrepresented, which would weaken a layer-specific benchmarking review.

## Endothelium Correction

Medium-priority endothelial records were audited to strengthen the endothelial layer.

- Medium-priority endothelial candidates checked: 39
- Added to endothelial core: 27
- Excluded/background: 12
- Final endothelium count after expansion: 33

## Epithelium/Limbus Correction

Medium-priority epithelium/limbus records were audited in multiple stages because the first candidate pass was too permissive.

Initial medium-priority epithelium/limbus candidates:

- Candidates checked: 147
- Strict add-to-core candidates: 79
- Manual check: 16
- Excluded/background: 52

A top-tier filter was then applied:

- Top-tier core additions: 44
- Supporting epithelium/limbus records: 35

Final supervisor-level refinement demoted non-core papers focused mainly on storage, characterization tools, clinical modifiers, or surgical technique:

- Refined top-tier epithelium/limbus additions kept: 38
- Demoted to supporting/context: 6

## Balanced Final PubMed Core

The final balanced PubMed core contains:

- Total records: 246

Layer distribution:

- multiple_layers: 104
- stroma: 56
- epithelium_limbus: 53
- endothelium: 33

## Files Created for the Balanced Core

### Final Core Record List

`screening/full_text/pubmed_balanced_final_core_records.csv`

### Full-Text Retrieval Tracker

`screening/full_text/pubmed_balanced_full_text_retrieval_tracker.csv`

### Data Extraction Template

`extraction/pubmed_balanced_core_data_extraction_template.csv`

## Methodological Interpretation

This PubMed core is now suitable for structured full-text retrieval and extraction.

However, it remains PubMed-only. It should not be described as the final review corpus until planned searches from additional databases, such as Scopus, Web of Science, Embase, or ClinicalTrials.gov, are completed or explicitly declared out of scope.

## Supervisor-Level Warning

The balanced core is improved but still needs disciplined extraction.

During full-text review, records should still be excluded from final synthesis if they do not provide extractable evidence for at least one of the following:

- material/scaffold/carrier composition
- fabrication method
- optical performance
- mechanical performance
- biological/cell response
- in vitro, ex vivo, animal, or clinical performance
- layer-specific translational relevance

The final manuscript should clearly distinguish between:

- core extracted studies
- supporting/background studies
- translational or clinical context papers
- excluded records
