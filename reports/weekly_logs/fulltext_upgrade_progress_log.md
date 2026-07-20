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

## Batch 2 — Consensus connector as a supplementary source (2026-07-20)

Tested whether the Consensus academic search connector could substitute for full-text access. Result: `include_full_text_chunks` is Enterprise-only (confirmed via direct API error) — Consensus cannot retrieve paywalled full text either. However, it returned independently-sourced abstracts (Semantic Scholar/PubMed/Scopus backed, not an AI-generated summary) with no rate-limit collisions with `web_fetch`, useful as a faster cross-check tool. Note: Consensus itself has its own rate limit (hit after ~2 rapid parallel calls; resets quickly, unlike the sustained `ebi.ac.uk` block).

Findings this batch:
- **PUBMED_0081** (30066447, Kim 2018) — Consensus abstract confirms and slightly extends prior extraction (graft-vs-control edema comparison at 3-4 weeks). No mechanical data in the abstract. Not upgraded.
- **PUBMED_0151** (30989737, Zhao 2019) — Consensus abstract matches existing extraction closely (cell density, corneal thickness at day 181). No mechanical data in the abstract. Not upgraded.
- **PUBMED_0322** (32805263, An 2020) — Consensus abstract matches existing extraction (>90% transparency vs control). No mechanical data in the abstract. Not upgraded.

For all three, the "mechanical" gap flagged in the gap-analysis table is now cross-verified as a genuine property of the source paper's abstract (no tensile/modulus data reported), not a missed extraction — noted directly in each record's `extraction_notes`. This is useful confirmation but not a tier upgrade, since it doesn't establish what (if anything) the full paywalled text contains beyond the abstract.

## Batch 3 — user-supplied PDFs (2026-07-20)

Samuel sourced 18 of the 22 requested PDFs via his own library access (4 confirmed paywalled even to him: PUBMED_0081, PUBMED_0151, PUBMED_0359, PUBMED_0649) and placed them in `Desktop/papers/`. Processed via the Read tool (bash/pdftotext repeatedly hit a filesystem lock on that mount — "Resource deadlock avoided" — so the Read tool was used directly on the Mac-side path instead).

**11 records upgraded to `full_text_verified`** with real transcribed numbers: PUBMED_0056, PUBMED_0171, PUBMED_0241, PUBMED_0322, PUBMED_0398, PUBMED_0450, PUBMED_0469 (gap confirmed genuine), PUBMED_0477 (gap confirmed genuine), PUBMED_0530, PUBMED_0623, PUBMED_0646, PUBMED_0981. See `extraction_notes` per record for exact figures and sourcing.

**Notable finding:** PUBMED_0981 is the Aouimeur et al. 2026 "Super TEEKs" paper (*Tissue Engineering Part A*) — confirms this record IS the companion paper flagged in Task #10, and its own reference list confirms the lineage Crouzet 2022 → Ben Moussa 2024 (PUBMED_1084, already in corpus) → Aouimeur 2026 (PUBMED_0981) as one continuous series from the Saint-Étienne BiiO lab (Gilles Thuret group).

**3 records read but not upgraded**, to avoid transcribing imprecise numbers:
- PUBMED_0690 (squid mantle) — full text reviewed, qualitative confirmation only (transparency achieved via CUBIC clearing, good biocompatibility); precise tensile/modulus figures not transcribed this pass.
- PUBMED_0934 — full text reviewed (confirms it's a real paper — WebSearch had failed to locate it earlier); precise figures not transcribed this pass.
- PUBMED_1015 — the PDF supplied was Supporting Information only, not the main manuscript. SI figures confirm optical transmittance and rheology data exist, but exact main-text values aren't in the SI.

**1 record could not be processed:** PUBMED_0937 exceeds the 20MB PDF read limit.

Net for Task #9: of the original 23 high-priority gap records, **12 are now genuinely `full_text_verified`** (PUBMED_0910 + 11 from this batch), 3 have abstract-level gaps confirmed as genuine paper limitations (not extraction misses), 4 are confirmed inaccessible even via Samuel's library access, 3 were read but held back from upgrade pending a precise-figures pass, and 1 (PUBMED_0937) needs a smaller file.

## Recommendation for continuing this task

Given the mixed success rate (1 of 5 attempted this batch), the realistic expectation for the remaining ~18-19 high-priority records is similarly partial: some will be genuinely open access and reachable, many will be paywalled or blocked by reCAPTCHA. This should be treated as an ongoing best-effort pass across future live sessions, not a task that can be driven to 100% completion — and that limitation (some corpus records could not be independently full-text verified despite good-faith attempts) is itself legitimate to state plainly in the manuscript's Methods/Limitations section, consistent with the project's existing transparency approach (`evidence_verification_level` field, `20260720_tier1_quality_control_pass.md`).
