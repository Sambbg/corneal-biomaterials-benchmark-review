# Project Status After PubMed Balancing

## Project Title

From Optical Clarity to Clinical Readiness: A Layer-Specific Benchmarking Review of Biomaterials for Corneal Tissue Engineering

## Current Stage

PubMed search, deduplication, title/abstract screening, prioritisation, manual correction, and balanced core construction are complete.

The project is now ready for either:

1. additional database searches, or
2. PubMed full-text retrieval and extraction.

## Completed PubMed Workflow

### Search and Deduplication

- PubMed raw records identified: 1,318
- Unique PubMed records after PMID deduplication: 1,082
- Duplicate records removed: 236

### Title/Abstract Screening

- Records screened: 1,082
- Include: 541
- Uncertain: 187
- Exclude: 354
- Include + Uncertain carried forward: 728

### Core Development

The first strict high-priority PubMed core was methodologically clean but layer-imbalanced.

Initial strict core:

- Total: 181
- multiple_layers: 104
- stroma: 56
- epithelium_limbus: 15
- endothelium: 6

Because this was too weak for a layer-specific review, selected medium-priority records were audited and added for underrepresented layers.

### Endothelium Correction

- Medium-priority endothelial candidates checked: 39
- Added to endothelial core: 27
- Final endothelium count: 33

### Epithelium/Limbus Correction

- Medium-priority epithelium/limbus candidates checked: 147
- Strict add-to-core candidates: 79
- Top-tier additions: 44
- Final refined top-tier additions: 38
- Final epithelium/limbus count: 53

## Balanced Final PubMed Core

Final balanced PubMed core:

- Total records: 246
- multiple_layers: 104
- stroma: 56
- epithelium_limbus: 53
- endothelium: 33

## Key Output Files

### Final Balanced Core

`screening/full_text/pubmed_balanced_final_core_records.csv`

### Full-Text Retrieval Tracker

`screening/full_text/pubmed_balanced_full_text_retrieval_tracker.csv`

### Data Extraction Template

`extraction/pubmed_balanced_core_data_extraction_template.csv`

### Main Checkpoint Report

`reports/weekly_logs/pubmed_balanced_core_checkpoint.md`

## Current Methodological Status

The PubMed corpus is now strong enough for structured full-text retrieval.

However, it should still be described as a PubMed-derived core only. It should not be presented as the final review corpus unless additional planned databases are either searched or explicitly declared outside the scope.

## Recommended Next Step

The next methodological step should be one of the following:

### Option A: Continue Database Expansion

Add Scopus, Web of Science, Embase, and ClinicalTrials.gov searches.

This is the stronger route for a publishable Q1-style review.

### Option B: Begin PubMed Full-Text Retrieval

Start retrieving full texts for the 246-record balanced PubMed core.

This is acceptable for internal development but weaker for a final publishable manuscript if no other databases are added.

## Supervisor-Level Recommendation

Do not begin extracting all 246 full texts blindly.

A more disciplined next step is to create a retrieval priority order:

1. clinical/translational studies
2. in vivo studies
3. ex vivo studies
4. strong in vitro biomaterial studies
5. supporting/background studies

This will prevent the extraction workload from becoming inefficient.
