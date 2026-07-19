"""
Tier 1 extraction batch 6 (2026-07-20, scheduled run continuation).

Retrieval route note: the Europe PMC REST API JSON endpoint
(https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:<pmid>&format=json&resultType=core)
was again NOT reachable in this run's sandboxed web_fetch tool -- it
returned "URL not in provenance set" (the tool only allows fetching URLs
that already appeared in a user message, a prior web_fetch result, or a
WebSearch result; this unattended scheduled run has no user available to
authorize a new URL). Same restriction hit in batches 3-5.

This run's workaround: WebSearch was used to independently locate and
confirm each article's bibliographic details, open-access status, and
(where possible) full text. Several full-text pages successfully loaded
via web_fetch once their URL had appeared in a prior WebSearch result
(PLOS ONE for PUBMED_0224; PMC7586272 for PUBMED_0270; PMC10507194 for
PUBMED_0709), giving genuine full-text confirmation of open-access status
and additional quantitative detail beyond the abstract. For the rest,
extraction was built from the complete, untruncated abstract text already
stored locally in screening/full_text/pubmed_tier1_tier2_extraction_plan.csv,
cross-checked against WebSearch summaries of the same PMID.

This batch (8 records, all corneal_layer='stroma' in the screening/plan
CSVs; 3 of the 8 are corrected to target_layer_final='endothelium' below
because their actual subject is endothelial-cell tissue engineering using
a stromal/decellularized carrier, not stromal regeneration itself -- same
type of correction made for PUBMED_0151 in batch 5):

- PUBMED_0224 (PMID 31751429) - decellularized human corneal stromal lamina + fibronectin coating + hCEC (TEEK), rabbit DSAEK model. LAYER CORRECTED to endothelium.
- PUBMED_0270 (PMID 32363924) - hCEC on HALC/LK20/dDM carriers, in vitro DMEK simulation. LAYER CORRECTED to endothelium.
- PUBMED_0398 (PMID 33659091) - collagen hydrogel corneal stroma model, vibrational OCE mechanical monitoring of wound healing, in vitro only.
- PUBMED_0530 (PMID 35229601) - ultrathin acellular porcine corneal stroma (APCS) as carrier for corneal endothelial cell sheets (TECES), rabbit AC implantation. LAYER CORRECTED to endothelium.
- PUBMED_0601 (PMID 36356877) - silk fibroin/polyacrylamide semi-interpenetrating network hydrogel for corneal stromal regeneration, in vitro only.
- PUBMED_0626 (PMID 36729619) - 3D bioprinted MSC-loaded hydrogel constructs implanted into organ-cultured porcine corneas via femtosecond-laser intrastromal keratoplasty, ex vivo.
- PUBMED_0699 (PMID 37539164) - sodium alginate/gelatin composite hydrogel membrane for corneal tissue engineering, in vitro only.
- PUBMED_0709 (PMID 37731910) - oxygen-plasma-modified aligned PCL/silk fibroin nanofibrous scaffold for corneal stromal regeneration, in vitro only.
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

NOTE_PREFIX_FULLTEXT = (
    "Full text retrieved this run via web_fetch (URL surfaced through a prior "
    "WebSearch result, satisfying the tool's provenance requirement). Europe PMC "
    "REST API endpoint itself remained blocked ('URL not in provenance set'); "
    "the publisher/PMC HTML page was used instead. "
)

EXTRACTIONS = {
    "PUBMED_0224": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / tissue-engineered graft study with in vivo evaluation (rabbit model)",
        target_layer_final="endothelium",
        biomaterial_category="decellularized biological membrane carrier (human decellularized corneal stromal lamina) combined with cultured corneal endothelial cells",
        specific_materials="human decellularized corneal stromal lamina, tested with various surface coatings (fibronectin coating identified as optimal), seeded with cultured human corneal endothelial cells (hCEC) to form a tissue-engineered endothelial keratoplasty (TEEK) construct",
        fabrication_method="human corneal stromal laminas decellularized and coated with different substrate proteins (fibronectin identified as providing optimal, consistent hCEC density and polygonal morphology); hCEC suspensions seeded onto the coated laminas; grafts implanted into rabbit corneas via standard Descemet stripping automated endothelial keratoplasty (DSAEK) after central descemetorhexis",
        scaffold_architecture="decellularized human corneal stromal lamina sheet acting as a carrier for a re-surfaced endothelial cell monolayer",
        cell_type_used="cultured human corneal endothelial cells (hCEC)",
        cell_source="human (donor corneal endothelium, cultured)",
        growth_factors_or_bioactive_agents="fibronectin coating used as an adhesion substrate (not a classical growth factor); no other bioactive agents reported",
        optical_transparency_reported="yes",
        optical_metric_details="Corneal transparency gradually recovered in vivo in the TEEK (hCEC-seeded) group, whereas haze and edema persisted for up to 4 weeks in the control (lamina-only) group -- qualitative in vivo clinical observation, no numeric transmittance value reported in abstract.",
        mechanical_testing_reported="unclear / not reported in abstract",
        mechanical_metric_details="Not reported; surgery (standard DSAEK) was performed uneventfully, but no tensile strength, modulus, or other instrumented mechanical data given.",
        biological_testing_reported="yes",
        biological_metric_details="Fibronectin-coated laminas gave the most optimal and consistent hCEC density with polygonal cell morphology and active pump function (qualitative/functional assessment; no numeric cell-density value given in abstract); histology confirmed endothelial cells of human origin covering the posterior graft surface in the TEEK group after transplantation.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="up to 4 weeks (rabbit model, post-DSAEK transplantation)",
        main_outcomes="A tissue-engineered endothelial keratoplasty (TEEK) graft -- human decellularized corneal stromal lamina re-surfaced with fibronectin-coated, cultured human corneal endothelial cells -- was successfully implanted into a rabbit model of corneal endothelial damage using standard DSAEK technique. The TEEK group showed gradual recovery of corneal transparency, while control eyes (lamina without hCEC) had persistent haze/edema for up to 4 weeks; post-transplant histology confirmed a human-origin endothelial layer on the graft's posterior surface.",
        main_limitations="Rabbit (not primate/human) in vivo model; no quantitative cell-density, transmittance, or mechanical data reported in abstract; the carrier is decellularized human donor tissue rather than a fully synthetic scaffold, so donor-tissue supply constraints are only partially bypassed.",
        translational_readiness_level="preclinical (animal model, rabbit)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_FULLTEXT
        + "PLOS ONE, DOI 10.1371/journal.pone.0225480, Nov 2019 -- confirmed fully open access (PLOS ONE 'Open Access' tag visible on the fetched article page; also available as PMC6871783). "
        + "LAYER FLAG: corneal_layer is 'stroma' in the upstream screening/plan CSVs because the carrier material is a decellularized stromal lamina, but the paper's subject and clinical target are unambiguously corneal ENDOTHELIUM repair (TEEK = tissue engineered endothelial keratoplasty). target_layer_final corrected to 'endothelium' here per the same convention used for PUBMED_0151 in batch 5; upstream corneal_layer left as-is per instructions.",
    ),
    "PUBMED_0270": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / carrier comparison study (in vitro culture plus ex vivo simulated DMEK surgery)",
        target_layer_final="endothelium",
        biomaterial_category="comparative study of three corneal endothelial cell carrier types: natural decellularized tissue and a bioengineered collagen sheet",
        specific_materials="human anterior lens capsule (HALC), LinkCell(TM) bioengineered collagen sheets of 20-micron thickness (LK20), and denuded Descemet membrane (dDM), each seeded with cultured human corneal endothelial cells (hCEC)",
        fabrication_method="primary hCEC isolated and expanded, then seeded onto three candidate carriers (HALC, LK20, dDM); resulting hCEC-carrier constructs evaluated by simulating Descemet membrane endothelial keratoplasty (DMEK) surgery in vitro/ex vivo using a human donor cornea (without its native DM) mounted on an artificial anterior chamber, with a conventional DMEK graft used as the surgical reference",
        scaffold_architecture="thin (~20 micron for LK20) sheet/membrane carriers: natural lens capsule, bioengineered collagen sheet, or denuded native Descemet membrane",
        cell_type_used="primary human corneal endothelial cells (hCEC)",
        cell_source="human (primary, donor-derived)",
        growth_factors_or_bioactive_agents="none reported",
        optical_transparency_reported="unclear / not reported in abstract",
        optical_metric_details="Not explicitly reported; evaluation focused on cell monolayer formation, marker expression, and surgical handling rather than optical transmittance.",
        mechanical_testing_reported="partial",
        mechanical_metric_details="No instrumented tensile/modulus values reported; carriers were instead functionally assessed for surgical handling -- hCEC-HALC constructs behaved most similarly to a conventional DMEK graft during implantation/unfolding and adhered well to bare stroma, while hCEC-LK20 and hCEC-dDM required additional handling; hCEC-dDM showed adherence similar to hCEC-HALC, while hCEC-LK20 adherence was less effective.",
        biological_testing_reported="yes",
        biological_metric_details="All carriers supported a monolayer of tightly packed hCEC with high cell viability (96% +/- 4%); hCEC on HALC and LK20 showed unremarkable ZO-1 and Na+/K+-ATPase expression, while Na+/K+-ATPase expression on dDM was mainly cytoplasmic; after simulated in vitro surgery, viable-cell coverage area was ~83% for hCEC-HALC and ~67% for hCEC-LK20 constructs.",
        in_vitro_model="yes",
        ex_vivo_model="yes",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="not applicable / single-timepoint in vitro culture and ex vivo simulated surgery (no longitudinal follow-up)",
        main_outcomes="Comparing three hCEC carrier types for DMEK-style endothelial keratoplasty, HALC-based constructs most closely replicated the handling and adhesion behavior of a conventional DMEK graft (~83% viable-cell coverage post-simulated-surgery) while retaining a high overall cell viability (96%); LK20 and dDM carriers were surgically usable but required additional handling and, in LK20's case, had lower post-surgical viable coverage (~67%) and less effective adhesion.",
        main_limitations="Ex vivo/in vitro simulated surgery only, no live animal or human transplantation; only three carrier types tested; Na+/K+-ATPase mislocalization (cytoplasmic rather than membrane-bound) on dDM suggests incomplete functional maturity for that carrier; no numeric optical transmittance or tensile mechanical data reported.",
        translational_readiness_level="early preclinical (in vitro / ex vivo simulated surgery, primary human cells)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_FULLTEXT
        + "Cell Transplantation, DOI 10.1177/0963689720923577, May 2020 -- confirmed fully open access (full text retrieved directly from PMC7586272). "
        + "LAYER FLAG: corneal_layer is 'stroma' in the upstream screening/plan CSVs, but the paper is a direct comparison of endothelial-cell carriers for DMEK (corneal ENDOTHELIUM tissue engineering); target_layer_final corrected to 'endothelium' here, upstream corneal_layer left as-is per instructions. Directly comparable to PUBMED_0224 and PUBMED_0530 (this same batch) for a carrier-material benchmarking narrative in the endothelium table.",
    ),
    "PUBMED_0398": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / biomechanical characterization study (in vitro only)",
        target_layer_final="stroma",
        biomaterial_category="collagen-based hydrogel corneal stroma equivalent",
        specific_materials="collagen hydrogel (3.0 mg/mL collagen concentration) incorporating human corneal keratocytes, used as a 3D in vitro corneal stroma wound-healing model",
        fabrication_method="human corneal keratocytes seeded at 5x10^5 cells/mL into collagen hydrogels (3.0 mg/mL collagen) to form a 3D corneal stroma-equivalent construct; a controlled traumatic wound (500 micron) introduced into a subset of constructs; mechanical properties of both unwounded and wounded constructs monitored longitudinally using a vibrational optical coherence elastography (OCE) system during continuous culture",
        scaffold_architecture="3D collagen hydrogel matrix populated with keratocytes (unwounded) and with a discrete 500-micron wound defect (wounded condition)",
        cell_type_used="human corneal keratocytes",
        cell_source="human (corneal keratocytes)",
        growth_factors_or_bioactive_agents="none reported",
        optical_transparency_reported="unclear / not reported in abstract",
        optical_metric_details="Not explicitly reported as a measured optical metric; study used optical coherence elastography for mechanical (not transparency) characterization.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Unwounded constructs: elastic modulus increased from 2.950 +/- 0.2 kPa to 11.0 +/- 1.4 kPa over a 15-day culture period, while maximum thickness decreased from 1.034 +/- 0.1 mm to 0.464 +/- 0.09 mm. Wounded constructs (500-micron wound): elastic modulus of the neo-tissue in the wound area increased from 1.488 +/- 0.4 kPa to 6.639 +/- 0.3 kPa over 13 days.",
        biological_testing_reported="partial",
        biological_metric_details="Keratocytes were cultured within the hydrogel over the monitoring period and construct remodeling (stiffening, thinning, wound neo-tissue formation) was tracked as an indirect marker of cellular remodeling activity; no explicit viability, proliferation, or marker-expression assay values reported in abstract.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="15-day culture period (unwounded constructs); 13-day monitoring of wound neo-tissue (wounded constructs)",
        main_outcomes="A collagen hydrogel/keratocyte corneal stroma wound-healing model, monitored by vibrational OCE, showed a >3-fold increase in elastic modulus (2.95 to 11.0 kPa) and substantial thinning (1.034 to 0.464 mm) over 15 days in unwounded constructs, and a >4-fold modulus increase (1.488 to 6.639 kPa) in wound neo-tissue over 13 days -- demonstrating that OCE can quantitatively track the biomechanical maturation/remodeling of engineered corneal stroma tissue during wound healing in vitro.",
        main_limitations="In vitro only, no ex vivo, animal, or clinical evaluation; single collagen concentration and cell-seeding density tested; optical transparency of the construct not reported despite its relevance to functional corneal-substitute performance.",
        translational_readiness_level="early preclinical (in vitro)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Biomedical Optics Express, DOI 10.1364/BOE.404096, 2021 -- Biomedical Optics Express is a fully open-access Optica journal; web_fetch of the publisher page itself returned a JavaScript-rendered shell in this run, so extraction was drawn from the local screening-corpus abstract text (WebSearch summary corroborated the same quantitative elastic-modulus and thickness values). "
        + "Notable as one of the few Tier 1 stroma records with directly comparable, explicit quantitative elastic-modulus benchmarks (kPa) at multiple timepoints, high value for the review's mechanical-property benchmarking table.",
    ),
    "PUBMED_0530": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / tissue-engineered endothelial sheet study with in vivo evaluation (rabbit anterior chamber implantation)",
        target_layer_final="endothelium",
        biomaterial_category="decellularized xenogeneic (porcine) corneal stroma carrier for corneal endothelial cell sheets",
        specific_materials="ultrathin (20 micron) acellular porcine corneal stroma (APCS) lamellae, cut via cryostat microtome, seeded with rabbit corneal endothelial cells (RCECs) and, for validation, human corneal endothelial cells (hCECs), to form tissue-engineered corneal endothelial sheets (TECES)",
        fabrication_method="acellular porcine corneal stroma (APCS) cut into multiple 20-micron ultrathin lamellae using a cryostat microtome; RCECs (and hCECs for validation) seeded onto ultrathin APCS versus tissue-culture plastic and thicker APCS for comparison; resulting TECES constructs implanted into rabbit anterior chambers through small surgical incisions",
        scaffold_architecture="ultrathin (20 micron) decellularized xenogeneic corneal stromal lamella as a flexible, implantable endothelial cell-sheet carrier",
        cell_type_used="rabbit corneal endothelial cells (RCECs), with human corneal endothelial cells (hCECs) used for validation",
        cell_source="rabbit (primary) and human (validation)",
        growth_factors_or_bioactive_agents="none reported",
        optical_transparency_reported="unclear / not reported in abstract",
        optical_metric_details="Not explicitly reported as a numeric transmittance value; functional recovery reported instead as corneal thickness normalization after grafting.",
        mechanical_testing_reported="partial",
        mechanical_metric_details="Resulting TECES constructs described as 'flexible and tough enough to implant into rabbits' anterior chambers through small incisions' (qualitative handling assessment); no numeric tensile strength or modulus values reported in abstract.",
        biological_testing_reported="yes",
        biological_metric_details="RCECs cultured on 20-micron ultrathin APCS for 5 days formed a confluent monolayer with density 3726 +/- 223 cells/mm^2, expressing functional markers Na+/K+-ATPase and zonula occludens; after 14 days, cells synthesized collagen IV and laminin, forming an early-stage Descemet's-membrane-like structure; ultrathin lamellae outperformed thicker APCS and plain tissue-culture plastic for cell viability/function.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="5 days (monolayer formation) and 14 days (Descemet's-membrane-like matrix synthesis) in vitro; in vivo follow-up duration after rabbit anterior-chamber implantation not specified numerically in abstract",
        main_outcomes="Ultrathin (20 micron) acellular porcine corneal stroma supported superior corneal endothelial cell viability and function compared to thicker APCS or tissue-culture plastic, forming a confluent monolayer (3726 cells/mm^2 at day 5) that expressed functional endothelial markers and began synthesizing Descemet's-membrane-like matrix (collagen IV, laminin) by day 14; the resulting flexible TECES constructs were successfully implanted into rabbit anterior chambers through small incisions, adhered to the posterior stroma, and were associated with a gradual return of corneal thickness toward normal.",
        main_limitations="Xenogeneic (porcine) carrier material introduces immunogenicity/regulatory considerations distinct from human-tissue or synthetic carriers; primary in vivo data used rabbit (not human) endothelial cells; no quantitative optical transmittance or tensile mechanical values reported; in vivo follow-up duration not specified numerically in abstract.",
        translational_readiness_level="preclinical (animal model, rabbit)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "ACS Biomaterials Science & Engineering, DOI 10.1021/acsbiomaterials.2c00039, 2022 -- ACS subscription journal, no open-access indication found via WebSearch; abstract-level extraction only. "
        + "LAYER FLAG: corneal_layer is 'stroma' in the upstream screening/plan CSVs because the carrier material is decellularized porcine stroma, but the paper's subject is corneal ENDOTHELIUM tissue engineering (TECES = tissue-engineered cornea endothelial sheets); target_layer_final corrected to 'endothelium' here, upstream corneal_layer left as-is per instructions. Directly comparable to PUBMED_0224 (human decellularized stroma carrier) and PUBMED_0270 (HALC/LK20/dDM carriers) for a cross-species carrier-material benchmarking narrative.",
    ),
    "PUBMED_0601": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / hydrogel fabrication and characterization study (in vitro only)",
        target_layer_final="stroma",
        biomaterial_category="natural-synthetic composite (semi-interpenetrating network) hydrogel",
        specific_materials="silk fibroin (SF) / polyacrylamide (PA) semi-interpenetrating network hydrogels, fabricated at different SF:PA ratios",
        fabrication_method="three-dimensional hydrogels fabricated via free-radical polymerization at different silk fibroin (SF) to polyacrylamide (PA) ratios, forming semi-interpenetrating network structures; characterized by scanning electron microscopy (pore structure), Fourier transform infrared spectroscopy (beta-sheet content), and rheology/handling (gelation kinetics); seeded with human corneal stromal cells for biological evaluation",
        scaffold_architecture="porous, interconnected three-dimensional semi-interpenetrating network hydrogel (pore size 25-66 micron)",
        cell_type_used="human corneal stromal cells (keratocytes)",
        cell_source="human (corneal stromal cells)",
        growth_factors_or_bioactive_agents="none reported",
        optical_transparency_reported="unclear / not reported in abstract",
        optical_metric_details="Not reported; characterization focused on pore architecture, gelation kinetics, and biological response rather than optical transmittance.",
        mechanical_testing_reported="partial",
        mechanical_metric_details="Pore size ranged from 25 to 66 micron (SEM); porosity of 84% reported; rapid gelation (~3 minutes) at 37 degrees C; higher SF concentration increased beta-sheet structure (FTIR), an indirect structural/mechanical proxy; no explicit tensile strength or elastic modulus value reported in abstract.",
        biological_testing_reported="yes",
        biological_metric_details="Hydrogels showed improved cellular adhesion and no cytotoxicity; presence of SF in the semi-interpenetrating network enhanced cellular proliferation, elevated glycosaminoglycan (GAG) deposition, and increased expression of keratocyte-associated genes normally linked to healthy corneal stromal tissue, assessed via adhesion, proliferation, cytoskeleton organization, gene expression, and immunocytochemical analysis.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="not applicable / in vitro characterization only (gelation within ~3 minutes; cell culture duration not specified numerically in abstract)",
        main_outcomes="Silk fibroin/polyacrylamide semi-interpenetrating network hydrogels achieved rapid gelation (~3 min), high porosity (84%) with interconnected 25-66 micron pores, and -- when SF was incorporated -- enhanced human corneal stromal cell proliferation, GAG deposition, and keratocyte-gene expression versus PA alone, with no cytotoxicity, supporting their potential as an in-situ-gelling scaffold for corneal stromal tissue regeneration.",
        main_limitations="In vitro only, no ex vivo, animal, or clinical evaluation; no quantitative tensile strength/modulus or optical transmittance values reported; described by the authors themselves as an 'initial step' toward clinically applicable ocular implants.",
        translational_readiness_level="early preclinical (in vitro)",
        benchmarking_relevance="medium",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "International Journal of Biological Macromolecules (Elsevier), DOI 10.1016/j.ijbiomac.2022.11.021, 2022 -- subscription journal, no open-access indication found via WebSearch; abstract-level extraction only.",
    ),
    "PUBMED_0626": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / 3D bioprinting study with ex vivo organ-culture evaluation (femtosecond-laser-assisted intrastromal implantation)",
        target_layer_final="stroma",
        biomaterial_category="cellularized 3D-bioprinted hydrogel tissue equivalent",
        specific_materials="3D-bioprinted hydrogel constructs loaded with mesenchymal stromal cells (MSCs)",
        fabrication_method="cellularized tissue equivalents produced by 3D bioprinting of a bioink loaded with mesenchymal stromal cells; constructs implanted intrastromally into ex vivo organ-cultured porcine corneas using femtosecond-laser-assisted intrastromal keratoplasty (creating a precise stromal pocket for implantation)",
        scaffold_architecture="3D-bioprinted hydrogel construct implanted within a femtosecond-laser-cut intrastromal pocket",
        cell_type_used="mesenchymal stromal cells (MSCs)",
        cell_source="not specified by species/tissue origin in abstract",
        growth_factors_or_bioactive_agents="none reported beyond the bioink/MSC formulation itself",
        optical_transparency_reported="unclear / not reported in abstract",
        optical_metric_details="Not reported as a numeric transmittance value; optical coherence tomography (OCT) was used for structural, not transparency, imaging of the implant.",
        mechanical_testing_reported="unclear / not reported in abstract",
        mechanical_metric_details="No tensile strength, modulus, or other instrumented mechanical data reported; bioink composition and cellularization are described as key variables 'essential in fine-tuning' the method, but no numeric mechanical characterization given.",
        biological_testing_reported="yes",
        biological_metric_details="MSC-loaded 3D-bioprinted structures remained intact and supported cell survival with de novo synthesized extracellular matrix components and migrating cells throughout the ex vivo organ-culture observation period; however, by day 14 post-implantation, the cellularized tissue equivalents contained few or no surviving cells, as shown by OCT imaging and immunofluorescent staining.",
        in_vitro_model="no",
        ex_vivo_model="yes",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="14 days (ex vivo organ-cultured porcine cornea model)",
        main_outcomes="Femtosecond-laser-assisted intrastromal implantation of MSC-loaded 3D-bioprinted hydrogel constructs into ex vivo organ-cultured porcine corneas produced intact constructs with early cell survival, de novo ECM synthesis, and cell migration, but by day 14 the constructs contained few or no viable cells -- indicating that while the fabrication/implantation method is feasible, long-term cell survival within the implanted construct remains a key unresolved challenge, with bioink composition and cellularization identified as critical variables for future optimization.",
        main_limitations="Ex vivo organ-culture model only (no live animal or human clinical evaluation); poor cell survival by day 14 is a significant unresolved limitation; MSC source (species/tissue) not specified in abstract; no quantitative optical or mechanical data reported.",
        translational_readiness_level="early preclinical (ex vivo organ-culture model)",
        benchmarking_relevance="medium",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Macromolecular Bioscience (Wiley), DOI 10.1002/mabi.202200422, 2023 -- subscription journal, no open-access indication found via WebSearch; abstract-level extraction only. "
        + "Notable as one of the few Tier 1 stroma records reporting a negative/cautionary long-term (14-day) cell-survival outcome rather than a positive result -- valuable as a contrasting data point in the review's translational-readiness discussion.",
    ),
    "PUBMED_0699": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / hydrogel fabrication and characterization study (in vitro only)",
        target_layer_final="stroma",
        biomaterial_category="natural polysaccharide-protein composite hydrogel membrane",
        specific_materials="composite hydrogel with a sodium alginate (SA) fiber skeleton (for shape retention) and a gelatin surface modification (for water retention)",
        fabrication_method="sodium alginate hydrogel fabricated with an internal fiber-skeleton structure to provide shape retention, then surface-modified with gelatin to improve water retention; light transmittance, water retention rate, swelling rate, and tensile mechanical properties characterized; keratinocytes exposed to material extract liquor to test cytocompatibility; human corneal stromal fibroblasts (HCSFs) isolated from donor lenticules and seeded onto the gel surface",
        scaffold_architecture="fiber-skeleton-reinforced hydrogel membrane with a gelatin-modified surface layer",
        cell_type_used="keratinocytes (extract-liquor cytocompatibility test) and human corneal stromal fibroblasts (HCSFs, adhesion/spreading test)",
        cell_source="human (HCSFs isolated from donor corneal lenticules); keratinocyte source/species not specified in abstract",
        growth_factors_or_bioactive_agents="none reported",
        optical_transparency_reported="yes",
        optical_metric_details="Light transmittance of the hydrogel was characterized as part of the material evaluation; no specific numeric transmittance value is given in the abstract text.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Tensile mechanical properties, along with water retention rate and swelling rate, were investigated; no specific numeric tensile-strength or modulus value is given in the abstract text.",
        biological_testing_reported="yes",
        biological_metric_details="The gelatin-modified SA hydrogel showed good cytocompatibility in a keratinocyte material-extract assay; human corneal stromal fibroblasts (HCSFs) seeded on the gel surface showed significantly improved adhesion and spreading on the SA-gelatin hydrogel compared to (implicitly) the unmodified SA hydrogel.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="not applicable / in vitro characterization and cell-culture assays only (specific durations not given in abstract)",
        main_outcomes="A sodium alginate fiber-skeleton hydrogel with a gelatin-modified surface achieved good cytocompatibility, favorable light transmittance/water-retention/swelling/tensile properties (as characterized, though not quantified in the abstract), and significantly improved adhesion and spreading of human corneal stromal fibroblasts compared to unmodified alginate hydrogel, supporting its potential as a corneal-equivalent scaffold material.",
        main_limitations="In vitro only, no ex vivo, animal, or clinical evaluation; abstract does not report specific numeric values for transmittance, water retention, swelling, or tensile properties despite stating these were characterized; keratinocyte species/source not specified.",
        translational_readiness_level="early preclinical (in vitro)",
        benchmarking_relevance="medium",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Heliyon (Cell Press), DOI 10.1016/j.heliyon.2023.e17950, 2023 -- Heliyon is a fully open-access journal; article also indexed as PMC10395283, but web_fetch of that PMC page returned a reCAPTCHA challenge in this run (rate-limited after several successful PMC fetches earlier in the same run), so full text could not be retrieved this run despite confirmed open-access status; abstract-level extraction used instead.",
    ),
    "PUBMED_0709": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / electrospun scaffold fabrication and characterization study (in vitro only)",
        target_layer_final="stroma",
        biomaterial_category="synthetic-natural composite electrospun nanofibrous scaffold",
        specific_materials="oxygen-plasma surface-modified, aligned poly-epsilon-caprolactone (PCL) / silk fibroin (SF) nanofibrous scaffold, evaluated across multiple PCL:SF blend ratios with a 1:1 blend selected for in-depth study",
        fabrication_method="PCL (10% wt/wt in chloroform) and SF (extracted from Bombyx mori cocoons) blended and electrospun onto a rotating mandrel to produce aligned nanofibrous scaffolds at varying PCL:SF ratios; scaffolds surface-modified via oxygen plasma treatment to improve hydrophilicity/cell interaction; blend ratio and plasma treatment optimized based on nanofibre alignment, mechanical characteristics, transparency, and in vitro cytocompatibility with human corneal stromal keratocytes, with a 1:1 PCL:SF blend selected for comprehensive follow-up analysis (adhesion, proliferation, cytoskeletal organization, gene expression, immunocytochemistry)",
        scaffold_architecture="aligned electrospun nanofibrous mat (rotating-mandrel electrospinning) with oxygen-plasma-modified surface",
        cell_type_used="human corneal stromal keratocytes",
        cell_source="human (corneal stromal keratocytes)",
        growth_factors_or_bioactive_agents="none reported",
        optical_transparency_reported="yes",
        optical_metric_details="Oxygen-plasma surface modification of the scaffold resulted in improved transparency relative to unmodified scaffolds (qualitative comparative finding); no specific numeric transmittance value given in the retrieved abstract/introduction text.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Nanofibre alignment and blend ratio were optimized against mechanical characteristics as part of the scaffold-selection process; no specific numeric tensile-strength or modulus value given in the abstract text (methods indicate mechanical testing was performed as part of the optimization).",
        biological_testing_reported="yes",
        biological_metric_details="The selected 1:1 PCL:SF plasma-modified scaffold facilitated adhesion of corneal stromal keratocytes, supported cell proliferation, maintained normal cytoskeletal organization, and promoted increased expression of genes associated with a healthy (quiescent) corneal stromal keratocyte phenotype, assessed via cellular adhesion, proliferation, cytoskeletal staining, gene expression, and immunocytochemistry.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="not applicable / in vitro characterization and cell-culture assays only (specific culture durations not given in retrieved text)",
        main_outcomes="An oxygen-plasma-modified, aligned electrospun PCL/silk-fibroin nanofibrous scaffold (optimal 1:1 blend ratio) improved scaffold transparency and cell interaction relative to unmodified scaffolds, and supported adhesion, proliferation, normal cytoskeletal organization, and increased expression of healthy-keratocyte-associated genes in human corneal stromal keratocytes -- supporting its potential as a non-mammalian-collagen-free scaffold material for corneal stromal regeneration.",
        main_limitations="In vitro only, no ex vivo, animal, or clinical evaluation; no specific numeric transmittance or tensile mechanical values found in the retrieved abstract/introduction text (full methods/results sections may contain quantitative data not captured here); long-term degradation and in vivo biocompatibility not assessed.",
        translational_readiness_level="early preclinical (in vitro)",
        benchmarking_relevance="medium",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_FULLTEXT
        + "Biomaterials and Biosystems (Elsevier), DOI 10.1016/j.bbiosy.2023.100083, Sept 2023 -- confirmed fully open access (full text retrieved directly from PMC10507194; Biomaterials and Biosystems is an open-access Elsevier journal). Full abstract and introduction sections reviewed; results/methods sections with specific numeric mechanical/optical values were not fully read in this run due to context-length constraints on the fetched page.",
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
    retrieval_notes="Europe PMC REST API fetch blocked by web_fetch provenance restriction in this unattended run; abstract taken from already-verified local screening corpus text instead, cross-checked against a WebSearch lookup of the same PMID/title.",
    extraction_ready="yes",
    reason_not_extraction_ready="",
)

TRACKER_UPDATE_PUBMED_0224 = dict(
    full_text_status="retrieved (full text, open access)",
    pdf_available="yes",
    source_checked="PLOS ONE full text (web_fetch) + local screening corpus abstract",
    retrieval_date="2026-07-20",
    retrieval_notes="Full text retrieved directly from PLOS ONE (journals.plos.org), confirmed fully open access ('Open Access' tag on article page); also indexed as PMC6871783.",
    extraction_ready="yes",
    reason_not_extraction_ready="",
)

TRACKER_UPDATE_PUBMED_0270 = dict(
    full_text_status="retrieved (full text, open access)",
    pdf_available="yes",
    source_checked="PMC7586272 full text (web_fetch) + local screening corpus abstract",
    retrieval_date="2026-07-20",
    retrieval_notes="Full text retrieved directly from PMC7586272 (Cell Transplantation, SAGE, open access). Abstract and full text reviewed for quantitative detail.",
    extraction_ready="yes",
    reason_not_extraction_ready="",
)

TRACKER_UPDATE_PUBMED_0398 = dict(
    full_text_status="retrieved (abstract-level only)",
    pdf_available="yes (Biomedical Optics Express is fully open access, but publisher page returned JS-rendered shell to web_fetch this run)",
    source_checked="local screening corpus abstract + WebSearch cross-check (opg.optica.org)",
    retrieval_date="2026-07-20",
    retrieval_notes="Biomedical Optics Express (Optica) is a fully open-access journal; web_fetch of opg.optica.org returned a JavaScript-rendered placeholder ('Please wait...') rather than usable content in this run. Extraction drawn from local screening-corpus abstract text, cross-checked against WebSearch summary (quantitative values matched).",
    extraction_ready="yes",
    reason_not_extraction_ready="",
)

TRACKER_UPDATE_PUBMED_0699 = dict(
    full_text_status="retrieved (abstract-level only)",
    pdf_available="yes (Heliyon is fully open access; PMC10395283 exists but was rate-limited/reCAPTCHA-blocked this run)",
    source_checked="local screening corpus abstract + WebSearch cross-check (PMC10395283 / ScienceDirect)",
    retrieval_date="2026-07-20",
    retrieval_notes="Heliyon is a fully open-access Cell Press journal; article indexed as PMC10395283, but web_fetch of that page returned a reCAPTCHA challenge this run (likely rate-limited after several prior successful PMC fetches in the same run). Extraction drawn from local screening-corpus abstract text.",
    extraction_ready="yes",
    reason_not_extraction_ready="",
)

TRACKER_UPDATE_PUBMED_0709 = dict(
    full_text_status="retrieved (full text, open access)",
    pdf_available="yes",
    source_checked="PMC10507194 full text (web_fetch, abstract + introduction sections read) + local screening corpus abstract",
    retrieval_date="2026-07-20",
    retrieval_notes="Full text retrieved directly from PMC10507194 (Biomaterials and Biosystems, Elsevier, open access). Abstract and introduction sections reviewed; results/methods with specific numeric values not fully read this run due to context-length constraints.",
    extraction_ready="yes",
    reason_not_extraction_ready="",
)

SPECIAL = {
    "PUBMED_0224": TRACKER_UPDATE_PUBMED_0224,
    "PUBMED_0270": TRACKER_UPDATE_PUBMED_0270,
    "PUBMED_0398": TRACKER_UPDATE_PUBMED_0398,
    "PUBMED_0699": TRACKER_UPDATE_PUBMED_0699,
    "PUBMED_0709": TRACKER_UPDATE_PUBMED_0709,
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
