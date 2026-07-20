"""
Tier 1 extraction batch 13 (2026-07-20, scheduled run continuation).

Retrieval route note: as in batches 3-12, a direct web_fetch to the Europe PMC
REST API (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:<pmid>&format=json&resultType=core)
was not attempted this run -- every prior run from batch 3 through batch 12
has confirmed this fails with "URL not in provenance set" (the sandboxed
web_fetch tool only allows fetching URLs that already appeared in a user
message, a prior web_fetch result, or a WebSearch result; this unattended
scheduled run has no user available to authorize a new URL). Per the task
instructions, this structural block was not re-attempted this run.

Extraction for this batch was built from the complete, untruncated abstract
text already stored locally in
screening/full_text/pubmed_tier1_tier2_extraction_plan.csv (verified
PubMed/journal abstracts captured during the original screening pass), with
open-access status assessed from known journal/publisher policy: Translational
Vision Science & Technology (ARVO) and Journal of Nanobiotechnology
(BMC-series/Springer Nature) are fully open access (gold OA); Scientific
Reports (Nature Portfolio) is fully open access (gold OA); Archives of
Medical Science (Termedia) is an open-access journal; International Journal
of Bioprinting is a fully open-access journal (Whioce/AccScience). Regenerative
Medicine (Taylor & Francis), Acta Biomaterialia (Elsevier), and Colloids and
Surfaces B: Biointerfaces (Elsevier) are hybrid/subscription titles --
open-access status of these specific articles not individually confirmed
this run. This is noted per-record in extraction_notes.

PUBMED_0672 is a narrative review article (not a primary experimental study)
on 3D bioprinting for LSCD -- it is extracted as a review/synthesis record
rather than force-fit into the primary-study extraction template, per the
"say so explicitly rather than guessing" instruction.

This batch (8 records):
- PUBMED_0672 (PMID 37273996) - narrative review of 3D bioprinting as a therapeutic strategy for LSCD.
- PUBMED_0702 (PMID 37594449) - Noggin-coated PCL/gelatin electrospun corneal bandage, in vitro wound-healing scratch assay.
- PUBMED_0799 (PMID 39050175) - RCT of cultured autologous oral mucosal epithelial cell sheet (CAOMECS) + amniotic membrane vs. amniotic membrane alone, human clinical study.
- PUBMED_0826 (PMID 39375390) - extrusion bioprinting of LESCs onto fibrin substrate vs. manual seeding, in vitro reproducibility study.
- PUBMED_0843 (PMID 39558722) - PRGF-enriched collagen/silk fibroin scaffold for Wharton's jelly MSC differentiation into corneal epithelial cells, in vitro.
- PUBMED_0867 (PMID 39800095) - Y-27632 + dual-media + spheroid auto-bioprinting of rabbit LESC sheets onto curved collagen membrane, in vitro + in vivo rabbit LSCD model.
- PUBMED_0908 (PMID 40168696) - decellularized human amniotic membrane hydrogel (dAM-gel) for LSC proliferation, in vitro.
- PUBMED_0919 (PMID 40296037) - self-healing oxidized guar gum/carboxymethyl chitosan hydrogel loaded with MSC exosomes, in vitro + in vivo rabbit corneal defect model.
"""
import csv
from pathlib import Path

path = Path("extraction/pubmed_balanced_core_data_extraction_template.csv")
with path.open(newline="", encoding="utf-8-sig") as f:
    r = csv.DictReader(f)
    rows = list(r)
    fieldnames = r.fieldnames

by_id = {row["screening_id"]: row for row in rows}

NOTE_PREFIX_LOCAL = (
    "Abstract sourced from local screening corpus "
    "(screening/full_text/pubmed_tier1_tier2_extraction_plan.csv), captured during "
    "original PubMed screening. Europe PMC REST API fetch was unavailable this run "
    "(web_fetch tool restricted to previously provenance-approved URLs; unattended "
    "run could not authorize the new URL); this is the same structural block "
    "documented in batches 3-12 and was not re-attempted this run. "
)

