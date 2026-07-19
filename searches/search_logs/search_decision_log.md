# Search Decision Log

This file records why search strings were accepted, rejected, expanded, or narrowed.

## Decision Template

### Date

### Database

### Search Version

### Result Count

### Decision

Accepted / revised / rejected

### Reason

### Changes Made

### Next Action

### Date
2026-05-25

### Database
PubMed

### Search Version
pubmed_pilot_search_v0.1

### Result Count
1822

### Decision
Revised.

### Reason
The search is too broad for a high-level biomaterials benchmarking review. The first results include general review articles and broad regenerative therapy papers rather than mainly primary studies with extractable biomaterial, optical, mechanical, biological, and translational performance data.

### Changes Made
The next search will narrow the strategy by:
- separating layer-specific searches;
- adding biomaterials/fabrication terms more explicitly;
- reducing broad regenerative medicine noise;
- checking whether primary studies are better represented.

### Next Action
Create PubMed pilot search v0.2 with layer-specific search strings for epithelium/limbus, stroma, endothelium, and full-thickness/multilayer constructs.

### Date
2026-05-25

### Database
PubMed

### Search Version
pubmed_pilot_search_v0.2

### Result Counts
Search A epithelium/limbus: 1481
Search B stroma: 502
Search C endothelium: 1090
Search D full-thickness/multilayer: 391

### Decision
Revised.

### Reason
Layer-specific searching improved structure but did not sufficiently reduce noise. Search A and Search C remain too broad. Search B and Search D are more manageable but still retrieve broad reviews near the top. The search strategy needs a sharper primary-evidence and biomaterials-performance focus.

### Changes Needed
Create PubMed pilot search v0.3 using:
- stronger biomaterials and fabrication constraints;
- title/abstract terms for measurable performance;
- optional exclusion of review publication types during primary-study retrieval;
- separate supplementary search for landmark reviews and background sources.

### Next Action
Create PubMed pilot search v0.3.

### Date
2026-05-25

### Database
PubMed

### Search Version
pubmed_pilot_search_v0.3

### Result Counts
A3 epithelium/limbus: 275
B3 stroma: 444
C3 endothelium: 841
D3 full-thickness/multilayer: 182

### Decision
Partially accepted.

### Reason
A3, B3 and D3 are now suitable for pilot screening. C3 remains too broad because it retrieves general endothelial transplantation and ophthalmology papers rather than mainly engineered endothelial substitutes, carriers, membranes, hydrogels or cell-sheet approaches.

### Next Action
Create a stricter endothelial search version C4.

### Date
2026-05-25

### Database
PubMed

### Search Version
pubmed_endothelium_search_C4

### Result Count
417

### Decision
Accepted for pilot screening.

### Reason
C4 reduced the endothelial search from 841 to 417 results and better prioritised engineered substitutes, iPSC-derived endothelial substitutes, endothelial graft manufacturing, phenotype markers, and translational cell-based evidence.

### Final PubMed Pilot Set
Accepted PubMed pilot searches:

- A3 epithelium/limbus: 275 results
- B3 stroma: 444 results
- C4 endothelium: 417 results
- D3 full-thickness/multilayer: 182 results

Total before deduplication: 1318 records

### Next Action
Create screening templates and begin title/abstract pilot screening using a small sample from each accepted search.

### Date
2026-07-19

### Database
Consensus (Semantic Scholar / PubMed / Scopus / ArXiv aggregator)

### Search Version
consensus_snowball_v0.1

### Result Count
2 queries, 20 results each (40 total reviewed)

### Decision
Accepted as supplementary evidence (protocol v0.2).

### Reason
Per protocol v0.2, the review stays single-database (PubMed) rather than expanding to Scopus/Web of Science/Embase, since the target is now a Q2 biomaterials journal rather than Acta Biomaterialia. To partially offset single-database risk, a targeted Consensus search was run against two query strings ("corneal tissue engineering biomaterials review layer-specific benchmarking" and "corneal endothelium bioengineered substitute clinical translation graft") to snowball-check recent (2022-2026) landmark primary studies and reviews against the existing PubMed screening corpus.

Cross-checked ~10 standout titles against `screening/title_abstract/pubmed_title_abstract_screening.csv`. Findings:
- Most recent landmark primary studies were already captured (RAFT collagen carrier work, allogeneic cornea-derived matrix graft, crosslinked amniotic membrane substitute, Hirayama et al. 2024 first-in-human iPSC corneal endothelial substitute trial).
- Review articles correctly absent (reviews are excluded as primary evidence per inclusion/exclusion criteria) - not a search failure.
- Two primary-study gaps confirmed genuinely missing: Puistola et al. 2024 (PMID 38513048, stroma-specific adipose-stem-cell-derived ECM bioink) and Ben Moussa et al. 2024 (PMID 38534529, femtosecond-laser-cut lens capsule endothelial carrier).
- One related-work flag: Anitua et al. 2025, a PROSPERO-registered PRISMA systematic review (CRD420250654641) comparing bioengineered corneal grafts to healthy corneas across layers in animal models. Overlaps in subject matter; requires explicit differentiation in the introduction/discussion (see protocol v0.2, "Related Work Requiring Explicit Differentiation").

### Changes Made
Added Puistola et al. 2024 (PUBMED_1083) and Ben Moussa et al. 2024 (PUBMED_1084) to the title/abstract screening master file, the balanced final core records, and the extraction template via `scripts/add_consensus_gap_papers.py`. Regenerated the retrieval priority order (now 248 records) and created a two-tier extraction plan (`scripts/create_tier1_tier2_extraction_plan.py`), manually promoting both new papers to Tier 1 despite below-cutoff heuristic scores, since they were deliberately curated additions rather than bulk-triaged records.

### Next Action
Begin Tier 1 full-text retrieval in the order set by `screening/full_text/pubmed_tier1_tier2_extraction_plan.csv` (101 records), starting with the highest-scoring endothelium records and the two newly added gap papers.
