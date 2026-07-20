"""
Tier 1 extraction batch 9 (2026-07-20, scheduled run continuation).

Retrieval route note: the Europe PMC REST API JSON endpoint
(https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:<pmid>&format=json&resultType=core)
was tested first this run and again returned "URL not in provenance set"
from the sandboxed web_fetch tool (it only allows fetching URLs that already
appeared in a user message, a prior web_fetch result, or a WebSearch result;
this unattended scheduled run has no user available to authorize a new URL).
A WebSearch lookup was then tried for the first record (PUBMED_0646, PMID
36989713) to attempt to bring a working URL into the fetch provenance set;
this successfully surfaced the PubMed URL, but fetching
https://pubmed.ncbi.nlm.nih.gov/36989713/ was blocked by a reCAPTCHA
challenge page (consistent with the known PubMed automated-request blocking
noted in the task instructions). Same structural restriction hit in
batches 3-8.

Consistent with the workaround established in batches 3-8, extraction for
this batch was built from the complete, untruncated abstract text already
stored locally in screening/full_text/pubmed_tier1_tier2_extraction_plan.csv
(verified PubMed/journal abstracts captured during the original screening
pass), with open-access status assessed from known journal/publisher policy
(Bioactive Materials is a KeAi gold open-access journal; iScience (Cell
Press) is a gold open-access journal; Advanced Science (Wiley) is a gold
open-access journal; Biomedicine & Pharmacotherapy, Acta Biomaterialia, and
International Journal of Biological Macromolecules are Elsevier
hybrid/subscription titles; Small is a Wiley hybrid/subscription title;
Journal of Materials Chemistry B is an RSC hybrid/subscription title -- none
of the hybrid-title articles had open-access status individually confirmed
this run). No new WebSearch-based abstract retrieval was needed beyond the
one exploratory lookup above, since the locally stored abstracts already
contain rich quantitative detail; this is noted per-record in
extraction_notes.

This batch (8 records):
- PUBMED_0646 (PMID 36989713) - NANOULCOR nanostructured fibrin-agarose allogeneic cell-laden scaffold, phase I-II clinical trial (n=5 eyes), severe trophic corneal ulcers with LSCD, 2-year follow-up.
- PUBMED_0688 (PMID 37456580) - suture-free PEG-Lysozyme injectable hydrogel, in vitro + in vivo rabbit lamellar keratoplasty, functional vision-restoration behavior test.
- PUBMED_0719 (PMID 37866722) - double-crosslinked nanocellulose-reinforced dexamethasone-loaded collagen hydrogel, in vitro drug release/anti-inflammatory assays + in vivo rabbit intra-stromal implantation (inflammatory suture model), 8-week follow-up.
- PUBMED_0770 (PMID 38646166) - Kuragel biomimetic gelatin-HA photo-crosslinked hydrogel, in vivo rabbit mechanical injury model, 1- and 3-month follow-up.
- PUBMED_0877 (PMID 39853921) - humanized corneal stroma-like adhesive patches (HCSPs, DPC-templated PEGDA skeleton + human ECM + GelMA), in vitro + in vivo rabbit lamellar keratoplasty/microperforation repair.
- PUBMED_0907 (PMID 40159843) - photocurable GelMA/OCS dual-network hydrogel, sutureless repair of large (6 mm) corneal defects, in vitro + in vivo rabbit model.
- PUBMED_0928 (PMID 40395134) - decellularized fish swim-bladder collagen matrix scaffold, in vitro RCEC/RCSC recellularization + subcutaneous in vivo implantation, strong quantitative optical/mechanical dataset.
- PUBMED_1006 (PMID 41203155) - photocurable GelMA/OHA/CMCS hybrid hydrogel (GOC), sutureless repair of large (7 mm) corneal defects, in vitro + in vivo model; close companion to PUBMED_0907.
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
    "run could not authorize the new URL); a WebSearch-derived PubMed URL was also "
    "tried and blocked by a reCAPTCHA challenge page. "
)

EXTRACTIONS = {
    "PUBMED_0646": dict(
        extraction_status="completed",
        study_type="clinical / first-in-human study (phase I-II clinical trial, interim analysis, n=5 eyes)",
        target_layer_final="multiple_layers (anterior corneal substitute: epithelium + stroma, limbal stem cell deficiency indication)",
        biomaterial_category="cell-laden natural-polymer scaffold (nanostructured fibrin-agarose + allogeneic corneal cells)",
        specific_materials="NANOULCOR construct: nanostructured (compacted) fibrin-agarose biocompatible scaffold combined with allogeneic human corneal epithelial cells and allogeneic human corneal stromal cells",
        fabrication_method="fibrin-agarose hydrogel scaffold nanostructured/compacted to improve biomechanical handling properties, then seeded with allogeneic (donor-derived) human corneal epithelial and stromal cells to create an anterior corneal substitute; surgically applied over the corneal surface in a phase I-II clinical trial in 5 eyes with trophic corneal ulcers refractory to conventional treatment (combined stromal degradation/fibrosis and limbal stem cell deficiency); followed for 2 years post-surgery with anterior segment OCT imaging",
        scaffold_architecture="nanostructured (compacted) fibrin-agarose hydrogel sheet, cell-seeded, applied as an anterior lamellar corneal substitute; fully bioabsorbed in situ",
        cell_type_used="allogeneic (donor-derived) human corneal epithelial cells and human corneal stromal cells",
        cell_source="human, allogeneic (donor-derived corneal epithelial and stromal cells)",
        growth_factors_or_bioactive_agents="none exogenous reported; therapeutic effect attributed to the allogeneic corneal epithelial/stromal cell content itself, not an added growth factor",
        optical_transparency_reported="partial",
        optical_metric_details="Anterior segment optical coherence tomography (AS-OCT) showed a more homogeneous and stable ocular surface post-treatment (qualitative imaging finding); no numeric transmittance/haze score given in the retrieved abstract.",
        mechanical_testing_reported="unclear / not reported in abstract",
        mechanical_metric_details="No mechanical testing metrics reported; the only structural/durability data point is that complete scaffold degradation (bioabsorption) occurred within 3-12 weeks after surgery.",
        biological_testing_reported="yes",
        biological_metric_details="Implant completely covered the corneal surface; ocular surface inflammation decreased post-surgery; only 4 adverse reactions recorded across 5 eyes, none severe; no detachment, ulcer relapse, or surgical re-intervention over 2 years of follow-up; no graft rejection, local infection, or corneal neovascularization observed; significant postoperative improvement on eye-complication grading scales; complete scaffold degradation within 3-12 weeks.",
        in_vitro_model="no",
        ex_vivo_model="no",
        animal_model="no",
        clinical_evidence="yes",
        follow_up_duration="2 years (minimum clinical follow-up reported); scaffold fully bioabsorbed within 3-12 weeks post-surgery",
        main_outcomes="In an interim phase I-II clinical trial, a nanostructured fibrin-agarose scaffold seeded with allogeneic human corneal epithelial and stromal cells (NANOULCOR) was surgically applied to 5 eyes with severe trophic corneal ulcers combining stromal degradation/fibrosis and limbal stem cell deficiency. The implant fully covered the corneal surface, reduced ocular surface inflammation, and fully bioabsorbed within 3-12 weeks, with no graft rejection, infection, neovascularization, detachment, or ulcer relapse over 2 years of follow-up (4 non-severe adverse reactions total), and significant improvement on eye-complication grading scales, demonstrating feasibility and safety with partial efficacy for corneal surface restoration.",
        main_limitations="Very small sample size (n=5 eyes), interim/early-phase (phase I-II) trial with no control group or randomization; efficacy explicitly described by the authors as only 'partial'; no quantitative optical transmittance or mechanical/biomechanical metrics reported in the abstract; single-center design implied but not stated; long-term (beyond 2-year) durability and visual-acuity outcomes not detailed in the retrieved abstract.",
        translational_readiness_level="early clinical (phase I-II clinical trial, interim results, n=5 eyes)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Biomedicine & Pharmacotherapy (Elsevier), DOI 10.1016/j.biopha.2023.114612, 2023 -- Elsevier hybrid/subscription journal; open-access status of this specific article not confirmed this run; abstract-level extraction only. One of very few Tier 1 records with actual human clinical trial evidence (phase I-II, n=5, 2-year follow-up) -- high value for the review's translational-readiness spectrum and as a clinical-stage benchmark for cell-laden fibrin-agarose scaffold approaches.",
    ),
    "PUBMED_0688": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / injectable in situ-forming hydrogel study with in vitro and in vivo evaluation (rabbit lamellar keratoplasty, functional vision-restoration behavior test)",
        target_layer_final="stroma (with epithelialization outcome also assessed)",
        biomaterial_category="chemically crosslinked bioactive protein-PEG in situ-forming injectable hydrogel",
        specific_materials="PEG-Lysozyme hydrogel formed via in situ amidation reaction between 4-arm PEG-N-hydroxysuccinimide (PEG-NHS) and lysozyme",
        fabrication_method="4-arm-PEG-NHS reacted with lysozyme through an in situ amidation reaction, producing a sol-gel phase transition upon mixing/injection without external trigger; physicochemical properties (including modulus and tissue adhesion) tuned via the PEG:lysozyme component ratio to mimic native corneal modulus and withstand elevated intraocular pressure; evaluated in vitro with human corneal epithelial cells (HCECs) and in vivo via rabbit lamellar keratoplasty, with a newly established animal 'forging behavior' test used to assess functional visual restoration",
        scaffold_architecture="injectable, self-curing, sol-gel transitioning hydrogel that is shape self-adaptive, filling irregular stromal defects and adhering to native stroma without sutures",
        cell_type_used="human corneal epithelial cells (HCECs, in vitro growth/migration assay)",
        cell_source="human corneal epithelial cells (in vitro only; no exogenous cell seeding in the in vivo arm, which relies on host tissue integration)",
        growth_factors_or_bioactive_agents="lysozyme functions as the intrinsic bioactive protein component (antimicrobial/bioactive enzyme) responsible for promoting HCEC growth/migration, rather than an added growth factor",
        optical_transparency_reported="unclear / not reported in abstract",
        optical_metric_details="Optical transparency is not explicitly quantified in the retrieved abstract; the implant's function is described in terms of shape adaptivity, modulus matching, and vision restoration rather than a stated transmittance value.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Physicochemical properties (including a 'mimetic corneal modulus') were tunable via the PEG:lysozyme component ratio, and the implant provided tissue adhesion sufficient to endure increased intraocular pressure (qualitative findings); no specific numeric modulus or adhesion-strength values given in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="In vitro: implant supported HCEC growth and migration, attributed to lysozyme bioactivity. In vivo (rabbit lamellar keratoplasty): hydrogel filled the defect to form a shape-adaptive implant adhered to native stroma, promoted epithelialization and stromal integrity, and restored normal corneal topology; a newly established animal forging-behavior test demonstrated rapid visual restoration in rabbits treated with the implant in a suture-free manner.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract (rabbit lamellar keratoplasty follow-up duration not given)",
        main_outcomes="A suture-free, injectable PEG-Lysozyme hydrogel, formed via in situ amidation between 4-arm-PEG-NHS and lysozyme, achieved a corneal-mimetic modulus and sufficient tissue adhesion to withstand elevated intraocular pressure, supported HCEC growth/migration in vitro via lysozyme bioactivity, and in a rabbit lamellar keratoplasty model formed a shape-adaptive, sutureless implant that promoted epithelialization, restored stromal integrity and normal corneal topology, and produced rapid functional visual restoration as measured by a novel animal forging-behavior test.",
        main_limitations="No quantitative modulus, adhesion-strength, or optical transmittance values given in the retrieved abstract despite tunability/adhesion claims; follow-up duration and sample size for the rabbit lamellar keratoplasty study not specified; the forging-behavior functional-vision test is a novel, non-standard assay whose validation against conventional visual-acuity measures is not described in the abstract.",
        translational_readiness_level="preclinical (animal model, rabbit)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Bioactive Materials (KeAi), DOI 10.1016/j.bioactmat.2023.05.008, 2023 -- Bioactive Materials is a fully open-access (gold OA) journal; full-text fetch not attempted this run, abstract-level extraction used. Notable for a rare functional (behavioral) vision-restoration readout in an animal model, complementing the more common structural/histological endpoints used elsewhere in this batch.",
    ),
    "PUBMED_0719": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / drug-eluting reinforced hydrogel study with in vitro release and bioactivity assays and in vivo evaluation (rabbit intra-stromal implantation, inflammatory suture model, 8-week follow-up)",
        target_layer_final="stroma",
        biomaterial_category="double-crosslinked nanocellulose-reinforced, drug-eluting natural-polymer (collagen) hydrogel",
        specific_materials="porcine skin collagen hydrogel reinforced with cellulose nanofibers extracted from the sea invertebrate Ciona intestinalis, double chemically and photochemically crosslinked, and loaded with the corticosteroid dexamethasone",
        fabrication_method="porcine skin collagen combined with Ciona intestinalis-derived cellulose nanofibers and subjected to sequential chemical and photochemical crosslinking (double crosslinking); dexamethasone loaded into the resulting matrix; in vitro drug release measured over 60 days; anti-inflammatory bioactivity assessed via tube-formation/migration assays on TNF-alpha-stimulated vascular endothelial cells and pro-inflammatory cytokine (CCL2, CXCL5) suppression in TNF-alpha-stimulated human corneal epithelial cells; implanted intra-stromally in 12 New Zealand white rabbit corneas subjected to an inflammatory suture stimulus and followed for 8 weeks",
        scaffold_architecture="double chemically/photochemically crosslinked, nanocellulose-reinforced collagen hydrogel matrix, functioning as both a structural stromal implant and a sustained drug-delivery depot",
        cell_type_used="human corneal epithelial cells (TNF-alpha-stimulated cytokine assay) and vascular endothelial cells (TNF-alpha-stimulated tube-formation/migration assay), used for in vitro bioactivity testing rather than structural cell seeding",
        cell_source="human corneal epithelial cells and vascular endothelial cells (in vitro assay lines/primary cells; exact species/source not further specified in the retrieved abstract beyond 'human corneal epithelial')",
        growth_factors_or_bioactive_agents="dexamethasone (corticosteroid anti-inflammatory drug), loaded into the hydrogel matrix for sustained release over 60 days in vitro",
        optical_transparency_reported="yes",
        optical_metric_details="The reinforced double-crosslinked hydrogel, after drug loading, 'maintained high optical transparency' (qualitative finding); in vivo, treated corneas showed reduced corneal haze and sustained corneal thickness/stromal morphology over 8 weeks; no single numeric transmittance percentage given in the retrieved abstract.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Mechanical characteristics were 'significantly improved' compared with non-reinforced hydrogels following nanocellulose reinforcement and double (chemical + photochemical) crosslinking (qualitative comparative finding); no specific numeric modulus or tensile-strength values given in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="Dexamethasone retained anti-inflammatory bioactivity after exposure to crosslinking/sterilization: it inhibited tube formation and migration of TNF-alpha-stimulated vascular endothelial cells and suppressed pro-inflammatory cytokines CCL2 and CXCL5 in TNF-alpha-stimulated human corneal epithelial cells. In vivo (8-week rabbit intra-stromal implantation with inflammatory suture stimulus, n=12 rabbits): dexamethasone-releasing hydrogels suppressed TNF-alpha, MMP-9, and leukocyte/fibroblast cell invasion, resulting in reduced corneal haze, sustained corneal thickness and stromal morphology, and reduced overall vessel (neovascularization) invasion versus comparators.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="60 days (in vitro sustained dexamethasone release); 8 weeks (in vivo rabbit intra-stromal implantation with inflammatory suture stimulus, n=12 New Zealand white rabbits)",
        main_outcomes="A double chemically/photochemically crosslinked, Ciona intestinalis nanocellulose-reinforced porcine collagen hydrogel loaded with dexamethasone maintained high optical transparency and significantly improved mechanical characteristics over non-reinforced hydrogels, released dexamethasone over 60 days in vitro while retaining anti-inflammatory bioactivity (suppressing endothelial tube formation/migration and epithelial CCL2/CXCL5 expression), and when implanted intra-stromally in an 8-week rabbit inflammatory-suture model (n=12), suppressed TNF-alpha, MMP-9, and leukocyte/fibroblast invasion, reducing corneal haze and vessel invasion while sustaining corneal thickness and stromal morphology -- supporting its use as a combined structural and anti-inflammatory drug-eluting corneal stromal implant, particularly relevant for resource-limited settings with suboptimal postoperative drug compliance.",
        main_limitations="No quantitative numeric values given in the retrieved abstract for optical transmittance, mechanical modulus/tensile strength, or magnitude of cytokine/haze reduction, despite significant-effect claims; rabbit (not primate/human) in vivo model with an induced inflammatory suture stimulus that may not fully replicate clinical corneal disease heterogeneity; long-term (beyond 8-week) durability, degradation, and integration outcomes not reported.",
        translational_readiness_level="preclinical (animal model, rabbit)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Acta Biomaterialia (Elsevier), DOI 10.1016/j.actbio.2023.10.020, 2023 -- Elsevier hybrid/subscription journal; open-access status of this specific article not confirmed this run; abstract-level extraction only. Notable for combining structural stromal reinforcement with sustained anti-inflammatory drug delivery and a resource-limited-setting translational framing, and for one of the more quantitatively described in vivo inflammatory-disease models in this batch (explicit sample size n=12, 8-week follow-up).",
    ),
    "PUBMED_0770": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / biomimetic photo-crosslinked hydrogel study with in vivo evaluation (New Zealand rabbit mechanical injury model, 1- and 3-month follow-up)",
        target_layer_final="multiple_layers (epithelium + stroma + sub-basal nerve plexus regeneration)",
        biomaterial_category="photo-crosslinked natural-polymer (gelatin-hyaluronic acid) biomimetic hydrogel",
        specific_materials="Kuragel: functionalized gelatin and hyaluronic acid combined to form a photo-crosslinkable, biodegradable hydrogel",
        fabrication_method="gelatin and hyaluronic acid chemically functionalized to enable photo-crosslinking; hydrogel composition tuned to match the transparency and compressive modulus of healthy human cornea, achieve sufficient adhesive strength for sutureless integration with host tissue, and minimize post-administration swelling; tested in a New Zealand white rabbit mechanical injury model affecting the corneal epithelium and stroma",
        scaffold_architecture="photo-crosslinked, biodegradable, sutureless adhesive hydrogel designed to biomimic native corneal transparency and compressive modulus",
        cell_type_used="not applicable / acellular hydrogel (relies on host-derived re-epithelialization, stromal regeneration, and sub-basal nerve plexus regeneration; no exogenous cell seeding reported)",
        cell_source="not applicable / host-derived (in vivo regeneration only)",
        growth_factors_or_bioactive_agents="none reported; regenerative effect attributed to the biomimetic hydrogel matrix itself, not an added bioactive factor",
        optical_transparency_reported="yes",
        optical_metric_details="Kuragel was designed and characterized to have transparency 'similar to healthy human cornea' (qualitative comparative finding); in vivo, the treatment 'restor[ed] transparency and thickness' in injured corneas; no single numeric transmittance percentage given in the retrieved abstract.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Compressive modulus was tuned to be 'similar to healthy human cornea,' and the hydrogel achieved sufficient adhesive strength for sutureless integration with host tissue with minimal post-administration swelling (qualitative findings); no specific numeric modulus, adhesion-strength, or swelling-ratio values given in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="In a New Zealand rabbit mechanical injury model affecting the corneal epithelium and stroma, Kuragel efficiently promoted re-epithelialization within 1 month of administration, while stromal tissue and the sub-basal nerve plexus regenerated within 3 months, with restoration of corneal transparency and thickness.",
        in_vitro_model="no",
        ex_vivo_model="no",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="1 month (re-epithelialization); 3 months (stromal and sub-basal nerve plexus regeneration)",
        main_outcomes="Kuragel, a photo-crosslinked biomimetic hydrogel made from functionalized gelatin and hyaluronic acid with corneal-matched transparency and compressive modulus, achieved sutureless adhesive integration with minimal swelling and, in a New Zealand rabbit corneal mechanical injury model, efficiently promoted re-epithelialization within 1 month and stromal plus sub-basal corneal nerve regeneration within 3 months, restoring corneal transparency and thickness -- positioning it as a candidate regenerative treatment for corneal defects including thinning.",
        main_limitations="No in vitro characterization or cell-compatibility data reported in the retrieved abstract (evaluation goes directly to an in vivo injury model); no quantitative transmittance, modulus, or swelling-ratio values given despite biomimetic-matching claims; rabbit (not primate/human) in vivo model; sample size not specified; long-term (beyond 3-month) durability and functional visual-acuity outcomes not reported.",
        translational_readiness_level="preclinical (animal model, rabbit)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "iScience (Cell Press), DOI 10.1016/j.isci.2024.109641, 2024 -- iScience is a fully open-access (gold OA) journal; full-text fetch not attempted this run, abstract-level extraction used. Notable for reporting corneal sub-basal nerve plexus regeneration as an explicit endpoint (uncommon among Tier 1 records processed so far), relevant to the review's sensory-reinnervation/functional-recovery benchmarking discussion.",
    ),
    "PUBMED_0877": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / hybrid decellularized-template hydrogel-composite study with in vitro and in vivo evaluation (rabbit lamellar keratoplasty and microperforation repair models)",
        target_layer_final="stroma (with epithelial healing outcome also assessed)",
        biomaterial_category="hybrid decellularized-scaffold/synthetic composite hydrogel (PEGDA-templated skeleton + human corneal ECM + GelMA adhesive)",
        specific_materials="humanized corneal stroma-like adhesive patches (HCSPs): polyethylene glycol diacrylate (PEGDA) cast and cured within decellularized porcine cornea (DPC) templates, then enzymatically digested to obtain hydrogel skeletons, which are integrated with human corneal extracellular matrix (ECM) and methacrylated gelatin (GelMA)",
        fabrication_method="multi-step process: (1) PEGDA cast and cured within DPC templates to replicate native stromal ultrastructure; (2) DPC templates enzymatically digested away, leaving PEGDA hydrogel skeletons that retain the corneal stromal hierarchical architecture; (3) skeletons integrated with human corneal ECM and GelMA; adhesive bonding to host corneal stroma achieved by delivering the GelMA component at ocular surface temperature (37 degrees C) and curing via 405 nm light irradiation; evaluated in rabbit models of lamellar keratoplasty and microperforation repair",
        scaffold_architecture="hierarchical hydrogel skeleton replicating natural corneal stromal ultrastructure (templated from decellularized porcine cornea), integrated with human ECM and a light-curable GelMA adhesive interface",
        cell_type_used="corneal epithelial cells and corneal stromal cells (in vitro survival/migration/phenotype-preservation assay; species not specified in the retrieved abstract)",
        cell_source="not fully specified in abstract beyond 'corneal epithelial and stromal cells'; scaffold itself is human-ECM/porcine-template-derived, with cell-source species for the in vitro survival/migration assay not explicitly stated",
        growth_factors_or_bioactive_agents="none exogenously added; human corneal ECM component provides native bioactive/structural cues rather than a defined added growth factor",
        optical_transparency_reported="yes",
        optical_metric_details="HCSPs were shown to 'replicate the ultrastructure, protein components, and optical properties of human corneas' (qualitative comparative finding); no single numeric transmittance percentage given in the retrieved abstract.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="HCSPs exhibited 'improved anti-swelling and anti-degradation capabilities compared with conventional DPCs and recombinant human collagen patches' (qualitative comparative finding against two named comparator materials); no specific numeric modulus, swelling-ratio, or degradation-rate values given in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="HCSPs promoted survival and migration of corneal epithelial and stromal cells while preserving their native phenotypes (in vitro). In rabbit models of lamellar keratoplasty and microperforation repair, HCSPs accelerated epithelial healing, minimized suture-associated complications (owing to light-cured adhesive bonding rather than sutures), and maintained structural stability.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract (rabbit lamellar keratoplasty / microperforation repair follow-up duration not given)",
        main_outcomes="Humanized corneal stroma-like adhesive patches (HCSPs), fabricated by casting PEGDA within decellularized porcine cornea templates, digesting away the template to yield a hierarchical hydrogel skeleton, and integrating it with human corneal ECM and light-curable GelMA, replicated the ultrastructure, protein composition, and optical properties of human corneas with improved anti-swelling/anti-degradation performance versus conventional decellularized porcine corneas and recombinant human collagen patches; the light-cured adhesive interface enabled stable bonding to host stroma without sutures, supported corneal epithelial and stromal cell survival/migration with phenotype preservation in vitro, and in rabbit lamellar keratoplasty and microperforation repair models accelerated epithelial healing, minimized suture-associated complications, and maintained structural stability -- positioning HCSPs as a promising donor-free corneal substitute.",
        main_limitations="No quantitative transmittance, modulus, or swelling/degradation-rate values given in the retrieved abstract despite explicit comparative-improvement claims; species/source of the in vitro corneal epithelial and stromal cells not specified; rabbit (not primate/human) in vivo model; follow-up duration not specified; long-term integration, transparency stability, and immunogenicity of the porcine-template-derived skeleton component not reported.",
        translational_readiness_level="preclinical (animal model, rabbit)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Advanced Science (Wiley), DOI 10.1002/advs.202411540, 2025 -- Advanced Science is a fully open-access (gold OA) Wiley journal; full-text fetch not attempted this run, abstract-level extraction used. Notable for direct comparative claims against two other named benchmark materials (conventional DPCs and recombinant human collagen patches), and for a light-cured sutureless adhesive strategy distinct from the injectable in-situ-gelling hydrogels elsewhere in this batch -- useful comparator record for the review's decellularized-scaffold and sutureless-adhesion benchmarking tables.",
    ),
    "PUBMED_0907": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / photocurable dual-network hydrogel study with in vitro and in vivo evaluation (rabbit large corneal defect model, 6 mm defect)",
        target_layer_final="multiple_layers (epithelium + stroma; large-area full-thickness-scale defect repair)",
        biomaterial_category="photocurable dual-network natural-polymer hydrogel",
        specific_materials="GelMA/OCS hydrogel: gelatin methacryloyl (GelMA) combined with oxidized chondroitin sulfate (OCS)",
        fabrication_method="GelMA and OCS combined and photocured to form an injectable dual-network hybrid hydrogel; evaluated in vitro for cytocompatibility with human corneal epithelial cells (HCECs); injected to accurately fill large (6 mm) corneal defects in rabbits, forming smooth-surfaced hydrogel grafts; evaluated postoperatively via slit-lamp examination, histology, and transcriptomic analysis",
        scaffold_architecture="injectable, photocured dual-network hydrogel; low swelling rate; fills large (6 mm) corneal defects and forms a smooth-surfaced graft with enhanced mechanical and adhesive properties versus non-hybrid hydrogels",
        cell_type_used="human corneal epithelial cells (HCECs)",
        cell_source="human corneal epithelial cells (in vitro proliferation/migration/adhesion assay); in vivo defect-filling arm uses host rabbit corneal tissue for re-epithelialization/stromal reconstruction, no exogenous cell seeding in vivo",
        growth_factors_or_bioactive_agents="none reported; oxidized chondroitin sulfate serves as a structural/crosslinking network component rather than a bioactive/growth factor",
        optical_transparency_reported="yes",
        optical_metric_details="GelMA/OCS hydrogel demonstrated 'excellent transparency' (qualitative finding), addressing the low-transparency limitation the authors note in prior photocurable hydrogels; no single numeric transmittance percentage given in the retrieved abstract.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Hydrogel showed 'low swelling rate, enhanced mechanical properties, and superior adhesion properties' compared with hydrogels lacking the dual-network design (qualitative comparative finding); no specific numeric modulus, swelling-ratio, or adhesion-strength values given in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="In vitro: GelMA/OCS supported proliferation, migration, and adhesion growth of HCECs, demonstrating satisfactory cytocompatibility and cell affinity. In vivo (rabbit large 6 mm corneal defect model): hydrogel accurately filled defects forming smooth-surfaced grafts; postoperative slit-lamp, histological, and transcriptomic analyses showed significant facilitation of corneal re-epithelialization and integration/reconstruction of stromal structures, alongside reduced inflammatory responses and scar formation.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract (rabbit large corneal defect follow-up duration not given)",
        main_outcomes="A photocurable GelMA/OCS dual-network hydrogel, designed to overcome the low-transparency and poor-mechanical-property limitations of prior focal-defect-only photocurable hydrogels, achieved excellent transparency, low swelling, enhanced mechanical strength, and strong adhesion; it supported HCEC proliferation/migration/adhesion in vitro and, in a rabbit model of large (6 mm) corneal defects, accurately filled the defects and, per slit-lamp, histological, and transcriptomic analysis, significantly promoted re-epithelialization and stromal reconstruction while reducing inflammation and scar formation, supporting sutureless repair even of large corneal defects rather than only focal ones.",
        main_limitations="No quantitative transmittance, modulus, or swelling-ratio values given in the retrieved abstract despite comparative-improvement claims; rabbit (not primate/human) in vivo model; follow-up duration and sample size not specified; long-term (beyond initial postoperative assessment) transparency and integration durability not reported.",
        translational_readiness_level="preclinical (animal model, rabbit)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Small (Wiley), DOI 10.1002/smll.202500150, 2025 -- Wiley hybrid/subscription journal; open-access status of this specific article not confirmed this run; abstract-level extraction used. Notably addresses large (6 mm), not just focal, corneal defect repair -- an important scale distinction for the benchmarking table -- and is a close methodological companion to PUBMED_1006 (this batch, also a photocurable GelMA-based hybrid hydrogel for large-defect sutureless repair, 7 mm); useful paired entries for comparing GelMA/OCS versus GelMA/OHA/CMCS network designs.",
    ),
    "PUBMED_0928": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / decellularized xenogeneic (fish) scaffold study with in vitro recellularization and subcutaneous in vivo implantation (no orthotopic corneal implantation reported)",
        target_layer_final="stroma (whole-cornea-replacement candidate scaffold)",
        biomaterial_category="decellularized xenogeneic (fish swim bladder) collagen matrix scaffold",
        specific_materials="decellularized swim bladder collagen matrix (SBCM) scaffold, elastin-fiber-preserving, dehydrated and cross-linked",
        fabrication_method="swim bladder tissue decellularized using a freezing-and-thawing process combined with 0.5% sodium deoxycholate and nuclease treatment, chosen specifically to preserve natural elastin fibers and enhance the scaffold's elastic properties; scaffold subsequently dehydrated and cross-linked, which increased light transmittance to 93.1 +/- 0.8% (slightly higher than human cornea) and further improved mechanical properties; recellularization tested in vitro with rabbit corneal epithelial cells (RCECs) and rabbit corneal stromal cells (RCSCs); subcutaneous implantation performed in vivo to assess inflammatory response and anti-degradation ability versus human amniotic membrane",
        scaffold_architecture="decellularized, elastin-fiber-preserving fish swim bladder collagen matrix, dehydrated and cross-linked for enhanced optical and mechanical performance",
        cell_type_used="rabbit corneal epithelial cells (RCECs) and rabbit corneal stromal cells (RCSCs)",
        cell_source="rabbit (corneal epithelial and stromal cells, source not further specified as primary vs. cell line in the retrieved abstract)",
        growth_factors_or_bioactive_agents="none reported; sodium deoxycholate and nuclease used only as decellularization processing reagents, not as bioactive/therapeutic agents",
        optical_transparency_reported="yes",
        optical_metric_details="Dehydration and cross-linking increased light transmittance of the decellularized swim bladder scaffold to 93.1 +/- 0.8%, reported as slightly higher than that of human corneas (specific human comparator numeric value not given in the retrieved abstract).",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Cross-linking improved mechanical properties: circumferential fracture tensile stress 25.66 +/- 4.42 MPa, elastic modulus 184.43 +/- 23.27 MPa, and suture strength 123.5 +/- 2.69 gf -- reported by the authors as far superior to most previously reported biocorneal scaffolds.",
        biological_testing_reported="yes",
        biological_metric_details="Decellularized swim bladder collagen matrix scaffolds (SBCMs) supported proliferation and adhesion of rabbit corneal epithelial cells (RCECs) and rabbit corneal stromal cells (RCSCs) in vitro. Subcutaneous implantation in vivo revealed a lower acute inflammatory response and better anti-degradation ability compared with human amniotic membranes used clinically.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract (subcutaneous implantation follow-up duration not given)",
        main_outcomes="A decellularized fish swim bladder collagen matrix scaffold (SBCM), processed via a freeze-thaw/sodium-deoxycholate/nuclease protocol designed to preserve natural elastin fibers, achieved light transmittance of 93.1 +/- 0.8% (slightly exceeding human cornea) and strong mechanical performance (circumferential fracture tensile stress 25.66 +/- 4.42 MPa, elastic modulus 184.43 +/- 23.27 MPa, suture strength 123.5 +/- 2.69 gf) after dehydration/cross-linking, exceeding most previously reported biocorneal scaffolds; it supported rabbit corneal epithelial and stromal cell proliferation/adhesion in vitro, and subcutaneous implantation showed a lower acute inflammatory response and better anti-degradation ability than clinically used human amniotic membrane -- positioning decellularized swim bladder as a novel, elastic, highly transparent, and mechanically robust candidate corneal scaffold material.",
        main_limitations="No orthotopic (in-eye) corneal implantation was performed in this study -- the only in vivo evidence is subcutaneous implantation for inflammatory-response/anti-degradation assessment, so functional corneal transparency, suture retention, and integration in an actual corneal defect model remain undemonstrated; fish species used for the swim bladder source is not specified in the retrieved abstract; xenogeneic (non-mammalian) tissue source carries unique immunogenicity/regulatory considerations not addressed in the abstract; no human corneal comparator numeric transmittance value given for direct statistical comparison.",
        translational_readiness_level="early preclinical (in vitro plus subcutaneous animal model; not yet an orthotopic corneal implantation study)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Journal of Materials Chemistry B (RSC), DOI 10.1039/d5tb00793c, 2025 -- RSC hybrid/subscription journal; open-access status of this specific article not confirmed this run; abstract-level extraction used. Notable for one of the richest quantitative optical/mechanical datasets among Tier 1 records processed so far (explicit transmittance %, tensile stress, elastic modulus, and suture strength with error bars) and for an unusual, low-cost xenogeneic tissue source (fish swim bladder rather than porcine/human) -- high value for the review's optical/mechanical benchmarking table despite the absence of orthotopic corneal implantation data.",
    ),
    "PUBMED_1006": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / photocurable hybrid hydrogel study with in vitro and in vivo evaluation (large corneal defect model, 7 mm defect)",
        target_layer_final="multiple_layers (epithelium + stroma; large-area defect repair)",
        biomaterial_category="photocurable hybrid natural-polymer hydrogel",
        specific_materials="GOC hydrogel: gelatin methacryloyl (GelMA), oxidized hyaluronic acid (OHA), and carboxymethyl chitosan (CMCS)",
        fabrication_method="GelMA, OHA, and CMCS combined and photocured to form an injectable hybrid hydrogel (GOC); evaluated in vitro for cytocompatibility with human corneal epithelial cells (HCECs); injected to fill large (7 mm) corneal defects, producing grafts with smooth surfaces; evaluated using slit-lamp microscopy, anterior-segment optical coherence tomography (AS-OCT), confocal microscopy, and histological evaluation",
        scaffold_architecture="injectable, photocured hybrid hydrogel network with low swelling rate, tunable mechanical performance, and adhesive properties; fills large (7 mm) corneal defects with a smooth-surfaced graft",
        cell_type_used="human corneal epithelial cells (HCECs)",
        cell_source="human corneal epithelial cells (in vitro proliferation/migration assay); in vivo large-defect model species not explicitly stated in the retrieved abstract (host tissue repopulation, no exogenous cell seeding reported for the in vivo arm)",
        growth_factors_or_bioactive_agents="none reported; oxidized hyaluronic acid and carboxymethyl chitosan serve as structural/crosslinking network components rather than bioactive/growth factors",
        optical_transparency_reported="yes",
        optical_metric_details="GOC hydrogel exhibited 'superior transparency' (qualitative finding), addressing the low-transparency limitation the authors note in prior focal-defect-focused photocurable hydrogels; no single numeric transmittance percentage given in the retrieved abstract.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Hydrogel demonstrated 'low swelling rate, tunable mechanical performance, and excellent adhesive properties' (qualitative finding); no specific numeric modulus, swelling-ratio, or adhesion-strength values given in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="In vitro: GOC hydrogel supported proliferation and migration of HCECs, indicating satisfactory cytocompatibility. In vivo (large 7 mm corneal defect model): hydrogel accurately filled defects and produced grafts with smooth surfaces; slit-lamp microscopy, AS-OCT, confocal microscopy, and histological evaluation showed effective repair via facilitated re-epithelialization and stromal reconstruction, alongside reduced inflammatory responses and corneal scarring.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract (large corneal defect in vivo follow-up duration not given)",
        main_outcomes="A photocurable hybrid hydrogel combining GelMA, oxidized hyaluronic acid, and carboxymethyl chitosan (GOC), designed to overcome the low mechanical strength and poor adhesion of prior focal-defect-only photocurable hydrogels, achieved superior transparency, low swelling, tunable mechanical performance, and excellent adhesion; it supported HCEC proliferation/migration in vitro and, in a large (7 mm) corneal defect model assessed by slit-lamp, AS-OCT, confocal microscopy, and histology, effectively repaired defects by facilitating re-epithelialization and stromal reconstruction while reducing inflammation and scarring, supporting sutureless repair of large, not just focal, corneal defects.",
        main_limitations="No quantitative transmittance, modulus, or swelling-ratio values given in the retrieved abstract despite superiority claims; in vivo animal species not explicitly specified in the retrieved abstract; follow-up duration and sample size not specified; long-term transparency and integration durability beyond the reported imaging/histology timepoints not detailed.",
        translational_readiness_level="preclinical (animal model)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "International Journal of Biological Macromolecules (Elsevier), DOI 10.1016/j.ijbiomac.2025.148835, 2025 -- Elsevier hybrid/subscription journal; open-access status of this specific article not confirmed this run; abstract-level extraction used. Close methodological companion to PUBMED_0907 (this batch): both are photocurable GelMA-based hybrid hydrogels developed for sutureless repair of large corneal defects (6 mm vs. 7 mm) using different secondary polysaccharide networks (oxidized chondroitin sulfate vs. oxidized hyaluronic acid + carboxymethyl chitosan) -- valuable paired entries for the review's large-defect sutureless-hydrogel benchmarking narrative.",
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

OA_IDS = {"PUBMED_0688", "PUBMED_0770", "PUBMED_0877"}
SUBSCRIPTION_IDS = {"PUBMED_0646", "PUBMED_0719", "PUBMED_0907", "PUBMED_0928", "PUBMED_1006"}

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
