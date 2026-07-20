"""
Tier 1 extraction batch 10 (2026-07-20, scheduled run continuation).

Retrieval route note: as in batches 3-9, a direct web_fetch to the Europe PMC
REST API (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:<pmid>&format=json&resultType=core)
was attempted first this run for the lead record (PUBMED_1015, PMID
41359360) and failed with "URL not in provenance set" (the sandboxed
web_fetch tool only allows fetching URLs that already appeared in a user
message, a prior web_fetch result, or a WebSearch result; this unattended
scheduled run has no user available to authorize a new URL). A WebSearch
query for the Europe PMC REST endpoint pattern was then tried to bring a
matching URL into the fetch provenance set; the search returned only
third-party documentation pages about the API (not the target query URL
itself), and a follow-up web_fetch to the exact target URL still failed with
the same provenance error. This is the same structural restriction
documented in batches 3-9's docstrings.

Consistent with the workaround established in batches 3-9, extraction for
this batch was built from the complete, untruncated abstract text already
stored locally in screening/full_text/pubmed_tier1_tier2_extraction_plan.csv
(verified PubMed/journal abstracts captured during the original screening
pass), with open-access status assessed from known journal/publisher policy
(BMC Biotechnology is a BMC-series gold open-access journal; Experimental
and Therapeutic Medicine (Spandidos) is a gold open-access journal; ACS
Applied Materials & Interfaces, Advanced Healthcare Materials (Wiley),
Molecular Medicine Reports (Spandidos), Experimental Eye Research
(Elsevier), and Journal of Tissue Engineering and Regenerative Medicine
(Wiley) are hybrid/subscription titles -- open-access status of these
specific articles not individually confirmed this run). This is noted
per-record in extraction_notes.

This batch (8 records):
- PUBMED_1015 (PMID 41359360) - ALP-triggered TB500 self-assembling peptide hydrogel, in vitro (HCEC/HCSF) + in vivo alkali burn corneal injury model.
- PUBMED_0081 (PMID 30066447) - 3D-bioprinted RNase5-overexpressing HCEC corneal endothelium graft on amniotic membrane, ex vivo functionality + in vivo rabbit transplantation.
- PUBMED_0171 (PMID 31258659) - ex vivo rabbit corneal endothelial cell sheet on porcine Descemet membrane carrier, Y-27632-enhanced proliferation, no in vivo transplantation.
- PUBMED_0202 (PMID 31545477) - dental pulp stem cells vs. limbal stem cells, in vitro comparative characterization study (cell-source alternative for LSCD).
- PUBMED_0832 (PMID 39425087) - prospective RCT (n=50 eyes) comparing autologous oral mucosal (COMET) vs. conjunctival (CCET) epithelial grafts on amniotic membrane for bilateral ocular surface disease.
- PUBMED_0322 (PMID 32805263) - decellularized porcine Descemet stripping scaffold + iPSC-derived corneal endothelial cells, in vitro reseeding only, no in vivo evaluation.
- PUBMED_0378 (PMID 33448665) - micropatterned polyacrylamide hydrogel substrates mimicking Descemet's membrane topology/modulus, in vitro bovine CEC monolayer study.
- PUBMED_0531 (PMID 35238557) - PLCL + umbilical-cord-MSC-derived ECM composite corneal endothelial cell carrier, in vitro + ex vivo engraftment simulation + in vivo rabbit anterior chamber transplantation (8 weeks).
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
    "run could not authorize the new URL); a WebSearch attempt to surface a usable "
    "Europe PMC URL also failed to bring the target query URL into provenance. "
)

EXTRACTIONS = {
    "PUBMED_1015": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / self-assembling peptide hydrogel drug-delivery study with in vitro and in vivo evaluation (animal alkali burn corneal injury model)",
        target_layer_final="multiple_layers (epithelium regeneration + stromal fibroblast response)",
        biomaterial_category="enzyme-triggered self-assembling peptide hydrogel (in situ drug-delivery scaffold)",
        specific_materials="Nap-YpYY-TB500: naphthalene-capped, phosphorylated peptide precursor conjugating TB500 (thymosin beta-4-derived peptide, sequence LKKTETQ) via a short peptide linker; alkaline phosphatase (ALP) dephosphorylation trigger",
        fabrication_method="enzyme-instructed self-assembly (EISA) of a phosphorylated peptide precursor; among three candidate sequences screened, Nap-YpYY-TB500 was selected for optimal gelation kinetics, nanostructure, and therapeutic efficacy; elevated ALP levels at the corneal wound site trigger site-specific dephosphorylation, driving nanofiber formation and in situ gelation (lesion-responsive, spatiotemporally controlled release of TB500); evaluated in vitro on human corneal epithelial cells (HCECs) and human corneal stromal fibroblasts (HCSFs), and in vivo in an alkali burn corneal injury model",
        scaffold_architecture="in situ self-assembled peptide nanofiber hydrogel network, lesion-responsive (ALP-triggered) gelation at the wound site",
        cell_type_used="human corneal epithelial cells (HCECs) and human corneal stromal fibroblasts (HCSFs)",
        cell_source="human (HCECs and HCSFs; primary vs. cell-line source not further specified in the retrieved abstract)",
        growth_factors_or_bioactive_agents="TB500 (thymosin beta-4-derived actin-binding regenerative peptide, sequence LKKTETQ), delivered via ALP-triggered in situ gelation; first reported ocular application of TB500",
        optical_transparency_reported="unclear / not reported in abstract",
        optical_metric_details="No optical transparency/transmittance data reported in the retrieved abstract; characterization focused on gelation kinetics and nanostructure rather than optical properties.",
        mechanical_testing_reported="unclear / not reported in abstract",
        mechanical_metric_details="Gelation kinetics and nanostructure were characterized and used to select the optimal peptide sequence, but no numeric mechanical (modulus, storage/loss modulus) values are given in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="In vitro: hydrogel promoted HCEC migration, proliferation, and tight junction recovery, and enhanced myofibroblastic differentiation and cytoskeletal reorganization of HCSFs. In vivo (alkali burn model): hydrogel significantly accelerated epithelial regeneration, reduced inflammation, and improved corneal barrier function.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="yes (species not specified in the retrieved abstract)",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract (alkali burn model follow-up duration not given)",
        main_outcomes="An ALP-triggered, lesion-responsive self-assembling peptide hydrogel (Nap-YpYY-TB500), formed via enzyme-instructed self-assembly and selected from three candidate sequences for optimal gelation/nanostructure/efficacy, delivered the regenerative peptide TB500 (first ocular application reported) in a spatiotemporally controlled manner. It promoted HCEC migration, proliferation, and tight-junction recovery and enhanced HCSF myofibroblastic differentiation/cytoskeletal reorganization in vitro, and in an alkali burn corneal injury model significantly accelerated epithelial regeneration, reduced inflammation, and improved corneal barrier function.",
        main_limitations="No optical transparency or numeric mechanical (modulus) data reported in the retrieved abstract; in vivo animal species not specified; follow-up duration and sample size not given; TB500 is novel to ocular application so long-term safety/immunogenicity and comparison against established corneal wound dressings not addressed in the abstract.",
        translational_readiness_level="early preclinical (in vitro plus animal alkali burn model)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "ACS Applied Materials & Interfaces (ACS), DOI 10.1021/acsami.5c14652, 2025 -- ACS hybrid/subscription journal; open-access status of this specific article not confirmed this run; abstract-level extraction only. Novel enzyme-triggered peptide drug-delivery hydrogel approach (first ocular TB500 use), useful comparator for the review's stimuli-responsive/lesion-targeted drug-delivery benchmarking discussion.",
    ),
    "PUBMED_0081": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / 3D-bioprinted cell-laden graft study with ex vivo functional assessment and in vivo evaluation (rabbit corneal endothelium transplantation model)",
        target_layer_final="endothelium",
        biomaterial_category="3D-bioprinted, gene-engineered cell-laden graft on decellularized amniotic membrane carrier",
        specific_materials="ribonuclease 5 (RNase 5)-overexpressing human corneal endothelial cells (R5-HCECs) and control HCECs, extrusion-bioprinted onto lyophilized amniotic membrane (AM) carrier",
        fabrication_method="HCECs transiently transfected with an RNase 5 plasmid vector to generate R5-HCECs (targets: PDCD4 inhibited, cyclin D1/E1 activated, enhancing proliferation/survival); R5-HCECs and control HCECs deposited onto lyophilized AM carriers via extrusion-based 3D bioprinting to produce ready-to-use R5-Graft and Ct-Graft constructs; grafts transplanted into rabbit corneas and assessed for corneal clarity/edema over 4 weeks, with ex vivo phenotypic marker expression assessed at 4 weeks",
        scaffold_architecture="3D-bioprinted cell-laden sheet on a lyophilized amniotic membrane carrier",
        cell_type_used="human corneal endothelial cells (HCECs) engineered to overexpress RNase 5 (R5-HCECs), plus non-transfected control HCECs",
        cell_source="human (HCECs transiently transfected with RNase 5 plasmid vector; primary vs. cell-line source not further specified in the retrieved abstract)",
        growth_factors_or_bioactive_agents="RNase 5 (ribonuclease 5) overexpression used as a pro-proliferative/pro-survival engineering strategy (via PDCD4 inhibition and cyclin D1/E1 activation) rather than an exogenously delivered soluble growth factor",
        optical_transparency_reported="partial",
        optical_metric_details="Both R5-Graft and Ct-Graft began restoring clarity of rabbit corneas from 2 weeks after transplantation, with central corneal edema much less than the control group at 3 and 4 weeks (qualitative/comparative finding); no single numeric transmittance or edema-score value given in the retrieved abstract.",
        mechanical_testing_reported="unclear / not reported in abstract",
        mechanical_metric_details="No mechanical testing metrics reported in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="R5-Graft showed clearer basolateral Na+-K+ ATPase pump expression and higher cell confluency than Ct-Graft; both grafts restored corneal clarity from 2 weeks post-transplant with central corneal edema much less than control at 3 and 4 weeks; ex vivo expression of corneal endothelial phenotypic markers was clearer in R5-Grafts than Ct-Grafts at 4 weeks.",
        in_vitro_model="no",
        ex_vivo_model="yes",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="4 weeks (rabbit graft transplantation; clarity/edema assessed at 2, 3, and 4 weeks; ex vivo marker expression assessed at 4 weeks)",
        main_outcomes="Human corneal endothelial cells engineered to overexpress RNase 5 (R5-HCECs), 3D-bioprinted onto a lyophilized amniotic membrane carrier to form a ready-to-use R5-Graft, showed clearer basolateral Na+-K+ ATPase expression and higher confluency than a non-engineered control graft, and after transplantation into rabbit corneas restored corneal clarity from 2 weeks with less central corneal edema than control at 3-4 weeks, with clearer ex vivo endothelial phenotypic marker expression at 4 weeks -- supporting RNase 5 overexpression combined with 3D bioprinting as a strategy to enhance graft cellularity and function for corneal endothelial transplantation.",
        main_limitations="No numeric transmittance/edema-score or mechanical data reported in the retrieved abstract; transient (not stable) RNase 5 transfection may limit durability of the proliferative effect; rabbit (not primate/human) in vivo model; only 4-week follow-up reported; no comparison to a gold-standard donor corneal endothelial graft (e.g., DSEK/DMEK) benchmark.",
        translational_readiness_level="preclinical (animal model, rabbit)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Advanced Healthcare Materials (Wiley), DOI 10.1002/adhm.201800398, 2018 -- Wiley hybrid/subscription journal; open-access status of this specific article not confirmed this run; abstract-level extraction only. One of few endothelium-layer Tier 1 records combining 3D bioprinting with genetic engineering (RNase 5 overexpression) of the seeded cells, useful comparator for the review's cell-engineering-augmented endothelial graft benchmarking discussion.",
    ),
    "PUBMED_0171": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / ex vivo tissue-engineered cell-sheet-on-carrier study (no in vivo transplantation)",
        target_layer_final="endothelium",
        biomaterial_category="decellularized xenogeneic (porcine) Descemet membrane carrier with cultured cell sheet",
        specific_materials="porcine Descemet membrane (DM) carrier combined with cultured rabbit corneal endothelial cells (RCECs); Rho-kinase (ROCK) inhibitor Y-27632 used in the experimental group",
        fabrication_method="RCECs isolated and cultured with (experimental) or without (control) the ROCK inhibitor Y-27632; RCEC morphology assessed by inverted microscopy; proliferation and apoptosis measured by flow cytometry; RCEC identity confirmed via RT-qPCR for Na+-K+-ATPase, aquaporin 1, collagen alpha2(IV), collagen alpha1(VIII), and keratin-12; porcine DM antigenicity assessed by histocompatibility testing; DM-RCEC graft constructed and morphology assessed via alizarin red-trypan blue and H&E staining; cell membrane potential measured for physical function; complex graft tension measured with a modified tension detector and compared with fresh porcine DM-endothelium complex",
        scaffold_architecture="ex vivo-constructed cell-sheet graft: a monolayer of RCECs with polygonal, cobblestone-like morphology formed on a porcine Descemet membrane carrier",
        cell_type_used="rabbit corneal endothelial cells (RCECs)",
        cell_source="rabbit (primary RCECs, isolated and cultured, +/- Y-27632)",
        growth_factors_or_bioactive_agents="Y-27632 (Rho-associated kinase / ROCK inhibitor), used to enhance RCEC proliferation and reduce apoptosis",
        optical_transparency_reported="unclear / not reported in abstract",
        optical_metric_details="Graft morphology was assessed by alizarin red-trypan blue and H&E staining rather than optical transmittance; no transparency/transmittance value reported in the retrieved abstract.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Complex graft tension: experimental (Y-27632) group 20.0248 +/- 1.048 g vs. control group 20.5013 +/- 0.657 g, compared against fresh porcine DM-endothelium complex, with no significant difference (P>0.05) -- indicating Y-27632 treatment did not compromise graft tension relative to control or native tissue.",
        biological_testing_reported="yes",
        biological_metric_details="RCEC proliferation rate: 62.68% (Y-27632 experimental group) vs. 34.50% (control), P<0.05; apoptosis rate: 8.99% (experimental) vs. 35.68% (control), P<0.05; action potential amplitude over -80 mV in both groups, indicating normal RCEC physiological function; no antigenicity observed with porcine DM on histocompatibility testing; RT-qPCR confirmed expression of Na+-K+-ATPase, aquaporin 1, collagen alpha2(IV), collagen alpha1(VIII), and keratin-12 in cultured RCECs.",
        in_vitro_model="yes",
        ex_vivo_model="yes",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="not applicable (ex vivo study; no in vivo transplantation or follow-up reported)",
        main_outcomes="Y-27632 (ROCK inhibitor) treatment significantly increased rabbit corneal endothelial cell (RCEC) proliferation (62.68% vs. 34.50% control, P<0.05) and reduced apoptosis (8.99% vs. 35.68% control, P<0.05); RCECs formed a polygonal, cobblestone-like monolayer expressing endothelial markers (Na+-K+-ATPase, aquaporin 1, collagen IV/VIII, keratin-12); porcine Descemet membrane showed no antigenicity on histocompatibility testing; the resulting DM-RCEC graft showed normal physiological membrane potential (>-80 mV) and graft tension not significantly different from fresh porcine DM-endothelium complex (P>0.05), demonstrating feasibility of ex vivo construction of a functional RCEC sheet on a porcine DM carrier.",
        main_limitations="No in vivo transplantation or functional/clinical outcome data (ex vivo/in vitro only); no optical transparency data reported; xenogeneic porcine DM immunogenicity assessed only by short-term histocompatibility testing, not long-term in vivo immune response; rabbit-derived cells only, not human; small unspecified sample sizes implied by statistical comparisons.",
        translational_readiness_level="early preclinical (ex vivo / in vitro only, no animal transplantation)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Experimental and Therapeutic Medicine (Spandidos), DOI 10.3892/etm.2019.7573, 2019 -- Experimental and Therapeutic Medicine is a fully open-access (gold OA) Spandidos journal; full-text fetch not attempted this run, abstract-level extraction used. Notable for quantitative proliferation/apoptosis/tension data with p-values and a direct graft-tension comparison against fresh native tissue -- useful comparator for the review's decellularized-carrier mechanical benchmarking table.",
    ),
    "PUBMED_0202": dict(
        extraction_status="completed",
        study_type="cell-source characterization / comparative in vitro study (dental pulp stem cells vs. limbal stem cells as an alternative cell source for LSCD treatment)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="cell-source characterization study; no defined fabricated biomaterial scaffold reported in the abstract",
        specific_materials="human dental pulp stem cells (DPSCs) cultured in limbal stem cell (LSC)-specific media, compared against native limbal stem cells; generic reference to unspecified culture medium/scaffold conditions",
        fabrication_method="DPSCs isolated and cultured in limbal stem cell media; morphology and culture pattern compared with LSCs grown under the same media; stem cell marker gene expression assessed by PCR; protein-level stem cell and corneal differentiation marker expression assessed by immunocytochemistry and western blot",
        scaffold_architecture="not specified / not a defined biomaterial scaffold in the retrieved abstract; study is primarily a cell-source characterization comparison rather than a scaffold-fabrication study",
        cell_type_used="human dental pulp stem cells (DPSCs), compared against limbal stem cells (LSCs)",
        cell_source="human (dental pulp-derived stem cells as the candidate alternative source; limbal stem cells as the comparator)",
        growth_factors_or_bioactive_agents="none exogenous reported beyond the limbal stem cell-specific culture media formulation itself",
        optical_transparency_reported="no / not applicable (no scaffold optical characterization performed)",
        optical_metric_details="Not applicable; study does not fabricate or optically characterize a biomaterial scaffold.",
        mechanical_testing_reported="no / not applicable in abstract",
        mechanical_metric_details="Not applicable; no mechanical testing reported.",
        biological_testing_reported="yes",
        biological_metric_details="Morphology and culture pattern of DPSCs and LSCs grown in limbal stem cell media were similar; PCR showed stem cell markers were highly expressed in LSCs compared with DPSCs regardless of medium/scaffold; despite low transcript-level marker expression in DPSCs, immunocytochemistry and western blot showed relatively high functional protein-level expression of stem cell and corneal differentiation markers in DPSCs, indicating potential as limbal stem cells in the appropriate microenvironment.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="not applicable (in vitro characterization only)",
        main_outcomes="Human dental pulp stem cells (DPSCs) cultured in limbal stem cell media showed morphology and culture patterns similar to native limbal stem cells; although transcript-level stem cell marker expression (PCR) was lower in DPSCs than LSCs, protein-level expression (immunocytochemistry, western blot) of stem cell and corneal differentiation markers was comparatively high in DPSCs, supporting their potential as an autologous or allogeneic alternative cell source for treating bilateral limbal stem cell deficiency where no residual native limbal stem cells are available.",
        main_limitations="Purely in vitro characterization with no in vivo/animal transplantation or functional corneal repair data; no defined scaffold/biomaterial architecture described; discrepancy between low transcript-level and higher protein-level marker expression not mechanistically explained; no quantitative optical or mechanical data (not applicable to this cell-characterization study); sample size and statistical detail not given in the retrieved abstract.",
        translational_readiness_level="early preclinical (in vitro cell characterization only)",
        benchmarking_relevance="medium",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Molecular Medicine Reports (Spandidos), DOI 10.3892/mmr.2019.10691, 2019 -- Spandidos hybrid/subscription journal; open-access status of this specific article not confirmed this run; abstract-level extraction only. Relevant as a cell-source alternative (non-scaffold) study for bilateral LSCD where autologous limbal biopsy is not possible; flag for the review as a cell-biology comparator rather than a biomaterial-fabrication benchmarking entry.",
    ),
    "PUBMED_0832": dict(
        extraction_status="completed",
        study_type="clinical study (prospective randomized controlled trial, n=50 eyes) of autologous tissue-engineered oral mucosal vs. conjunctival epithelial grafts on amniotic membrane",
        target_layer_final="epithelium_limbus",
        biomaterial_category="cultivated autologous epithelial cell-sheet graft on human amniotic membrane carrier",
        specific_materials="two ex vivo tissue-engineered constructs compared head-to-head: Cultivated Oral Mucosal Epithelial Transplantation (COMET) and Conjunctival Cultivated Epithelial Transplantation (CCET), both autologous epithelial cell sheets expanded on human amniotic membrane",
        fabrication_method="autologous oral mucosal or conjunctival biopsy tissue harvested from each patient; epithelial cells expanded ex vivo by tissue engineering onto human amniotic membrane substrate to form COMET or CCET grafts; grafts surgically transplanted for ocular surface reconstruction in a prospective RCT (n=50 patients/eyes, 25 per arm; registered with CTRI [REF/2018/10/021791] and ISRCTN [45780], IEC-approved) in patients with bilateral ocular surface disease due to Stevens-Johnson Syndrome or chemical injury; standardized pre-/post-operative medication protocol applied to all patients",
        scaffold_architecture="human amniotic membrane substrate carrying a cultivated autologous epithelial cell sheet (oral mucosal or conjunctival origin)",
        cell_type_used="autologous oral mucosal epithelial cells (COMET arm) or autologous conjunctival epithelial cells (CCET arm)",
        cell_source="human, autologous (patient's own oral mucosa or bulbar conjunctiva, ex vivo expanded)",
        growth_factors_or_bioactive_agents="not specified in the retrieved abstract beyond a standardized pre-/post-operative medication protocol; no scaffold-incorporated bioactive agent described",
        optical_transparency_reported="partial",
        optical_metric_details="Corneal clarity was assessed as a clinical outcome measure at baseline, day 1, 1 week, 2 weeks, 1 month, 2 months, 3 months, and 6 months, but the retrieved abstract text is truncated before reporting the final numeric corneal-clarity comparison between arms.",
        mechanical_testing_reported="no / not applicable (clinical trial; no bench-level mechanical testing reported)",
        mechanical_metric_details="Not applicable; this is a clinical trial of surgically transplanted autologous grafts, not a bench mechanical characterization study.",
        biological_testing_reported="yes",
        biological_metric_details="Prospective RCT, n=50 patients/eyes (25 COMET, 25 CCET); mean ages 29 +/- 15.86 years (COMET) and 26.36 +/- 10.85 years (CCET), age range 12-65 years; outcomes assessed at baseline, day 1, 1 week, 2 weeks, 1 month, 2 months, 3 months, and 6 months, including patient comfort, best corrected visual acuity (BCVA), ocular surface status, and corneal clarity; efficacy measured via improvement in vision, reduction in vascularization, symblepharon, and corneal clarity (retrieved abstract text truncated before final comparative statistics between COMET and CCET arms were given).",
        in_vitro_model="no",
        ex_vivo_model="yes",
        animal_model="no",
        clinical_evidence="yes",
        follow_up_duration="6 months (assessments at baseline, day 1, 1 week, 2 weeks, 1 month, 2 months, 3 months, and 6 months)",
        main_outcomes="A prospective, registered randomized controlled trial (n=50 eyes, 25 per arm) compared two autologous ex vivo tissue-engineered epithelial grafts on human amniotic membrane -- cultivated oral mucosal epithelial transplantation (COMET) and conjunctival cultivated epithelial transplantation (CCET) -- for ocular surface reconstruction in bilateral ocular surface disease due to Stevens-Johnson Syndrome or chemical injury, assessing patient comfort, BCVA, ocular surface status, and corneal clarity over 6 months; the retrieved abstract text was truncated before the final comparative efficacy statistics between the two arms were reported.",
        main_limitations="Retrieved abstract text is truncated before the RESULTS section's comparative statistics, so which construct (COMET vs. CCET) performed better, and by how much, could not be extracted; relatively small per-arm sample size (n=25 each); single-registry (India) trial; longer-term (beyond 6-month) outcomes not available in the retrieved text.",
        translational_readiness_level="clinical (prospective randomized controlled clinical trial, n=50 eyes, registered)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "BMC Biotechnology (BMC series), DOI 10.1186/s12896-024-00876-z, 2024 -- BMC Biotechnology is a fully open-access (gold OA) journal; full-text fetch not attempted this run, abstract-level extraction used, and the locally stored abstract text is itself truncated mid-RESULTS. Rare clinical-trial-level (RCT) evidence among Tier 1 records for epithelium/limbus tissue-engineered grafts -- high value for the review's translational-readiness spectrum; recommend a full-text follow-up pass (via the actual paper, not abstract) to capture the final comparative COMET-vs-CCET statistics if a future run has broader fetch access.",
    ),
    "PUBMED_0322": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / decellularized xenogeneic scaffold study with in vitro stem-cell reseeding (no in vivo evaluation)",
        target_layer_final="endothelium",
        biomaterial_category="decellularized xenogeneic (porcine) Descemet stripping scaffold reseeded with stem-cell-derived corneal endothelial cells",
        specific_materials="ultra-thin decellularized porcine Descemet stripping (DS) scaffold reseeded with corneal endothelial cell lines or induced pluripotent stem cell (iPSC)-derived corneal endothelial cells (iCECs)",
        fabrication_method="protocol optimized to prepare an ultra-thin, decellularized DS scaffold from porcine cornea; a drying method applied to reduce graft rolling and edema and increase transparency during culture; scaffold reseeded with corneal endothelial cell lines or iCECs and cultured for 7 days",
        scaffold_architecture="ultra-thin, decellularized, dried Descemet stripping (DS) scaffold derived from porcine cornea, retaining the collagen matrix with porcine-derived cells and xenogenic antigens removed",
        cell_type_used="corneal endothelial cell lines and induced pluripotent stem cell (iPSC)-derived corneal endothelial cells (iCECs)",
        cell_source="not fully specified in the retrieved abstract; iCECs are iPSC-derived, species/donor origin of iPSCs and the comparator corneal endothelial cell line not stated",
        growth_factors_or_bioactive_agents="none reported; the key engineering intervention is the decellularization/drying protocol rather than an added bioactive factor",
        optical_transparency_reported="yes",
        optical_metric_details="Decellularized DS layers showed over 90% transparency compared with control; the drying method further reduced graft rolling/edema and increased transparency during culture (no single combined numeric transmittance value beyond \">90%\" given in the retrieved abstract).",
        mechanical_testing_reported="unclear / not reported in abstract",
        mechanical_metric_details="Graft rolling and edema behavior were discussed qualitatively (reduced by the drying method); no numeric tensile/elastic modulus values reported in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="Porcine-derived cells and xenogenic antigens disappeared after decellularization while the collagen matrix was retained; reseeded corneal endothelial cell lines/iCECs were evenly distributed over the graft, and most cells survived after 7 days of culture.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="7 days (in vitro reseeding culture period)",
        main_outcomes="An ultra-thin, decellularized porcine Descemet stripping (DS) scaffold, produced with a drying protocol that reduced graft rolling/edema and increased transparency, achieved over 90% light transparency versus control while retaining the native collagen matrix and clearing porcine-derived cells/xenoantigens; reseeded with corneal endothelial cell lines or iPSC-derived corneal endothelial cells (iCECs), the scaffold supported even cell distribution and survival of most cells over 7 days of culture, supporting the feasibility of this xenogeneic scaffold plus stem-cell-derived cell combination as a bio-engineered corneal endothelial graft precursor, with the authors explicitly noting future clinical studies are warranted.",
        main_limitations="No in vivo or ex vivo functional transplantation data reported despite the tissue-engineering goal (explicitly identified by the authors as future work); no mechanical/biomechanical testing reported; cell survival described only qualitatively (\"most survived\") without a quantitative viability percentage; species/origin of the iCECs and comparator corneal endothelial cell line not detailed in the retrieved abstract.",
        translational_readiness_level="early preclinical (in vitro scaffold reseeding only, no animal or clinical evidence)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Experimental Eye Research (Elsevier), DOI 10.1016/j.exer.2020.108192, 2020 -- Elsevier hybrid/subscription journal; open-access status of this specific article not confirmed this run; abstract-level extraction only. Explicit >90% transparency figure is valuable for the review's optical benchmarking table; combines a decellularized xenogeneic scaffold with iPSC-derived (rather than donor-derived) corneal endothelial cells, a useful comparator to donor-cell-based endothelium constructs elsewhere in the corpus.",
    ),
    "PUBMED_0378": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / micropatterned synthetic hydrogel substrate study (in vitro only, bovine corneal endothelial cells)",
        target_layer_final="endothelium",
        biomaterial_category="micropatterned synthetic polymer (polyacrylamide) cell-culture substrate, biomimetic Descemet's membrane surrogate",
        specific_materials="polyacrylamide (PA) hydrogel substrates, microfabricated with hexagonal surface topography, surface-modified with Collagen IV (Col IV)",
        fabrication_method="PA hydrogels prepared in two micropatterned designs: a small pattern with physiologically relevant hexagon density (~2000 hexagons/mm^2) and a large, sparsely populated pattern (~400 hexagons/mm^2); substrates engineered with an elastic modulus similar to native Descemet's membrane (~50 kPa) and surface-functionalized with Collagen IV to mimic native DM biochemical content; bovine corneal endothelial cells seeded on small-patterned, large-patterned, and flat (unpatterned) substrate groups and behavior compared",
        scaffold_architecture="2D micropatterned (hexagonal topography) polyacrylamide hydrogel substrate, elastic-modulus-matched (~50 kPa) to native Descemet's membrane, Collagen IV-functionalized",
        cell_type_used="bovine corneal endothelial cells",
        cell_source="bovine (primary vs. cell-line source not specified in the retrieved abstract)",
        growth_factors_or_bioactive_agents="Collagen IV surface coating used as a biochemical/adhesion cue rather than a soluble growth factor",
        optical_transparency_reported="no / not reported in abstract",
        optical_metric_details="No optical transparency/transmittance data reported in the retrieved abstract.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="PA hydrogel substrates were engineered with an elastic modulus similar to native Descemet's membrane (~50 kPa); two hexagon-pattern densities tested (~2000 hexagons/mm^2 small pattern vs. ~400 hexagons/mm^2 large pattern); no separate numeric modulus values given per pattern beyond the ~50 kPa DM-mimetic design target.",
        biological_testing_reported="yes",
        biological_metric_details="Bovine corneal endothelial cell proliferation on small-patterned substrates was significantly higher than on large-patterned substrates (P=0.0004); small-patterned substrates produced a significantly more densely populated monolayer than flat substrates (P=0.001) and large-patterned substrates (P<0.0001).",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="not applicable / not specified (in vitro substrate characterization study only)",
        main_outcomes="Polyacrylamide hydrogel substrates microfabricated with a hexagonal topography inspired by native corneal endothelial cell dimensions, tuned to an elastic modulus similar to native Descemet's membrane (~50 kPa) and functionalized with Collagen IV, significantly augmented bovine corneal endothelial cell monolayer formation: physiologically relevant small-pattern hexagon density (~2000 hexagons/mm^2) produced significantly higher proliferation (P=0.0004) and a significantly more densely populated monolayer than both flat (P=0.001) and sparsely patterned large-hexagon (P<0.0001) substrates, demonstrating that bioinspired surface topography can be used to engineer corneal endothelial cell substrates with desired cell density in vitro.",
        main_limitations="Bovine (not human) corneal endothelial cells used; purely in vitro substrate characterization, with no ex vivo or in vivo transplantation/graft functional testing; no optical transparency data reported despite this being a candidate Descemet's-membrane-mimetic biomaterial; specific numeric elastic modulus per hexagon pattern not separately reported beyond the ~50 kPa overall design target.",
        translational_readiness_level="early preclinical (in vitro only, no animal or clinical evidence)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Journal of Tissue Engineering and Regenerative Medicine (Wiley), DOI 10.1002/term.3173, 2021 -- Wiley hybrid/subscription journal; open-access status of this specific article not confirmed this run; abstract-level extraction only. Mechanically- and topographically-mimetic Descemet's membrane substrate design with quantitative p-value-backed proliferation/monolayer-density comparisons -- useful comparator for the review's synthetic (non-decellularized) endothelium substrate benchmarking entries.",
    ),
    "PUBMED_0531": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / composite polymer-ECM carrier study with in vitro, ex vivo, and in vivo evaluation (rabbit anterior chamber transplantation, 8-week follow-up)",
        target_layer_final="endothelium",
        biomaterial_category="synthetic-natural hybrid composite carrier (biodegradable polymer coupled with decellularized mesenchymal-stem-cell-derived extracellular matrix)",
        specific_materials="ECM-PLCL: poly(lactide-co-caprolactone) (PLCL) coupled with decellularized extracellular matrix (UMDM) derived from in vitro cultured human umbilical cord blood-derived mesenchymal stem cells (MSCs)",
        fabrication_method="PLCL solution poured onto decellularized ECM (UMDM) derived from in vitro cultured umbilical cord blood-MSCs; once fully dried, the composite ECM-PLCL membrane was peeled off the substrate; surface characterized by atomic force microscopy (roughness, surface charge); human corneal endothelial cell line (B4G12) and primary rabbit corneal endothelial cells (CECs) seeded onto the carrier; a simulation engraftment test performed into decellularized porcine corneal tissue; the carrier transplanted into the anterior chamber of rabbit eyes and assessed after 8 weeks",
        scaffold_architecture="20 micrometer-thick, transparent, rough (54.0 +/- 4.50 nm), positively surface-charged (65.2 +/- 57.8 mV) ECM-PLCL composite membrane carrier, rich in fibronectin and collagen type IV",
        cell_type_used="human corneal endothelial cell line (B4G12) and primary rabbit corneal endothelial cells",
        cell_source="human (B4G12 corneal endothelial cell line) and rabbit (primary corneal endothelial cells); underlying ECM derived from human umbilical cord blood-derived mesenchymal stem cells",
        growth_factors_or_bioactive_agents="no exogenous soluble growth factor added; the decellularized MSC-derived ECM (rich in fibronectin and collagen type IV) provides the bioactive/adhesive cues",
        optical_transparency_reported="yes",
        optical_metric_details="The 20 micrometer-thick ECM-PLCL carrier was reported as transparent (qualitative finding); no single numeric light-transmittance percentage given in the retrieved abstract.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Surface roughness 54.0 +/- 4.50 nm and surface charge +65.2 +/- 57.8 mV measured via atomic force microscopy; carrier thickness 20 micrometers; no bulk tensile/elastic modulus values given in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="Human CECs (B4G12) on ECM-PLCL showed good cell attachment with a cell density similar to normal cornea and maintained cell phenotype with well-formed cell-cell junctions (ZO-1, N-cadherin) at 14 days, in contrast to an FNC-coated PLCL positive control; the function-related marker Na+/K+-ATPase was confirmed via western blot and immunofluorescence; primary rabbit CECs showed normal shape and expressed structural/functional proteins on ECM-PLCL; a simulation engraftment test into decellularized porcine corneal tissue showed a high engraftment level and cell viability; in vivo transplantation into the rabbit anterior chamber for 8 weeks maintained normal cornea properties.",
        in_vitro_model="yes",
        ex_vivo_model="yes",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="14 days (in vitro phenotype/cell-junction maintenance); 8 weeks (in vivo rabbit anterior chamber transplantation)",
        main_outcomes="A transparent, 20 micrometer-thick composite carrier (ECM-PLCL), formed by coupling biodegradable PLCL with decellularized ECM from umbilical-cord-blood-derived mesenchymal stem cells, was rough (54.0 +/- 4.50 nm) and positively charged (65.2 +/- 57.8 mV) with retained fibronectin/collagen IV content; it supported good attachment, normal cell density, and stable cell-cell junction phenotype (ZO-1, N-cadherin) of human corneal endothelial cells (B4G12) at 14 days, supported normal rabbit primary CEC morphology and marker expression, achieved high engraftment and viability in a simulated decellularized porcine cornea engraftment test, and maintained normal cornea properties after 8 weeks of in vivo transplantation into the rabbit anterior chamber -- positioning ECM-PLCL as a promising corneal endothelium graft carrier with an ECM-rich microenvironment for CECs.",
        main_limitations="No numeric bulk mechanical (tensile/elastic modulus) values or light-transmittance percentage given in the retrieved abstract; \"normal cornea properties\" maintained at 8 weeks is not further quantified (e.g., no corneal thickness or endothelial cell density numbers given); rabbit (not primate/human) in vivo model; sample size for the in vivo transplantation arm not specified.",
        translational_readiness_level="preclinical (animal model, rabbit, 8-week in vivo follow-up)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "ACS Applied Materials & Interfaces (ACS), DOI 10.1021/acsami.2c01709, 2022 -- ACS hybrid/subscription journal; open-access status of this specific article not confirmed this run; abstract-level extraction only. Rich AFM-based surface-characterization dataset (roughness, surface charge) plus a full in vitro/ex vivo/in vivo evaluation chain culminating in an 8-week functional in vivo endpoint; MSC-derived-ECM/synthetic-polymer hybrid approach is a useful comparator to the purely decellularized-tissue carriers elsewhere in this batch (e.g., PUBMED_0171, PUBMED_0322).",
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

OA_IDS = {"PUBMED_0171", "PUBMED_0832"}
SUBSCRIPTION_IDS = {"PUBMED_1015", "PUBMED_0081", "PUBMED_0202", "PUBMED_0322", "PUBMED_0378", "PUBMED_0531"}

for sid in EXTRACTIONS:
    if sid not in tby_id:
        print("WARNING missing in tracker:", sid)
        continue
    update = TRACKER_UPDATE_OA if sid in OA_IDS else TRACKER_UPDATE_SUBSCRIPTION
    tby_id[sid].update(update)

with tracker_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=tfieldnames)
    w.writeheader()
    w.writerows(trows)

print("Tracker updated for:", list(EXTRACTIONS.keys()))
