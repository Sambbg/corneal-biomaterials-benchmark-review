"""
Tier 1 extraction batch 2 (2026-07-19, continued).

Retrieval route: pubmed.ncbi.nlm.nih.gov was blocking automated requests with
a reCAPTCHA challenge for several records in batch 1 (PUBMED_0021,
PUBMED_0032). Switched to the Europe PMC REST API
(https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:<pmid>&format=json&resultType=core),
which returns full structured abstracts (including MeSH terms, journal
metadata, and open-access/PMC status) without the CAPTCHA issue. This is now
the preferred retrieval route for subsequent Tier 1 batches.

This batch:

- PUBMED_0021 (PMID 29281419, endothelium) - electrospun PMMA/PLGA/PCL
  scaffolds, retrieved via Europe PMC (subscription-required full text, but
  abstract itself is fully quantitative).
- PUBMED_0382 (PMID 33463278, endothelium) - fish-scale collagen membrane,
  retrieved via Europe PMC (subscription-required full text).
"""
import csv
from pathlib import Path

path = Path("extraction/pubmed_balanced_core_data_extraction_template.csv")
with path.open(newline="", encoding="utf-8-sig") as f:
    r = csv.DictReader(f)
    rows = list(r)
    fieldnames = r.fieldnames

by_id = {row["screening_id"]: row for row in rows}

EXTRACTIONS = {
    "PUBMED_0021": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / scaffold comparison study (in vitro)",
        target_layer_final="endothelium",
        biomaterial_category="electrospun synthetic polymer scaffolds",
        specific_materials="poly(methyl-methacrylate) (PMMA), poly(lactic-co-glycolic acid) (PLGA), polycaprolactone (PCL) - three scaffolds compared head-to-head",
        fabrication_method="electrospinning of PMMA, PLGA, and PCL under equal spinning parameters",
        scaffold_architecture="electrospun nanofibrous/microfibrous mesh scaffolds",
        cell_type_used="HCEC-12 (immortalized human corneal endothelial cell line)",
        cell_source="human (cell line)",
        growth_factors_or_bioactive_agents="none reported",
        optical_transparency_reported="yes",
        optical_metric_details="Light transmission measured as part of scaffold evaluation (method stated; comparative numeric transmittance values not given in abstract).",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Fiber diameter: PMMA 2.99+/-0.24 um, PCL 2.29+/-0.11 um, PLGA 1.84+/-0.21 um (PMMA>PCL p=0.003, PCL>PLGA p=0.002). Interstitial/pore spacing (porometry): PMMA 26.77+/-17.48 um, PCL 13.30+/-5.47 um, PLGA 10.42+/-6.15 um (PMMA vs PCL p=0.04, PMMA vs PLGA p=0.002, PCL vs PLGA not significant p=0.26).",
        biological_testing_reported="yes",
        biological_metric_details="SEM: only PLGA preserved normal HCEC-12 morphology. Live/dead staining and cell viability assay at 7 days: PLGA vs PCL no significant difference in cell number/death/viability; PMMA significantly more cytotoxic (p<0.001) - viability PLGA 1626.2+/-183.8 RLU, PCL 1580.2+/-171.02 RLU, PMMA 841.9+/-92.7 RLU.",
        in_vitro_model="yes", ex_vivo_model="no", animal_model="no", clinical_evidence="no",
        follow_up_duration="3-7 days in vitro culture",
        main_outcomes="Head-to-head comparison of three electrospun polymers for corneal endothelial scaffolds: PLGA and PCL were equally biocompatible and non-cytotoxic, while PMMA was significantly cytotoxic; only PLGA preserved normal HCEC-12 morphology, making it the most promising candidate for tissue-engineered endothelial graft (TEEG) construction among the three.",
        main_limitations="Immortalized cell line (HCEC-12), not primary human corneal endothelial cells; in vitro only; short follow-up (up to 7 days); comparative light transmission values described but not quantified in the abstract itself.",
        translational_readiness_level="early preclinical (in vitro material screening)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes="Retrieved via Europe PMC REST API (structured abstract; full text is subscription-required, DOI 10.1080/02713683.2017.1377258, Current Eye Research). Strong material-comparison data for the mechanical/biological benchmarking domains; useful direct three-way polymer comparison, unusual among Tier 1 records so far.",
    ),
    "PUBMED_0382": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / decellularized carrier study with in vivo evaluation",
        target_layer_final="endothelium",
        biomaterial_category="decellularized biological tissue carrier (non-mammalian source)",
        specific_materials="fish-scale collagen membrane (FSCM)",
        fabrication_method="fish scales decellularized, decalcified, and curved to form a membrane carrier",
        scaffold_architecture="curved collagen membrane derived from fish scale",
        cell_type_used="corneal endothelial cells (CECs)",
        cell_source="not specified as human/animal in abstract; seeded onto FSCM for implantation into rabbit anterior chambers",
        growth_factors_or_bioactive_agents="none reported",
        optical_transparency_reported="yes",
        optical_metric_details="FSCM reported to have 'excellent transparency' (qualitative descriptor); no numeric transmittance value in abstract.",
        mechanical_testing_reported="partial",
        mechanical_metric_details="Adequate water content and biocompatibility/durability assessed; no explicit tensile/modulus values reported in abstract. TGA used to validate decalcification (thermal, not mechanical, property).",
        biological_testing_reported="yes",
        biological_metric_details="Fluorescence microscopy, SEM and TGA validated decellularization/microstructure/decalcification; cytotoxicity (LDH) and viability (WST-1) assays performed; CEC tight junctions and ZO-1 structure observed by SEM and confocal microscopy; cultivated CECs on FSCM were similar to normal CECs in vivo.",
        in_vitro_model="yes", ex_vivo_model="no", animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="not specified beyond implantation evaluation; rabbit anterior chamber host tissue reaction assessed",
        main_outcomes="Fish-scale collagen membrane (a non-mammalian, potentially lower-cost and lower-zoonotic-risk carrier source) seeded with corneal endothelial cells showed excellent transparency, adequate water content, good biocompatibility, normal-appearing CECs with ZO-1 tight junctions, and was implanted into rabbit anterior chambers to assess host tissue reaction.",
        main_limitations="Exact quantitative transparency/mechanical values not given in abstract; cell source species not specified in abstract; in vivo evaluation limited to short-term host tissue reaction rather than long-term functional/transplantation outcome.",
        translational_readiness_level="early-to-mid preclinical (in vitro plus small-animal in vivo host-reaction evaluation)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes="Retrieved via Europe PMC REST API (structured abstract; full text subscription-required, DOI 10.1021/acsbiomaterials.9b00562, ACS Biomaterials Science & Engineering). Novel non-mammalian biomaterial source (fish scale) - relevant to the manufacturing/sourcing and immunogenicity benchmarking domains as an alternative to bovine/porcine/human-donor-derived carriers.",
    ),
}

for sid, vals in EXTRACTIONS.items():
    if sid in by_id:
        by_id[sid].update(vals)
    else:
        print("WARNING missing:", sid)

with path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fieldnames)
    w.writeheader()
    w.writerows(rows)

print("Extraction template updated for:", list(EXTRACTIONS.keys()))
