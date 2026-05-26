# PubMed Pipeline Checkpoint

## Project

Layer-specific benchmarking review of biomaterials for corneal tissue engineering.

## Completed Work

### 1. Repository setup

The project repository has been structured for a reproducible review workflow, including protocol files, search logs, screening files, extraction files, figures, tables, reports, and scripts.

### 2. PubMed search and export

Four PubMed search blocks were used:

- A3: epithelium/limbus
- B3: stroma
- C4: endothelium
- D3: full-thickness/multilayer

Raw PubMed records before deduplication:

- 1318 records

### 3. Deduplication

Records were deduplicated by PMID.

- Unique PubMed records: 1082
- Duplicate records removed: 236

### 4. Title and abstract screening

All 1082 unique PubMed records were screened.

Final title/abstract decisions:

- Include: 541
- Uncertain: 187
- Exclude: 354

Records carried forward for full-text/manual audit consideration:

- 728

### 5. Priority separation

The screened records were separated into priority groups.

- High-priority Include: 187
- Medium-priority Include: 354
- Uncertain/manual audit: 187

### 6. High-priority audit

The high-priority Include records were audited for obvious false positives.

- High-priority records checked: 187
- Likely false positives removed: 1
- Core candidate records retained: 186

### 7. Provisional final PubMed core

After audit prefill and provisional filtering:

- Provisional final PubMed core records: 185
- Unresolved manual-check records retained provisionally: 23

Layer distribution:

- multiple_layers: 108
- stroma: 56
- epithelium_limbus: 15
- endothelium: 6

### 8. Full-text retrieval tracker

A full-text retrieval tracker was created for the 185 provisional final core records.

### 9. Data extraction template

A data extraction template was created for the 185 provisional final core records.

The extraction template captures:

- Study type
- Target corneal layer
- Biomaterial category
- Specific materials
- Fabrication method
- Scaffold architecture
- Cell type and source
- Optical performance
- Mechanical performance
- Biological performance
- In vitro, ex vivo, animal, or clinical evidence
- Follow-up duration
- Translational readiness
- Benchmarking relevance
- Final inclusion decision

### 10. PRISMA-style PubMed summary

A PubMed-only PRISMA-style screening summary was created.

Important limitation:

This is not yet the final review PRISMA flow. It covers PubMed only. Additional sources such as Scopus, Web of Science, Embase, ClinicalTrials.gov, or other planned databases still need to be searched and deduplicated before a final PRISMA flow can be claimed.

## Critical Methodological Warning

The current PubMed core pool is heavily weighted toward multilayer and stromal studies.

Endothelium is underrepresented:

- Endothelium high-priority provisional core records: 6

This means selected medium-priority endothelial records will probably need to be reviewed later to avoid an unbalanced manuscript.

## Next Recommended Step

Before retrieving full texts, resolve the 23 unresolved manual-check records.

After that:

1. Create the final PubMed core list.
2. Begin full-text retrieval.
3. Start extraction using the extraction template.
4. Add selected medium-priority endothelial records if the endothelium evidence base remains too thin.
