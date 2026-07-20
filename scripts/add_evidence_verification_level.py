"""
Quality-control follow-up (2026-07-20) after the Tier 1 extraction batches.

Adds an explicit `evidence_verification_level` column to the extraction
template so every downstream table/figure/manuscript claim can be traced to
how thoroughly its source was actually read, rather than treating all 101
Tier 1 rows as equally verified. This is standard practice for evidence
synthesis (comparable to a lightweight certainty-of-evidence flag) and is
necessary here because most Tier 1 records were extracted from PubMed/Europe
PMC abstract text rather than full article text, due to a tool-level fetch
restriction encountered during the unattended scheduled-task batches (see
reports/weekly_logs/tier1_extraction_progress_log.md for the full history).

Three levels, derived from each record's own `extraction_notes` (written at
extraction time, not reconstructed after the fact):

- full_text_verified: the actual article page/PMC full text was fetched and
  read (methods, results, discussion, not just the abstract).
- abstract_plus_figures: the PubMed/PMC abstract page was read together with
  figure captions (richer than a bare abstract, but not the full body text).
- abstract_only: only the structured abstract text was available (via
  Europe PMC REST API or the locally-stored screening-corpus abstract).

Also reclassifies PUBMED_0672, which extraction revealed to be a narrative
review rather than a primary study, which the project's own protocol
(protocol/review_protocol_v0.1.md, "Exclusion Criteria": "Reviews as primary
evidence") excludes from primary evidence. It is removed from the "Tier 1
primary studies" count and its `include_in_final_review` field updated to
reflect background-citation-only status, rather than silently left as if it
were a normal included primary study.
"""
import csv
from pathlib import Path

path = Path("extraction/pubmed_balanced_core_data_extraction_template.csv")
with path.open(newline="", encoding="utf-8-sig") as f:
    r = csv.DictReader(f)
    rows = list(r)
    fieldnames = r.fieldnames

if "evidence_verification_level" not in fieldnames:
    fieldnames = fieldnames + ["evidence_verification_level"]


def classify(notes: str) -> str:
    n = notes or ""
    if "Full text retrieved this run via web_fetch" in n:
        return "full_text_verified"
    if "Full abstract and figure captions reviewed via PMC" in n:
        return "abstract_plus_figures"
    if "Full open-access text available via PMC" in n:
        # PUBMED_1083/1084 (Consensus gap-fill additions): the full PubMed/PMC
        # page including figure-by-figure captions and methods detail was
        # read directly during manual extraction (2026-07-19), not just the
        # bare abstract - same evidentiary depth as abstract_plus_figures.
        return "abstract_plus_figures"
    # Everything else completed was abstract-level only: Europe PMC REST API
    # structured abstract, the locally-stored screening-corpus abstract text,
    # or an explicitly paywalled/abstract-only case.
    return "abstract_only"


# Known-for-certain overrides: these 6 records were extracted manually
# (2026-07-19, this session) by directly reading the full pubmed.ncbi.nlm.nih.gov
# page for each - which includes figure-by-figure captions and methods detail
# when the article is PMC-hosted, or confirms paywalled/abstract-only status
# when it is not. This is first-hand knowledge, more reliable than pattern-
# matching noisy extraction_notes text written across 14 different batches.
KNOWN_OVERRIDES = {
    "PUBMED_0075": "abstract_plus_figures",  # PMC6048920, full page + figures read
    "PUBMED_0157": "abstract_only",          # Elsevier paywalled, no PMC/figures
    "PUBMED_1083": "abstract_plus_figures",  # PMC10995904, full page + figures read
    "PUBMED_1084": "abstract_plus_figures",  # PMC10968626, full page + figures read
    "PUBMED_0021": "abstract_only",          # Europe PMC REST API JSON only
    "PUBMED_0382": "abstract_only",          # Europe PMC REST API JSON only
}

counts = {"full_text_verified": 0, "abstract_plus_figures": 0, "abstract_only": 0, "": 0}
for row in rows:
    if row.get("extraction_status") == "completed":
        sid = row["screening_id"]
        level = KNOWN_OVERRIDES.get(sid) or classify(row.get("extraction_notes", ""))
        row["evidence_verification_level"] = level
        counts[level] += 1
    else:
        row["evidence_verification_level"] = ""
        counts[""] += 1

# Reclassify PUBMED_0672 (narrative review, not a primary study).
# Guarded so re-running this script doesn't duplicate the note.
RECLASSIFY_NOTE = (
    " RECLASSIFIED 2026-07-20 QC pass: this is a narrative review, not a primary "
    "study, and the project's own protocol excludes reviews as primary evidence "
    "(protocol/review_protocol_v0.1.md, Exclusion Criteria). Removed from the "
    "'Tier 1 primary studies' count; retained in this file only as a candidate "
    "background/introductory citation, not a benchmarking-table entry."
)
for row in rows:
    if row["screening_id"] == "PUBMED_0672":
        row["include_in_final_review"] = "no - reclassified as background citation only"
        if "RECLASSIFIED 2026-07-20 QC pass" not in row["extraction_notes"]:
            row["extraction_notes"] = row["extraction_notes"] + RECLASSIFY_NOTE

with path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)

print("Evidence verification levels assigned:")
for k, v in counts.items():
    print(f"  {k or '(not completed)'}: {v}")

primary_study_count = sum(
    1 for row in rows
    if row.get("extraction_status") == "completed"
    and row["screening_id"] != "PUBMED_0672"
)
print(f"\nTrue Tier 1 primary-study count (excluding reclassified review): {primary_study_count}")