EXTRACTIONS = {
    "PUBMED_0672": dict(
        extraction_status="completed",
        study_type="narrative review article (not a primary experimental study) synthesizing 3D bioprinting approaches for LSCD treatment",
        target_layer_final="epithelium_limbus",
        biomaterial_category="review scope: multiple bioprintable biomaterials/bio-inks surveyed across the cited primary literature (not a single scaffold system studied by this paper itself)",
        specific_materials="not applicable -- this is a review; no single material system was fabricated or tested by the authors of this record",
        fabrication_method="not applicable -- review discusses 3D bioprinting techniques (e.g., extrusion, laser-assisted, DLP) reported across the field rather than reporting an original fabrication protocol",
        scaffold_architecture="not applicable -- review discusses single- and multilayer corneal limbus equivalent constructs reported in prior literature",
        cell_type_used="not applicable -- review; discusses limbal epithelial stem cells (LESCs) generally as used across the cited literature",
        cell_source="not applicable -- review",
        growth_factors_or_bioactive_agents="not applicable -- review",
        optical_transparency_reported="unclear / not reported in abstract",
        optical_metric_details="Review discusses 'ocular optical function restoration' as an unresolved challenge for the field generally; no original data or specific numeric values reported by this record.",
        mechanical_testing_reported="unclear / not reported in abstract",
        mechanical_metric_details="No original mechanical testing performed or numerically reported; review discusses fabrication of cell-laden scaffolds generally.",
        biological_testing_reported="unclear / not reported in abstract",
        biological_metric_details="No original biological data; review summarizes progress, applications, and limitations of prior LESC-deficiency treatment approaches and 3D-bioprinted corneal limbus alternatives.",
        in_vitro_model="not applicable (review)",
        ex_vivo_model="not applicable (review)",
        animal_model="not applicable (review)",
        clinical_evidence="not applicable (review); notes that cultured LESC therapy was first clinically described in 1997 and that donor cornea shortage (demand exceeds supply by >70:1) motivates the need for limbus alternatives",
        follow_up_duration="not applicable (review)",
        main_outcomes="This narrative review surveys 3D bioprinting as a prospective strategy to address limbal stem cell deficiency (LSCD), motivated by severe donor-cornea shortage (fewer than 1 donor per 70 cases needed). It summarizes progress and limitations of current LESC-deficiency treatments, highlights 3D bioprinting's potential for personalized corneal implants and single-/multilayer corneal limbus equivalents, and outlines prospects and technical challenges (original geometry reconstruction, epithelial regeneration, optical function restoration) for future in vivo and in vitro research in this space.",
        main_limitations="This is a review, not a primary study -- it reports no original experimental data, materials, or quantitative outcomes; conclusions reflect the authors' synthesis and interpretation of the cited literature rather than new findings.",
        translational_readiness_level="not applicable (review article; synthesizes field-wide translational status rather than reporting a single readiness level)",
        benchmarking_relevance="medium (useful as background/context and for identifying candidate primary studies, but contributes no extractable quantitative benchmarking data itself)",
        include_in_final_review="yes (as background/context reference, not as a primary-data benchmarking entry)",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "International Journal of Bioprinting, DOI 10.18063/ijb.710, 2023 -- fully open-access journal (Whioce/AccScience Publishing); full text freely available. This record is a narrative review, not a primary experimental study; extracted as a scope/synthesis record per instructions rather than force-fitting review content into primary-study data fields. Flagging for review-team awareness that this record may be more appropriately used as a background citation than as a benchmarking-table entry.",
    ),
    "PUBMED_0702": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / drug-eluting electrospun scaffold study (in vitro only)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="synthetic/natural polymer blend electrospun nanofibrous scaffold coated with a bioactive protein (BMP antagonist)",
        specific_materials="electrospun polycaprolactone (PCL)/gelatin blend nanofibers at varying blend ratios, surface-coated with different concentrations of Noggin protein",
        fabrication_method="electrospun nanofibrous scaffolds fabricated at different PCL:gelatin blend ratios; electrospinning parameters optimized to produce uniform nanofibers; scaffolds coated with varying concentrations of Noggin protein; morphology, mechanical properties, degradation, and surface chemistry characterized; biocompatibility assessed with corneal epithelial cells via viability, proliferation, and immunostaining assays; in vitro wound healing assessed by scratch-assay wound closure rate in the presence of the Noggin-coated scaffold",
        scaffold_architecture="electrospun nanofibrous mat (PCL/gelatin blend) functioning as a corneal bandage, surface-coated with Noggin protein for sustained topical drug delivery",
        cell_type_used="corneal epithelial cells (species not specified in the retrieved abstract)",
        cell_source="not specified in the retrieved abstract",
        growth_factors_or_bioactive_agents="Noggin protein (a BMP antagonist), coated onto the scaffold surface at varying concentrations for sustained local delivery",
        optical_transparency_reported="no / not reported in abstract",
        optical_metric_details="Not reported; characterization focused on morphology, mechanical properties, degradation, and surface chemistry rather than optical transparency.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Mechanical properties of the optimized Noggin-coated PCL/gelatin scaffold were reported as better than or similar to commercially available contact lenses used for corneal wound healing; no specific numeric modulus/tensile values are given in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="Corneal epithelial cells showed higher proliferation and higher wound-closure (scratch assay) rate in the presence of the Noggin-coated scaffold compared to controls; biocompatibility confirmed via cell viability, proliferation, and immunostaining assays.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract (short-term in vitro scratch-assay wound closure)",
        main_outcomes="A Noggin-coated electrospun PCL/gelatin nanofibrous scaffold was successfully fabricated with mechanical properties comparable to or better than commercial therapeutic contact lenses used for corneal wound healing; the Noggin coating increased corneal epithelial cell proliferation and accelerated in vitro scratch-wound closure, supporting the scaffold as a tunable drug-eluting corneal bandage platform for treating indolent/nonhealing corneal ulcers.",
        main_limitations="Purely in vitro (scratch assay) evaluation with no ex vivo or in vivo/animal wound-healing data reported in this abstract; no numeric mechanical or optical transmittance values given; cell source/species not specified; no clinical evidence.",
        translational_readiness_level="early preclinical (in vitro only)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Translational Vision Science & Technology (ARVO), DOI 10.1167/tvst.12.8.15, 2023 -- ARVO's Translational Vision Science & Technology is a fully open-access (gold OA) journal; full text freely available; full-text fetch not attempted this run, abstract-level extraction used. Notable as a drug-eluting (Noggin/BMP-antagonist) corneal bandage concept, explicitly benchmarked against commercial contact-lens mechanical properties -- useful comparator for the review's bioactive-coating and mechanical-property benchmarking entries.",
    ),
    "PUBMED_0799": dict(
        extraction_status="completed",
        study_type="clinical/first-in-human study (randomized comparative clinical trial)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="carrier-free cultured autologous oral mucosal epithelial cell sheet (CAOMECS) combined with amniotic membrane (AM) as a biologic transplant substrate",
        specific_materials="cultured autologous oral mucosal epithelial cell sheet (CAOMECS); human amniotic membrane (AM) as substrate/comparator",
        fabrication_method="patients with LSCD randomized to two groups: Group A received CAOMECS combined with AM transplantation; Group B received AM transplantation alone; clinical outcomes assessed via slit-lamp examination and standard ophthalmic clinical measures over a postoperative follow-up period",
        scaffold_architecture="cultured epithelial cell sheet layered onto amniotic membrane substrate for ocular surface transplantation",
        cell_type_used="autologous oral mucosal epithelial cells",
        cell_source="human, autologous (patient's own oral mucosa)",
        growth_factors_or_bioactive_agents="not specified in the retrieved abstract beyond standard cell-sheet culture protocol",
        optical_transparency_reported="yes",
        optical_metric_details="Corneal transparency was assessed clinically as an outcome measure; Group A (CAOMECS + AM) showed obvious advantages in improving corneal transparency compared to Group B (AM alone), though no specific numeric transmittance/haze grading scale value is given in the retrieved abstract.",
        mechanical_testing_reported="no / not applicable in abstract",
        mechanical_metric_details="Not applicable; this is a clinical study with no bench mechanical testing reported.",
        biological_testing_reported="yes",
        biological_metric_details="Normal corneal epithelialization rate was higher in Group A (73.33%) than Group B (35.48%); average healing time was shorter in Group A (3.45 +/- 2.12 weeks vs. 4.64 +/- 1.63 weeks in Group B); symblepharon improved in both groups in the first 3 months, with recurrence in part of Group B after 6 months; corneal neovascularization (CNV) score at 6 months was better in Group A (1.47 +/- 0.64) than Group B (1.94 +/- 0.85); both groups showed some improvement in ocular surface inflammation.",
        in_vitro_model="no",
        ex_vivo_model="no",
        animal_model="no",
        clinical_evidence="yes",
        follow_up_duration="6 months (with interim assessments at 3 months)",
        main_outcomes="In a randomized clinical comparison for LSCD treatment, adding cultured autologous oral mucosal epithelial cell sheet (CAOMECS) transplantation to standard amniotic membrane (AM) treatment significantly outperformed AM alone: higher normal corneal epithelialization rate (73.33% vs. 35.48%), faster healing (3.45 vs. 4.64 weeks), better corneal transparency, lower corneal neovascularization at 6 months (1.47 vs. 1.94), and less symblepharon recurrence, supporting CAOMECS + AM as a safe and more effective alternative for ocular surface reconstruction in LSCD.",
        main_limitations="Best corrected visual acuity was listed as an outcome measure but its quantitative result is not reported in the retrieved abstract; sample size (number of eyes/patients per group) is not given in the abstract; single-center study details, blinding, and long-term (beyond 6-month) outcomes are not described.",
        translational_readiness_level="clinical (randomized comparative human trial)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Archives of Medical Science (AMS, Termedia), DOI 10.5114/aoms/115576, 2024 -- Archives of Medical Science is an open-access journal; full text freely available; full-text fetch not attempted this run, abstract-level extraction used. This is one of the relatively rare Tier 1 records with genuine randomized human clinical outcome data (quantitative epithelialization rate, healing time, and neovascularization score) directly usable for the review's clinical-evidence benchmarking table, alongside PUBMED_0646 and PUBMED_0832 elsewhere in the corpus.",
    ),
    "PUBMED_0826": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / bioprinting process-engineering study (in vitro, method comparison)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="fibrin-based cell-carrier scaffold, seeded via extrusion bioprinting versus manual pipette application",
        specific_materials="flat, transparent fibrin substrate, 0.5 mm thick",
        fabrication_method="0.5 mm thick flat transparent fibrin substrates prepared; limbal epithelial stem cells (LESCs) applied to the fibrin substrate either via extrusion bioprinting (test) or traditional manual pipette seeding (control); resulting cell density, viability, epithelial growth rate, and phenotype (p63, CK14 marker expression) compared between the two seeding methods",
        scaffold_architecture="flat fibrin substrate scaffold seeded with LESCs via extrusion bioprinting or manual pipette application",
        cell_type_used="limbal epithelial stem cells (LESCs)",
        cell_source="not specified in detail beyond 'in vivo cultured' LESCs; species not explicitly stated in the retrieved abstract portion",
        growth_factors_or_bioactive_agents="none exogenous reported; fibrin substrate itself serves as the cell-adhesive carrier",
        optical_transparency_reported="yes",
        optical_metric_details="The fibrin substrate is explicitly described as transparent; no specific numeric transmittance percentage is given in the retrieved abstract.",
        mechanical_testing_reported="unclear / not reported in abstract",
        mechanical_metric_details="No numeric mechanical (modulus/tensile) testing values reported in the retrieved abstract; the study focuses on seeding-process control rather than bulk mechanical characterization.",
        biological_testing_reported="yes",
        biological_metric_details="Extrusion bioprinting achieved uniform scaffold surface coverage with LESC density in printed lines close to the targeted value; bioprinted cells showed higher viability than manually seeded cells (91.1 +/- 8.2% vs. 82.6 +/- 12.8%); epithelium growth rate was higher in bioprinted samples; both bioprinted and manually seeded groups showed favorable phenotypic features (p63-positive and CK14-positive).",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract (in vitro epithelial growth/viability follow-up)",
        main_outcomes="Extrusion bioprinting of limbal epithelial stem cells (LESCs) onto a transparent fibrin substrate achieved more uniform scaffold coverage, cell density closer to targeted values, significantly higher cell viability (91.1% vs. 82.6%), and a faster epithelial growth rate compared to traditional manual pipette seeding, while preserving favorable stem/epithelial phenotype (p63+, CK14+) in both methods -- supporting 3D bioprinting as a promising approach to improve process control and reproducibility for LSCD cell-therapy manufacturing, potentially reducing cell requirements and preserving LESC proliferative potential at lower passages.",
        main_limitations="Purely in vitro process-comparison study with no ex vivo or in vivo/animal transplantation evaluation reported in this abstract; no numeric mechanical or transmittance data given; cell source/species and sample sizes not fully specified in the retrieved abstract; long-term functional outcome of bioprinted vs. manually seeded grafts not assessed.",
        translational_readiness_level="early preclinical (in vitro manufacturing process-engineering study)",
        benchmarking_relevance="medium",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Scientific Reports (Nature Portfolio), DOI 10.1038/s41598-024-73383-y, 2024 -- Scientific Reports is a fully open-access (gold OA) journal; full text freely available; full-text fetch not attempted this run, abstract-level extraction used. This record is notable as a manufacturing-process/reproducibility study (bioprinting vs. manual seeding) rather than a novel scaffold-material study; useful comparator for the review's process-control/manufacturing-scalability discussion alongside PUBMED_0447 and PUBMED_0867 in this same batch.",
    ),
    "PUBMED_0843": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / growth-factor-enriched scaffold study (in vitro, cell differentiation focus)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="natural polymer blend hydrogel/scaffold (collagen/silk fibroin) enriched with a platelet-derived growth factor concentrate",
        specific_materials="collagen/silk fibroin (Co/SF) scaffold loaded with Platelet-Rich Growth Factor (PRGF)",
        fabrication_method="Co/SF scaffolds fabricated and loaded with PRGF; PRGF release kinetics characterized via release studies; cytotoxicity assays performed; Wharton's jelly-derived mesenchymal stem cells (WJMSCs) and limbal epithelial stem cells (LESCs) cultured on PRGF-loaded Co/SF scaffolds at varying PRGF concentrations; proliferation assessed via MTT assay; differentiation of WJMSCs toward corneal epithelial cells (CECs) assessed via real-time PCR and immunostaining for stem (P63, ABCG2) and differentiated epithelial (cytokeratin 3/12) markers",
        scaffold_architecture="collagen/silk fibroin composite scaffold functioning as a sustained-release depot for PRGF and a substrate for cell attachment/differentiation",
        cell_type_used="Wharton's jelly-derived mesenchymal stem cells (WJMSCs) and limbal epithelial stem cells (LESCs)",
        cell_source="WJMSCs are human umbilical-cord Wharton's jelly-derived (allogeneic, easily accessible source); LESCs source not further specified in the retrieved abstract",
        growth_factors_or_bioactive_agents="Platelet-Rich Growth Factor (PRGF), loaded into the Co/SF scaffold in a concentration-dependent release format",
        optical_transparency_reported="no / not reported in abstract",
        optical_metric_details="Not reported; characterization focused on PRGF release kinetics, cytotoxicity, and cell proliferation/differentiation marker expression rather than optical transparency.",
        mechanical_testing_reported="no / not reported in abstract",
        mechanical_metric_details="No numeric mechanical (modulus/tensile) testing data reported in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="PRGF-loaded Co/SF scaffold significantly promoted proliferation of both WJMSCs and LESCs in a concentration-dependent manner (MTT assay); real-time PCR and immunostaining showed a significant increase in P63, ABCG2, and cytokeratin 3/12 expression in WJMSCs (consistent with early differentiation toward a corneal epithelial phenotype), alongside a significant decrease in P63/ABCG2 (stemness markers) and increase in cytokeratin 3/12 (differentiated epithelial markers), indicating successful WJMSC-to-CEC differentiation; scaffold was non-cytotoxic.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract",
        main_outcomes="A PRGF-loaded collagen/silk fibroin scaffold significantly and dose-dependently promoted proliferation of both Wharton's jelly-derived mesenchymal stem cells (WJMSCs) and limbal epithelial stem cells (LESCs), and successfully drove differentiation of WJMSCs toward a corneal epithelial cell phenotype (decreased P63/ABCG2, increased cytokeratin 3/12), positioning WJMSCs on a PRGF-enriched Co/SF scaffold as a promising, more accessible alternative cell source and biomaterial platform to conventional cultivated limbal epithelial transplantation (CLET) and amniotic membrane for LSCD treatment.",
        main_limitations="No optical transparency or mechanical (modulus) data reported; purely in vitro, with no ex vivo or in vivo/animal transplantation evaluation; sample sizes and exact culture/differentiation timeline not specified numerically in the retrieved abstract; functional (barrier/transplant) performance of the differentiated cells not assessed.",
        translational_readiness_level="early preclinical (in vitro only)",
        benchmarking_relevance="medium",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Regenerative Medicine (Taylor & Francis), DOI 10.1080/17460751.2024.2427513, 2024 -- Taylor & Francis hybrid/subscription journal; open-access status of this specific article not confirmed this run; abstract-level extraction only. Notable as an alternative-cell-source (Wharton's jelly MSC, umbilical-cord derived) plus growth-factor-delivery (PRGF) combination study, complementing PUBMED_0202 (dental pulp vs. limbal stem cells) elsewhere in the corpus for the review's cell-source comparison discussion.",
    ),
    "PUBMED_0867": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / cell-culture optimization and bioprinting study with in vitro and in vivo evaluation (rabbit LSCD model)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="cell-sheet/spheroid bio-ink auto-bioprinted onto a custom curved natural-polymer (collagen) membrane carrier",
        specific_materials="collagen membrane (custom-made, curved) as the bioprinting substrate/carrier for LESC spheroid bio-ink",
        fabrication_method="rabbit limbal epithelial stem cells (LESCs) cultured with Rho kinase inhibitor Y-27632 and a dual-media approach (proliferative medium M1, stabilizing medium M2); spheroid culture used to form LESC spheroids; immunofluorescent staining and RNA sequencing used to characterize gene expression changes; LESC spheroids formulated into a bio-ink and auto-bioprinted onto a custom-made curved collagen membrane to create a bioactive, transplantable anterior corneal sheet; sheet transplanted via anterior superficial corneal transplantation in a rabbit LSCD model to assess in vivo epithelial wound-healing capacity",
        scaffold_architecture="auto-bioprinted LESC-spheroid bio-ink layered onto a custom-made curved collagen membrane, forming a transplantable anterior corneal cell sheet with anatomically matched curvature",
        cell_type_used="rabbit limbal epithelial stem cells (LESCs)",
        cell_source="rabbit, primary",
        growth_factors_or_bioactive_agents="Rho kinase (ROCK) inhibitor Y-27632, used during proliferative (M1) and stabilizing (M2) dual-media culture and spheroid formation",
        optical_transparency_reported="no / not reported in abstract",
        optical_metric_details="Not reported; characterization focused on cell growth, proliferation, gene expression, and in vivo wound-healing outcomes rather than optical transparency.",
        mechanical_testing_reported="no / not reported in abstract",
        mechanical_metric_details="No numeric mechanical (modulus/tensile) testing data reported in the retrieved abstract; the collagen membrane carrier's mechanical properties are not quantified in the abstract text retrieved (abstract text is truncated in the local corpus before the discussion/conclusion section).",
        biological_testing_reported="yes",
        biological_metric_details="Y-27632 significantly enhanced LESC growth, proliferation, and reduced apoptosis; the dual-media (M1/M2) approach combined with Y-27632 improved LESC proliferation while maintaining stemness; in spheroid culture, Y-27632 decreased cell death and promoted proliferation; immunofluorescent staining and RNA sequencing showed upregulation of tight-junction and cell-adhesion genes and downregulation of aging- and cell-cycle-associated genes; anterior superficial corneal transplantation of the auto-bioprinted LESC sheets significantly accelerated epithelial wound healing in a rabbit LSCD model.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in the retrieved (truncated) abstract",
        main_outcomes="Combining the Rho kinase inhibitor Y-27632 with a dual-media (proliferative/stabilizing) culture approach and spheroid culture significantly improved rabbit LESC growth, proliferation, stemness maintenance, and gene-expression profile (upregulated tight-junction/adhesion genes, downregulated aging/cell-cycle genes); LESC spheroids were successfully auto-bioprinted as a bio-ink onto a custom curved collagen membrane to form a bioactive, transplantable anterior corneal cell sheet, which significantly accelerated epithelial wound healing when transplanted into a rabbit LSCD model -- demonstrating a complete cell-culture-to-bioprinted-graft pipeline for LSCD therapy.",
        main_limitations="Retrieved abstract text in the local screening corpus is truncated before the full discussion/conclusion, so exact quantitative wound-healing/follow-up metrics and mechanical characterization of the collagen membrane are not available for this extraction; rabbit (not human) model only, with no clinical evidence.",
        translational_readiness_level="preclinical (animal model, rabbit)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Acta Biomaterialia (Elsevier), DOI 10.1016/j.actbio.2025.01.022, 2025 -- Elsevier hybrid/subscription journal; open-access status of this specific article not confirmed this run; abstract-level extraction only, and the locally stored abstract text is itself truncated before the full RESULTS/discussion, flagged here for a possible future full-text follow-up. Notable as a complete pipeline record (ROCK-inhibitor + dual-media LESC optimization -> spheroid bio-ink -> curved-membrane auto-bioprinting -> in vivo rabbit transplantation), directly complementing PUBMED_0826 (fibrin-substrate bioprinting) in this same batch for the review's bioprinting-manufacturing benchmarking discussion.",
    ),
    "PUBMED_0908": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / decellularized tissue-derived hydrogel study (in vitro only)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="decellularized allogeneic (human) amniotic membrane-derived injectable hydrogel",
        specific_materials="decellularized human amniotic membrane hydrogel (dAM-gel), produced via a freeze-thaw decellularization protocol",
        fabrication_method="human amniotic membrane decellularized using a freeze-thaw protocol designed to preserve ECM integrity; decellularization efficiency assessed via collagen content, glycosaminoglycan (GAG) content, and residual DNA quantification; dAM-gel formed at varying concentrations and gelation capacity/time characterized; limbal stem cell (LSC) migration and proliferation assessed in the presence of dAM-gel; agrin content and Yap1-cyclin D1 signaling pathway investigated as a mechanistic explanation for LSC proliferation effects",
        scaffold_architecture="injectable/gelling hydrogel (dAM-gel) derived from decellularized amniotic membrane ECM, not a solid pre-formed scaffold",
        cell_type_used="limbal stem cells (LSCs), particularly the p63-positive subpopulation",
        cell_source="not specified in detail beyond 'limbal stem cells'; species not explicitly stated in the retrieved abstract",
        growth_factors_or_bioactive_agents="endogenous agrin, retained within the decellularized amniotic membrane ECM and implicated in driving LSC proliferation via the Yap1-cyclin D1 signaling pathway",
        optical_transparency_reported="no / not reported in abstract",
        optical_metric_details="Not reported; characterization focused on collagen/GAG/DNA content, gelation kinetics, and cell proliferation/signaling rather than optical transparency.",
        mechanical_testing_reported="partial",
        mechanical_metric_details="Collagen content decreased modestly after decellularization (313.50 +/- 27.89 to 284.8 +/- 14.82 microg/mg, P=0.08); GAG content shifted from 7.20 +/- 1.66 to 6.28 +/- 0.55 microg/mg (P=0.27); residual DNA dropped from 7.41 +/- 0.78 to 0.14 +/- 0.06 microg/mg (P<0.0001), confirming near-complete decellularization; robust gelation achieved at 14 mg/mL, completing within 28.26 +/- 1.21 minutes (limited gelation capacity noted at lower concentrations); no bulk elastic-modulus/tensile data reported.",
        biological_testing_reported="yes",
        biological_metric_details="dAM-gel facilitated migration and proliferation of limbal stem cells, particularly the p63-positive subpopulation associated with clinical treatment success; the effect was mechanistically linked to a high concentration of agrin in the gel acting via the Yap1-cyclin D1 signaling pathway to preserve stemness while promoting proliferation.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="not applicable / not specified (short-term in vitro gelation and cell proliferation assays)",
        main_outcomes="A freeze-thaw-decellularized human amniotic membrane hydrogel (dAM-gel) achieved near-complete DNA removal (minimal immunogenicity risk) with only modest, non-significant reductions in collagen and GAG content, and formed robust hydrogels at 14 mg/mL within ~28 minutes; the gel promoted migration and proliferation of p63-positive limbal stem cells, mechanistically attributed to a high endogenous agrin content acting through the Yap1-cyclin D1 pathway to expand LSCs while preserving stemness -- suggesting dAM-gel could help overcome the insufficient stem-cell-quantity limitation behind variable clinical success of allogeneic cultured LESC transplantation.",
        main_limitations="Purely in vitro study with no ex vivo or in vivo/animal transplantation evaluation reported; no optical transparency or bulk mechanical (modulus) data given; cell source/species and sample sizes not fully specified in the retrieved abstract; collagen/GAG content changes were not statistically significant (P=0.08 and P=0.27), a limitation on decellularization-protocol ECM preservation claims.",
        translational_readiness_level="early preclinical (in vitro only)",
        benchmarking_relevance="medium",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Colloids and Surfaces B: Biointerfaces (Elsevier), DOI 10.1016/j.colsurfb.2025.114656, 2025 -- Elsevier hybrid/subscription journal; open-access status of this specific article not confirmed this run; abstract-level extraction only. Rich quantitative decellularization-efficiency data (collagen/GAG/DNA with p-values, gelation time) makes this a strong comparator for the review's decellularized-ECM-hydrogel benchmarking entries, alongside other amniotic-membrane and decellularized-scaffold records in the corpus.",
    ),
    "PUBMED_0919": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / injectable self-healing hydrogel study with in vitro and in vivo evaluation (rabbit corneal defect model)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="natural polysaccharide-based self-healing, adhesive, injectable hydrogel loaded with cell-derived extracellular vesicles",
        specific_materials="aldehyde-modified oxidized guar gum (OGG) crosslinked with carboxymethyl chitosan (CMCS) via dynamic Schiff base bonds, loaded with mesenchymal stem cell exosomes (MSC-Exos)",
        fabrication_method="OGG synthesized via oxidation to introduce aldehyde groups; OGG combined with CMCS through dynamic, reversible Schiff base bonding to form a self-healing hydrogel network; MSC-derived exosomes (MSC-Exos) loaded into the hydrogel; physicochemical properties (porosity, mechanical strength, light transmittance) tuned by varying OGG concentration; shear-thinning, self-healing, injectability, and tissue-adhesion properties characterized; corneal epithelial cell uptake of exosomes and migration assessed in vitro; therapeutic efficacy assessed in a rabbit cornea defect model evaluating collagen deposition and inflammation",
        scaffold_architecture="injectable, self-healing, tissue-adhesive hydrogel network (OGG-CMCS via Schiff base chemistry) with tunable porosity and mechanical strength, loaded with exosomes",
        cell_type_used="corneal epithelial cells (in vitro exosome-uptake/migration assays); species not specified in the retrieved abstract",
        cell_source="mesenchymal stem cell exosomes (MSC-Exos) as the bioactive cargo; source MSCs not further specified in the retrieved abstract",
        growth_factors_or_bioactive_agents="mesenchymal stem cell-derived exosomes (MSC-Exos), loaded into the hydrogel as the primary bioactive/regenerative cargo",
        optical_transparency_reported="yes",
        optical_metric_details="The hydrogel was explicitly reported as transparent, with light transmittance identified as one of the physicochemical properties precisely tunable by adjusting OGG concentration; no specific numeric transmittance percentage is given in the retrieved abstract.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Mechanical strength was reported as precisely tunable by adjusting OGG concentration, alongside porosity and light transmittance; the hydrogel exhibited outstanding shear-thinning and self-healing properties enabling easy needle injection, and achieved robust tissue adhesion at physiological temperature via Schiff base interactions; no specific numeric elastic-modulus or tensile-strength values are given in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="MSC-Exos were taken up by corneal epithelial cells and promoted their migration in vitro; in a rabbit cornea defect model, the MSC-Exos-loaded hydrogel adhered firmly to the defected cornea and significantly improved wound repair by enhancing collagen deposition and reducing inflammation.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract",
        main_outcomes="A self-healing, injectable, tissue-adhesive hydrogel formed from aldehyde-modified oxidized guar gum and carboxymethyl chitosan via dynamic Schiff base chemistry, loaded with mesenchymal stem cell exosomes, achieved tunable porosity, mechanical strength, and light transmittance via OGG concentration; the exosome cargo was taken up by corneal epithelial cells and promoted their migration in vitro, and in a rabbit corneal defect model the hydrogel adhered firmly to the wound and significantly improved repair by enhancing collagen deposition and reducing inflammation -- supporting this multifunctional, cell-free (exosome-based) hydrogel as a promising injectable therapeutic for corneal wound healing.",
        main_limitations="No specific numeric transmittance, modulus, or tensile-strength values reported despite qualitative claims of tunability; exact OGG concentration used for the in vivo studies and follow-up duration not specified numerically in the retrieved abstract; rabbit (not human) model only, with no clinical evidence; long-term degradation/integration of the hydrogel not assessed.",
        translational_readiness_level="preclinical (animal model, rabbit)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Journal of Nanobiotechnology (BMC-series, Springer Nature), DOI 10.1186/s12951-025-03366-2, 2025 -- BMC-series journals are fully open-access (gold OA); full text freely available; full-text fetch not attempted this run, abstract-level extraction used. Cell-free exosome-delivery approach (rather than encapsulated live cells) is a notable design distinct from most other Tier 1 records in this batch; useful comparator for the review's acellular/exosome-based bioactive-hydrogel benchmarking entries, alongside PUBMED_0623 (self-assembling peptide hydrogel) elsewhere in the corpus.",
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

