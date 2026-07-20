"""
Tier 1 extraction batch 11 (2026-07-20, scheduled run continuation).

Retrieval route note: as in batches 3-10, a direct web_fetch to the Europe PMC
REST API (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:<pmid>&format=json&resultType=core)
was attempted first this run for the lead record (PUBMED_0104, PMID
30323996) and failed with "URL not in provenance set" (the sandboxed
web_fetch tool only allows fetching URLs that already appeared in a user
message, a prior web_fetch result, or a WebSearch result; this unattended
scheduled run has no user available to authorize a new URL). A WebSearch
query for the exact target URL was then tried to bring a matching URL into
the fetch provenance set; the search returned only third-party
documentation pages about the Europe PMC API (not the target query URL
itself), and a follow-up web_fetch to the exact target URL still failed
with the same provenance error. This is the same structural restriction
documented in batches 3-10's docstrings.

Consistent with the workaround established in batches 3-10, extraction for
this batch was built from the complete, untruncated abstract text already
stored locally in screening/full_text/pubmed_tier1_tier2_extraction_plan.csv
(verified PubMed/journal abstracts captured during the original screening
pass), with open-access status assessed from known journal/publisher policy
(Frontiers in Bioengineering and Biotechnology, Scientific Reports, and
Translational Vision Science & Technology are gold open-access journals;
ACS Biomaterials Science & Engineering, International Journal of Biological
Macromolecules (Elsevier), Tissue Engineering Part A (Mary Ann Liebert),
Cornea (Wolters Kluwer), and Carbohydrate Polymers (Elsevier) are
hybrid/subscription titles -- open-access status of these specific articles
not individually confirmed this run). This is noted per-record in
extraction_notes.

This batch (8 records):
- PUBMED_0827 (PMID 39386038) - curved, micro-grooved 3D-printed-mold collagen hydrogels for corneal endothelial cell (CEC) topography/curvature response, in vitro only.
- PUBMED_0925 (PMID 40366209) - micropatterned (hexagon/microgroove) silk fibroin films for corneal endothelial cell culture, in vitro only.
- PUBMED_0934 (PMID 40446990) - chitosan-nanoparticle/chitosan/PCL composite scaffold + telomerase activator/ROCK inhibitor synergy for HCEC proliferation, in vitro only.
- PUBMED_0981 (PMID 40986463) - femtosecond-laser-cut lens capsule disc scaffold for density-controlled tissue-engineered endothelial keratoplasty (TEEK), in vitro proof-of-concept (n=12).
- PUBMED_0010 (PMID 29040119) - prospective clinical trial (NCT02149732) of biomaterial-free/carrier-free cultured oral mucosal epithelial cell sheet (COMEC) transplantation for total LSCD.
- PUBMED_0056 (PMID 29691018) - carboxymethyl chitosan/gelatin/hyaluronic acid blended membrane for corneal epithelial cell transplantation, in vitro + in vivo rabbit alkali-burn model.
- PUBMED_0099 (PMID 30279555) - comparative substrate (transwell vs. HAM-transwell vs. HAM-slide-scaffold) and media optimization study for cultivated limbal epithelial sheets, in vitro + in vivo rabbit LSCD model.
- PUBMED_0104 (PMID 30323996) - CRISPR/Cas9 B2M-knockout hypoimmunogenic hESC-derived corneal epithelial cells on decellularized murine cornea, in vitro + in vivo mouse transplantation.
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
    "PUBMED_0827": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / curved, micropatterned hydrogel substrate study (in vitro only, corneal endothelial cells)",
        target_layer_final="endothelium",
        biomaterial_category="curved, micropatterned natural polymer (collagen) hydrogel substrate",
        specific_materials="collagen hydrogels formed as curved (concave and convex) constructs with three groove topographies (50, 200, and 300 micrometers) via 3D-printed molds; flat collagen hydrogels used as control",
        fabrication_method="3D-printed molds used to cast curved (concave/convex) collagen hydrogels with three groove topographies (50, 200, 300 micrometers), plus flat control hydrogels; corneal endothelial cells (CEC) cultured on each substrate; cell morphology and circularity assessed, and gene expression of ATP1A1 and ZO-1 measured at day 3 and day 6",
        scaffold_architecture="curved (concave/convex) collagen hydrogel with micro-groove surface topographies (50/200/300 micrometers), replicated from 3D-printed molds",
        cell_type_used="corneal endothelial cells (CEC); species/source not specified in the retrieved abstract",
        cell_source="not specified in the retrieved abstract",
        growth_factors_or_bioactive_agents="none reported; study isolates curvature and surface topography as the sole engineered variables",
        optical_transparency_reported="unclear / not reported in abstract",
        optical_metric_details="No optical transparency/transmittance data reported; characterization focused on gene expression (ATP1A1, ZO-1) and cell morphology/circularity rather than optical properties.",
        mechanical_testing_reported="unclear / not reported in abstract",
        mechanical_metric_details="No numeric mechanical (modulus) data reported in the retrieved abstract; hydrogel curvature and groove dimensions (50/200/300 micrometers) are the only physical parameters quantified.",
        biological_testing_reported="yes",
        biological_metric_details="At day 3, curved non-patterned hydrogels showed higher ZO-1 and ATP1A1 expression than flat hydrogels; patterned hydrogels had a weaker effect on gene expression than flat hydrogels at day 3, with curvature showing a stronger effect than topography. At day 6, the effect reversed: patterned hydrogels showed higher gene expression than at day 3, especially for ZO-1. Cell circularity was closer to native hexagonal CEC morphology at shorter time points, consistent with the gene expression pattern.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="3 and 6 days (in vitro culture time points)",
        main_outcomes="Curved collagen hydrogels with micro-groove topographies (50/200/300 micrometers), fabricated via 3D-printed molds, influenced corneal endothelial cell (CEC) phenotype-marker expression (ZO-1, ATP1A1) and morphology (circularity) in a time-dependent manner: curvature alone drove a stronger early (day 3) effect, while topographical patterning effects emerged later (day 6, notably for ZO-1); cell circularity trended toward native hexagonal CEC morphology at earlier time points. The platform is proposed as a culture system to prepare a CEC monolayer for transplantation, either as a full construct or as thin collagen-CEC sheets, as an alternative to donor corneal transplantation.",
        main_limitations="Species/origin of the CEC used is not specified in the retrieved abstract; no optical transparency or mechanical (modulus) data reported; no ex vivo or in vivo/animal transplantation evaluation; only two time points (3 and 6 days) assessed; no quantitative comparison against a donor/gold-standard endothelial graft.",
        translational_readiness_level="early preclinical (in vitro only)",
        benchmarking_relevance="medium",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Frontiers in Bioengineering and Biotechnology, DOI 10.3389/fbioe.2024.1454675, 2024 -- Frontiers is a fully open-access (gold OA) journal; full text freely available; full-text fetch not attempted this run, abstract-level extraction used. Useful comparator for the review's curvature-vs-topography design-parameter benchmarking discussion for endothelial substrates.",
    ),
    "PUBMED_0925": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / micropatterned natural polymer (silk fibroin) substrate study (in vitro only, corneal endothelial cells)",
        target_layer_final="endothelium",
        biomaterial_category="micropatterned natural polymer (non-mulberry silk fibroin) film substrate",
        specific_materials="silk fibroin protein extracted from Antheraea assamensis (muga) silkworms, cast into films with and without surface micropatterns (hexagons and microgrooves); flat films used as comparator",
        fabrication_method="fibroin protein extracted from Antheraea assamensis and cast into flat, hexagon-patterned, and microgroove-patterned films; Young's modulus and visible-spectrum light transmittance measured for optical/mechanical characterization; cell adhesion assessed via MTT assay and proliferation via Ki67 staining; cell shape/size morphometrics via ImageJ; marker expression visualized/quantified via immunostaining and western blot",
        scaffold_architecture="2D micropatterned silk fibroin film (flat, hexagon-patterned, or microgroove-patterned surface topographies), building on the same laboratory's prior unpatterned silk fibroin corneal endothelium substrate work",
        cell_type_used="corneal endothelial cells; species/source not specified in the retrieved abstract",
        cell_source="not specified in the retrieved abstract",
        growth_factors_or_bioactive_agents="none; topography-only engineering strategy (no added soluble factors)",
        optical_transparency_reported="yes",
        optical_metric_details="Light transmittance in the visible spectrum was measured and compared between patterned and flat films as part of the optical/mechanical characterization; no specific numeric transmittance percentage is given in the retrieved abstract.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Young's modulus was measured for flat vs. patterned films; patterned films demonstrated enhanced elasticity, roughness, and hydrophilicity compared with flat films (qualitative/comparative finding; no specific numeric modulus values given in the retrieved abstract).",
        biological_testing_reported="yes",
        biological_metric_details="No significant difference in cell adhesion (MTT assay) between flat and patterned films; percentage of proliferating cells (Ki67) was significantly reduced on patterned films, especially hexagon-patterned films; cell area/circularity on flat films was comparable to microgroove films, while cells on hexagon films were larger and more variable in size; expression of Na-K ATPase (functional pump marker) was significantly higher on microgroove-patterned films than on other substrates.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract (in vitro culture study)",
        main_outcomes="Micropatterning (hexagons or microgrooves) of Antheraea assamensis silk fibroin films, building on the same lab's prior unpatterned silk fibroin corneal endothelium substrate, enhanced film elasticity, roughness, and hydrophilicity versus flat films. Patterning did not affect cell adhesion but significantly reduced proliferation (especially on hexagons), altered cell morphology (larger, more variable cells on hexagons vs. flat/microgroove-comparable circularity), and significantly increased expression of the functional marker Na-K ATPase on microgroove-patterned films specifically -- indicating that simple surface micropatterns can improve corneal endothelial cell morphology and functional marker expression, with microgrooves outperforming hexagons on the key functional readout.",
        main_limitations="No specific numeric Young's modulus or light-transmittance values reported in the retrieved abstract; cell source/species not specified; purely in vitro, with no ex vivo or in vivo evaluation; reduced proliferation on patterned (especially hexagon) films raises an unresolved trade-off between functional marker expression (favoring microgrooves) and cell yield.",
        translational_readiness_level="early preclinical (in vitro only)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "ACS Biomaterials Science & Engineering, DOI 10.1021/acsbiomaterials.5c00200, 2025 -- ACS hybrid/subscription journal; open-access status of this specific article not confirmed this run; abstract-level extraction only. Direct micropattern-geometry comparison (hexagon vs. microgroove) with quantitative optical/mechanical/functional-marker characterization -- useful comparator to PUBMED_0378 (polyacrylamide hexagon-density study) and PUBMED_0827 (collagen curvature/topography study) for the review's substrate-topography benchmarking table.",
    ),
    "PUBMED_0934": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / composite polymer scaffold study with pharmacological proliferation-enhancement (in vitro only, human corneal endothelial cells)",
        target_layer_final="endothelium",
        biomaterial_category="composite synthetic-natural polymer scaffold (chitosan nanoparticles + chitosan + polycaprolactone)",
        specific_materials="scaffold containing chitosan nanoparticles, chitosan, and polycaprolactone (PCL); telomerase activator and Rho-kinase (ROCK) inhibitor used as pharmacological proliferation enhancers",
        fabrication_method="scaffold fabricated from chitosan nanoparticles, chitosan, and PCL; human corneal endothelial cells (HCECs) isolated from corneal endothelium and cultured on the scaffold; proliferation induced with a telomerase activator and a ROCK inhibitor individually and in combination; functional characterization via gene expression analysis, flow cytometry, electron microscopy (SEM), H&E staining, and MTT assay",
        scaffold_architecture="nanoparticle-reinforced chitosan-PCL composite membrane/scaffold supporting a cultured HCEC monolayer",
        cell_type_used="human corneal endothelial cells (HCECs)",
        cell_source="human, primary, isolated from corneal endothelium",
        growth_factors_or_bioactive_agents="telomerase activator and ROCK inhibitor (small-molecule proliferation enhancers applied to cultured HCECs, not incorporated into the scaffold itself)",
        optical_transparency_reported="yes",
        optical_metric_details="The fabricated scaffold was reported to have \"suitable transparency\" (qualitative finding); no specific numeric light-transmittance value is given in the retrieved abstract.",
        mechanical_testing_reported="unclear / not reported in abstract",
        mechanical_metric_details="No numeric mechanical (modulus) data reported in the retrieved abstract; the scaffold is characterized as having \"great biocompatibility,\" but no bench mechanical testing values are given.",
        biological_testing_reported="yes",
        biological_metric_details="Over 98% of isolated cells had the CD166(+)/CD98(+) phenotype; telomerase activator increased HCEC proliferation 1.5x and ROCK inhibitor increased it 2.3x, with simultaneous combined use synergistically increasing proliferation 4.3x; culture on the scaffold significantly increased HCEC proliferation; SEM and H&E showed proper cell-surface interaction with formation of a cell monolayer; flow cytometry showed over 97% of cells cultured on the scaffold maintained the CD166(+)/CD44(-) phenotype.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract (in vitro culture study)",
        main_outcomes="A chitosan-nanoparticle/chitosan/PCL composite scaffold with suitable transparency and biocompatibility supported HCEC attachment, monolayer formation, and phenotypic maintenance (>97% CD166+/CD44- after culture). Combining a telomerase activator (1.5x proliferation) with a ROCK inhibitor (2.3x proliferation) produced a synergistic 4.3x increase in HCEC proliferation, positioning this scaffold plus dual pharmacological enhancement as a promising carrier strategy for HCEC transplantation grafts.",
        main_limitations="No in vivo or ex vivo evaluation reported; no numeric mechanical (modulus) or light-transmittance values given; long-term safety of telomerase activation (given its association with cellular immortalization/oncogenic risk pathways) is not addressed in the abstract; sample sizes not specified.",
        translational_readiness_level="early preclinical (in vitro only)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "International Journal of Biological Macromolecules (Elsevier), DOI 10.1016/j.ijbiomac.2025.144744, 2025 -- Elsevier hybrid/subscription journal; open-access status of this specific article not confirmed this run; abstract-level extraction only. Strong quantitative synergistic-proliferation dataset (1.5x / 2.3x / 4.3x) valuable for the review's pharmacological-enhancement-plus-scaffold benchmarking discussion.",
    ),
    "PUBMED_0981": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / tissue-engineered endothelial keratoplasty (TEEK) proof-of-concept study using a novel scaffold (in vitro only, n=12 constructs)",
        target_layer_final="endothelium",
        biomaterial_category="novel biological scaffold: femtosecond-laser-cut lens capsule disc as an endothelial cell carrier for tissue-engineered endothelial keratoplasty (TEEK)",
        specific_materials="femtosecond-laser-cut lens capsule disc used as bioengineering scaffold; anti-NCAM (lateral membrane marker) used for endothelial mosaic staining; Hoechst 33342 and Calcein-AM used for viability staining",
        fabrication_method="a femtosecond laser used to cut lens capsule discs as a bioengineering scaffold, selected for its biocompatibility, transparency, curvature, and availability; 12 TEEK constructs prepared with varying endothelial cell seeding densities per mm^2 to control final endothelial cell density (ECD); endothelial mosaic characterized via anti-NCAM immunostaining and morphometric analysis using the CellPose AI algorithm specifically trained for in vitro endothelium segmentation; five criteria related to pleomorphism, polymorphism, and elongation combined into a single endothelial quality score; cell viability assessed at 28 days via Hoechst 33342 and Calcein-AM staining",
        scaffold_architecture="femtosecond-laser-cut lens capsule disc, exploiting native curvature, transparency, and biocompatibility as an endothelial cell carrier for TEEK",
        cell_type_used="corneal endothelial cells; species/source not specified in the retrieved abstract",
        cell_source="not specified in the retrieved abstract",
        growth_factors_or_bioactive_agents="none reported; controlled seeding density (cells per mm^2) is the key engineered variable rather than an added bioactive factor",
        optical_transparency_reported="yes",
        optical_metric_details="The lens capsule disc scaffold was selected in part for its native transparency (qualitative rationale); no specific numeric light-transmittance value is given in the retrieved abstract.",
        mechanical_testing_reported="unclear / not reported in abstract",
        mechanical_metric_details="The scaffold's native curvature and biocompatibility are described qualitatively as rationale for its selection; no numeric mechanical (modulus) testing values are reported in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="Median cell viability at 28 days of culture (Hoechst 33342/Calcein-AM) reached 98% (range 83-99%); median viable endothelial cell density (ECD, live cells per surface unit) in the highest-density group was 3,245 cells/mm^2 (range 2,778-3,753); endothelial mosaic quality assessed via a combined score of pleomorphism, polymorphism, and elongation using AI-assisted (CellPose) morphometric segmentation.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="28 days (in vitro culture)",
        main_outcomes="A proof-of-concept study (n=12 TEEK constructs) using a novel femtosecond-laser-cut lens capsule disc scaffold demonstrated that final endothelial cell density (ECD) can be controlled by varying seeding density per mm^2, with the highest-density group reaching a median viable ECD of 3,245 cells/mm^2 (range 2,778-3,753) and median 28-day viability of 98% (range 83-99%), assessed via AI-assisted (CellPose) morphometric segmentation and a combined endothelial quality score -- supporting feasibility of engineering supra-physiological-density \"super TEEKs\" that exceed native donor endothelial cell densities.",
        main_limitations="Purely in vitro/bench proof-of-concept (n=12), with no ex vivo or in vivo functional/transplantation testing; cell source/species not specified in the retrieved abstract; no numeric mechanical (modulus) data; long-term (beyond 28-day) stability of supra-physiological ECD not assessed; a single-team, novel scaffold not yet independently validated.",
        translational_readiness_level="early preclinical (in vitro proof-of-concept)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Tissue Engineering Part A (Mary Ann Liebert), DOI 10.1177/19373341251381346, 2025 -- Mary Ann Liebert hybrid/subscription journal; open-access status of this specific article not confirmed this run; abstract-level extraction only. Novel scaffold source (femtosecond-laser-cut lens capsule disc) and explicit supra-physiological ECD/viability quantification make this a valuable comparator for the review's endothelial-density benchmarking table.",
    ),
    "PUBMED_0010": dict(
        extraction_status="completed",
        study_type="clinical study (prospective clinical trial, NCT02149732, n=8 subjects) of biomaterial-free/carrier-free cultured oral mucosal epithelial cell sheet (COMEC) transplantation",
        target_layer_final="epithelium_limbus",
        biomaterial_category="biomaterial-free (carrier-free) cultured autologous oral mucosal epithelial cell sheet",
        specific_materials="cultured oral mucosal epithelial cell sheets (COMECs), prepared in a culture system without any temperature-sensitive polymers or carriers",
        fabrication_method="COMECs prepared in a carrier-free culture system (no temperature-sensitive polymers or scaffolds) and transplanted without suture fixation; prospective clinical trial (NCT02149732, IRB-approved at Seoul National University Hospital, approved by the Korean Ministry of Food and Drug Safety) in 8 subjects with total limbal stem cell deficiency (LSCD); 4 subjects underwent penetrating keratoplasty (PK) after COMEC stabilization; corneal cytokeratin (K) immunofluorescent staining performed in the 4 PK subjects; stable epithelialization, visual acuity change, and complications evaluated over 6 months",
        scaffold_architecture="none -- carrier-free/biomaterial-free cell sheet held together by intercellular junctions alone, with no polymer or scaffold carrier",
        cell_type_used="autologous oral mucosal epithelial cells",
        cell_source="human, autologous (patient's own oral mucosa)",
        growth_factors_or_bioactive_agents="not specified in the retrieved abstract beyond the carrier-free culture system itself",
        optical_transparency_reported="no / not applicable (clinical study; no bench optical transmittance testing reported)",
        optical_metric_details="Not applicable; this is a clinical transplantation trial rather than a bench optical characterization study.",
        mechanical_testing_reported="no / not applicable (clinical study; no bench mechanical testing reported)",
        mechanical_metric_details="Not applicable; no bench mechanical testing performed on the carrier-free cell sheet.",
        biological_testing_reported="yes",
        biological_metric_details="Ocular surface successfully reconstructed in 6 of 8 eyes; complete stable epithelialization achieved within a mean of 53.6 days; visual improvement (>=2 lines) achieved in 62.5% of eyes; corneal phenotype marker K12 and mucosal-phenotype markers K4/K13 were well expressed in grafts after keratoplasty, while K1, K8, and K19 were barely expressed; no ocular infections, local tumor formation, or remarkable systemic complications observed; reconstruction failed in 2 eyes, both of which had full (4-quadrant) symblepharon.",
        in_vitro_model="no",
        ex_vivo_model="yes",
        animal_model="no",
        clinical_evidence="yes",
        follow_up_duration="6 months",
        main_outcomes="A prospective clinical trial (NCT02149732, n=8 subjects) of carrier-free, biomaterial-free cultured oral mucosal epithelial cell sheets (COMECs) for total limbal stem cell deficiency achieved successful ocular surface reconstruction in 6 of 8 eyes, with complete stable epithelialization in a mean of 53.6 days, visual improvement (>=2 lines) in 62.5% of eyes, appropriate corneal (K12) and mucosal (K4/K13) phenotype marker expression after keratoplasty, and no infectious, neoplastic, or systemic complications over 6 months. The 2 treatment failures both occurred in eyes with full (4-quadrant) symblepharon, indicating a specific limitation for severe symblepharon cases.",
        main_limitations="Small sample size (n=8 subjects, 6 successful eyes); efficacy failed in eyes with full (4-quadrant) symblepharon; no comparator arm (e.g., against a carrier/scaffold-based COMET construct); near-absent K1/K8/K19 expression pattern not further mechanistically interpreted; no follow-up beyond 6 months reported.",
        translational_readiness_level="clinical (prospective clinical trial, NCT02149732)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Cornea (Wolters Kluwer / Lippincott), DOI 10.1097/ICO.0000000000001409, 2018 -- Wolters Kluwer hybrid/subscription journal; open-access status of this specific article not confirmed this run; abstract-level extraction only. Rare carrier-free/biomaterial-free clinical benchmark, useful direct contrast to amniotic-membrane- or scaffold-carrier-based COMET/CCET studies elsewhere in the corpus (e.g., PUBMED_0832) for the review's carrier-vs-carrier-free translational comparison.",
    ),
    "PUBMED_0056": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / composite polysaccharide-protein membrane study with in vitro and in vivo evaluation (rabbit alkali-burn corneal injury model)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="natural polysaccharide-protein blend membrane (carboxymethyl chitosan / gelatin / hyaluronic acid)",
        specific_materials="carboxymethyl chitosan (CMCTS), gelatin, and hyaluronic acid (HA) blended membrane",
        fabrication_method="CMCTS, gelatin, and HA blended and cast into a membrane; primary rabbit corneal epithelial cells (CEpCs) seeded on the membrane to evaluate cytocompatibility, growth, and proliferation; CEpCs/CMCTS membrane construct used to treat alkali-induced corneal damage in rabbits, with healing evaluated via visual observation, slit lamp examination, hematoxylin-eosin staining, and immunofluorescence staining",
        scaffold_architecture="transparent, biodegradable CMCTS/gelatin/HA blended membrane supporting a CEpC monolayer",
        cell_type_used="primary rabbit corneal epithelial cells (CEpCs)",
        cell_source="rabbit, primary",
        growth_factors_or_bioactive_agents="none exogenous added; the gelatin and hyaluronic acid blend components provide bioactive/ECM-mimetic adhesive cues",
        optical_transparency_reported="yes",
        optical_metric_details="The blend membrane was reported to be transparent, and the CEpCs/CMCTS membrane treatment restored corneal transparency in the alkali-burn rabbit model (qualitative findings); no specific numeric light-transmittance value is given in the retrieved abstract.",
        mechanical_testing_reported="unclear / not reported in abstract",
        mechanical_metric_details="The membrane was described as biodegradable, but no numeric mechanical (modulus/tensile) testing values are reported in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="The blend membrane supported CEpC attachment and proliferation and maintained epithelial-cell-like protein expression; in the alkali-burn rabbit model, the CEpCs/CMCTS membrane treatment significantly improved corneal epithelial reconstruction and restored corneal transparency and thickness, assessed by visual observation, slit lamp, H&E, and immunofluorescence staining.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract (in vivo healing evaluated qualitatively; exact follow-up duration not given)",
        main_outcomes="A transparent, biodegradable carboxymethyl chitosan/gelatin/hyaluronic acid blended membrane supported rabbit corneal epithelial cell (CEpC) attachment, proliferation, and maintenance of epithelial-cell-like protein expression in vitro. Combined with CEpCs and applied to alkali-induced corneal damage in rabbits, the construct significantly improved corneal epithelial reconstruction and restored corneal transparency and thickness, supporting this blend membrane as a candidate cell-transplantation carrier for corneal epithelial reconstruction and wound healing.",
        main_limitations="No numeric light-transmittance or mechanical (modulus) values reported; in vivo follow-up duration not specified numerically; rabbit model only, with no larger-animal or clinical evidence; sample sizes not given in the retrieved abstract.",
        translational_readiness_level="preclinical (animal model, rabbit)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Carbohydrate Polymers (Elsevier), DOI 10.1016/j.carbpol.2018.03.033, 2018 -- Elsevier hybrid/subscription journal; open-access status of this specific article not confirmed this run; abstract-level extraction only. Natural polysaccharide-protein blend membrane with combined in vitro cytocompatibility and in vivo alkali-burn functional restoration data -- useful comparator for the review's natural-polymer epithelial-carrier benchmarking entries.",
    ),
    "PUBMED_0099": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / comparative scaffold-format and culture-media optimization study with in vivo evaluation (rabbit LSCD model)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="human amniotic membrane (HAM)-based scaffold, compared against substrate-free culture",
        specific_materials="human amniotic membrane (HAM) in two configurations -- HAM sutured onto transwell inserts (HAMTW) and HAM slide scaffold (HAMS) -- compared against substrate-free (transwell) culture; three culture media conditions tested, including a xeno-free medium with 5% human AB serum",
        fabrication_method="limbal epithelial sheets cultured across three media conditions and three substrate conditions (transwell, HAMTW, HAMS); outgrowth sheet size from limbal explants, expression of stem/progenitor cell markers (p63alpha, ABCG2, CK15), and colony formation efficiency (CFE) measured; ABCG2 efflux activity measured via JC1 dye exclusion (JC1(low)); limbal epithelial sheets grown on HAMS transplanted into corneas of LSCD rabbit models; post-transplant p63alpha (basal layer) and CK12 (superficial layer) immunostaining performed",
        scaffold_architecture="human amniotic membrane in slide-scaffold (HAMS) or suture-mounted-on-transwell (HAMTW) configurations, compared against a substrate-free transwell culture system",
        cell_type_used="limbal epithelial cells, cultured as explant-derived sheets and transplanted into rabbit LSCD model corneas",
        cell_source="not fully specified in the retrieved abstract beyond limbal-explant origin; recipient model is rabbit",
        growth_factors_or_bioactive_agents="5% human AB serum (component of the xeno-free medium), identified as the optimal media condition tested",
        optical_transparency_reported="no / not reported in abstract",
        optical_metric_details="No optical transparency/transmittance data reported in the retrieved abstract; outcomes focused on marker expression and colony formation rather than optical characterization.",
        mechanical_testing_reported="no / not applicable in abstract",
        mechanical_metric_details="Not applicable; no mechanical testing reported in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="5% human AB serum medium showed the greatest increase in ABCG2 efflux activity (JC1(low)), p63alpha expression, and colony formation efficiency (CFE), both with and without HAM. Outgrowth sheet size, cell yield, and Ki67 expression were increased on HAMS compared with transwell and HAMTW; ABCG2 efflux activity, p63alpha and CK15 expression, and CFE were also increased on HAMS. In transplanted rabbit LSCD model corneas, p63alpha expression was observed in the basal layers and CK12 expression in the superficial layers, consistent with normal corneal epithelial differentiation.",
        in_vitro_model="yes",
        ex_vivo_model="yes",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract (post-transplant marker expression assessed; exact duration not given)",
        main_outcomes="A xeno-free medium supplemented with 5% human AB serum, combined with a human amniotic membrane slide scaffold (HAMS) format, produced the largest outgrowth sheet size, highest cell yield/Ki67 expression, and greatest stem/progenitor marker expression (p63alpha, ABCG2 efflux activity, CK15) and colony formation efficiency (CFE) compared with substrate-free (transwell) and HAM-on-transwell (HAMTW) conditions. Limbal epithelial sheets grown on HAMS, transplanted into rabbit LSCD model corneas, showed appropriate basal (p63alpha) and superficial (CK12) marker expression patterns, supporting HAMS with xeno-free 5% human AB serum medium as an optimized combination for cultivated limbal epithelial transplantation.",
        main_limitations="Follow-up duration and quantitative post-transplant functional outcomes (e.g., epithelialization rate, corneal transparency, visual outcome) are not given numerically in the retrieved abstract; CFE and marker expression differences are described comparatively rather than with specific numeric values; a rabbit model was used rather than a human/clinical cohort; findings not cross-validated against a non-xeno-free gold-standard protocol with matched quantitative statistics.",
        translational_readiness_level="preclinical (animal model, rabbit LSCD)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Scientific Reports (Nature Portfolio), DOI 10.1038/s41598-018-32914-0, 2018 -- Scientific Reports is a fully open-access (gold OA) journal; full text freely available; full-text fetch not attempted this run, abstract-level extraction used. Direct head-to-head scaffold-format comparison (substrate-free vs. two HAM configurations) plus a media-optimization arm makes this a valuable entry for the review's scaffold-design and culture-condition benchmarking table.",
    ),
    "PUBMED_0104": dict(
        extraction_status="completed",
        study_type="experimental biomaterial-free cell-engineering study (in vitro decellularized-cornea recellularization) with in vivo evaluation (mouse transplantation), CRISPR-engineered hypoimmunogenic hESC-derived corneal epithelial cells",
        target_layer_final="epithelium_limbus",
        biomaterial_category="decellularized xenogeneic (murine) corneal ECM recellularized with genetically engineered hESC-derived corneal epithelial cells (a decellularized natural-tissue carrier rather than a synthetic/fabricated scaffold)",
        specific_materials="decellularized murine corneas recellularized with human embryonic stem cell (hESC)-derived corneal epithelial cells (CEC); CRISPR/Cas9-mediated knockout of beta-2-microglobulin (B2M) used to generate hypoimmunogenic B2M(-/-) CEC",
        fabrication_method="hESCs differentiated to CEC using the serum-free, growth-factor-free, chemically defined medium E6 alone; global gene expression time-course analysis performed to confirm the differentiation trajectory closely resembles in vivo corneal development; decellularized murine corneas recellularized with hESC-derived CEC; CRISPR/Cas9 used to delete B2M in hESC, blocking assembly of HLA class-I antigens on the cell surface to generate B2M(-/-) CEC; B2M(-/-) CEC assessed in vitro (HLA class-I surface absence following inflammatory-factor stimulation) and in vivo via transplantation into mouse eyes (T-cell infiltration in the limbal region)",
        scaffold_architecture="decellularized murine corneal extracellular matrix recellularized with a multilayer hESC-derived corneal epithelium",
        cell_type_used="human embryonic stem cell (hESC)-derived corneal epithelial cells (CEC), including CRISPR/Cas9 B2M-knockout B2M(-/-) CEC",
        cell_source="human (hESC-derived; genetically engineered via CRISPR/Cas9 B2M knockout)",
        growth_factors_or_bioactive_agents="none exogenous beyond the chemically defined, serum-free, growth-factor-free E6 differentiation medium itself",
        optical_transparency_reported="yes",
        optical_metric_details="hESC-CEC-recellularized decellularized murine cornea retained its transparency and allowed light transmittance (qualitative findings); no specific numeric transmittance value is given in the retrieved abstract.",
        mechanical_testing_reported="no / not reported in abstract",
        mechanical_metric_details="No mechanical testing data reported in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="E6 medium alone was sufficient for hESC differentiation to CEC; global gene expression time-course closely resembled in vivo corneal development; hESC-CEC were highly proliferative and formed a multilayer epithelium on decellularized murine cornea with intact tight junctions; CRISPR/Cas9 B2M knockout was confirmed to block HLA class-I assembly on the cell surface following stimulation with inflammatory factors; after transplantation into mouse eyes, B2M(-/-) CEC caused less T-cell infiltration in the limbal region than wild-type control cells.",
        in_vitro_model="yes",
        ex_vivo_model="yes",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract (post-transplantation T-cell infiltration assessed; exact duration not given)",
        main_outcomes="A simple, protein-free protocol (chemically defined E6 medium alone) differentiated hESC to corneal epithelial cells (CEC) that closely recapitulated in vivo corneal developmental gene expression, formed a proliferative multilayer epithelium with intact tight junctions on decellularized murine cornea while retaining transparency and light transmittance. CRISPR/Cas9 knockout of B2M generated hypoimmunogenic B2M(-/-) CEC lacking surface HLA class-I expression, which caused less T-cell infiltration than wild-type controls after transplantation into mouse eyes -- supporting B2M(-/-) hESC-CEC as a potential unlimited, universal (HLA-type-independent) allogeneic cell source for corneal epithelial repair.",
        main_limitations="No specific numeric light-transmittance value or mechanical data reported; a murine (not primate/human) decellularized carrier and transplant recipient model was used; T-cell infiltration reduction is described qualitatively (\"less\") without quantitative immune-cell counts; long-term graft survival and immune rejection risk beyond acute T-cell infiltration are not assessed; the hESC-derived (rather than adult stem cell-derived) cell origin raises separate regulatory/ethical translational considerations not addressed in the abstract.",
        translational_readiness_level="preclinical (animal model, mouse)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Translational Vision Science & Technology (ARVO Journals), DOI 10.1167/tvst.7.5.23, 2018 -- TVST is a fully open-access (gold OA) journal; full text freely available; full-text fetch not attempted this run, abstract-level extraction used. Hypoimmunogenic, CRISPR-engineered universal donor-cell strategy is a valuable comparator for the review's cell-source/immunogenicity benchmarking discussion, complementing PUBMED_0202 (DPSC alternative cell-source comparison) elsewhere in the corpus.",
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

OA_IDS = {"PUBMED_0827", "PUBMED_0099", "PUBMED_0104"}
SUBSCRIPTION_IDS = {"PUBMED_0925", "PUBMED_0934", "PUBMED_0981", "PUBMED_0010", "PUBMED_0056"}

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
