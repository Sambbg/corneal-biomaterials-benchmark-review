from pathlib import Path
import csv

DEDUP_REPORT = Path("reports/searches/pubmed_deduplication_report.md")
SCREENING_SUMMARY = Path("screening/title_abstract/pubmed_title_abstract_screening_summary.md")
CORE_REPORT = Path("screening/full_text/pubmed_provisional_final_core_report.md")

OUTPUT = Path("reports/searches/pubmed_prisma_style_summary.md")

MASTER = Path("screening/title_abstract/pubmed_title_abstract_screening.csv")
CORE = Path("screening/full_text/pubmed_provisional_final_core_records.csv")
EXCLUDED = Path("screening/title_abstract/pubmed_excluded_records.csv")
UNRESOLVED = Path("screening/full_text/pubmed_unresolved_manual_check_records.csv")
REMOVED = Path("screening/full_text/pubmed_manual_audit_removed_records.csv")

with MASTER.open(newline="", encoding="utf-8-sig") as f:
    master_rows = list(csv.DictReader(f))

with CORE.open(newline="", encoding="utf-8-sig") as f:
    core_rows = list(csv.DictReader(f))

with EXCLUDED.open(newline="", encoding="utf-8-sig") as f:
    excluded_rows = list(csv.DictReader(f))

with UNRESOLVED.open(newline="", encoding="utf-8-sig") as f:
    unresolved_rows = list(csv.DictReader(f))

with REMOVED.open(newline="", encoding="utf-8-sig") as f:
    removed_rows = list(csv.DictReader(f))

decision_counts = {}
for r in master_rows:
    d = r.get("decision", "") or "Unscreened"
    decision_counts[d] = decision_counts.get(d, 0) + 1

raw_pubmed_records = 1318
unique_pubmed_records = len(master_rows)
duplicates_removed = raw_pubmed_records - unique_pubmed_records

include_records = decision_counts.get("Include", 0)
uncertain_records = decision_counts.get("Uncertain", 0)
excluded_title_abstract = decision_counts.get("Exclude", 0)

carried_forward = include_records + uncertain_records

with OUTPUT.open("w", encoding="utf-8") as f:
    f.write("# PubMed PRISMA-Style Screening Summary\n\n")

    f.write("## Identification\n\n")
    f.write(f"- Records identified from PubMed searches: {raw_pubmed_records}\n")
    f.write(f"- Duplicate records removed by PMID: {duplicates_removed}\n")
    f.write(f"- Unique PubMed records after deduplication: {unique_pubmed_records}\n\n")

    f.write("## Title and Abstract Screening\n\n")
    f.write(f"- Records screened by title/abstract: {unique_pubmed_records}\n")
    f.write(f"- Records excluded at title/abstract stage: {excluded_title_abstract}\n")
    f.write(f"- Records marked Include: {include_records}\n")
    f.write(f"- Records marked Uncertain: {uncertain_records}\n")
    f.write(f"- Records carried forward for full-text/manual audit consideration: {carried_forward}\n\n")

    f.write("## Core Candidate Selection\n\n")
    f.write("- High-priority Include records were separated from medium-priority and uncertain records.\n")
    f.write("- Obvious false-positive records were audited before full-text retrieval.\n")
    f.write(f"- Provisional final PubMed core records retained: {len(core_rows)}\n")
    f.write(f"- Records removed during core audit: {len(removed_rows)}\n")
    f.write(f"- Unresolved manual-check records retained provisionally: {len(unresolved_rows)}\n\n")

    f.write("## Current Status\n\n")
    f.write("The PubMed search, deduplication, title/abstract screening, priority separation, manual-audit preparation, provisional core selection, full-text retrieval tracker, and data extraction template have been created.\n\n")

    f.write("## Important Limitation\n\n")
    f.write("This PRISMA-style summary currently covers PubMed only. It should not be presented as the final review PRISMA flow until Scopus, Web of Science, Embase, ClinicalTrials.gov, or other planned sources are searched and deduplicated.\n\n")

    f.write("## Linked Project Files\n\n")
    f.write(f"- Master screening file: `{MASTER}`\n")
    f.write(f"- Excluded title/abstract records: `{EXCLUDED}`\n")
    f.write(f"- Provisional final core records: `{CORE}`\n")
    f.write(f"- Unresolved manual-check records: `{UNRESOLVED}`\n")
    f.write(f"- Removed audit records: `{REMOVED}`\n")

print("PubMed PRISMA-style summary created.")
print(f"Records identified from PubMed searches: {raw_pubmed_records}")
print(f"Duplicates removed: {duplicates_removed}")
print(f"Unique records screened: {unique_pubmed_records}")
print(f"Excluded at title/abstract stage: {excluded_title_abstract}")
print(f"Include: {include_records}")
print(f"Uncertain: {uncertain_records}")
print(f"Provisional final core records: {len(core_rows)}")
print(f"Unresolved manual-check records: {len(unresolved_rows)}")