TRACKER_UPDATE_OA = dict(
    full_text_status="retrieved (abstract-level only)",
    pdf_available="yes (fully open-access journal; full-text fetch not attempted this run)",
    source_checked="local screening corpus abstract (screening/full_text/pubmed_tier1_tier2_extraction_plan.csv)",
    retrieval_date="2026-07-20",
    retrieval_notes="Europe PMC REST API fetch blocked by web_fetch provenance restriction in this unattended run; abstract taken from already-verified local screening corpus text (open-access journal, full text known to be freely available).",
    extraction_ready="yes",
    reason_not_extraction_ready="",
)

TRACKER_UPDATE_SUBSCRIPTION = dict(
    full_text_status="retrieved (abstract-level only)",
    pdf_available="unknown / not verified this run (subscription/hybrid journal, open-access status of this specific article not confirmed)",
    source_checked="local screening corpus abstract (screening/full_text/pubmed_tier1_tier2_extraction_plan.csv)",
    retrieval_date="2026-07-20",
    retrieval_notes="Europe PMC REST API fetch blocked by web_fetch provenance restriction in this unattended run; abstract taken from already-verified local screening corpus text. Journal is a hybrid/subscription title; full-text access not confirmed.",
    extraction_ready="yes",
    reason_not_extraction_ready="",
)

OA_IDS = {"PUBMED_0672", "PUBMED_0702", "PUBMED_0799", "PUBMED_0826", "PUBMED_0919"}
SUBSCRIPTION_IDS = {"PUBMED_0843", "PUBMED_0867", "PUBMED_0908"}

for sid in EXTRACTIONS:
    if sid not in tby_id:
        print("WARNING missing in tracker:", sid)
        continue
    if sid in OA_IDS:
        update = TRACKER_UPDATE_OA
    else:
        update = TRACKER_UPDATE_SUBSCRIPTION
    tby_id[sid].update(update)

with tracker_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=tfieldnames)
    w.writeheader()
    w.writerows(trows)

print("Tracker updated for:", list(EXTRACTIONS.keys()))
