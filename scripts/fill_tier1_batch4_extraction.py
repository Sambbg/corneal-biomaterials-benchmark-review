"""
Tier 1 extraction batch 4 (2026-07-19, continued).

Retrieval route note: as in batch 3, the Europe PMC REST API JSON endpoint
(https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:<pmid>&format=json&resultType=core)
was NOT reachable in this run's sandboxed web_fetch tool -- it enforces a
"provenance set" restriction that blocks fetching any URL that has not
already appeared in a prior search/fetch result, and this unattended
scheduled run has no user available to authorize a new URL. Repeated
attempts (including after surfacing the base API URL and the PMID via
WebSearch first) were all rejected with "URL not in provenance set".

A WebSearch lookup was tried instead for PUBMED_0761 (PMID 38486306) and
successfully located open-access full text at PMC10941625 (Stem Cell
Research & Therapy), confirming OA/PMC status for that record; the deep
full-text HTML fetch (via web_fetch on the PMC page) returned ~88k
characters of markup, far too large to read for every record in the batch
within this run's context budget, so it was not repeated for the other 7
records. All 8 extractions in this batch are instead built from the
complete (untruncated) abstract field already stored in
screening/full_text/pubmed_tier1_tier2_extraction_plan.csv (verified
accurate for PUBMED_0761 by cross-reference against the WebSearch/PMC
result). Open-access/PMC status for the other 7 records was NOT
independently re-verified this run.

This batch:

- PUBMED_0761 (PMID 38486306, endothelium) - bioprinted hiPSC-CEC + hydrazone-crosslinked HA bioink; ex vivo rat/porcine/human Descemet membrane. Confirmed open access, PMC10941625.
- PUBMED_0777 (PMID 38780042, endothelium) - alginate hydrogel + fibroblast-derived decellularized ECM (ECM-AH) delivery system for hCECs.
- PUBMED_0841 (PMID 39551331, endothelium) - thermosensitive HPCH/CMCS hydrogel + iPSC-derived hCECs, rabbit CED in vivo model.
- PUBMED_0910 (PMID 40221533, endothelium) - RAFT plastic-compressed collagen scaffold + porcine CEC, ex vivo human cornea organ culture transplantation.
- PUBMED_0940 (PMID 40536661, endothelium) - decellularized porcine corneal ECM (SDS vs NaCl) scaffold, hCEC in vitro + rabbit CED in vivo.
- PUBMED_0950 (PMID 40665979, endothelium) - human acellular amniotic membrane (HAAM) scaffold + immortalized HCECs, in vitro only.
- PUBMED_1009 (PMID 41218465, endothelium) - polyacrylamide hydrogel matrix-stiffness (25/50/100 kPa) mechanistic study, YAP/glycolysis signaling, in vitro only.
- PUBMED_0131 (PMID 30716697, epithelium_limbus) - PLA films functionalized with collagen IV as LESC carrier substrata, in vitro only.
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
    "(screening/full_text/pubmed_tier1_tier2_extraction_plan.csv); Europe PMC "
    "REST API fetch was unavailable this run (web_fetch tool restricted to "
    "previously-searched URLs, unattended run could not authorize a new URL). "
)

EXTRACTIONS = {
    "PUBMED_0761": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / bioprinting study with ex vivo evaluation (rat, porcine, and human Descemet membrane)",
        target_layer_final="endothelium",
        biomaterial_category="bioprintable natural polymer hydrogel bioink",
        specific_materials="hydrazone crosslinked hyaluronic acid (HA) bioink, optimized for human pluripotent stem cell (hPSC)-derived corneal endothelial cells (CECs)",
        fabrication_method="hPSC-derived CECs differentiated then bioprinted using optimized hydrazone-crosslinked HA bioink; biocompatibility pre-tested via transplantation onto ex vivo denuded rat and porcine corneas and denuded human Descemet membrane before bioprinting proper",
        scaffold_architecture="3D-bioprinted hydrogel construct",
        cell_type_used="human pluripotent stem cell (hPSC)-derived corneal endothelial cells",
        cell_source="human (hPSC-derived)",
        growth_factors_or_bioactive_agents="none reported (bioink is a structural hydrogel carrier, not a growth-factor delivery system)",
        optical_transparency_reported="unclear / not reported in abstract",
        optical_metric_details="Optical transparency not quantified in abstract; focus is on viability/printability and phenotype markers.",
        mechanical_testing_reported="unclear / not reported in abstract",
        mechanical_metric_details="No tensile strength, modulus, or rheological values given in abstract beyond qualitative bioink 'printability'.",
        biological_testing_reported="yes",
        biological_metric_details="Live/dead staining confirmed cell viability after bioprinting; ZO-1, Na+/K+-ATPase, and CD166 immunofluorescence/histology confirmed CEC phenotype; STEM121 marker confirmed human-cell identity on ex vivo rat/porcine Descemet membrane up to 10 days; polygonal morphology and native-like marker localization observed 7 days post-bioprinting; some mesenchymal-like cells noted spreading beneath the CEC layer in certain culture areas (a limitation).",
        in_vitro_model="yes", ex_vivo_model="yes", animal_model="no", clinical_evidence="no",
        follow_up_duration="up to 10 days (ex vivo transplantation) / 7 days post-bioprinting (in vitro culture)",
        main_outcomes="Hydrazone-crosslinked HA bioink successfully supported viability and printability of hPSC-derived CECs; ex vivo biocompatibility was confirmed on rat, porcine, and human Descemet membrane, with bioprinted cells retaining CEC-specific marker expression (ZO-1, Na+/K+-ATPase, CD166) and polygonal morphology up to 7-10 days, supporting feasibility of bioprinting corneal endothelium as a step toward full-thickness bioprinted cornea.",
        main_limitations="No live animal (in vivo) transplantation, only ex vivo organ-culture evaluation; mesenchymal-like cell subpopulations observed spreading under the CEC layer, raising concern about endothelial-mesenchymal transition (EnMT) in some culture areas; no optical transparency or mechanical property data reported in abstract; relatively short (7-10 day) follow-up.",
        translational_readiness_level="preclinical (ex vivo organ-culture model)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "DOI 10.1186/s13287-024-03672-w, Stem Cell Research & Therapy, 2024. Cross-checked via WebSearch: confirmed open access, full text available at PMC10941625 (https://pmc.ncbi.nlm.nih.gov/articles/PMC10941625/), authors Gronroos/Moro/Puistola/Skottman et al. (Tampere University). Notable as one of the few bioprinting-specific (as opposed to cast/electrospun) endothelial scaffold studies in the Tier 1 set; flagged EnMT/mesenchymal-like cell subpopulation as a real limitation worth cross-referencing against PUBMED_0777 (same EnMT theme, alginate-ECM system).",
    ),
    "PUBMED_0777": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / scaffold fabrication and mechanistic in vitro comparison study",
        target_layer_final="endothelium",
        biomaterial_category="natural polymer hydrogel integrated with decellularized extracellular matrix (composite carrier)",
        specific_materials="alginate hydrogel (AH) physically integrated with human fibroblast-derived decellularized extracellular matrix (ECM-AH composite), ~50 um thick; compared against FNC (ferritic nitrocarburizing)-coated substrate as positive control",
        fabrication_method="Human fibroblast-derived ECM decellularized and physically integrated with alginate hydrogel to form a thin (~50 um) transparent, permeable ECM-AH composite membrane",
        scaffold_architecture="thin (~50 um) transparent permeable composite hydrogel membrane",
        cell_type_used="human corneal endothelial cells (hCECs)",
        cell_source="human (hCEC line/culture, donor detail not specified in abstract)",
        growth_factors_or_bioactive_agents="TGF-beta1 used experimentally to induce EnMT for a recovery test; decellularized fibroblast ECM itself is the primary bioactive component (not a purified growth factor)",
        optical_transparency_reported="yes",
        optical_metric_details="ECM-AH described as transparent (qualitative); no numeric transmittance value given in abstract; thickness ~50 um.",
        mechanical_testing_reported="partial",
        mechanical_metric_details="Surface roughness and surface potential characterized as favorable for CEC adhesion/growth; no explicit tensile strength or modulus values reported in abstract.",
        biological_testing_reported="yes",
        biological_metric_details="Western blot and qPCR showed ZO-1 (structural) and Na+/K+-ATPase (functional) marker expression on ECM-AH comparable to FNC-coated positive control; cell density per unit area significantly better on ECM-AH than FNC at day 7; in vitro engraftment simulation showed hCECs successfully transferred into decellularized porcine corneal tissue with high viability; EnMT-inductive factors Smad2 and vimentin were significantly reduced on ECM-AH vs. FNC, while EnMT-inhibitory factor Smad7 was significantly elevated; TGF-beta1-treated hCECs on ECM-AH showed faster recovery of normal cell phenotype.",
        in_vitro_model="yes", ex_vivo_model="yes", animal_model="no", clinical_evidence="no",
        follow_up_duration="up to 7 days in vitro culture; engraftment simulation timepoint not specified numerically",
        main_outcomes="An alginate hydrogel integrated with human fibroblast-derived decellularized ECM (ECM-AH) supported hCEC structural/functional marker expression and higher cell density than an FNC positive-control substrate at day 7, successfully enabled cell engraftment onto decellularized porcine corneal tissue, and suppressed endothelial-mesenchymal transition (EnMT) markers (reduced Smad2/vimentin, elevated Smad7), including faster phenotypic recovery after TGF-beta1-induced EnMT -- positioning ECM-AH as a promising hCEC delivery vehicle.",
        main_limitations="In vitro and ex vivo (porcine tissue engraftment simulation) only, no live animal or clinical evaluation; no quantitative tensile/modulus mechanical data reported in abstract; donor/passage details of hCECs not specified.",
        translational_readiness_level="preclinical (ex vivo porcine tissue engraftment model)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "DOI 10.1021/acsbiomaterials.4c00040, ACS Biomaterials Science & Engineering, 2024. EnMT-suppression mechanistic data (Smad2/vimentin/Smad7) is directly comparable to the EnMT concern flagged in PUBMED_0761 (bioprinted HA construct) -- worth cross-referencing in the discussion/benchmarking synthesis as two different biomaterial strategies addressing the same EnMT failure mode.",
    ),
    "PUBMED_0841": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / scaffold fabrication study with in vivo evaluation (rabbit corneal endothelial dysfunction model)",
        target_layer_final="endothelium",
        biomaterial_category="thermosensitive natural polysaccharide hydrogel scaffold combined with iPSC-derived cells",
        specific_materials="thermosensitive hydroxypropyl chitin/carboxymethyl chitosan (HPCH/CMCS) hydrogel, combined with induced pluripotent stem cell (iPSC)-derived human corneal endothelial cells (hCECs)",
        fabrication_method="HPCH/CMCS thermosensitive hydrogels fabricated and characterized for gelation/biocompatibility; iPSCs differentiated into hCECs via neural crest cells (NCCs) using a two-step small-molecule induction protocol; hydrogel used as fixation/support carrier for transplantation",
        scaffold_architecture="in situ thermosensitive gelling hydrogel (fixation/support carrier)",
        cell_type_used="iPSC-derived human corneal endothelial cells (hCECs), via neural crest cell (NCC) intermediate",
        cell_source="human (iPSC-derived)",
        growth_factors_or_bioactive_agents="small-molecule compounds used in the two-step iPSC-to-hCEC differentiation protocol (not classical protein growth factors delivered via the scaffold itself)",
        optical_transparency_reported="yes",
        optical_metric_details="HPCH/CMCS hydrogels exhibited 'superior transparency' (qualitative) in material characterization; in vivo, slit-lamp microscopy showed significant corneal transparency improvement in the HPCH/CMCS/hCECs group vs. controls (P = 0.006), though transparency was described as not homogeneous across all corneal areas.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Hydrogels described as having 'appropriate mechanical properties' for use as a fixation/support carrier (qualitative); no explicit numeric tensile strength or modulus values given in abstract.",
        biological_testing_reported="yes",
        biological_metric_details="Biocompatibility of HPCH/CMCS confirmed; histological examination and immunofluorescence showed higher corneal endothelial cell density and positive expression of relevant functional markers in the HPCH/CMCS/hCECs treatment group vs. controls, in a rabbit corneal endothelial dysfunction model.",
        in_vitro_model="yes", ex_vivo_model="no", animal_model="yes", clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract (described as 'preliminary attempt', in vivo rabbit model)",
        main_outcomes="Thermosensitive HPCH/CMCS hydrogel combined with iPSC-derived hCECs (via a two-step NCC-based small-molecule differentiation protocol) significantly improved corneal transparency (P = 0.006) and endothelial cell density/marker expression in a rabbit corneal endothelial dysfunction model, supporting the combined hydrogel + iPSC-derived cell strategy as a potential local repair approach for endothelial dysfunction.",
        main_limitations="Explicitly described by authors as a 'preliminary attempt'; transparency improvement was not homogeneous across all corneal areas; exact follow-up duration, animal numbers, and quantitative mechanical/transparency values not given in abstract; rabbit (not primate/human) model.",
        translational_readiness_level="preclinical (animal model, rabbit)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "DOI 10.1016/j.actbio.2024.11.021, Acta Biomaterialia, 2025. One of relatively few Tier 1 records combining an iPSC-derived (rather than primary donor or immortalized-line) cell source with an in vivo animal model and a statistically significant transparency outcome -- high benchmarking value.",
    ),
    "PUBMED_0910": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / scaffold fabrication study with ex vivo evaluation (human cornea organ culture model)",
        target_layer_final="endothelium",
        biomaterial_category="plastic-compressed collagen 3D matrix (biologic scaffold)",
        specific_materials="Real Architecture For 3D Tissues (RAFT) -- a plastic-compressed collagen 3D matrix",
        fabrication_method="Porcine corneal endothelial cells (PCECs) seeded onto RAFT collagen matrix to construct a tissue-engineered corneal endothelium; cell-seeded RAFT graft then transplanted onto a human cornea and maintained in an ex vivo organ culture model",
        scaffold_architecture="plastic-compressed 3D collagen matrix (RAFT)",
        cell_type_used="porcine corneal endothelial cells (PCECs)",
        cell_source="porcine (xenogeneic, non-human)",
        growth_factors_or_bioactive_agents="none reported",
        optical_transparency_reported="unclear / not reported in abstract",
        optical_metric_details="Optical transparency not directly quantified in abstract; functional outcome reported instead as restoration of corneal thickness to normal.",
        mechanical_testing_reported="unclear / not reported in abstract",
        mechanical_metric_details="No tensile strength or modulus values reported in abstract; RAFT is characterized functionally (as a compressed collagen matrix) rather than mechanically in this abstract.",
        biological_testing_reported="yes",
        biological_metric_details="PCECs formed a high-density monolayer on RAFT expressing endothelial markers ZO-1, Na/K-ATPase, and N-cadherin; cell-seeded RAFT transplantation onto endothelium-wounded human cornea (ex vivo organ culture) restored corneal thickness to normal within two weeks.",
        in_vitro_model="yes", ex_vivo_model="yes", animal_model="no", clinical_evidence="no",
        follow_up_duration="2 weeks (ex vivo human cornea organ culture, post-transplantation)",
        main_outcomes="A porcine corneal endothelial cell (PCEC)-seeded RAFT plastic-compressed collagen matrix formed a high-density, marker-positive (ZO-1+, Na/K-ATPase+, N-cadherin+) monolayer and, when transplanted onto endothelium-wounded human corneas in an ex vivo organ culture model, restored normal corneal thickness within two weeks -- supporting RAFT as a scaffold for tissue-engineered corneal endothelium grafts.",
        main_limitations="Xenogeneic (porcine) cell source used on human ex vivo tissue rather than human cells; ex vivo organ culture only, no live in vivo animal or clinical evaluation; short (2-week) follow-up; no quantitative transparency or mechanical data reported in abstract.",
        translational_readiness_level="preclinical (ex vivo human organ-culture model)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "DOI 10.1038/s41598-025-96494-6, Scientific Reports, 2025 (open-access journal by default policy, though OA status not independently re-verified this run). Notable for direct functional thickness-restoration data in an ex vivo human (not just animal) cornea model -- a relatively high-fidelity preclinical readout among Tier 1 endothelium records.",
    ),
    "PUBMED_0940": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / decellularized matrix scaffold study with in vitro and in vivo evaluation (rabbit corneal endothelial dystrophy model)",
        target_layer_final="endothelium",
        biomaterial_category="decellularized xenogeneic extracellular matrix scaffold",
        specific_materials="decellularized porcine corneal extracellular matrix (dECM), compared using two decellularization protocols: 0.3% sodium dodecyl sulfate (SDS) vs. 1.5 M sodium chloride (NaCl), both followed by enzymatic nucleic acid digestion",
        fabrication_method="Porcine corneas decellularized via SDS or NaCl protocol plus enzymatic nucleic acid digestion; histological/biochemical assessment of decellularization efficiency and ECM preservation; hCECs cultured on the better-performing SDS-dECM scaffold",
        scaffold_architecture="decellularized native corneal ECM sheet/scaffold",
        cell_type_used="human corneal endothelial cells (hCECs)",
        cell_source="human (hCEC line/culture, donor detail not specified in abstract)",
        growth_factors_or_bioactive_agents="none reported (native ECM components -- sulfated glycosaminoglycans, collagen -- are structural, not exogenous growth factors)",
        optical_transparency_reported="yes",
        optical_metric_details="Light transmittance at 400 nm increased from 65.82% (acellular dECM) to 90.13% (double-sided hCEC culture); in vivo, high-dose treatment group achieved transparency and pachymetry comparable to normal corneas (thickness ~602 um, grading score 0.00 +/- 0.00) by 16 weeks.",
        mechanical_testing_reported="partial",
        mechanical_metric_details="Residual DNA: SDS 123.60 +/- 8.92 ng/mg vs. NaCl 146.15 +/- 5.49 ng/mg; SDS retained 95.2% sulfated GAGs with 40% collagen loss vs. native; NaCl retained 100% collagen but only 71.0% sGAG with incomplete decellularization. These are biochemical/compositional rather than tensile mechanical metrics; no explicit tensile strength/modulus values given.",
        biological_testing_reported="yes",
        biological_metric_details="hCECs on SDS-dECM showed progressive proliferation, viability surpassing tissue-culture plastic (TCPS) by day 14 (389.01 +/- 5.68 vs. 359.65 +/- 7.92, p<0.05); immunofluorescence confirmed polygonal morphology and ZO-1 expression (intact barrier phenotype); in vivo, dose-dependent corneal clarity restoration in a rabbit corneal endothelial dystrophy (CED) model.",
        in_vitro_model="yes", ex_vivo_model="no", animal_model="yes", clinical_evidence="no",
        follow_up_duration="up to 14 days in vitro; 16 weeks in vivo (rabbit CED model)",
        main_outcomes="SDS-based decellularization of porcine corneal ECM outperformed NaCl-based decellularization on DNA clearance and sGAG retention (at some collagen cost); hCECs cultured on SDS-dECM showed superior viability vs. TCPS by day 14, intact barrier phenotype (ZO-1+), and increasing scaffold transparency with culture (65.82% to 90.13% at 400 nm); in a rabbit CED model, high-dose hCEC-seeded SDS-dECM restored corneal transparency and thickness (~602 um) comparable to normal corneas by 16 weeks, supporting dECM as a donor-alternative scaffold for endothelial dysfunction.",
        main_limitations="Xenogeneic (porcine) scaffold source; SDS decellularization caused 40% collagen loss relative to native tissue, a potential mechanical trade-off not directly quantified; rabbit (not primate/human) in vivo model; no explicit tensile/modulus mechanical testing reported in abstract.",
        translational_readiness_level="preclinical (animal model, rabbit, 16-week follow-up)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "DOI 10.1007/s13770-025-00734-9, Tissue Engineering and Regenerative Medicine, 2025. Rich quantitative dataset spanning decellularization chemistry, in vitro viability, transmittance, and 16-week in vivo transparency/pachymetry outcomes -- one of the more comprehensive quantitative benchmarking records in this batch.",
    ),
    "PUBMED_0950": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / scaffold fabrication study (in vitro only)",
        target_layer_final="endothelium",
        biomaterial_category="decellularized biological membrane (acellular amniotic membrane)",
        specific_materials="human acellular amniotic membrane (HAAM), coated with fibronectin and chondroitin sulfate (FNC) to enhance cell adhesion",
        fabrication_method="HAAM fabricated via sequential chemical treatments (trypsin/EDTA, Triton X-100, sodium deoxycholate, peracetic acid/ethanol) combined with physical agitation to decellularize while preserving ECM structure; lyophilized, sterilized, then FNC-coated; seeded with immortalized human corneal endothelial cells (HCECs)",
        scaffold_architecture="decellularized amniotic membrane sheet with preserved collagen fiber structure",
        cell_type_used="immortalized human corneal endothelial cells (HCECs)",
        cell_source="human (immortalized cell line)",
        growth_factors_or_bioactive_agents="fibronectin and chondroitin sulfate (FNC) coating (adhesion factors, not classical growth factors)",
        optical_transparency_reported="yes",
        optical_metric_details="HAAM scaffold described as demonstrating 'excellent transparency' (qualitative); no numeric transmittance value given in abstract.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="HAAM described as having favorable 'mechanical properties' supporting attachment/proliferation (qualitative); intact collagen fiber structure maintained after decellularization; no explicit numeric tensile/modulus values given in abstract.",
        biological_testing_reported="yes",
        biological_metric_details="HCECs adhered closely to HAAM forming a continuous monolayer; CCK-8 and EdU assays confirmed cell viability and proliferation; immunofluorescence confirmed tight-junction protein ZO-1 expression; RNA-seq (transcriptome) and qPCR confirmed upregulation of genes regulating barrier function, ion transport, and ECM synthesis.",
        in_vitro_model="yes", ex_vivo_model="no", animal_model="no", clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract (in vitro culture only)",
        main_outcomes="A human acellular amniotic membrane (HAAM), decellularized via sequential chemical/physical treatment and FNC-coated, supported immortalized HCEC adhesion, viability, proliferation, and functional gene expression (barrier, ion transport, ECM synthesis pathways confirmed by RNA-seq/qPCR and ZO-1 immunofluorescence), suggesting HAAM functionally mimics native corneal endothelium and may serve as a transplantation scaffold, pending further preclinical/clinical validation.",
        main_limitations="In vitro only, no ex vivo, animal, or clinical evaluation reported; immortalized (not primary donor) HCECs used; authors explicitly state further studies are needed to explore long-term efficacy and safety in preclinical/clinical settings; no numeric transparency or mechanical values reported in abstract.",
        translational_readiness_level="early preclinical (in vitro material/cell characterization only)",
        benchmarking_relevance="medium",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "DOI 10.3389/fmed.2025.1592123, Frontiers in Medicine, 2025 (open-access journal by default policy, though OA status not independently re-verified this run). Amniotic-membrane-as-endothelial-scaffold theme is directly comparable to PUBMED_0537 (crosslinked amniotic membrane, batch 3) -- useful cross-reference for benchmarking amniotic membrane approaches specifically, though this record lacks the animal-model evidence that PUBMED_0537 has.",
    ),
    "PUBMED_1009": dict(
        extraction_status="completed",
        study_type="mechanistic in vitro biomaterial characterization study (scaffold mechanical microenvironment / cell-signaling study, no novel transplantable construct)",
        target_layer_final="endothelium",
        biomaterial_category="synthetic hydrogel used as a tunable-stiffness mechanistic substrate (not intended as a final transplant scaffold in this study)",
        specific_materials="polyacrylamide hydrogels fabricated at three defined stiffnesses (25, 50, and 100 kPa) to simulate the mechanical properties of native Descemet's membrane",
        fabrication_method="Polyacrylamide hydrogels cast at three controlled stiffness levels (25/50/100 kPa); human corneal endothelial (HCE) cells cultured on each stiffness variant to study mechanotransduction effects",
        scaffold_architecture="flat hydrogel substrate of defined, tunable stiffness (mechanistic study format, not a fabricated implantable scaffold)",
        cell_type_used="human corneal endothelium (HCE) cells",
        cell_source="human (cell source/donor detail not specified in abstract)",
        growth_factors_or_bioactive_agents="none reported (study is about matrix mechanical stiffness, not biochemical/growth-factor signaling inputs)",
        optical_transparency_reported="unclear / not reported in abstract",
        optical_metric_details="Optical transparency not assessed in abstract; study is focused on mechanotransduction (YAP/glycolysis), not optical scaffold performance.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Three defined hydrogel stiffness conditions used as the independent variable: 25 kPa, 50 kPa, and 100 kPa, spanning/approximating native Descemet's membrane stiffness range.",
        biological_testing_reported="yes",
        biological_metric_details="Increased scaffold stiffness promoted HCE cell proliferation via enhanced mechanical response and increased nuclear translocation of YAP (Yes-associated protein), upregulating downstream proliferation genes; increased stiffness also enhanced glycolysis by upregulating key glycolytic enzymes, improving cell viability and energy yield; proposed positive-feedback loop linking matrix stiffness, YAP-driven glycolysis, and proliferation.",
        in_vitro_model="yes", ex_vivo_model="no", animal_model="no", clinical_evidence="no",
        follow_up_duration="not applicable / short-term in vitro mechanistic study",
        main_outcomes="Increasing polyacrylamide hydrogel stiffness (25 to 100 kPa, spanning the native Descemet's membrane range) promoted human corneal endothelial cell proliferation and glycolytic metabolism via YAP nuclear translocation, revealing a stiffness-dependent 'metabolic response-proliferation' feedback mechanism relevant to designing tissue-engineered corneal endothelium scaffolds with optimized mechanical microenvironments.",
        main_limitations="Purely mechanistic in vitro study using a simplified tunable-stiffness hydrogel, not a candidate transplantable scaffold itself; no ex vivo, animal, or clinical evaluation; no optical transparency data; findings would need validation in an actual biomaterial scaffold formulation intended for transplantation.",
        translational_readiness_level="early preclinical (in vitro, basic mechanistic/mechanobiology research)",
        benchmarking_relevance="medium",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "DOI 10.1016/j.bioadv.2025.214594, Biomaterials Advances, 2026. Not a scaffold-fabrication/transplantation study per se, but directly informs the design-parameter (stiffness) rationale for endothelial scaffolds elsewhere in this corpus (e.g. RAFT/collagen, amniotic membrane, agarose constructs) -- useful mechanistic support reference for the benchmarking discussion rather than a standalone benchmarking data point.",
    ),
    "PUBMED_0131": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / carrier substratum study (in vitro only, human primary limbal epithelial cells)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="synthetic biodegradable polymer film functionalized with a natural ECM protein",
        specific_materials="poly-L/DL-lactic acid 70:30 (PLA) films functionalized with type IV collagen (col IV)",
        fabrication_method="PLA films cast/fabricated at a 70:30 L/DL ratio and surface-functionalized with type IV collagen; limbal epithelial cell suspensions isolated from human limbal rings and cultured on the films using animal-component-free medium",
        scaffold_architecture="thin synthetic polymer film substratum",
        cell_type_used="human corneal epithelial cells (initial biocompatibility test) and primary limbal epithelial stem cells (LESCs) isolated from human limbal rings",
        cell_source="human (primary, from limbal rings; animal-component-free culture medium)",
        growth_factors_or_bioactive_agents="type IV collagen (structural ECM protein coating, not a classical growth factor)",
        optical_transparency_reported="unclear / not reported in abstract",
        optical_metric_details="Optical transparency not assessed in abstract; PLA-col IV evaluated for biocompatibility and cell-adhesion/phenotype outcomes rather than optical performance.",
        mechanical_testing_reported="unclear / not reported in abstract",
        mechanical_metric_details="No tensile strength or modulus values reported in abstract.",
        biological_testing_reported="yes",
        biological_metric_details="PLA-col IV films were biocompatible and supported human corneal epithelial cell proliferation; limbal epithelial cells adhered significantly faster to PLA-col IV than to tissue culture plastic (TCP); mRNA expression of LESC markers K15, P63alpha, and ABCG2 was similar or greater (K15 significantly higher) on PLA-col IV vs. TCP; percentage of cells expressing corneal markers K3/K12 and LESC markers P63alpha/ABCG2 was similar between substrata.",
        in_vitro_model="yes", ex_vivo_model="no", animal_model="no", clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract (in vitro culture only)",
        main_outcomes="PLA films functionalized with type IV collagen were biocompatible, promoted faster limbal epithelial cell attachment than tissue culture plastic, and helped maintain the undifferentiated LESC phenotype (via K15/P63alpha/ABCG2 marker expression), supporting PLA-col IV as an animal-component-free carrier substratum alternative for cultivated limbal epithelial transplantation.",
        main_limitations="In vitro only, no ex vivo, animal, or clinical transplantation evaluation reported; no optical transparency or mechanical property data in abstract; long-term stability/degradation of the PLA film not addressed.",
        translational_readiness_level="early preclinical (in vitro, primary human limbal cells, animal-component-free protocol)",
        benchmarking_relevance="medium",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "DOI 10.1016/j.colsurfb.2019.01.054, Colloids and Surfaces B: Biointerfaces, 2019. This is the first epithelium/limbus-layer record processed in Tier 1 batches so far (batches 1-3 and the rest of this batch were endothelium-focused); animal-component-free culture protocol is a notable translational/regulatory-relevance point for the epithelium/limbus benchmarking table.",
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
    source_checked="local screening corpus abstract (screening/full_text/pubmed_tier1_tier2_extraction_plan.csv); Europe PMC REST API unavailable this run (web_fetch provenance restriction)",
    retrieval_date="2026-07-19",
    retrieval_notes="Europe PMC REST API fetch blocked by web_fetch provenance restriction in this unattended run; abstract taken from already-verified local screening corpus text instead. Open-access/PMC status not independently re-verified; confirm when fetch access is available.",
    extraction_ready="yes",
    reason_not_extraction_ready="",
)

TRACKER_UPDATE_PUBMED_0761 = dict(
    full_text_status="retrieved (full text, open access)",
    pdf_available="yes",
    source_checked="WebSearch + PMC (PMC10941625)",
    retrieval_date="2026-07-19",
    retrieval_notes="Confirmed open access via WebSearch; full text available at https://pmc.ncbi.nlm.nih.gov/articles/PMC10941625/ (Stem Cell Research & Therapy, 2024). Extraction still drawn from the local screening-corpus abstract text (verified accurate against this source) rather than the full HTML, due to context-size constraints of fetching full text for every record in this run.",
    extraction_ready="yes",
    reason_not_extraction_ready="",
)

for sid in EXTRACTIONS:
    if sid not in tby_id:
        print("WARNING missing in tracker:", sid)
        continue
    if sid == "PUBMED_0761":
        tby_id[sid].update(TRACKER_UPDATE_PUBMED_0761)
    else:
        tby_id[sid].update(TRACKER_UPDATE_DEFAULT)

with tracker_path.open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=tfieldnames)
    w.writeheader()
    w.writerows(trows)

print("Tracker updated for:", list(EXTRACTIONS.keys()))
