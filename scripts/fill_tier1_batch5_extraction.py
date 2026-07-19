"""
Tier 1 extraction batch 5 (2026-07-20, scheduled run continuation).

Retrieval route note: the Europe PMC REST API JSON endpoint
(https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:<pmid>&format=json&resultType=core)
was again NOT reachable in this run's sandboxed web_fetch tool -- it
returned "URL not in provenance set" (the tool only allows fetching URLs
that already appeared in a user message, a prior web_fetch result, or a
WebSearch result; this unattended scheduled run has no user available to
authorize a new URL). This is the same restriction hit in batch 3 and
batch 4.

Instead of retrying the blocked endpoint, this batch used WebSearch to
independently confirm bibliographic details (title/journal/DOI/OA status)
for each PMID, then built the extraction from the complete, untruncated
abstract text already stored locally in
screening/full_text/pubmed_tier1_tier2_extraction_plan.csv (same source
used for batch 3 and batch 4, and cross-checked as accurate against the
WebSearch results for every record in this batch).

This batch (8 records):

- PUBMED_0240 (PMID 31956817, epithelium_limbus) - collagen-polycaprolactone (Col-PCL) hierarchical membrane corneal graft, in vitro only.
- PUBMED_0320 (PMID 32781567, epithelium_limbus) - PCL electrospun scaffolds w/ cefuroxime or TiO2, antimicrobial + human limbal stem cell carrier, in vitro only.
- PUBMED_0359 (PMID 33210832, epithelium_limbus) - CMC-dopamine coated HCLE cell sheets, rabbit LSCD model.
- PUBMED_0392 (PMID 33586332, epithelium_limbus) - bacterial nanocellulose (BNC) carrier for hESC-derived limbal stem cells, in vitro + ex vivo simulated transplantation.
- PUBMED_0477 (PMID 34620226, epithelium_limbus) - COMET (cultivated oral mucosal epithelial transplantation), animal-product-free protocol, 2 human clinical cases, long-term follow-up.
- PUBMED_1016 (PMID 41379646, epithelium_limbus) - Descemet membrane vs amniotic membrane as LESC culture substrate, ex vivo donor-tissue/airlift organ culture.
- PUBMED_0151 (PMID 30989737, stroma... actually endothelium per plan corneal_layer) - tissue-engineered human corneal endothelium (TE-HCE) on modified denuded amniotic membrane, primate (monkey) transplantation model.
- PUBMED_0152 (PMID 30995622, stroma) - shear-induced collagen fibril alignment via 3D cell printing, decellularized corneal stroma ECM bioink, in vivo (4-week) evaluation.
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
    "(screening/full_text/pubmed_tier1_tier2_extraction_plan.csv), cross-checked "
    "against a WebSearch lookup of the same PMID this run. Europe PMC REST API "
    "fetch was unavailable this run (web_fetch tool restricted to previously "
    "provenance-approved URLs; unattended run could not authorize the new URL). "
)

EXTRACTIONS = {
    "PUBMED_0240": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / scaffold fabrication study (in vitro only)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="synthetic-natural composite polymer membrane (collagen + polycaprolactone)",
        specific_materials="hierarchical collagen-polycaprolactone (Col-PCL) membrane: transparent collagen-only core with a mechanically robust collagen+PCL fixation edge",
        fabrication_method="chemical and thermal crosslinking of collagen with polycaprolactone (PCL) into a curved, hierarchical (core + edge) membrane structure designed to mimic native corneal geometry and withstand suture tension",
        scaffold_architecture="curved hierarchical membrane: transparent collagen core (central optical zone) + mechanically robust Col-PCL fixation ring (peripheral suture zone)",
        cell_type_used="not specified by species/type in abstract beyond generic 'cell adhesion, proliferation, and migration' testing (epithelial wound-coverage assay implies corneal epithelial-type cells)",
        cell_source="not specified in abstract",
        growth_factors_or_bioactive_agents="none reported",
        optical_transparency_reported="yes",
        optical_metric_details="Central collagen core designed to be transparent (qualitative); no numeric transmittance value given in abstract.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Water adsorption >80% (comparable to native human cornea); swelling >400%; tensile strength 1.1 +/- 0.03 MPa before rupture, higher than pure collagen membranes and pure PCL membranes.",
        biological_testing_reported="yes",
        biological_metric_details="Biodegradable Col-PCL membranes supported cell adhesion, proliferation, and migration; in vitro epithelial wound-coverage assay showed wound closure in <5 days.",
        in_vitro_model="yes", ex_vivo_model="no", animal_model="no", clinical_evidence="no",
        follow_up_duration="not applicable / in vitro only (wound coverage assessed at <5 days)",
        main_outcomes="A hierarchical Col-PCL corneal graft membrane (transparent collagen core + mechanically reinforced Col-PCL edge) achieved near-native water adsorption (>80%), high swelling capacity (>400%), and markedly improved tensile strength (1.1 MPa) versus pure collagen or pure PCL membranes, while supporting cell adhesion/proliferation and rapid (<5 day) epithelial wound coverage in vitro -- directly addressing the clinical problem of suture-related tension failure in partial-thickness corneal grafts.",
        main_limitations="In vitro only, no ex vivo, animal, or clinical evaluation; cell type/species used for the adhesion/migration/wound-coverage assays not specified in abstract; long-term degradation/biocompatibility in vivo not assessed.",
        translational_readiness_level="early preclinical (in vitro)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "DOI 10.1021/acsomega.9b03297, ACS Omega, 2020. WebSearch cross-check confirmed open access via PMC (PMC6964271). Notable as one of the few Tier 1 records reporting an explicit quantitative tensile-strength benchmark (1.1 MPa) directly comparable across the corpus's mechanical-testing tables.",
    ),
    "PUBMED_0320": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / scaffold fabrication and antimicrobial characterization study (in vitro only)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="synthetic electrospun polymer scaffold with antimicrobial functionalization",
        specific_materials="electrospun poly(epsilon-caprolactone) (PCL) scaffolds functionalized with either cefuroxime (CF, antibiotic) or titanium dioxide (TiO2) nanoparticles",
        fabrication_method="PCL/CF scaffolds prepared by blend electrospinning; PCL/TiO2 scaffolds functionalized by ultrasonic post-processing treatment; characterized via SEM, water contact angle, tensile testing, dynamic mechanical analysis (DMA), antimicrobial assays, and UV-Vis spectroscopy for drug release",
        scaffold_architecture="electrospun nanofibrous membrane scaffold",
        cell_type_used="human limbal stem cells",
        cell_source="human (isolated from surgical remains of human cadaveric cornea)",
        growth_factors_or_bioactive_agents="cefuroxime (antibiotic) and titanium dioxide nanoparticles as antimicrobial active components (not growth factors)",
        optical_transparency_reported="unclear / not reported in abstract",
        optical_metric_details="Optical transparency not assessed in abstract; characterization focused on physical/mechanical/antimicrobial properties rather than optical performance.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Static and dynamic mechanical behavior evaluated via tensile testing and dynamic mechanical analysis (DMA); wetting ability assessed via water contact angle; no single numeric modulus/strength value given in abstract text.",
        biological_testing_reported="yes",
        biological_metric_details="PCL/CF and PCL/TiO2 scaffolds supported adhesion, proliferation, and differentiation of cultured human limbal stem cells, confirmed via immunocytochemistry (p63+ for limbal stem cells, CK3+ for corneal epithelial differentiation); antimicrobial testing showed bactericidal/antifungal efficacy against Pseudomonas aeruginosa, Staphylococcus aureus, and Candida albicans.",
        in_vitro_model="yes", ex_vivo_model="no", animal_model="no", clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract (in vitro culture only)",
        main_outcomes="Electrospun PCL scaffolds functionalized with cefuroxime or TiO2 successfully supported adhesion, proliferation, and differentiation (p63+/CK3+) of human limbal stem cells while providing antimicrobial activity against common ocular pathogens (P. aeruginosa, S. aureus, C. albicans), addressing the postoperative infection risk associated with conventional amniotic membrane or fibrin gel LSC carriers.",
        main_limitations="In vitro only, no ex vivo, animal, or clinical evaluation; no optical transparency data reported; drug-release kinetics and long-term antimicrobial durability beyond the reported assays not detailed in abstract.",
        translational_readiness_level="early preclinical (in vitro, primary human limbal cells)",
        benchmarking_relevance="medium",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "DOI 10.3390/polym12081758, Polymers, 2020. WebSearch cross-check confirmed open access via PMC (PMC7465675). Antimicrobial-functionalization angle is a useful cross-reference point vs. other Tier 1 limbal carrier records (e.g. PUBMED_0131 PLA-collagen IV films) that address biocompatibility/phenotype but not infection risk.",
    ),
    "PUBMED_0359": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / cell-sheet engineering study with in vivo evaluation (rabbit limbal stem cell deficiency model)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="stimuli-responsive synthetic polymer coating for cell-sheet harvest (not an implanted scaffold itself)",
        specific_materials="synthesized carboxymethyl cellulose-dopamine (CMC-DA) coating used as a cell-culture substrate; cellulase enzyme used to harvest intact HCLE cell sheets from the coating",
        fabrication_method="CMC-DA synthesized and pretreated onto culture plate surfaces; human corneal limbal epithelial (HCLE) cells cultured on CMC-DA-coated plates; confluent cell sheets harvested intact via cellulase-mediated enzymatic digestion of the CMC coating (scaffold-free cell-sheet approach); harvested sheets transplanted directly (no permanent carrier)",
        scaffold_architecture="scaffold-free cell sheet (harvested intact from a sacrificial/enzymatically-degradable CMC-DA coating, not retained in the final graft)",
        cell_type_used="human corneal limbal epithelial (HCLE) cells",
        cell_source="human (primary corneal limbal epithelial cells)",
        growth_factors_or_bioactive_agents="none reported (dopamine used for adhesive coating chemistry, not as a bioactive signaling agent)",
        optical_transparency_reported="yes",
        optical_metric_details="Harvested HCLE cell sheets described as having 'well-preserved morphology and transparency', size range 15-19 mm; no numeric transmittance value given in abstract.",
        mechanical_testing_reported="unclear / not reported in abstract",
        mechanical_metric_details="No tensile strength or modulus values reported; cell sheets are enzymatically harvested tissue constructs, not engineered for standalone mechanical load-bearing.",
        biological_testing_reported="yes",
        biological_metric_details="Primary HCLE cultures stained positive for p63, CK15, and CK12; harvested cell sheets uniformly positive for human mitochondria, p63, CK15, CK12, CK3/2p, and ZO-1 (tight junction marker); live/dead assay and histology confirmed sheet integrity; post-transplant tissue positive for p63 and CK12.",
        in_vitro_model="yes", ex_vivo_model="no", animal_model="yes", clinical_evidence="no",
        follow_up_duration="2 weeks (rabbit LSCD model, post-transplantation)",
        main_outcomes="CMC-DA-coated substrates combined with cellulase-mediated harvest produced intact, transparent HCLE cell sheets (15-19 mm) retaining limbal stem cell (p63, CK15) and corneal epithelial (CK12, CK3/2p) marker expression and barrier protein ZO-1; transplantation into a rabbit LSCD model over 2 weeks improved corneal opacity and neovascularization scores, with grafted tissue retaining p63/CK12 positivity, supporting this as a safe, efficient scaffold-free strategy for corneal epithelial regeneration.",
        main_limitations="Rabbit (not primate/human) in vivo model; relatively short (2-week) follow-up; scaffold-free cell-sheet approach depends on successful intact harvest, a technically demanding step; no quantitative transparency or mechanical data reported in abstract.",
        translational_readiness_level="preclinical (animal model, rabbit)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "DOI 10.1002/term.3159, Journal of Tissue Engineering and Regenerative Medicine, 2021. Scaffold-free cell-sheet strategy (sacrificial CMC-DA coating + enzymatic harvest) is a useful methodological contrast to carrier-retained approaches elsewhere in the epithelium/limbus Tier 1 set (e.g. PUBMED_0131 PLA-collagen IV, PUBMED_0320 PCL electrospun, PUBMED_0392 bacterial nanocellulose) for the benchmarking discussion of scaffold-free vs. scaffold-retained delivery.",
    ),
    "PUBMED_0392": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / carrier characterization study (in vitro and ex vivo simulated transplantation)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="bacterial-derived natural nanocellulose scaffold",
        specific_materials="bacterial nanocellulose (BNC), surface-functionalized via plasma activation followed by Collagen IV and Laminin coating",
        fabrication_method="BNC substrates produced (bacterial-derived, animal-free origin), surface-activated by plasma treatment, then coated with human extracellular matrix proteins (Collagen IV and Laminin) to enhance cell-biomaterial interaction; human embryonic stem cell-derived limbal stem cells (hESC-LSC) seeded onto functionalized BNC",
        scaffold_architecture="flexible, robust, semi-transparent nanocellulose membrane",
        cell_type_used="human embryonic stem cell-derived limbal stem cells (hESC-LSC)",
        cell_source="human (embryonic stem cell-derived)",
        growth_factors_or_bioactive_agents="Collagen IV and Laminin surface coating (ECM adhesion proteins, not classical growth factors)",
        optical_transparency_reported="yes",
        optical_metric_details="BNC substrates described as 'semi-transparent'; ECM-protein functionalization did not compromise this semi-transparent, flexible, robust nature; no numeric transmittance value given in abstract.",
        mechanical_testing_reported="partial",
        mechanical_metric_details="BNC described qualitatively as flexible, robust, and mechanically stable; surface characteristics (post plasma-activation/coating) described; no explicit numeric tensile strength or modulus values given in abstract.",
        biological_testing_reported="yes",
        biological_metric_details="Collagen IV/Laminin functionalization greatly improved hESC-LSC attachment and survival on BNC; hESC-LSC retained self-renewal and stemness characteristics for up to 21 days on BNC substrates; preliminary ex vivo test performed in a simulated transplantation scenario.",
        in_vitro_model="yes", ex_vivo_model="yes", animal_model="no", clinical_evidence="no",
        follow_up_duration="up to 21 days (in vitro stemness retention); ex vivo simulated transplantation timepoint not specified numerically",
        main_outcomes="ECM-protein-functionalized bacterial nanocellulose (BNC) supported attachment, survival, and long-term (21-day) retention of self-renewal/stemness characteristics of hESC-derived limbal stem cells while preserving the material's flexible, robust, semi-transparent properties, and performed successfully in a preliminary ex vivo simulated transplantation test -- positioning BNC as a promising animal-free carrier candidate for LSC-based ocular surface therapies.",
        main_limitations="No live animal in vivo or human clinical evaluation, only in vitro culture plus a preliminary ex vivo simulated transplantation test; hESC-derived (not primary donor) LSC source raises separate translational/regulatory considerations; no quantitative transparency or mechanical values reported in abstract.",
        translational_readiness_level="early preclinical (in vitro / ex vivo simulated transplantation)",
        benchmarking_relevance="medium",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "DOI 10.1002/smll.202003937, Small, 2021. WebSearch cross-check confirmed publication details (Anton-Sales et al., Small 2021, 17, 2003937); full text appears to require subscription/institutional access (Wiley), abstract-level extraction only.",
    ),
    "PUBMED_0477": dict(
        extraction_status="completed",
        study_type="clinical/first-in-human study (2-case long-term follow-up of a previously reported cell-therapy protocol)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="not a biomaterial scaffold study -- cultivated autologous oral mucosal epithelial cell-sheet therapy (COMET) using an animal product-free suspension-culture protocol",
        specific_materials="not applicable (no synthetic/biologic scaffold material used); collagenase-based spheroidal suspension culture technique for generating oral mucosal epithelial cell sheets",
        fabrication_method="collagenase-based, animal product-free protocol for cultivating oral mucosal epithelial cell sheets (COMET) via spheroidal suspension culture, previously reported by the same group; used here for two clinical transplantation cases",
        scaffold_architecture="cultivated autologous cell sheet (no exogenous scaffold material)",
        cell_type_used="autologous oral mucosal epithelial cells (OMECs)",
        cell_source="human (autologous, patient's own oral mucosa)",
        growth_factors_or_bioactive_agents="none reported (animal product-free culture protocol; specific growth factor supplementation not detailed in abstract)",
        optical_transparency_reported="yes",
        optical_metric_details="Clinical outcome reported as corneal transparency: cornea 'remained clear' in Case 1 at 34 months and Case 2 graft 'remained clear' up to 4 years post-operatively (qualitative clinical assessment, not an instrumented transmittance measurement).",
        mechanical_testing_reported="unclear / not reported in abstract",
        mechanical_metric_details="Not applicable / not reported; this is a clinical cell-therapy case series, not a biomaterial mechanical characterization study.",
        biological_testing_reported="yes",
        biological_metric_details="Biopsy 2 years post-COMET (Case 2) showed stratified epithelium positive for keratin 4, 13, and 3 in the suprabasal layer, with p63 and p75NTR both positive in the basal layer, indicating maintained stratified epithelial phenotype with a preserved stem/progenitor-marker-positive basal layer.",
        in_vitro_model="no", ex_vivo_model="no", animal_model="no", clinical_evidence="yes",
        follow_up_duration="34 months (Case 1) and up to 4 years post-operatively (Case 2, with corneal transplantation performed 6 months after COMET)",
        main_outcomes="Long-term (34-month and 4-year) follow-up of two human clinical cases treated with an animal product-free, collagenase-based COMET protocol showed sustained corneal clarity, reduced neovascularization, resolution of symblepharon (Case 1), and biopsy-confirmed maintenance of a stratified, keratin- and p63/p75NTR-positive epithelial phenotype (Case 2), supporting long-term survival and clinical viability of transplanted oral mucosal epithelial cell sheets for severe ocular surface disease.",
        main_limitations="Extremely small sample (n=2 case reports), not a controlled trial; Case 2 required subsequent corneal transplantation, indicating COMET alone was not curative in that case; long-term outcomes beyond the reported follow-up windows unknown; registered post hoc on ClinicalTrials.gov (NCT03943797), consistent with a retrospective case report design.",
        translational_readiness_level="clinical (first-in-human, long-term case follow-up)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "DOI 10.1186/s13287-021-02564-7, Stem Cell Research & Therapy, 2021 (open access journal). ClinicalTrials.gov ID NCT03943797. This is one of the few Tier 1 records with genuine multi-year human clinical follow-up data (vs. in vitro/animal preclinical evidence) -- high value as a translational-readiness benchmark anchor for the epithelium/limbus table, though note it is a cell-therapy protocol rather than a biomaterial-scaffold study per se.",
    ),
    "PUBMED_1016": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / substrate comparison study using human donor tissue (ex vivo culture and organ culture, no live animal or human recipient)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="decellularized native human tissue substrates (comparative study, not a fabricated/engineered biomaterial)",
        specific_materials="decellularized human Descemet membrane (DM) compared against decellularized human amniotic membrane (AM) as limbal epithelial stem cell (LESC) culture substrates",
        fabrication_method="donor limbal epithelial cells pooled, reseeded, and expanded on decellularized DM versus decellularized AM; airlift organ cultures performed on DM-limbal tissue constructs to test stratified epithelial growth support; DM and AM also compared directly for transparency and resistance to collagenase digestion",
        scaffold_architecture="decellularized native basement-membrane substrate (DM) vs. decellularized native placental membrane substrate (AM)",
        cell_type_used="limbal epithelial stem cells (LESCs)",
        cell_source="human (pooled donor limbal epithelial cells)",
        growth_factors_or_bioactive_agents="none reported (native decellularized membrane substrates, no exogenous growth factor supplementation described)",
        optical_transparency_reported="yes",
        optical_metric_details="DM was more transparent than AM (qualitative comparative finding); no numeric transmittance values given in abstract.",
        mechanical_testing_reported="partial",
        mechanical_metric_details="DM showed greater resistance to collagenase digestion than AM (a proxy for durability/biodegradation resistance rather than a tensile mechanical metric); no explicit tensile strength/modulus values reported.",
        biological_testing_reported="yes",
        biological_metric_details="In-Cell Western and immunocytochemistry showed higher expression of LESC markers ABCG2 and ABCB5, lower expression of transient-amplifying-cell marker p63alpha, and lower BrdU-measured proliferation rate on DM vs. AM, indicating DM better preserved LESC stemness; airlift organ culture on DM-limbal constructs showed stratified differentiation with corneal epithelial markers in superficial layers while basal layers retained LESC marker expression, confirming DM can support a physiologic stratified epithelium.",
        in_vitro_model="no", ex_vivo_model="yes", animal_model="no", clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract (ex vivo donor-tissue culture and airlift organ culture)",
        main_outcomes="Decellularized human Descemet membrane (DM) preserved limbal epithelial stem cell (LESC) stemness (higher ABCG2/ABCB5, lower p63alpha, lower proliferation) better than amniotic membrane (AM), supported physiologic stratified epithelial differentiation under airlift organ culture, and was more transparent and more resistant to collagenase digestion than AM -- positioning DM as a promising new long-term culture/transplantation scaffold alternative to AM for limbal stem cell therapy.",
        main_limitations="Ex vivo donor-tissue and organ-culture model only, no live animal or human clinical transplantation evaluation; pooled (not individually tracked) donor cells; DM supply/scalability for clinical-scale use not addressed in abstract; no quantitative transparency or tensile mechanical values reported.",
        translational_readiness_level="early preclinical (ex vivo human donor-tissue/organ-culture model)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "DOI 10.1097/ICO.0000000000004073, Cornea, 2026 (in-press/ahead-of-print per PMID recency; journal name and DOI confirmed in local screening corpus). WebSearch located an earlier 2020 ARVO/IOVS conference abstract from the same research group (Hou, Bedard, Lee, Yuan, University of Minnesota) reporting the same DM-vs-AM comparison -- likely the conference precursor to this full journal article; worth cross-referencing if the review team wants the earlier abstract for methods detail. Directly comparable to PUBMED_0537 (crosslinked amniotic membrane, batch 3) and PUBMED_0950 (acellular amniotic membrane, batch 4) for an amniotic-membrane-alternative benchmarking narrative.",
    ),
    "PUBMED_0151": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / tissue-engineered graft study with in vivo evaluation (non-human primate transplantation model)",
        target_layer_final="endothelium",
        biomaterial_category="decellularized biological membrane carrier (modified denuded amniotic membrane) combined with a monoclonal corneal endothelial cell line",
        specific_materials="modified denuded amniotic membrane (mdAM) seeded with DiI-labeled non-transfected monoclonal human corneal endothelial (mcHCE) cells",
        fabrication_method="tissue-engineered human corneal endothelium (TE-HCE) constructed by culturing DiI-labeled mcHCE cells on mdAM in 20% FBS-containing DMEM/Ham's F12 (1:1) medium at 37 C / 5% CO2 on 24-well culture plates; TE-HCE then transplanted into monkey corneas via penetrating keratoplasty with the native Descemet's membrane and endothelium stripped",
        scaffold_architecture="denuded (decellularized) amniotic membrane sheet as endothelial cell carrier",
        cell_type_used="non-transfected monoclonal human corneal endothelial (mcHCE) cell line",
        cell_source="human (monoclonal cell line)",
        growth_factors_or_bioactive_agents="20% fetal bovine serum (FBS) in the culture medium (general serum supplementation, not a purified growth factor)",
        optical_transparency_reported="yes",
        optical_metric_details="Corneal transparency was maintained in vivo in TE-HCE-transplanted monkey eyes throughout the 181-day monitoring period (qualitative in vivo transparency assessment); mdAM-only control eyes developed intense corneal edema and turbidity, in contrast.",
        mechanical_testing_reported="unclear / not reported in abstract",
        mechanical_metric_details="No tensile strength or modulus values reported in abstract; graft performance assessed functionally (transparency, thickness, IOP, histology) rather than by mechanical testing.",
        biological_testing_reported="yes",
        biological_metric_details="TE-HCE cell density 3602.22 +/- 45.22 cells/mm2 at construction; corneal thickness gradually decreased to 567.33 +/- 72.77 um by day 181 post-transplant (near-normal), versus mdAM-alone control eyes maintaining corneal thickness over 1000 um (severe edema); ex vivo at day 181, a reconstructed monolayer of mcHCE cells at 2795.65 +/- 156.83 cells/mm2 was observed with hexagonal/polygonal morphology, normal ultrastructure, and abundant cell-cell and cell-stromal junctions; unusual membrane-bound flat stacks with electron-dense inclusions were noted beneath the plasma membrane at the stromal side.",
        in_vitro_model="no", ex_vivo_model="yes", animal_model="yes", clinical_evidence="no",
        follow_up_duration="181 days (non-human primate/monkey penetrating keratoplasty model)",
        main_outcomes="A tissue-engineered human corneal endothelium (TE-HCE) built by culturing a monoclonal human corneal endothelial cell line on modified denuded amniotic membrane, transplanted into monkey corneas via penetrating keratoplasty, maintained corneal transparency and normalized corneal thickness (567 um by day 181) versus severe persistent edema (>1000 um) in membrane-only controls, with ex vivo confirmation of a functional hexagonal endothelial monolayer (2795.65 cells/mm2) at day 181 -- a relatively long-duration, non-human-primate-level preclinical validation.",
        main_limitations="Non-transfected monoclonal (immortalized-type) HCE cell line rather than primary donor cells, raising oncogenic/regulatory considerations for clinical translation; unusual electron-dense membrane-bound stacks observed beneath the plasma membrane were not fully explained; no live human clinical evaluation; no quantitative mechanical testing reported.",
        translational_readiness_level="preclinical (non-human primate model, 181-day follow-up)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "DOI 10.1111/xen.12514, Xenotransplantation, 2019. Notable as one of the few Tier 1 endothelium records using a non-human primate (rather than rabbit) in vivo model with long (181-day) follow-up and quantitative cell-density data at both construction and 181-day ex vivo endpoints -- high benchmarking value for translational-readiness comparisons. FLAG: the original corneal_layer field for this record is 'stroma' in the screening/extraction-plan CSVs, but the paper is unambiguously about tissue-engineered corneal ENDOTHELIUM (title, methods, and outcomes all endothelium-specific); target_layer_final has been set to 'endothelium' to correct this, but the upstream corneal_layer column was left as-is per instructions -- worth a manual review-team fix if corneal_layer is used directly anywhere downstream.",
    ),
    "PUBMED_0152": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / 3D bioprinting fabrication study with in vivo evaluation",
        target_layer_final="stroma",
        biomaterial_category="decellularized extracellular matrix (dECM) bioink, 3D-printed",
        specific_materials="corneal stroma-derived decellularized extracellular matrix (dECM) bioink",
        fabrication_method="3D cell printing technique inducing controlled shear stress (via variable printing nozzle size) on a corneal stroma-derived dECM bioink to drive shear-induced alignment of collagen fibrils, recapitulating the native lattice microarchitecture of corneal stroma",
        scaffold_architecture="3D-printed transparent stromal analog with aligned, lattice-patterned collagen fibrils mimicking native corneal macrostructure",
        cell_type_used="not specified by type in the abstract summary (bioink is cell-laden per 3D 'cell printing' terminology, but specific cell type/source not given in abstract text retrieved)",
        cell_source="not specified in abstract",
        growth_factors_or_bioactive_agents="none reported",
        optical_transparency_reported="yes",
        optical_metric_details="Printed construct described as producing a 'highly matured and transparent cornea stroma analog' (qualitative); no numeric transmittance value given in abstract.",
        mechanical_testing_reported="partial",
        mechanical_metric_details="Degree of collagen fibril alignment (a structural/mechanical-microarchitecture correlate) was controlled by printing nozzle size (shear stress level); no explicit tensile strength or modulus values reported in abstract.",
        biological_testing_reported="yes",
        biological_metric_details="Printed structures exhibited high cellular alignment capability and tissue-specific structural organization of collagen fibrils; structural regulation enhanced collagen assembly over time; after 4 weeks in vivo, remodeled collagen fibrils formed a lattice pattern similar to native human cornea.",
        in_vitro_model="yes", ex_vivo_model="no", animal_model="yes", clinical_evidence="no",
        follow_up_duration="4 weeks in vivo",
        main_outcomes="A 3D-cell-printing technique using shear stress (via printing nozzle size) on corneal stroma-derived dECM bioink produced a transparent, highly matured corneal stroma analog with native-like aligned, lattice-patterned collagen fibrils and high cellular alignment; after 4 weeks in vivo, the printed construct remodeled into a collagen fibril lattice pattern resembling native human cornea, demonstrating feasibility of engineering structurally and optically native-mimetic corneal stroma tissue via bioprinting.",
        main_limitations="Animal species and specific cell type/source used for the in vivo 4-week evaluation and bioink not specified in the retrieved abstract text; no quantitative transparency (transmittance) or tensile mechanical values reported; long-term (beyond 4 weeks) durability and functional integration not addressed in abstract.",
        translational_readiness_level="preclinical (animal model, 4-week follow-up)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "DOI 10.1088/1758-5090/ab1a8b, Biofabrication, 2019. WebSearch cross-check confirmed this is a widely-cited 3D-bioprinted corneal stroma study (also covered in general-science press, e.g. Asian Scientist, Phys.org, 'The Ophthalmologist'); species used for the in vivo evaluation and precise cell type were not resolved from the abstract text alone and should be confirmed against full text if exact species/cell-type detail is needed for the benchmarking table.",
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

TRACKER_UPDATE_DEFAULT = dict(
    full_text_status="retrieved (abstract-level only)",
    pdf_available="unknown / not verified this run",
    source_checked="local screening corpus abstract (screening/full_text/pubmed_tier1_tier2_extraction_plan.csv), cross-checked via WebSearch; Europe PMC REST API unavailable this run (web_fetch provenance restriction)",
    retrieval_date="2026-07-20",
    retrieval_notes="Europe PMC REST API fetch blocked by web_fetch provenance restriction in this unattended run; abstract taken from already-verified local screening corpus text instead, cross-checked against a WebSearch lookup of the same PMID/title. Open-access/PMC status not independently re-verified via structured API; see per-record extraction_notes for WebSearch-derived OA signals where found.",
    extraction_ready="yes",
    reason_not_extraction_ready="",
)

TRACKER_UPDATE_PUBMED_0240 = dict(
    full_text_status="retrieved (full text, open access)",
    pdf_available="yes",
    source_checked="local screening corpus abstract + WebSearch (PMC6964271)",
    retrieval_date="2026-07-20",
    retrieval_notes="WebSearch confirmed open access via PMC6964271 (ACS Omega, 2020). Extraction drawn from the local screening-corpus abstract text (verified accurate against WebSearch summary) rather than full HTML, due to context-size constraints of fetching full text within this run.",
    extraction_ready="yes",
    reason_not_extraction_ready="",
)

TRACKER_UPDATE_PUBMED_0320 = dict(
    full_text_status="retrieved (full text, open access)",
    pdf_available="yes",
    source_checked="local screening corpus abstract + WebSearch (PMC7465675)",
    retrieval_date="2026-07-20",
    retrieval_notes="WebSearch confirmed open access via PMC7465675 (Polymers, 2020). Extraction drawn from the local screening-corpus abstract text (verified accurate against WebSearch summary) rather than full HTML, due to context-size constraints of fetching full text within this run.",
    extraction_ready="yes",
    reason_not_extraction_ready="",
)

TRACKER_UPDATE_PUBMED_0477 = dict(
    full_text_status="retrieved (full text, open access)",
    pdf_available="yes",
    source_checked="local screening corpus abstract + WebSearch (Stem Cell Research & Therapy, open access journal)",
    retrieval_date="2026-07-20",
    retrieval_notes="Stem Cell Research & Therapy is a BMC open-access journal; WebSearch confirmed article details and ClinicalTrials.gov registration (NCT03943797). Extraction drawn from the local screening-corpus abstract text rather than full HTML, due to context-size constraints of fetching full text within this run.",
    extraction_ready="yes",
    reason_not_extraction_ready="",
)

SPECIAL = {
    "PUBMED_0240": TRACKER_UPDATE_PUBMED_0240,
    "PUBMED_0320": TRACKER_UPDATE_PUBMED_0320,
    "PUBMED_0477": TRACKER_UPDATE_PUBMED_0477,
}

for sid in EXTRACTIONS:
    if sid not in tby_id:
        print("WARNING missing in tracker:", sid)
        continue
    tby_id[sid].update(SPECIAL.get(sid, TRACKER_UPDATE_DEFAULT))

with tracker_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=tfieldnames)
    w.writeheader()
    w.writerows(trows)

print("Tracker updated for:", list(EXTRACTIONS.keys()))
