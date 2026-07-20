"""
Targeted full-text upgrade pass (Task #9), batch 1.

Applies genuine full-text-verified data to records from
tables/gap_analysis_for_fulltext_upgrade.csv where the actual article body
(not just the abstract) was read this run. Only PUBMED_0910 qualifies for a
real upgrade in this batch -- the Nature/Scientific Reports article is fully
open access and its Results/Discussion sections were read directly
(https://www.nature.com/articles/s41598-025-96494-6).

Other records investigated this batch (PUBMED_0081/Kim 2018 Adv Healthc
Mater, PUBMED_0151/primate transplant, PUBMED_0690/squid mantle) were
paywalled (Wiley) or blocked (PMC reCAPTCHA), so only WebSearch-derived
secondary summaries were available -- these are NOT treated as full-text
verification and are left as abstract_only, consistent with the QC standard
already applied to the rest of the corpus (no fabrication, no upgrading
evidence tier without actually reading the source).
"""
import csv
from pathlib import Path

PATH = Path("extraction/pubmed_balanced_core_data_extraction_template.csv")

with PATH.open(newline="", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))
    fieldnames = list(rows[0].keys())

for row in rows:
    if row["screening_id"] != "PUBMED_0910":
        continue

    row["optical_transparency_reported"] = "yes"
    row["optical_metric_details"] = (
        "Full text (Results, Fig. 1B): RAFT collagen matrix light transmittance "
        "60.71 +/- 1.17% at 550 nm (n=3 biological replicates), measured across "
        "400-700 nm. Qualitatively, cell-seeded RAFT grafts became visibly "
        "transparent by day 14 post-transplantation (recipient cornea regained "
        "regular light reflection), versus acellular-RAFT recipients that remained "
        "cloudy with irregular light reflection throughout (Fig. 2C-D)."
    )

    row["mechanical_testing_reported"] = "partial"
    row["mechanical_metric_details"] = (
        "No tensile/modulus testing reported. Full text does report a functional "
        "mechanical/physiological readout: corneal thickness (edema) as a proxy for "
        "endothelial pump function. Cell-seeded-RAFT group: thickness fell from "
        "926.27 +/- 30.17 micron (baseline) to 673.86 +/- 49.83 micron (day 2) to "
        "641.6 +/- 57.00 micron (day 14). Acellular-RAFT group: thickness stayed "
        "elevated, 915.20 +/- 46.1 micron (baseline) to 733.27 +/- 34.94 micron "
        "(day 2) to 752.87 +/- 48.87 micron (day 14). Mean thickness difference "
        "between groups = 82.57 +/- 15.62 micron, p<0.05 (n=3 donor cornea pairs)."
    )

    row["biological_metric_details"] = (
        row["biological_metric_details"]
        + " Full text adds: endothelial cell density ~3000 cells/mm2 on the graft "
        "at day 14 (Na/K-ATPase+ staining); Live/Dead assay confirmed cells "
        "remained viable at day 14; H&E cross-sections showed the RAFT graft "
        "attached to the posterior stroma with collagen fibre integration."
    )

    row["main_limitations"] = (
        "Xenogeneic (porcine) cell source used on human ex vivo tissue rather than "
        "human cells; ex vivo organ culture only (no live in vivo animal or "
        "clinical evaluation); short (2-week) follow-up; small n (3 donor cornea "
        "pairs); cell-cell boundary staining became less organized/blurred over "
        "culture, attributed by the authors to serum-driven keratocyte "
        "differentiation at the graft-stroma interface (discussed as a limitation "
        "requiring culture-medium optimization in future work)."
    )

    row["extraction_notes"] = (
        row["extraction_notes"]
        + " FULL-TEXT UPGRADE 2026-07-20 (Task #9, batch 1): genuine open-access "
        "full text read at https://www.nature.com/articles/s41598-025-96494-6 "
        "(Results, Discussion). Quantitative transmittance and corneal-thickness "
        "data added above; optical_transparency_reported and "
        "mechanical_testing_reported upgraded from 'unclear/not reported' "
        "accordingly. mechanical_testing_reported set to 'partial' because the "
        "paper reports a functional/physiological thickness readout, not a "
        "direct tensile/modulus measurement -- flagging so this isn't conflated "
        "with true mechanical testing in Table 2 aggregation."
    )

    row["evidence_verification_level"] = "full_text_verified"

with PATH.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)

print("Updated PUBMED_0910 with full-text-verified data.")
