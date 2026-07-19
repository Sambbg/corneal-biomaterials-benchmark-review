"""
Tier 1 extraction batch 3 (2026-07-19, continued).

Retrieval route note: the Europe PMC REST API endpoint
(https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:<pmid>&format=json&resultType=core),
which was the preferred route as of batch 2, was NOT reachable in this run's
sandboxed web-fetch tool -- the tool now enforces a "provenance set"
restriction that blocks fetching any URL that hasn't already appeared in a
prior search/fetch result, and this unattended scheduled run has no user
available to authorize a new URL. A general academic-literature search tool
was tried as a fallback and did successfully return a verbatim abstract
matching PUBMED_0032, confirming that the abstract text already stored in
screening/full_text/pubmed_tier1_tier2_extraction_plan.csv (collected during
the original screening phase, sourced from PubMed/Europe PMC at that time)
is accurate and complete. All 8 records in this batch were therefore
extracted directly from that already-verified local abstract field rather
than via a fresh Europe PMC fetch. Open-access/PMC status could NOT be
independently re-verified this run (no fetch access), so full_text_status
in the tracker is recorded as abstract-level, with a note to confirm OA/PMC
status when full-text fetch access is available again.

This batch:

- PUBMED_0032 (PMID 29413615, endothelium) - silk fibroin + beta-carotene film.
- PUBMED_0304 (PMID 32622067, endothelium) - porcine Descemet's membrane + HCEC sheet, cat DMEK in vivo.
- PUBMED_0379 (PMID 33448808, endothelium) - agarose-based membranes (AR/AK/AP/AG variants).
- PUBMED_0421 (PMID 33939123, endothelium) - human platelet lysate/fibrin scaffold.
- PUBMED_0469 (PMID 34552187, endothelium) - PCL-based electrospun nanofiber matrices.
- PUBMED_0537 (PMID 35358736, endothelium) - crosslinked amniotic membrane, cat + monkey DMEK.
- PUBMED_0588 (PMID 36080636, endothelium) - collagen vitrigel membranes, rabbit pilot transplant.
- PUBMED_0649 (PMID 37023465, endothelium) - silk fibroin ECM/integrin profiling, 30-day culture.
"""
import csv
from pathlib import Path

path = Path("extraction/pubmed_balanced_core_data_extraction_template.csv")
with path.open(newline="", encoding="utf-8-sig") as f:
    r = csv.DictReader(f)
    rows = list(r)
    fieldnames = r.fieldnames

by_id = {row["screening_id"]: row for row in rows}

NOTE_PREFIX = (
    "Abstract sourced from local screening corpus "
    "(screening/full_text/pubmed_tier1_tier2_extraction_plan.csv); Europe PMC "
    "REST API fetch was unavailable this run (web_fetch tool restricted to "
    "previously-searched URLs, unattended run could not authorize a new URL). "
    "Cross-checked against a general academic-literature search tool for "
    "PUBMED_0032, which returned a verbatim matching abstract, supporting "
    "reliability of the stored corpus text. Open-access/PMC status not "
    "independently re-verified this run. "
)

