# PubMed Core Candidate Records Report

## Purpose

This report creates a cleaner core candidate set from the high-priority Include records. Only records marked as likely false positives are removed automatically. Records marked as needing manual check are retained but separated for audit.

## Counts

- Original high-priority Include records: 187
- Automatically removed likely false positives: 1
- Core candidate records retained: 186
- Core records requiring manual audit: 64

## Core Candidate Records by Layer

- multiple_layers: 108
- stroma: 56
- epithelium_limbus: 16
- endothelium: 6

## Manual Audit Records by Layer

- multiple_layers: 48
- stroma: 11
- epithelium_limbus: 5

## Automatically Removed Records

- PUBMED_0822 / PMID 39337712: Influence of Intraocular Pressure on the Expression and Activity of Sodium-Potassium Pumps in the Corneal Endothelium.

## Output Files

- Core candidate records: `screening/full_text/pubmed_core_candidate_records.csv`
- Manual audit subset: `screening/full_text/pubmed_core_candidate_manual_audit_records.csv`
- Removed likely false positives: `screening/full_text/pubmed_removed_likely_false_positives.csv`
