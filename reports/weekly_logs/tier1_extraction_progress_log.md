# Tier 1 extraction progress log

Running log of scheduled-task batches completing full data extraction for the
101 "Tier 1 - full extraction" records identified in
`screening/full_text/pubmed_tier1_tier2_extraction_plan.csv`. Each entry
covers one scheduled-task run.

- 2026-07-19 — batch of 4 completed (PUBMED_0075, PUBMED_0157, PUBMED_1083, PUBMED_1084) — running total 4/101
- 2026-07-19 — batch of 2 completed (PUBMED_0021, PUBMED_0382) — running total 6/101
- 2026-07-19 — batch of 8 completed (PUBMED_0032, PUBMED_0304, PUBMED_0379, PUBMED_0421, PUBMED_0469, PUBMED_0537, PUBMED_0588, PUBMED_0649) — running total 14/101. Retrieval route note: Europe PMC REST API fetch was blocked this run by a new web_fetch "provenance set" restriction (only URLs already surfaced by search/prior fetch can be fetched, and no user was available to authorize a new URL in this unattended run). Fell back to the already-verified abstract text stored in the screening corpus (`pubmed_tier1_tier2_extraction_plan.csv`) for all 8 records; spot-checked PUBMED_0032 against an independent academic-literature search tool, which returned a verbatim matching abstract. Open-access/PMC status could not be re-verified this run and is flagged accordingly in the full-text tracker for future confirmation.