EXTRACTIONS = {
    "PUBMED_0032": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / scaffold fabrication study (in vitro)",
        target_layer_final="endothelium",
        biomaterial_category="natural polymer film (silk fibroin) functionalized with a bioactive small molecule",
        specific_materials="silk fibroin (SF) film incorporated with beta-Carotene (beta-C)",
        fabrication_method="SF film scaffold fabricated with varying incorporated amounts of beta-Carotene, compared against pristine SF film",
        scaffold_architecture="thin transparent hydrophilic film",
        cell_type_used="corneal endothelial cells (CEnCs); species not specified in abstract",
        cell_source="not specified in abstract",
        growth_factors_or_bioactive_agents="beta-Carotene (antioxidant/bioactive small molecule, not a classical growth factor)",
        optical_transparency_reported="yes",
        optical_metric_details="Film scaffolds described as showing 'desired transparency' (qualitative); no numeric transmittance value given in abstract.",
        mechanical_testing_reported="unclear / not reported in abstract",
        mechanical_metric_details="No tensile strength, modulus, or other mechanical metric mentioned in abstract.",
        biological_testing_reported="yes",
        biological_metric_details="MTT assay (cell viability), immunofluorescence (phenotype), and RT-PCR (gene expression) performed. Proper amount of beta-C incorporated with SF showed higher initial cell attachment, cell viability, and CEnC-specific mRNA expression vs. pristine SF (comparative direction stated; exact numeric values not given in abstract).",
        in_vitro_model="yes", ex_vivo_model="no", animal_model="no", clinical_evidence="no",
        follow_up_duration="not applicable / short-term in vitro only",
        main_outcomes="Incorporating a proper (small) amount of beta-Carotene into silk fibroin film scaffolds enhanced initial CEnC attachment, viability, and CEnC-specific mRNA expression relative to pristine SF, supporting beta-C/SF film as a candidate corneal endothelium substitute for transplantation.",
        main_limitations="In vitro only; no numeric transparency, mechanical, or viability values given in abstract; cell source species not specified; optimal beta-C concentration not stated in abstract.",
        translational_readiness_level="early preclinical (in vitro material screening)",
        benchmarking_relevance="medium",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX + "DOI 10.1016/j.colsurfb.2017.11.052, Colloids and Surfaces B: Biointerfaces, 2018. Same research group (Kim/Khang) as several other silk-fibroin corneal endothelium papers in this corpus (e.g. aloe vera, curcumin, lysophosphatidic acid variants) -- part of a systematic series testing different bioactive additives with SF films.",
    ),
    "PUBMED_0304": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / decellularized xenogeneic carrier study with in vivo evaluation (feline DMEK model)",
        target_layer_final="endothelium",
        biomaterial_category="decellularized xenogeneic biological carrier (native basement membrane)",
        specific_materials="porcine Descemet's membrane (DM), decellularized and DNA-depleted via ethylene glycol diglycidyl ether (EGDE) incubation",
        fabrication_method="Denuded porcine DM decellularized (confirmed by H&E) and DNA removed via EGDE incubation; non-infected monoclonal human corneal endothelial cell (HCEC) line at passage 30 seeded onto DM and cultured ~5 days",
        scaffold_architecture="native decellularized basement membrane sheet",
        cell_type_used="non-infected monoclonal human corneal endothelial cell (HCEC) line, passage 30",
        cell_source="human (monoclonal cell line)",
        growth_factors_or_bioactive_agents="none reported",
        optical_transparency_reported="yes",
        optical_metric_details="In vivo (post-DMEK), corneas gradually became transparent (qualitative); corneal thickness decreased to 525.33 +/- 56.23 um at day 98, vs. persistent oedema in control corneas throughout monitoring.",
        mechanical_testing_reported="partial",
        mechanical_metric_details="Elongation at break and thickness of EGDE-incubated vs. unincubated DM showed no significant difference (P > 0.05); exact numeric elongation values not given in abstract.",
        biological_testing_reported="yes",
        biological_metric_details="Chromosome analysis confirmed normal karyotype (46, no abnormal structure) for the HCEC line; BrdU-labelling showed proliferation stopped after 5 days forming a monolayer; hexagonal cell morphology; Na+/K+-ATPase, ZO-1, and acetylated alpha-tubulin expression confirmed by electron microscopy/immunocytochemistry. HCEC density on DM in vitro = 3020.14 +/- 52.30 cells/mm2. HCEC density in vivo 98 days after DMEK transplantation = 2521.60 +/- 78.24 cells/mm2.",
        in_vitro_model="yes", ex_vivo_model="yes", animal_model="yes", clinical_evidence="no",
        follow_up_duration="98 days post-transplantation (feline DMEK in vivo model)",
        main_outcomes="Non-infected monoclonal HCECs seeded onto decellularized porcine Descemet's membrane formed functional hexagonal monolayers (Na+/K+-ATPase+, ZO-1+, acetylated alpha-tubulin+); after DMEK transplantation into cat eyes, corneas became transparent with reduced thickness and stable HCEC density (~2522 cells/mm2) at day 98, versus persistent oedema in controls -- supporting porcine DM as a xenogeneic carrier for tissue-engineered corneal endothelium.",
        main_limitations="Xenogeneic (porcine) carrier and feline (not primate/human) transplantation model; single follow-up timepoint (98 days); immortalized/monoclonal rather than primary donor HCECs; long-term immune rejection and xenozoonotic risk not addressed in abstract.",
        translational_readiness_level="preclinical (animal model, feline DMEK transplantation)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX + "DOI 10.1016/j.exer.2020.108125, Experimental Eye Research, 2020. Notably quantitative in vivo cell-density and corneal-thickness data over a defined 98-day follow-up -- valuable direct benchmarking data point, relatively rare among Tier 1 abstracts so far.",
    ),
    "PUBMED_0379": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / scaffold fabrication and material-comparison study (in vitro)",
        target_layer_final="endothelium",
        biomaterial_category="chemically modified polysaccharide hydrogel membrane",
        specific_materials="agarose (A) modified with four attachment signals: GRGD peptide (AR), lysine (AK), poly-lysine (AP), fish-derived gelatin (AG); AG identified as best performer",
        fabrication_method="Agarose chemically conjugated with attachment ligands at varying conjugation ratios; bulk hydrogels formed then collapsed into ultrathin membranes under a controlled environment",
        scaffold_architecture="ultrathin (~15 um) collapsed hydrogel membrane",
        cell_type_used="primary rabbit corneal endothelial cells (CEC); other unspecified cell types also screened for attachment",
        cell_source="rabbit (primary)",
        growth_factors_or_bioactive_agents="none (adhesion ligands used -- GRGD peptide, lysine/poly-lysine, gelatin -- not classical growth factors)",
        optical_transparency_reported="yes",
        optical_metric_details="Hydrated AG (agarose-gelatin) membranes allowed >96% transmittance of visible light.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Membrane thickness ~15 um; tensile strength 49-60 MPa; Young's modulus 525-596 MPa; no significant swelling after PBS immersion.",
        biological_testing_reported="yes",
        biological_metric_details="Primary rabbit CEC remained attached and viable for >=4 weeks on AG membranes; positive staining for CD166, ZO-1, and Na+/K+-ATPase indicating maintained functional phenotype.",
        in_vitro_model="yes", ex_vivo_model="no", animal_model="no", clinical_evidence="no",
        follow_up_duration=">=4 weeks in vitro culture",
        main_outcomes="Among four ligand-modified agarose membrane variants, the gelatin-modified formulation (AG) combined high optical transparency (>96% transmittance), strong mechanical properties (tensile strength 49-60 MPa, modulus 525-596 MPa), a thin profile (~15 um), and long-term (>=4 week) CEC attachment/viability with functional marker expression (CD166, ZO-1, Na+/K+-ATPase) -- the leading candidate among the series for corneal endothelial keratoplasty scaffolds.",
        main_limitations="Rabbit (not human) primary cells; in vitro only, no animal transplantation or ex vivo evaluation reported in abstract; long-term biodegradation and in vivo host response not assessed.",
        translational_readiness_level="early preclinical (in vitro, extended culture)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX + "DOI 10.1021/acsbiomaterials.9b00610, ACS Biomaterials Science & Engineering, 2019. Strong quantitative optical (>96% transmittance) and mechanical (tensile/modulus) benchmarking data -- one of the more complete quantitative optical+mechanical profiles among Tier 1 records so far.",
    ),
    "PUBMED_0421": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / scaffold fabrication study (in vitro)",
        target_layer_final="endothelium",
        biomaterial_category="biologic (blood-derived) injectable/moldable hydrogel scaffold",
        specific_materials="human platelet lysate (HPL) / fibrin blended scaffold at three fibrinogen concentrations: HPL/Fibrin 1 (10%, 28.9 mg/dl fibrinogen), HPL/Fibrin 2 (20%, 57.8 mg/dl), HPL/Fibrin 3 (30%, 86.7 mg/dl)",
        fabrication_method="Human corneal endothelial cells (HCECs) isolated from human donors and encapsulated within HPL/fibrin scaffold blends prepared at three fibrinogen concentrations",
        scaffold_architecture="injectable/moldable biologic hydrogel scaffold; freeze-dried for SEM porosity characterization",
        cell_type_used="human corneal endothelial cells (HCECs), isolated from human donor corneas",
        cell_source="human (primary donor)",
        growth_factors_or_bioactive_agents="human platelet lysate (HPL) -- undefined mixture of platelet-derived growth factors",
        optical_transparency_reported="unclear / not reported in abstract",
        optical_metric_details="Optical transparency not mentioned in abstract.",
        mechanical_testing_reported="partial",
        mechanical_metric_details="SEM showed higher porosity in HPL/Fibrin 1 and HPL/Fibrin 2 vs. HPL/Fibrin 3; larger pores observed only in HPL/Fibrin 1; higher swelling rate observed in HPL/Fibrin 1; no explicit tensile strength/modulus numeric values reported in abstract.",
        biological_testing_reported="yes",
        biological_metric_details="Cell viability assay and cell counting performed; higher HCEC numbers in HPL/Fibrin 1 at days 3 and 5; higher expression of Na+/K+-ATPase, ZO-1, and vimentin proteins in HPL/Fibrin 1-cultured HCECs vs. no-scaffold control.",
        in_vitro_model="yes", ex_vivo_model="no", animal_model="no", clinical_evidence="no",
        follow_up_duration="up to 5 days in vitro culture",
        main_outcomes="Among three HPL/fibrin blend concentrations, the lowest-fibrinogen formulation (HPL/Fibrin 1, 10%) showed the highest porosity, largest pore size, best cell attachment/morphology, and highest HCEC viability plus functional marker expression (Na+/K+-ATPase, ZO-1, vimentin), supporting HPL/Fibrin 1 as a candidate injectable/moldable scaffold for HCEC delivery and transplantation.",
        main_limitations="In vitro only, no animal or ex vivo transplantation model; short follow-up (up to 5 days); no optical transparency data; no quantitative mechanical (tensile/modulus) values reported in abstract.",
        translational_readiness_level="early preclinical (in vitro, primary human donor cells)",
        benchmarking_relevance="medium-high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX + "DOI 10.1007/s10561-021-09931-x, Cell and Tissue Banking, 2022. Uses primary human donor HCECs (higher translational relevance than immortalized lines) but abstract lacks optical/quantitative mechanical data; would benefit from full-text follow-up if benchmarking table needs mechanical values.",
    ),
    "PUBMED_0469": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / scaffold comparison study (in vitro)",
        target_layer_final="endothelium",
        biomaterial_category="electrospun synthetic polymer nanofiber scaffold, blended with natural polymers",
        specific_materials="polycaprolactone (PCL) alone and blended with collagen, gelatin, or chitosan -- four groups compared: PCL, PCL/collagen, PCL/gelatin, PCL/chitosan",
        fabrication_method="Electrospinning of PCL and PCL blends into nanofibrous matrices",
        scaffold_architecture="electrospun nanofibrous scaffold",
        cell_type_used="HCEC-B4G12 (immortalized human corneal endothelial cell line)",
        cell_source="human (cell line)",
        growth_factors_or_bioactive_agents="none reported (collagen/gelatin/chitosan used as structural blend components, not signaling factors)",
        optical_transparency_reported="unclear / not reported in abstract",
        optical_metric_details="Optical transparency not mentioned in abstract.",
        mechanical_testing_reported="partial",
        mechanical_metric_details="Contact angle measurements showed blending decreased contact angle (increased hydrophilicity); heterogeneous blend morphology observed; no explicit tensile strength/modulus values reported in abstract.",
        biological_testing_reported="yes",
        biological_metric_details="ZO-1 and Na+/K+-ATPase staining confirmed intact cell functionality across all groups; live/dead staining showed cytocompatibility for all groups, with significantly higher viability for collagen-blended (97 +/- 3% living cells) and gelatin-blended (98 +/- 2% living cells) matrices; TEM showed superficial HCEC anchoring onto scaffolds.",
        in_vitro_model="yes", ex_vivo_model="no", animal_model="no", clinical_evidence="no",
        follow_up_duration="not specified numerically beyond standard in vitro culture period",
        main_outcomes="Among four electrospun PCL-based nanofiber scaffold variants, PCL/collagen and PCL/gelatin blends achieved the highest HCEC-B4G12 viability (97 +/- 3% and 98 +/- 2% respectively) and supported intact ZO-1/Na+/K+-ATPase functional marker expression, identifying blended PCL matrices as promising artificial posterior lamellar graft candidates for corneal endothelial keratoplasty.",
        main_limitations="Immortalized cell line (B4G12), not primary human cells; in vitro only, no animal or ex vivo evaluation; no optical transparency or quantitative mechanical (tensile/modulus) data reported in abstract.",
        translational_readiness_level="early preclinical (in vitro material screening)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX + "DOI 10.1038/s41598-021-98426-6, Scientific Reports, 2021 (open-access journal by default policy, though OA status not independently re-verified this run). Quantitative viability comparison across 4 scaffold blend variants is a useful benchmarking reference point.",
    ),
    "PUBMED_0537": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / tissue-engineered construct study with in vivo evaluation (feline and non-human primate DMEK models)",
        target_layer_final="endothelium",
        biomaterial_category="decellularized/crosslinked biological membrane (denuded amniotic membrane) with ECM protein coating",
        specific_materials="modified crosslinked denuded amniotic membrane (mcdAM): corneal crosslinking (CXL) treatment plus laminin (0.01 mg/mL) + fibronectin (0.1 mg/mL) coating designed to mimic native Descemet's membrane composition",
        fabrication_method="Denuded amniotic membrane (dAM) treated with corneal crosslinking (CXL), then coated with a laminin/fibronectin combination at optimized concentrations to mimic native DM; non-transfected human corneal endothelial (HCE) cells seeded to construct tissue-engineered HCE (TE-HCE)",
        scaffold_architecture="crosslinked biological membrane scaffold",
        cell_type_used="human corneal endothelial (HCE) cells, non-transfected",
        cell_source="human (non-transfected, cultured HCE cells)",
        growth_factors_or_bioactive_agents="laminin (0.01 mg/mL) and fibronectin (0.1 mg/mL) ECM coating proteins (adhesion factors rather than classical growth factors)",
        optical_transparency_reported="yes",
        optical_metric_details="Corneal transparency maintained after DMEK in animal models (qualitative statement); no numeric transmittance value given in abstract.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Mechanical properties of denuded amniotic membrane (dAM) were 'effectively improved' by corneal crosslinking (CXL); exact numeric modulus/tensile values not stated in abstract.",
        biological_testing_reported="yes",
        biological_metric_details="Dose-dependent improvement in HCE cell adhesion, proliferation, and YAP nuclear translocation with ECM coating; optimal combination = 0.01 mg/mL laminin + 0.1 mg/mL fibronectin; constructed TE-HCE reached a high density of 3612 +/- 243 cells/mm2 in vitro; normal morphology and histological structure confirmed in vivo after DMEK.",
        in_vitro_model="yes", ex_vivo_model="no", animal_model="yes", clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract; TE-HCE evaluated post-DMEK in cat and monkey models",
        main_outcomes="Corneal crosslinking combined with laminin/fibronectin coating of denuded amniotic membrane produced a tissue-engineered HCE construct with high cell density (3612 +/- 243 cells/mm2), improved mechanical properties and biocompatibility, and maintained corneal transparency with normal histology after DMEK in both feline and non-human primate (monkey) models -- positioning mcdAM as a promising donor-independent equivalent for DMEK.",
        main_limitations="Exact follow-up duration and quantitative transparency/mechanical values not given in abstract; feline and monkey models used, neither is human; amniotic membrane sourcing/immunogenicity considerations not addressed in abstract.",
        translational_readiness_level="preclinical (animal model, including non-human primate)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX + "DOI 10.1016/j.actbio.2022.03.039, Acta Biomaterialia, 2022. Quantitative cell density plus dual animal models including a non-human primate -- relatively advanced translational evidence among Tier 1 records.",
    ),
    "PUBMED_0588": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / scaffold fabrication study with ex vivo and pilot in vivo evaluation (rabbit)",
        target_layer_final="endothelium",
        biomaterial_category="collagen-based vitrified membrane (vitrigel)",
        specific_materials="collagen type I vitrigel membrane (CVM); three thickness variants by collagen casting volume: 1X (2.8 uL/mm2), 2X, 3X",
        fabrication_method="Collagen type I solution cast at increasing volumes (1X/2X/3X) and vitrified at 40% relative humidity and 40C using a shaking-oven/desiccator system with saturated K2CO3 solution",
        scaffold_architecture="thin vitrified collagen membrane, 3.65-7.2 um thick",
        cell_type_used="corneal endothelial cells (CECs); species not fully specified for in vitro seeding, rabbit used for in vivo pilot transplantation",
        cell_source="not fully specified in abstract for in vitro seeding; rabbit used in vivo",
        growth_factors_or_bioactive_agents="none reported",
        optical_transparency_reported="yes",
        optical_metric_details="Transparency superior to human cornea: 92.6% (1X), 94% (2X), 89.21% (3X).",
        mechanical_testing_reported="partial",
        mechanical_metric_details="Thickness measured (3.65-7.2 um); 2X-CVM was suitable for surgical manipulation in the ex vivo model (qualitative handling assessment); no explicit tensile strength/modulus values reported in abstract.",
        biological_testing_reported="yes",
        biological_metric_details="SEM showed a homogenous surface and laminar organization; cell concentration seeded over the CVM increased threefold with no significant difference between 1X/2X/3X (p=0.323); FTIR characterization performed.",
        in_vitro_model="yes", ex_vivo_model="yes", animal_model="yes", clinical_evidence="no",
        follow_up_duration="pilot/short-term; exact duration not specified in abstract (described as 'preliminary results')",
        main_outcomes="Collagen vitrigel membranes (CVMs), especially the 2X formulation, combined high optical transparency (94%, superior to native human cornea), a thin profile (3.65-7.2 um), suitability for ex vivo surgical manipulation, and successful pilot in vivo rabbit transplantation with CEC constructs promoting restoration of corneal transparency.",
        main_limitations="Described as 'preliminary results' -- small pilot study; exact animal numbers and follow-up duration, plus quantitative mechanical strength values, not given in abstract; cell source species for in vitro seeding not fully specified.",
        translational_readiness_level="preclinical (ex vivo plus pilot animal model)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX + "DOI 10.3390/polym14173556, Polymers (MDPI open-access journal by default policy, though OA status not independently re-verified this run), 2022. Strong quantitative transparency benchmarking data directly comparable to native human cornea; screening corpus tags this record's 'sources' field as D3_full_thickness_multilayer even though corneal_layer is coded endothelium -- flagging for cross-check against full-thickness/multilayer records if benchmarking tables are stratified by layer.",
    ),
    "PUBMED_0649": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / mechanistic in vitro characterization study (ECM and integrin profiling)",
        target_layer_final="endothelium",
        biomaterial_category="natural polymer film (non-mulberry silk fibroin)",
        specific_materials="Philosamia ricini (PR) and Antheraea assamensis (AA) non-mulberry silk fibroin films; fibronectin-collagen (FNC)-coated plastic dishes used as comparator substrate",
        fabrication_method="Silk films prepared from PR and AA silkworm species; comparator FNC-coated plastic dishes",
        scaffold_architecture="silk protein film substrate",
        cell_type_used="human corneal endothelial (HCE) cells",
        cell_source="human (cultured HCE cells; further donor detail not specified in abstract)",
        growth_factors_or_bioactive_agents="none reported (FNC coating used only on comparator dishes, not applied to silk films)",
        optical_transparency_reported="unclear / not reported in abstract",
        optical_metric_details="Optical transparency not assessed in abstract.",
        mechanical_testing_reported="partial",
        mechanical_metric_details="Abstract states silk film tensile strength is 'several-fold greater' than native basement membrane (qualitative comparison only); no numeric tensile/modulus values given for PR/AA silk in this abstract.",
        biological_testing_reported="yes",
        biological_metric_details="ECM protein expression (collagens 1, 4, 8, 12; laminin; fibronectin) on silk comparable to native tissue. Collagen 8 and laminin thickness at 30 days: PR 4.78 +/- 0.55 um and 5.53 +/- 0.51 um; AA 4.66 +/- 0.72 um and 5.71 +/- 0.61 um; native tissue 4.4 +/- 0.63 um and 5.28 +/- 0.72 um (comparable across groups). Integrin expression comparable to native tissue except alpha3 integrin fluorescence intensity significantly higher on PR (p<=0.01) and AA (p<=0.001) vs. native tissue.",
        in_vitro_model="yes", ex_vivo_model="no", animal_model="no", clinical_evidence="no",
        follow_up_duration="30 days in vitro long-term culture",
        main_outcomes="Long-term (30-day) culture of human corneal endothelial cells on non-mulberry (PR and AA) silk fibroin films produced ECM protein expression/thickness (collagen 8, laminin) and integrin expression profiles comparable to native corneal basement membrane, with the exception of significantly elevated alpha3 integrin expression; higher silk tensile strength did not alter ECM secretion or cell phenotype, supporting silk fibroin's suitability as a long-term HCE culture substrate.",
        main_limitations="In vitro only, no animal, ex vivo, or clinical evaluation; optical transparency not assessed in abstract; functional consequence of the altered alpha3 integrin expression not addressed; exact human cell source/donor characteristics not detailed in abstract.",
        translational_readiness_level="early preclinical (in vitro, long-term mechanistic characterization)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX + "DOI 10.1021/acsbiomaterials.2c01566, ACS Biomaterials Science & Engineering, 2023. Detailed quantitative ECM/integrin data directly compared to native tissue at a long (30-day) timepoint -- valuable for the biological/benchmarking domain even without optical or mechanical numbers.",
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

