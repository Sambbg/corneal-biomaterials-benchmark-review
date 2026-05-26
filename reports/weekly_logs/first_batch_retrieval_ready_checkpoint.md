# First PubMed Retrieval Batch Ready Checkpoint

## Project Title

From Optical Clarity to Clinical Readiness: A Layer-Specific Benchmarking Review of Biomaterials for Corneal Tissue Engineering

## Purpose

This checkpoint documents the final preparation of the first PubMed full-text retrieval batch.

The original first retrieval batch was constructed as a balanced workflow batch of 80 records, with 20 records selected per corneal layer. A layer-label audit then identified records whose assigned layer labels needed correction before retrieval and extraction.

## Retrieval Batch History

### Initial First Retrieval Batch

- Source file: `screening/full_text/pubmed_balanced_first_retrieval_batch.csv`
- Total records: 80
- Initial workflow balance:
  - endothelium: 20
  - epithelium_limbus: 20
  - multiple_layers: 20
  - stroma: 20

### Layer-Label Audit

- Audit file: `screening/full_text/pubmed_first_batch_layer_label_audit.csv`
- Records audited: 80
- Label OK: 59
- Manual check: 21

### Manual Layer Corrections

- Corrected batch file: `screening/full_text/pubmed_corrected_first_retrieval_batch.csv`
- Records checked: 80
- Actual layer-label changes: 12
- Reviewed but unchanged: 68

Corrected biological layer distribution:

- endothelium: 23
- stroma: 23
- epithelium_limbus: 21
- multiple_layers: 13

## Active Retrieval Tracker

The active tracker for full-text retrieval is:

`screening/full_text/pubmed_first_batch_retrieval_tracker_corrected_layers.csv`

This supersedes the earlier tracker:

`screening/full_text/pubmed_first_batch_retrieval_tracker.csv`

The corrected tracker should be used for manual retrieval status, PDF availability, source checked, retrieval date, and extraction readiness.

## Supporting Lookup Files

For faster searching:

`screening/full_text/pubmed_first_batch_lookup_list.md`

`screening/full_text/pubmed_first_batch_lookup_queries.txt`

## Methodological Note

The first retrieval batch was initially balanced numerically by layer, but corrected afterward for biological accuracy.

This is methodologically preferable. For a layer-specific review, correct biological layer assignment is more important than artificial numerical symmetry.

## Ready for Retrieval

The project is now ready to begin full-text retrieval for the first 80 PubMed records.

Recommended retrieval order:

1. Use `pubmed_first_batch_retrieval_tracker_corrected_layers.csv`
2. Search by DOI first where available.
3. Search by PMID/title if DOI lookup fails.
4. Record retrieval status immediately.
5. Mark extraction readiness only after confirming the article is a primary biomaterial/tissue-engineering study with extractable methods/results.
