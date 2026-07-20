"""
Tier 1 extraction batch 12 (2026-07-20, scheduled run continuation).

Retrieval route note: as in batches 3-11, a direct web_fetch to the Europe PMC
REST API (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:<pmid>&format=json&resultType=core)
was not attempted this run -- every prior run from batch 3 through batch 11
has confirmed this fails with "URL not in provenance set" (the sandboxed
web_fetch tool only allows fetching URLs that already appeared in a user
message, a prior web_fetch result, or a WebSearch result; this unattended
scheduled run has no user available to authorize a new URL, and a WebSearch
for the exact target URL does not itself return that URL verbatim). Per the
task instructions, this structural block was not re-attempted this run.

Extraction for this batch was built from the complete, untruncated abstract
text already stored locally in
screening/full_text/pubmed_tier1_tier2_extraction_plan.csv (verified
PubMed/journal abstracts captured during the original screening pass), with
open-access status assessed from known journal/publisher policy: BioImpacts
(BI) and MDPI journals (Pharmaceutics, Polymers) are fully open-access (gold
OA); Journal of Biomedical Materials Research Part A (Wiley) is normally
hybrid but this specific article's abstract text carries a "(c) 2018 The
Authors ... published by Wiley Periodicals, Inc." open-access copyright
notice, indicating this particular article was published open access;
Tissue Engineering and Regenerative Medicine (Springer), Cell and Tissue
Research (Springer), Biofabrication (IOP), and Acta Biomaterialia (Elsevier)
are hybrid/subscription titles -- open-access status of these specific
articles not individually confirmed this run. This is noted per-record in
extraction_notes.

This batch (8 records):
- PUBMED_0120 (PMID 30548137) - in situ self-crosslinking alginate-chitosan hydrogel (ACH) for LSC transplantation, in vitro + in vivo rabbit alkali-burn model.
- PUBMED_0241 (PMID 31988856) - electrospun PCL vs. PCL/gelatin nanofibrous scaffolds for LESC propagation, in vitro + in vivo animal alkaline-injury model.
- PUBMED_0300 (PMID 32572811) - peripheral blood-derived mononuclear cells (PBMNCs) as alternative corneal epithelial cell source, in vitro + ex vivo rabbit eye cell-sheet transfer.
- PUBMED_0447 (PMID 34302219) - clinical-grade, carrier-free cultured autologous oral mucosal epithelial cell sheet (cG-CAOMECS), rabbit in vitro GMP manufacturing proof-of-concept.
- PUBMED_0450 (PMID 34330126) - DLP bioprinted dual-ECM (GelMA/HAGM) hydrogel scaffolds for active vs. quiescent LSC phenotype, in vitro rabbit + human LSCs.
- PUBMED_0485 (PMID 34684011) - decellularized porcine corneal limbus scaffold recellularized with SIRC line or hADSCs, in vitro/ex vivo.
- PUBMED_0623 (PMID 36708851) - self-assembling fibronectin-mimetic (PHSRN) peptide supramolecular hydrogel, in vitro + in vivo animal corneal scrape model.
- PUBMED_0632 (PMID 36772078) - melt electrospun PLA modified with silk fibroin or gelatin for LSC adhesion, in vitro, three human donors.
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
    "documented in batches 3-11 and was not re-attempted this run. "
)

EXTRACTIONS = {
    "PUBMED_0120": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / in situ self-crosslinking hydrogel study with in vitro and in vivo evaluation (rabbit alkali-burn corneal model)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="natural polysaccharide-based in situ self-crosslinking hydrogel (alginate-chitosan)",
        specific_materials="carboxymethyl chitosan crosslinked with sodium alginate dialdehyde (SAD, periodate-oxidized sodium alginate) via Schiff's base formation between aldehyde and amino groups; no exogenous chemical crosslinker used",
        fabrication_method="SAD prepared by periodate-mediated oxidation of sodium alginate; carboxymethyl chitosan rapidly crosslinked with SAD via Schiff's base reaction, forming an in situ self-crosslinking hydrogel (ACH) directly on the wound surface; gelation time, transmittance, microscopic structure, equilibrium swelling, cytotoxicity, histocompatibility, and degradability characterized; rabbit primary LSCs encapsulated in the hydrogel and transplanted to alkali burn wounds in vivo; reconstruction evaluated by visual observation, slit lamp, histology, and immunofluorescence",
        scaffold_architecture="injectable, in situ-forming hydrogel (ACH) that self-crosslinks directly on the wound surface without added chemical crosslinkers, encapsulating LSCs",
        cell_type_used="rabbit primary limbal stem cells (LSCs)",
        cell_source="rabbit, primary",
        growth_factors_or_bioactive_agents="none exogenous; the alginate-chitosan blend itself is the bioactive/adhesive scaffold",
        optical_transparency_reported="yes",
        optical_metric_details="The in situ hydrogel was reported as highly transparent, and light transmittance was measured as part of the physicochemical characterization; no specific numeric transmittance percentage is given in the retrieved abstract.",
        mechanical_testing_reported="partial",
        mechanical_metric_details="Gelation time, equilibrium swelling ratio, and degradability were assessed as structural/physicochemical characterization, but no numeric elastic modulus or tensile strength values are reported in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="The hydrogel was biocompatible with low cytotoxicity and good histocompatibility; LSCs cultured in vitro expressed the stem marker p63 but lacked the differentiated epithelial markers cytokeratin 3 and 12; in vivo, the LSC-encapsulated hydrogel formed quickly on alkali-burn wounds and significantly improved epithelial reconstruction.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract",
        main_outcomes="A novel in situ self-crosslinking alginate-chitosan hydrogel (ACH), formed via Schiff base chemistry without exogenous crosslinkers, was highly transparent, rapidly gelling, biocompatible, and low-cytotoxicity. LSCs encapsulated in the hydrogel retained stem marker p63 expression in vitro without premature differentiation (CK3/CK12 negative) and, when applied to alkali burn corneal wounds in rabbits, significantly improved epithelial reconstruction, supporting ACH as a rapid, effective in situ LSC-delivery system for corneal wound healing.",
        main_limitations="No numeric mechanical (modulus) or transmittance values reported; follow-up duration not specified numerically; rabbit model only, with no clinical evidence; long-term hydrogel degradation/integration and functional visual outcomes not assessed.",
        translational_readiness_level="preclinical (animal model, rabbit)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Journal of Biomedical Materials Research Part A (Wiley), DOI 10.1002/jbm.a.36589, 2019 -- Wiley is normally a hybrid journal, but this article's abstract text carries a '(c) 2018 The Authors ... published by Wiley Periodicals, Inc.' open-access copyright notice, indicating this specific article was published open access; full-text fetch not attempted this run, abstract-level extraction used. Rapid in situ self-crosslinking (no exogenous crosslinker) hydrogel design is a useful comparator for the review's injectable/in-situ-forming scaffold benchmarking entries.",
    ),
    "PUBMED_0241": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / comparative electrospun nanofibrous scaffold study with in vivo evaluation (animal alkaline corneal injury model)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="synthetic/natural polymer blend electrospun nanofibrous scaffold (polycaprolactone vs. polycaprolactone/gelatin)",
        specific_materials="electrospun polycaprolactone (PCL) nanofibers and PCL/gelatin (PCL/Gel) blend nanofibers at mass ratios 70:30 and 50:50",
        fabrication_method="PCL and PCL/Gel nanofibrous scaffolds fabricated by electrospinning at two mass ratios (70:30, 50:50); human LESCs cultured on each scaffold to assess proliferation and attachment; scaffolds evaluated in an animal model of alkaline corneal injury for epithelial regeneration, ease of use, vascularization/inflammation, and final corneal transparency",
        scaffold_architecture="electrospun nanofibrous mat (PCL alone or PCL/gelatin blend)",
        cell_type_used="human limbal epithelial stem cells (LESCs)",
        cell_source="human, primary",
        growth_factors_or_bioactive_agents="none exogenous; the gelatin blend component provides ECM-mimetic adhesive cues in the PCL/Gel group",
        optical_transparency_reported="yes",
        optical_metric_details="Final corneal transparency was assessed qualitatively as an outcome criterion in the animal model; no specific numeric transmittance value is given in the retrieved abstract.",
        mechanical_testing_reported="unclear / not reported in abstract",
        mechanical_metric_details="No numeric mechanical (modulus/tensile) data reported; scaffold 'ease of use' was assessed qualitatively rather than via bench mechanical testing.",
        biological_testing_reported="yes",
        biological_metric_details="PCL was more suitable than PCL/Gel for LESC adherence, induction of epithelial morphology, and proliferation; histopathology of transplanted animal corneas showed similar epithelial regeneration between PCL and PCL/Gel groups, but vascularization and inflammation were significantly lower in the PCL group.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract",
        main_outcomes="Comparing electrospun PCL and PCL/gelatin nanofibrous scaffolds for LESC transplantation, PCL alone outperformed PCL/Gel for cell adherence, epithelial morphology, and proliferation; in an animal alkaline-injury model, epithelial regeneration was similar between groups, but PCL showed significantly lower vascularization and inflammation than PCL/Gel, indicating PCL alone as the preferred carrier for LESC-based corneal cell therapy.",
        main_limitations="No numeric mechanical or transmittance data reported; the mechanism behind PCL/Gel's higher inflammation/vascularization is not elucidated; animal model only, with no clinical evidence; sample sizes not specified in the abstract.",
        translational_readiness_level="preclinical (animal model)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "BioImpacts (BI), DOI 10.15171/bi.2020.06, 2020 -- BioImpacts is a fully open-access (gold OA) journal; full text freely available; full-text fetch not attempted this run, abstract-level extraction used. Direct head-to-head PCL vs. PCL/gelatin comparison with in vivo inflammation/vascularization readouts is a useful comparator for the review's synthetic-vs-blended-polymer scaffold benchmarking table.",
    ),
    "PUBMED_0300": dict(
        extraction_status="completed",
        study_type="experimental biomaterial-free cell-source study (in vitro, with ex vivo cell-sheet transfer demonstration)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="cell-source alternative (peripheral blood-derived mesenchymal-like cells) engineered into a cell sheet using a thermo-responsive polymer carrier, not a permanent scaffold",
        specific_materials="rabbit peripheral blood-derived mononuclear cells (PBMNCs) differentiated to corneal epithelial lineage; in-house developed thermo-responsive polymer used to fabricate a transferable cell sheet",
        fabrication_method="rabbit PBMNCs isolated via density gradient centrifugation; evaluated for mesenchymal stem cell-like properties/stemness; differentiated to corneal epithelial lineage using rabbit limbal explant conditioned media, confirmed via immunocytochemistry and gene expression (CK3/12); differentiated PBMNCs engineered into a cell sheet using an in-house thermo-responsive polymer; cell sheet transfer demonstrated on an ex vivo excised rabbit eye",
        scaffold_architecture="thermo-responsive polymer-supported, harvestable cell sheet (carrier-free once detached and transferred)",
        cell_type_used="peripheral blood-derived mononuclear cells (PBMNCs), differentiated toward corneal epithelial lineage",
        cell_source="rabbit, autologous/peripheral-blood-derived (minimally invasive collection)",
        growth_factors_or_bioactive_agents="rabbit limbal explant conditioned media, used to drive corneal epithelial lineage differentiation",
        optical_transparency_reported="no / not reported in abstract",
        optical_metric_details="Not reported; no optical transmittance/transparency data given in the retrieved abstract.",
        mechanical_testing_reported="no / not applicable in abstract",
        mechanical_metric_details="Not applicable; no mechanical testing reported in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="PBMNCs demonstrated mesenchymal stem cell-like properties; corneal epithelial lineage commitment confirmed by positive CK3/12 marker expression; differentiated PBMNCs formed a functional in vitro cell sheet that was successfully transferred onto an ex vivo excised rabbit eye.",
        in_vitro_model="yes",
        ex_vivo_model="yes",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="not applicable / not specified (short-term in vitro/ex vivo feasibility study)",
        main_outcomes="Rabbit peripheral blood-derived mononuclear cells (PBMNCs), an easily and minimally invasively collected alternative to limbal stem cells, showed mesenchymal stem cell-like properties and were successfully differentiated to a corneal epithelial lineage (CK3/12-positive) using limbal explant conditioned media; the differentiated cells were engineered into a transferable cell sheet using a thermo-responsive polymer and successfully transferred onto an ex vivo excised rabbit eye, supporting PBMNCs as a feasible autologous alternative cell source for corneal epithelial reconstruction, particularly relevant for bilateral LSCD patients.",
        main_limitations="Purely in vitro/ex vivo feasibility study with no in vivo (live animal) transplantation or long-term functional/clinical evaluation; no optical or mechanical characterization of the cell sheet reported; sample sizes not specified in the abstract.",
        translational_readiness_level="early preclinical (in vitro / ex vivo feasibility)",
        benchmarking_relevance="medium",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Tissue Engineering and Regenerative Medicine (Springer), DOI 10.1007/s13770-020-00273-5, 2020 -- Springer hybrid/subscription journal; open-access status of this specific article not confirmed this run; abstract-level extraction only. Notable as a biomaterial-free/thermo-responsive-carrier alternative cell-source study (peripheral blood vs. limbal stem cells), useful comparator for the review's cell-source benchmarking discussion alongside PUBMED_0010 (carrier-free oral mucosal cell sheet).",
    ),
    "PUBMED_0447": dict(
        extraction_status="completed",
        study_type="experimental biomaterial-free clinical-grade cell manufacturing study (in vitro, GMP-compliant process development; rabbit proof-of-concept for future clinical translation)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="biomaterial-free (carrier-free) clinical-grade cultured autologous oral mucosal epithelial cell sheet (cG-CAOMECS), grown on a temporary cGMP-certified culture surface rather than a permanent scaffold",
        specific_materials="rabbit buccal oral mucosal epithelial cells cultured on a cGMP-certified cell culture surface coated with GMP-grade extracellular matrix; clinical-grade KaFa(TM) medium used for expansion; collagenase used for cell-sheet detachment/harvest",
        fabrication_method="oral mucosal epithelial cells isolated from rabbit buccal biopsy; seeded on a cGMP-certified culture surface coated with GMP-grade ECM; expanded in a chemically defined, clinical-grade KaFa(TM) medium; cell sheet detached/harvested via collagenase treatment; live cell imaging and morphological analysis used to monitor growth; immunostaining and western blot performed for deltaNp63, K3/K12, E-cadherin, beta-catenin, Cnx43, and integrin-beta1/beta4",
        scaffold_architecture="carrier/scaffold-free multilayered epithelial cell sheet grown on a temporary GMP-grade ECM-coated culture surface, harvested as a free-standing sheet",
        cell_type_used="rabbit oral mucosal epithelial cells (autologous, buccal biopsy-derived)",
        cell_source="rabbit, autologous (buccal biopsy)",
        growth_factors_or_bioactive_agents="clinical-grade, chemically defined KaFa(TM) expansion medium (specific composition not detailed in the abstract)",
        optical_transparency_reported="no / not reported in abstract",
        optical_metric_details="Not reported; this study focuses on cell-sheet manufacturing and marker expression rather than optical characterization.",
        mechanical_testing_reported="no / not applicable in abstract",
        mechanical_metric_details="Not applicable; no mechanical testing reported in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="Colony-forming units (CFUs) formed within the first 5 days; a basal monolayer cell sheet formed in less than 10 days; a multilayered epithelial cell sheet was harvested after 17-19 days; deltaNp63 was expressed in basal cells and K3/K12 in apical cells (corneal epithelial-like phenotype); E-cadherin, beta-catenin, and Cnx43 were expressed, indicating epithelial integrity; integrin-beta1 and beta4 expression confirmed collagenase harvesting did not adversely affect the cell sheet.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="17-19 days (in vitro culture/manufacturing timeline)",
        main_outcomes="A clinical-grade, GMP-compliant, chemically defined process (cG-CAOMECS) successfully produced a rabbit carrier-free multilayered oral mucosal epithelial cell sheet with corneal epithelial-like marker expression (deltaNp63 basal, K3/K12 apical) and preserved epithelial integrity (E-cadherin, beta-catenin, Cnx43) after collagenase harvesting, within a 17-19 day manufacturing timeline -- establishing a rabbit proof-of-concept manufacturing protocol intended to translate to FDA-compliant clinical-grade human CAOMECS production for bilateral limbal stem cell deficiency.",
        main_limitations="Rabbit (not human) proof-of-concept only, with no in vivo transplantation or functional/clinical outcome data in this abstract; no optical or mechanical characterization reported; scalability and batch-to-batch consistency of the clinical-grade process are not addressed.",
        translational_readiness_level="early preclinical (in vitro manufacturing proof-of-concept, designed for future clinical translation)",
        benchmarking_relevance="medium",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Cell and Tissue Research (Springer), DOI 10.1007/s00441-021-03507-7, 2021 -- Springer hybrid/subscription journal; open-access status of this specific article not confirmed this run; abstract-level extraction only. GMP/clinical-grade manufacturing process detail is a useful comparator for the review's translational-readiness benchmarking discussion, complementing PUBMED_0010's clinical-trial-stage carrier-free COMEC data.",
    ),
    "PUBMED_0450": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / 3D bioprinted hydrogel scaffold study (in vitro, primary rabbit and human LSC encapsulation)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="bioprinted dual extracellular-matrix-mimetic hydrogel scaffolds (GelMA and HAGM)",
        specific_materials="gelatin methacrylate (GelMA) and hyaluronic acid glycidyl methacrylate (HAGM) photocrosslinkable hydrogels",
        fabrication_method="digital light processing (DLP)-based bioprinting used to fabricate microscale hydrogel scaffolds from GelMA or HAGM encapsulating primary limbal stem/progenitor cells (LSCs); primary rabbit LSCs (rbLSCs) and primary human LSCs encapsulated and cultured; LSC phenotype (active vs. quiescent) assessed via immunocytochemistry and transcriptional analysis in each ECM scaffold type",
        scaffold_architecture="DLP-bioprinted microscale hydrogel scaffolds (GelMA or HAGM), forming a bioprinted dual-ECM 'Yin-Yang' model that supports both active and quiescent LSC phenotypes within different hydrogel chemistries",
        cell_type_used="primary limbal stem/progenitor cells (LSCs) -- rabbit (rbLSCs) and human",
        cell_source="rabbit (primary) and human (primary)",
        growth_factors_or_bioactive_agents="none exogenous; the GelMA vs. HAGM extracellular-matrix chemistry itself is the engineered variable driving LSC phenotype",
        optical_transparency_reported="unclear / not reported in abstract",
        optical_metric_details="No optical transparency/transmittance data reported in the retrieved abstract; characterization focused on cell viability and ECM-dependent phenotype (active vs. quiescent).",
        mechanical_testing_reported="unclear / not reported in abstract",
        mechanical_metric_details="No numeric mechanical (modulus) data reported in the retrieved abstract; DLP bioprinting resolution/microscale dimensions are described qualitatively as 'microscale' without specific numeric values given.",
        biological_testing_reported="yes",
        biological_metric_details="DLP-bioprinted GelMA and HAGM scaffolds supported viability of encapsulated primary rbLSCs in culture; immunocytochemistry and transcriptional analysis showed rbLSCs remained active (proliferative) in GelMA-based scaffolds but exhibited quiescence in HAGM-based scaffolds; primary human LSCs encapsulated in the same scaffold types showed consistent ECM-dependent active/quiescent status patterns.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract",
        main_outcomes="DLP-based bioprinting of GelMA and HAGM hydrogel scaffolds enabled high-throughput, microscale fabrication of ECM-mimetic constructs encapsulating primary LSCs; GelMA-based scaffolds maintained LSCs in an active/proliferative state while HAGM-based scaffolds induced quiescence, consistently across rabbit and human LSCs, establishing a novel bioprinted dual-ECM 'Yin-Yang' model that can support both active and quiescent LSC states -- providing a platform to study and potentially control LSC stemness/quiescence for regenerative therapy.",
        main_limitations="No optical transparency or mechanical (modulus) data reported; purely in vitro, with no ex vivo or in vivo/animal transplantation evaluation; the functional/therapeutic consequence of maintaining LSCs in active vs. quiescent states in vivo is not addressed in the abstract; sample sizes not specified.",
        translational_readiness_level="early preclinical (in vitro only)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Biofabrication (IOP Publishing), DOI 10.1088/1758-5090/ac1992, 2021 -- IOP is a hybrid/subscription-model journal; open-access status of this specific article not confirmed this run; abstract-level extraction only. Direct ECM-chemistry-dependent LSC active/quiescent phenotype comparison (GelMA vs. HAGM) via advanced DLP bioprinting is a valuable comparator for the review's scaffold-chemistry and stem-cell-phenotype benchmarking table.",
    ),
    "PUBMED_0485": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / decellularized-scaffold recellularization study (in vitro/ex vivo, porcine tissue-derived scaffold with two cell types)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="decellularized xenogeneic (porcine) corneal limbus extracellular matrix scaffold, recellularized with two different cell types",
        specific_materials="decellularized full-thickness and half-thickness porcine corneal limbus (four decellularization protocols tested, including 0.1% SDS); recellularized with the limbal epithelial cell line SIRC or human adipose-derived mesenchymal stem cells (hADSCs)",
        fabrication_method="four decellularization protocols applied to full-thickness and half-thickness porcine limbus; decellularization efficiency and ECM preservation (transparency, composition) compared; best-performing protocol (0.1% SDS on half-thickness limbus) selected; decellularized limbi recellularized with SIRC cell line or hADSCs; stratified epithelium formation assessed via limbal marker expression (p63, pancytokeratin, crystallin Z) at day 7 (SIRC) and days 14-21 (hADSCs); laminin and collagen IV basal lamina expression assessed at days 14 and 21; picrosirius red and alcian blue staining used to compare recellularized tissue with native control limbi",
        scaffold_architecture="decellularized porcine limbal extracellular matrix (half-thickness, 0.1% SDS-decellularized) recellularized to form a stratified epithelium",
        cell_type_used="limbal epithelial cell line (SIRC) and human adipose-derived mesenchymal stem cells (hADSCs)",
        cell_source="SIRC is an established rabbit corneal epithelial cell line; hADSCs are human, adipose-derived (autologous/allogeneic status not specified in abstract)",
        growth_factors_or_bioactive_agents="none exogenous reported beyond the decellularized ECM's native composition; hADSC induction toward limbal phenotype occurred over 14-21 days without stated exogenous factors",
        optical_transparency_reported="yes",
        optical_metric_details="Among the four decellularization protocols tested, 0.1% SDS applied to half-thickness limbus best preserved transparency and ECM composition (qualitative comparative finding); no specific numeric transmittance value is given in the retrieved abstract.",
        mechanical_testing_reported="no / not reported in abstract",
        mechanical_metric_details="No numeric mechanical (modulus/tensile) testing data reported in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="All four decellularization protocols achieved efficient decellularization; recellularization with SIRC generated a stratified epithelium expressing limbal markers p63, pancytokeratin, and crystallin Z from day 7; hADSCs achieved similar marker expression after 14-21 days of induction; laminin and collagen IV were detected at the basal lamina for both cell types at days 14 and 21; SIRC-recellularized tissue showed picrosirius red/alcian blue staining intensity comparable to native control limbi, while hADSC-containing limbi showed normal collagen staining intensity.",
        in_vitro_model="yes",
        ex_vivo_model="yes",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="up to 21 days (in vitro/ex vivo recellularization follow-up)",
        main_outcomes="Among four decellularization protocols tested on porcine corneal limbus, 0.1% SDS applied to half-thickness tissue best preserved transparency and ECM composition; recellularization with either the SIRC cell line (faster, by day 7) or human adipose-derived mesenchymal stem cells (slower, 14-21 days) generated a stratified epithelium expressing limbal markers (p63, pancytokeratin, crystallin Z) and appropriate basal lamina proteins (laminin, collagen IV), with staining characteristics resembling native limbus -- supporting decellularized porcine limbus as a promising biomimetic scaffold for limbal substitute generation using either a cell line or an easily accessible autologous-type stem cell source (hADSCs).",
        main_limitations="Preliminary/proof-of-concept study with no in vivo or clinical evaluation; no numeric transmittance or mechanical data reported; xenogeneic (porcine) scaffold source raises immunogenicity considerations not addressed in the abstract; SIRC is an immortalized cell line rather than primary human limbal cells, limiting direct clinical translatability of that arm.",
        translational_readiness_level="early preclinical (in vitro / ex vivo)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Pharmaceutics (MDPI), DOI 10.3390/pharmaceutics13101718, 2021 -- MDPI journals are fully open-access (gold OA); full text freely available; full-text fetch not attempted this run, abstract-level extraction used. Systematic decellularization-protocol comparison plus dual-cell-type recellularization (cell line vs. hADSC) is a valuable comparator for the review's decellularized-scaffold benchmarking entries alongside other xenogeneic ECM studies in the corpus.",
    ),
    "PUBMED_0623": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / self-assembling peptide supramolecular hydrogel study with in vitro and in vivo evaluation (animal corneal scrape model)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="self-assembling peptide-amphiphile supramolecular hydrogel (fibronectin-mimetic)",
        specific_materials="naphthalene-conjugated fibronectin-mimetic peptide amphiphiles (Nap-FPHRSN, Nap-FFPHSRN, Nap-FFFPHSRN) based on the PHSRN fibronectin-derived sequence; Nap-FFPHSRN identified as the optimized formulation",
        fabrication_method="self-assembled motifs (Nap-F, Nap-FF, Nap-FFF) conjugated to the fibronectin-mimetic peptide PHSRN and screened for self-assembly behavior and chemical stability against protease hydrolysis; Nap-FFPHSRN selected as optimal and self-assembled into a supramolecular hydrogel; in vitro assays assessed corneal epithelial cell migration (F-actin remodeling) and tight-junction protein ZO-1 expression; in vivo precorneal retention and ocular tolerance assessed after topical instillation; therapeutic effect evaluated in an animal corneal scrape model comparing once-daily Nap-FFPHSRN hydrogel against three-times-daily PHSRN or fibronectin",
        scaffold_architecture="injectable/topically applied self-assembling supramolecular peptide-amphiphile hydrogel (no solid scaffold; forms in situ upon self-assembly)",
        cell_type_used="corneal epithelial cells (in vitro migration/tight-junction assays); species not specified in the retrieved abstract",
        cell_source="not specified in the retrieved abstract",
        growth_factors_or_bioactive_agents="fibronectin-mimetic PHSRN peptide sequence itself is the bioactive component, mimicking fibronectin's cell-adhesion/migration-promoting activity",
        optical_transparency_reported="no / not reported in abstract",
        optical_metric_details="Not reported; the study characterizes self-assembly behavior, chemical stability, and biological activity rather than optical transparency.",
        mechanical_testing_reported="unclear / not reported in abstract",
        mechanical_metric_details="Chemical/proteolytic stability of the peptide amphiphiles was assessed (protease hydrolysis resistance), but no numeric bulk mechanical (modulus) testing values are reported in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="Nap-FFPHSRN self-assembly drastically improved chemical stability against protease hydrolysis versus unmodified PHSRN, with minimal loss of biological activity; the hydrogel increased corneal epithelial cell motility via F-actin remodeling and boosted tight-junction integrity via increased ZO-1 expression; in vivo, once-daily topical Nap-FFPHSRN provided extended precorneal retention with good ocular tolerance; in an animal corneal scrape model, once-daily Nap-FFPHSRN achieved a therapeutic effect for re-epithelialization equivalent to fibronectin dosed three times daily, and superior to PHSRN alone, with complete morphological and architectural recovery.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract (in vivo corneal scrape healing evaluated to complete morphological/architectural recovery; exact duration not given)",
        main_outcomes="Conjugating self-assembling motifs (Nap-F/FF/FFF) to a fibronectin-mimetic PHSRN peptide dramatically improved its chemical/proteolytic stability while preserving bioactivity; the optimized Nap-FFPHSRN self-assembled into a supramolecular hydrogel that promoted corneal epithelial cell migration (F-actin remodeling) and tight-junction integrity (ZO-1), provided extended precorneal retention and good ocular tolerance after topical instillation, and achieved complete morphological and architectural corneal re-epithelialization with once-daily dosing -- matching the efficacy of three-times-daily fibronectin and outperforming three-times-daily unmodified PHSRN, positioning this peptide hydrogel as a reduced-dosing-frequency biomimetic alternative to fibronectin eye drops for clinical corneal injury treatment.",
        main_limitations="No numeric optical or bulk mechanical (modulus) data reported; corneal epithelial cell species/source not specified for the in vitro assays; exact in vivo follow-up duration not given numerically; no human/clinical evidence yet, despite explicit clinical-translation framing in the abstract.",
        translational_readiness_level="preclinical (animal model)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Acta Biomaterialia (Elsevier), DOI 10.1016/j.actbio.2023.01.047, 2023 -- Elsevier hybrid/subscription journal; open-access status of this specific article not confirmed this run; abstract-level extraction only. Reduced-dosing-frequency, fibronectin-equivalent-efficacy peptide hydrogel is a strong comparator for the review's topical/injectable wound-healing biomaterial benchmarking table.",
    ),
    "PUBMED_0632": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / comparative melt-electrospun fibrous scaffold study (in vitro, three human LSC donors)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="synthetic/natural polymer blend melt-electrospun fibrous scaffold (polylactic acid modified with silk fibroin or gelatin)",
        specific_materials="melt electrospun polylactic acid (PLA), PLA modified with silk fibroin, and PLA modified with gelatin",
        fabrication_method="PLA fibrous scaffolds fabricated by melt electrospinning and modified with silk fibroin or gelatin; scaffold porosity, pore area, swelling percentage, and biodegradation rate characterized for each formulation; LSCs from three different human donors cultured on each scaffold; cell adhesion/localization visualized, cell viability (total number) determined, and p63/CK3 expression assessed by staining",
        scaffold_architecture="melt-electrospun microfibrous mat (PLA alone, PLA/silk fibroin, or PLA/gelatin), with cells adhering to individual microfiber surfaces (PLA, PLA/gelatin) or between microfibers (PLA/silk fibroin)",
        cell_type_used="limbal stem cells (LSCs) from three different human donors",
        cell_source="human, primary, three donors",
        growth_factors_or_bioactive_agents="none exogenous; silk fibroin and gelatin modifications provide ECM-mimetic/bioactive surface cues",
        optical_transparency_reported="no / not reported in abstract",
        optical_metric_details="Not reported; characterization focused on porosity, swelling, biodegradation, and cell viability/marker expression rather than optical transparency.",
        mechanical_testing_reported="partial",
        mechanical_metric_details="Scaffold porosity (with significantly larger pore area for PLA/gelatin), swelling percentage, and biodegradation rate were characterized and improved by both modifications versus unmodified PLA; no numeric elastic modulus or tensile strength values are reported in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="Both silk fibroin and gelatin modifications slightly increased PLA scaffold porosity (PLA/gelatin had significantly larger pore area) and improved swelling percentage and biodegradation rate versus unmodified PLA; LSCs attached to all three scaffold types, showing flattened conformations or 3D spheres/colonies; PLA/silk fibroin showed the most intense red fluorescence (cell-binding signal) and the highest viability at 98% of 2.9x10^6 LSCs, with >98% p63 and <20% CK3 expression, indicating maintained stemness with limited premature differentiation; all scaffolds were biocompatible.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract",
        main_outcomes="Melt-electrospun PLA scaffolds modified with silk fibroin or gelatin both improved porosity, swelling, and biodegradation versus unmodified PLA and supported adhesion of LSCs from three human donors; PLA/silk fibroin performed best, achieving 98% viability of 2.9x10^6 LSCs with >98% p63 and <20% CK3 expression (indicating strong maintenance of stem-cell phenotype with limited premature differentiation), supporting melt-electrospun PLA/silk fibroin as a promising bio-engineered scaffold alternative to human amniotic membrane for LSC transplantation.",
        main_limitations="No numeric mechanical (modulus) or optical transparency data reported; purely in vitro, with no ex vivo or in vivo/animal transplantation evaluation; only total cell number/viability reported quantitatively for PLA/silk fibroin, with less granular data given for PLA and PLA/gelatin groups; long-term functional outcome (transplantation efficacy) not assessed.",
        translational_readiness_level="early preclinical (in vitro only)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Polymers (MDPI), DOI 10.3390/polym15030777, 2023 -- MDPI journals are fully open-access (gold OA); full text freely available; full-text fetch not attempted this run, abstract-level extraction used. Multi-donor (n=3 human donors), multi-modification (silk fibroin vs. gelatin) melt-electrospun PLA comparison is a valuable comparator for the review's synthetic-fiber scaffold-modification benchmarking table, complementing PUBMED_0241 (electrospun PCL/PCL-gelatin) elsewhere in the corpus.",
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

TRACKER_UPDATE_ARTICLE_LEVEL_OA = dict(
    full_text_status="retrieved (abstract-level only)",
    pdf_available="yes (article-level open access per (c) The Authors copyright notice in abstract; journal itself is hybrid)",
    source_checked="local screening corpus abstract (screening/full_text/pubmed_tier1_tier2_extraction_plan.csv)",
    retrieval_date="2026-07-20",
    retrieval_notes="Europe PMC REST API fetch blocked by web_fetch provenance restriction in this unattended run; abstract taken from already-verified local screening corpus text. Journal is normally hybrid, but this article's abstract carries an explicit '(c) The Authors' open-access copyright notice.",
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

OA_IDS = {"PUBMED_0241", "PUBMED_0485", "PUBMED_0632"}
ARTICLE_LEVEL_OA_IDS = {"PUBMED_0120"}
SUBSCRIPTION_IDS = {"PUBMED_0300", "PUBMED_0447", "PUBMED_0450", "PUBMED_0623"}

for sid in EXTRACTIONS:
    if sid not in tby_id:
        print("WARNING missing in tracker:", sid)
        continue
    if sid in OA_IDS:
        update = TRACKER_UPDATE_OA
    elif sid in ARTICLE_LEVEL_OA_IDS:
        update = TRACKER_UPDATE_ARTICLE_LEVEL_OA
    else:
        update = TRACKER_UPDATE_SUBSCRIPTION
    tby_id[sid].update(update)

with tracker_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=tfieldnames)
    w.writeheader()
    w.writerows(trows)

print("Tracker updated for:", list(EXTRACTIONS.keys()))