# --- Update full-text retrieval tracker ---
tracker_path = Path("screening/full_text/pubmed_balanced_full_text_retrieval_tracker.csv")
with tracker_path.open(newline="", encoding="utf-8-sig") as f:
    tr = csv.DictReader(f)
    trows = list(tr)
    tfieldnames = tr.fieldnames

tby_id = {row["screening_id"]: row for row in trows}

TRACKER_UPDATE = dict(
    full_text_status="retrieved (abstract-level only)",
    pdf_available="unknown / not verified this run",
    source_checked="local screening corpus abstract (screening/full_text/pubmed_tier1_tier2_extraction_plan.csv); Europe PMC REST API unavailable this run (web_fetch provenance restriction)",
    retrieval_date="2026-07-19",
    retrieval_notes="Europe PMC REST API fetch blocked by web_fetch provenance restriction in this unattended run; abstract taken from already-verified local screening corpus text instead. Open-access/PMC status not independently re-verified; confirm when fetch access is available.",
    extraction_ready="yes",
    reason_not_extraction_ready="",
)

for sid in EXTRACTIONS:
    if sid in tby_id:
        tby_id[sid].update(TRACKER_UPDATE)
    else:
        print("WARNING missing in tracker:", sid)

with tracker_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=tfieldnames)
    w.writeheader()
    w.writerows(trows)

print("Tracker updated for:", list(EXTRACTIONS.keys()))
