# Targeted Full-Text Upgrade Pass — Progress Log (Task #9)

Source list: `tables/gap_analysis_for_fulltext_upgrade.csv` (40 flagged records, 23 high-priority = high benchmarking_relevance + evidence_verification_level=abstract_only).

## Access reality check (2026-07-20, batch 1)

Two access routes were tested this run:
- **Europe PMC REST API (`ebi.ac.uk`)** — rate-limited (HTTP 429) on the very first call and remained limited across multiple retries with waits in between. Same wall hit during Tier 1 extraction; likely an hourly-scale limit on this specific domain via the sandboxed `web_fetch` tool.
- **Publisher domains directly (`nature.com`, `wiley.com`, etc.) via WebSearch → web_fetch** — NOT subject to the same rate limit. This is a materially better route going forward: search for the paper, grab the publisher URL, fetch it directly.
- **`pubmed.ncbi.nlm.nih.gov` / `pmc.ncbi.nlm.nih.gov`** — still blocked by reCAPTCHA (consistent with earlier findings in this project).

Net effect: full-text upgrade work is possible in live sessions by routing through publisher pages instead of Europe PMC, but is still gated by (a) whether the specific article is genuinely open access, and (b) the general web_fetch rate limit, which is not domain-specific in an absolute sense — it re-appeared after ~40s on a second ebi.ac.uk call, so pacing across a session, not just switching domains, still matters.

## Batch 1 results

| Record | PMID | Outcome |
|---|---|---|
| PUBMED_0910 | 40221533 | **Upgraded to `full_text_verified`.** Fully open-access Scientific Reports article, read directly. Added real quantitative data: RAFT collagen matrix light transmittance (60.71 ± 1.17% at 550 nm) and corneal thickness/edema time-course data (functional endothelial-pump readout, 82.57 ± 15.62 µm group difference, p<0.05, n=3 donor pairs). See `extraction_notes` for the record. |
| PUBMED_0081 | 30066447 | Investigated, not upgraded. Paper (Kim et al. 2018, *Adv Healthc Mater*) is paywalled on Wiley — only the abstract page was reachable. WebSearch returned a secondary AI-generated summary, which is **not** treated as full-text verification (no fabricated upgrade applied). Left as `abstract_only`. |
| PUBMED_0151 | 30989737 | Investigated, not upgraded. WebSearch did not surface the exact paper (search results returned related-but-different primate CE transplantation studies). Left as `abstract_only`. |
| PUBMED_0690 | 37476050 | Investigated, not upgraded. Genuinely open-access (PMC10354768, also on Wiley/AIChE's *Bioengineering & Translational Medicine*), but both the PMC page (reCAPTCHA) and the Wiley page (returned empty / JS-rendered shell) were unreachable via `web_fetch` this run. Left as `abstract_only`. |
| PUBMED_0934 | 40446990 | Investigated, not upgraded. WebSearch did not locate this specific paper (very recent, 2025) — no reliable full-text or abstract-confirming source found this run. Left as `abstract_only`; flag for a follow-up search rather than treating this as resolved. |

## Recommendation for continuing this task

Given the mixed success rate (1 of 5 attempted this batch), the realistic expectation for the remaining ~18-19 high-priority records is similarly partial: some will be genuinely open access and reachable, many will be paywalled or blocked by reCAPTCHA. This should be treated as an ongoing best-effort pass across future live sessions, not a task that can be driven to 100% completion — and that limitation (some corpus records could not be independently full-text verified despite good-faith attempts) is itself legitimate to state plainly in the manuscript's Methods/Limitations section, consistent with the project's existing transparency approach (`evidence_verification_level` field, `20260720_tier1_quality_control_pass.md`).
