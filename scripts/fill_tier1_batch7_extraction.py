"""
Tier 1 extraction batch 7 (2026-07-20, scheduled run continuation).

Retrieval route note: the Europe PMC REST API JSON endpoint
(https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:<pmid>&format=json&resultType=core)
was again NOT reachable in this run's sandboxed web_fetch tool -- it
returned "URL not in provenance set" (the tool only allows fetching URLs
that already appeared in a user message, a prior web_fetch result, or a
WebSearch result; this unattended scheduled run has no user available to
authorize a new URL). Same restriction hit in batches 3-6.

This run's workaround: WebSearch was used to independently locate and
confirm each article's bibliographic details and open-access status. Full
text was successfully retrieved via web_fetch for PUBMED_0821 (PMC11426139,
Materials Today Bio, fully open access), once its URL had surfaced through
a prior WebSearch result -- giving genuine full-text confirmation of
quantitative optical, mechanical, and in vivo data well beyond the abstract.
For the remaining 7 records, extraction was built from the complete,
untruncated abstract text already stored locally in
screening/full_text/pubmed_tier1_tier2_extraction_plan.csv, cross-checked
against WebSearch summaries of the same PMID/title/DOI.

This batch (8 records):
- PUBMED_0821 (PMID 39328788) - HHP-decellularized porcine cornea, transparency/mechanics/in vivo rabbit interlamellar keratoplasty. FULL TEXT retrieved.
- PUBMED_0871 (PMID 39819884) - DLP bioprinted GelMA/OxiCMC corneal stroma equivalent, in vitro only.
- PUBMED_0947 (PMID 40613723) - graphene oxide/Nb2C MXene nanocomposite scaffold, rabbit cornea + alkali burn model, in vivo.
- PUBMED_0990 (PMID 41073348) - decellularized human stromal lenticules + rapamycin delivery, rabbit interstromal implantation, in vivo.
- PUBMED_0038 (PMID 29495264) - aligned PVA/collagen electrospun nanofibrous scaffold, in vitro only.
- PUBMED_0049 (PMID 29637812) - cultured oral mucosal epithelial cell sheet detachment method, ex vivo porcine stroma model.
- PUBMED_0144 (PMID 30918800) - full-thickness corneal substitute from acellular porcine corneal matrix (APCM) + human corneal cells, ex vivo organ culture + surgical (PKP) handling test.
- PUBMED_0273 (PMID 32368948) - multilayered decellularized porcine sheet + collagen I hydrogel corneal stromal equivalent, ex vivo porcine cornea suture test.
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
    "against a WebSearch lookup of the same PMID/DOI this run. Europe PMC REST API "
    "fetch was unavailable this run (web_fetch tool restricted to previously "
    "provenance-approved URLs; unattended run could not authorize the new URL). "
)

NOTE_PREFIX_FULLTEXT = (
    "Full text retrieved this run via web_fetch (URL surfaced through a prior "
    "WebSearch result, satisfying the tool's provenance requirement). Europe PMC "
    "REST API endpoint itself remained blocked ('URL not in provenance set'); "
    "the PMC HTML page was used instead. "
)

EXTRACTIONS = {
    "PUBMED_0821": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / decellularized tissue engineering study with in vivo evaluation (rabbit interlamellar keratoplasty)",
        target_layer_final="stroma",
        biomaterial_category="decellularized xenogeneic (porcine) corneal stroma (acellular ECM scaffold)",
        specific_materials="porcine cornea decellularized by a modified high hydrostatic pressure (HHP) method (600 MPa, 15% glycerol pressure medium), producing a 'transparent decellularized cornea' retaining native collagen type I, GAGs, and Descemet's membrane (collagen IV)",
        fabrication_method="fresh porcine corneas processed by detergent-free HHP decellularization; hydrostatic pressure (200-1000 MPa) and glycerol concentration (0-30%) in the pressure medium optimized (600 MPa / 15% glycerol selected) to balance swelling ratio against light transmittance; dissected to 160 micron thickness via microkeratome for in vivo grafting",
        scaffold_architecture="whole decellularized porcine corneal lamellar stroma, collagen fibril lamellae preserved (fibril diameter ~29-30 nm, comparable to untreated cornea), with intact Descemet's membrane basement membrane layer",
        cell_type_used="porcine corneal endothelial cells (PCEnCs, primary, for in vitro recellularization); mouse L929 fibroblasts (cytotoxicity/extract assay only)",
        cell_source="porcine (PCEnCs, primary, isolated from fresh porcine eye globes); mouse (L929, ATCC, cytotoxicity control only)",
        growth_factors_or_bioactive_agents="bFGF (10 ng/mL) included only in PCEnC expansion culture medium prior to seeding, not incorporated into the scaffold itself; no bioactive agents added to the decellularized matrix",
        optical_transparency_reported="yes",
        optical_metric_details="Visible-light (380-770 nm) transmittance: untreated porcine cornea 92.3 +/- 1.2%, transparent decellularized cornea 86.4 +/- 1.5% (comparable to fresh human cornea, 87.1 +/- 2.0%, and higher than eye-bank preserved human cornea, 62.5%). Refractive index: untreated porcine cornea 1.375 +/- 0.007, decellularized cornea 1.367 +/- 0.001 (vs. human cornea 1.373-1.380). In vivo: haze score grade 2 (Fantes scale) immediately post-transplant, reaching transparency within 72 h, average postoperative haze grade 0.3 +/- 0.29 over 4-week follow-up.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Suture retention (maximum tear strength, n=10): significantly higher in decellularized vs. untreated corneas (exact N values in figure, not reproduced in text). Compression test (n=4): elastic modulus of decellularized cornea slightly lower than untreated cornea; no significant difference in stress at 50% or 100% deformation. Residual dsDNA reduced from 575.0 +/- 38.7 ng/mg (untreated) to 42.9 +/- 7.3 ng/mg (>93% reduction, p<0.05); collagen content unchanged (650.0 +/- 36.2 vs. 635.3 +/- 50.4 ng/mg) and GAG content unchanged (21.3 +/- 2.3 vs. 24.0 +/- 7.5 ng/mg) between untreated and decellularized tissue.",
        biological_testing_reported="yes",
        biological_metric_details="L929 extract cytotoxicity assay: cell viability with decellularized-cornea extracts not significantly different from fresh-medium positive control (glycerol/DMSO negative controls showed significant cytotoxicity). PCEnC recellularization: cells formed a confluent monolayer with tight junctions and hexagonal morphology by 1-2 weeks; cell density lower than native endothelium but increased with culture time; Na+/K+-ATPase expression confirmed by immunofluorescence at 2 weeks; Descemet's-membrane-like basement membrane reconstructed between PCEnC monolayer and the decellularized matrix (not seen on collagen-gel control).",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="4 weeks (rabbit interlamellar keratoplasty in vivo follow-up); 1-2 weeks (in vitro PCEnC recellularization)",
        main_outcomes="A detergent-free, HHP-decellularized porcine cornea achieved near-native visible-light transmittance (86.4% vs. 92.3% untreated, comparable to fresh human cornea 87.1%) and preserved core matrisome proteins (2431 proteins identified, 91.7% ECM components) without post-decellularization glycerol/washing steps. The matrix supported endothelial cell recellularization with basement-membrane reconstruction, showed no in vivo cytotoxicity, and after rabbit interlamellar transplantation regained macroscopic transparency within 72 h and remained clear and well-integrated (haze grade 0.3, minimal CD68+ macrophage infiltration, no alpha-SMA+ myofibroblasts) over a 4-week follow-up.",
        main_limitations="Xenogeneic (porcine) source material carries immunogenicity/regulatory considerations for eventual human clinical use, even though this study reports low xeno-immune response short-term; in vivo follow-up limited to 4 weeks (authors cite prior unpublished 12-month data but it is not included in this study); refractive index slightly lower than native human cornea; PCEnC density after recellularization remained below native endothelial density.",
        translational_readiness_level="preclinical (animal model, rabbit; xenogeneic material already used in 3 NMPA-approved clinical decellularized corneal products per discussion, suggesting a credible path to clinical translation)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_FULLTEXT
        + "Materials Today Bio, DOI 10.1016/j.mtbio.2024.101241, Sept 2024 -- confirmed fully open access (full text retrieved directly from PMC11426139). One of the strongest Tier 1 stroma records for benchmarking: paired quantitative transmittance, refractive index, dsDNA/collagen/GAG, and in vivo haze-score data against both untreated porcine and human corneal reference values.",
    ),
    "PUBMED_0871": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / 3D bioprinting fabrication and characterization study (in vitro only)",
        target_layer_final="stroma",
        biomaterial_category="synthetic-natural composite interpenetrating network (IPN) hydrogel, digital-light-processing (DLP) bioprinted",
        specific_materials="gelatin methacryloyl (GelMA) / oxidized carboxymethyl cellulose (OxiCMC) interpenetrating network hydrogel, dual-crosslinked (Schiff base reaction + photocrosslinking), with tartrazine used as a photoabsorber during printing",
        fabrication_method="GelMA and OxiCMC combinations screened for printability and rheological gelation behavior; DLP bioprinting used (tartrazine photoabsorber) to biofabricate 3D constructs mimicking native corneal stromal curvature; dual crosslinking strategy (Schiff base + photocrosslinking) applied without synthetic polymers, toxic crosslinkers, or nanoparticles; human corneal keratocytes incorporated into the bioink",
        scaffold_architecture="3D-bioprinted, curved construct mimicking native corneal stroma geometry (central thickness 478.9 +/- 56.5 micron, peripheral thickness 864.0 +/- 79.3 micron), porous interconnected network confirmed by SEM",
        cell_type_used="human corneal keratocytes",
        cell_source="human (corneal keratocytes)",
        growth_factors_or_bioactive_agents="none reported; tartrazine used only as a photoabsorber for print resolution, not a bioactive agent",
        optical_transparency_reported="yes",
        optical_metric_details="Optical transparency of tartrazine-containing bioprinted constructs was reported as comparable to native cornea following PBS washing (qualitative/comparative statement; no single numeric transmittance percentage given in the retrieved abstract).",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Compressive modulus of the dual-crosslinked (Schiff base + photocrosslinking) construct was 106.3 +/- 7.7 kPa, closely matching native corneal tissue modulus of 115.3 +/- 13.6 kPa (both figures as reported in abstract), achieved without synthetic polymers, toxic crosslinkers, or nanoparticles.",
        biological_testing_reported="yes",
        biological_metric_details="In vitro biological assays demonstrated high human corneal keratocyte viability (>93%) and desirable proliferation within the biofabricated constructs; SEM confirmed improved porosity and interconnected network structure facilitating nutrient diffusion and cell viability.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="not applicable / single-timepoint in vitro characterization and cell-culture assays (specific culture duration not given in abstract)",
        main_outcomes="A DLP-bioprinted GelMA/OxiCMC interpenetrating-network hydrogel achieved a compressive modulus (106.3 kPa) closely matching native corneal stroma (115.3 kPa), native-mimicking curvature/thickness geometry, native-comparable optical transparency after washing, and high keratocyte viability (>93%) with good proliferation -- all without synthetic polymers, toxic crosslinkers, or nanoparticles, positioning the dual-crosslinking IPN strategy as a promising biomimetic corneal stroma equivalent fabrication route.",
        main_limitations="In vitro only, no ex vivo, animal, or clinical evaluation; no numeric optical transmittance percentage given in abstract despite a qualitative transparency claim; long-term degradation, suturability, and surgical handling not assessed.",
        translational_readiness_level="early preclinical (in vitro)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Biofabrication (IOP Publishing), DOI 10.1088/1758-5090/adab27, published online 2025 (print Feb 2025, Vol 17 No 2) -- WebSearch confirms open access format on IOPscience; direct full-text web_fetch not attempted this run to conserve run budget, abstract-level extraction used and is already highly quantitative. Directly comparable to PUBMED_0398 (batch 6) and PUBMED_0821 (this batch) for a mechanical-modulus benchmarking narrative in the stroma table.",
    ),
    "PUBMED_0947": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / nanocomposite scaffold characterization study with in vivo evaluation (rabbit normal cornea and alkali-burn injury model)",
        target_layer_final="stroma",
        biomaterial_category="inorganic 2D-nanomaterial composite scaffold (graphene oxide / MXene)",
        specific_materials="graphene oxide (GO) / niobium carbide MXene (Nb2C) composite nanocomposite scaffold, intended as a full artificial-cornea material",
        fabrication_method="GO and Nb2C MXene combined into a composite nanocomposite scaffold; physical characterization by nanoindentation (mechanical properties) and long-term corrosion assays combined with atomic force microscopy and scanning electron microscopy; in vitro cytocompatibility evaluated with human corneal stromal cells; in vivo evaluation via implantation in normal rabbit corneas and in a rabbit corneal alkali-burn injury model",
        scaffold_architecture="nanocomposite scaffold formed from 2D graphene oxide sheets combined with niobium carbide MXene, structural details (thickness, porosity) not specified in abstract",
        cell_type_used="human corneal stromal cells",
        cell_source="human (corneal stromal cells)",
        growth_factors_or_bioactive_agents="none reported; biological activity attributed to intrinsic antioxidative/anti-inflammatory properties of the GO/Nb2C material itself rather than an added bioactive agent",
        optical_transparency_reported="unclear / not reported in abstract",
        optical_metric_details="Not reported; characterization focused on mechanical, corrosion-resistance, cytocompatibility, and immunomodulatory/biocompatibility properties rather than optical transmittance.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Nanoindentation used to assess mechanical strength and long-term corrosion assays (with AFM/SEM) used to assess corrosion resistance/durability; no specific numeric modulus, hardness, or corrosion-rate values given in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="In vitro: survival, proliferation, and attachment of human corneal stromal cells assessed (qualitative 'high biocompatibility' conclusion, no specific percentages given in abstract). In vivo (normal rabbit cornea and alkali-burn model): fibrosis markers Hsp47, fibronectin (FN), and alpha-SMA were negative; inflammatory cytokines IL-2 and IL-6 were downregulated, along with oxidative stress indices; immunofluorescence showed decreased CD11b (myeloid/inflammatory marker) expression around the surgical area in the alkali-burn model.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract (described only as 'long-term' for corrosion assays; in vivo follow-up duration for the rabbit implantation and alkali-burn models not given)",
        main_outcomes="A graphene oxide/niobium carbide MXene (GO/Nb2C) nanocomposite scaffold combined high mechanical strength and corrosion resistance (by nanoindentation/AFM/SEM) with strong in vitro cytocompatibility for human corneal stromal cells and favorable in vivo biocompatibility in rabbit corneas, including negative fibrosis markers (Hsp47, FN, alpha-SMA), downregulated inflammatory cytokines (IL-2, IL-6) and oxidative stress, and reduced CD11b+ inflammatory cell infiltration in an alkali-burn injury model -- supporting its potential as a functional scaffold material for artificial corneas with intrinsic antioxidative and anti-inflammatory activity.",
        main_limitations="No quantitative optical transparency data reported despite this being essential for a functional artificial cornea; specific numeric values for mechanical strength, corrosion rate, and cell survival/proliferation percentages not given in the retrieved abstract; rabbit (not human) in vivo model; the material is an inorganic 2D-nanomaterial composite rather than a biologically native/biomimetic scaffold, raising long-term biodegradation/clearance questions not addressed in the abstract.",
        translational_readiness_level="preclinical (animal model, rabbit)",
        benchmarking_relevance="medium",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Nanoscale (RSC Publishing), DOI 10.1039/d5nr01312g, 2025 (Vol 17, Issue 28, pp. 16882-16899) -- RSC Nanoscale is a subscription journal; no open-access indication found via WebSearch for this specific article, abstract-level extraction only. Notable as an unconventional (non-biological, inorganic nanomaterial) scaffold approach among the mostly protein/polysaccharide-hydrogel-based Tier 1 stroma records, useful as a contrasting material-class data point in the review's benchmarking table.",
    ),
    "PUBMED_0990": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / drug-delivery graft study with in vivo evaluation (rabbit interstromal transplantation)",
        target_layer_final="stroma",
        biomaterial_category="decellularized human tissue-derived drug-eluting graft (biological carrier + immunosuppressant)",
        specific_materials="decellularized human corneal stromal lenticules (donor-derived, from refractive surgery) loaded with rapamycin (RAPA) solubilized using a deep eutectic solvent (DES) delivery system; grafts tested up to 1% RAPA loading",
        fabrication_method="human stromal lenticules decellularized, then loaded with rapamycin solubilized via deep eutectic solvents to enable interlamellar corneal implantation; drug incorporation evaluated for effects on lenticule transparency, biomechanical strength, biocompatibility, and in vitro drug release kinetics; 1% RAPA-loaded grafts implanted via interstromal transplantation into rabbit corneas",
        scaffold_architecture="native decellularized human corneal stromal lenticule (biological ECM sheet) used as an implantable, sustained-release drug depot",
        cell_type_used="not applicable (acellular decellularized biological carrier; no exogenous cells seeded); host-mediated nerve regeneration into the graft assessed via neuronal markers post-implantation",
        cell_source="not applicable / decellularized acellular human donor tissue",
        growth_factors_or_bioactive_agents="rapamycin (RAPA), an mTOR-inhibitor immunosuppressive/anti-inflammatory small molecule, solubilized with deep eutectic solvents and loaded up to 1% into the lenticules for localized, sustained release",
        optical_transparency_reported="yes",
        optical_metric_details="In vitro: RAPA-loaded lenticules maintained high transparency comparable to native human cornea (qualitative comparison; no single numeric transmittance percentage given in abstract). In vivo: 1% RAPA-loaded grafts preserved corneal clarity for more than one month after interstromal transplantation in rabbits.",
        mechanical_testing_reported="partial",
        mechanical_metric_details="Drug incorporation process was reported to enhance the biomechanical strength of the lenticules relative to unmodified controls (qualitative comparative finding); no specific numeric tensile strength or modulus values given in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="In vitro controlled RAPA release sustained for over 35 days; drug incorporation also enhanced biocompatibility of the lenticules (qualitative). In vivo: no observable immune rejection over more than one month post-transplantation; histological evaluation confirmed presence of neuronal markers within the grafts, indicating host-mediated corneal nerve regeneration into the implant.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="over 35 days (in vitro sustained drug release); more than 1 month (rabbit interstromal transplantation in vivo follow-up)",
        main_outcomes="Decellularized human stromal lenticules loaded with rapamycin via a deep-eutectic-solvent delivery strategy achieved sustained drug release (>35 days in vitro), maintained near-native transparency and enhanced biomechanical strength/biocompatibility versus unmodified lenticules, and after interstromal implantation into rabbit corneas preserved corneal clarity for over a month without observable immune rejection, while also supporting host nerve regeneration into the graft (confirmed by neuronal marker histology) -- positioning the construct as a dual-function immunomodulatory and pro-regenerative corneal biomaterial with, per the authors, strong potential for clinical translation.",
        main_limitations="Rabbit (not primate/human) in vivo model; follow-up limited to just over 1 month, insufficient to establish long-term immunomodulatory durability or late rejection risk; relies on human donor stromal lenticule tissue (from refractive surgery byproduct) rather than a fully synthetic or unlimited-supply scaffold, so donor-tissue supply constraints are only partially mitigated; no numeric transmittance or tensile mechanical values given in the retrieved abstract despite qualitative claims of comparability/enhancement.",
        translational_readiness_level="preclinical (animal model, rabbit)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "ACS Biomaterials Science & Engineering, DOI 10.1021/acsbiomaterials.5c01309, 2025 (Vol 11, Issue 11, pp. 6751-6766) -- ACS subscription journal, no open-access indication found via WebSearch; abstract-level extraction only. Notable as a drug-delivery/immunomodulation-focused stromal lenticule application (rather than pure structural scaffold), and as reuse of refractive-surgery byproduct tissue (SMILE-derived lenticules), a supply-chain angle relevant to the review's translational-readiness discussion.",
    ),
    "PUBMED_0038": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / electrospun scaffold fabrication and characterization study (in vitro only)",
        target_layer_final="multiple_layers (epithelium + stroma co-culture on the same scaffold)",
        biomaterial_category="synthetic-natural composite electrospun nanofibrous scaffold",
        specific_materials="aligned polyvinyl alcohol (PVA) / collagen (PVA-COL) composite nanofibrous electrospun scaffold (note: abstract text says 'polyvinyl acetate' in one location but the scaffold abbreviation and corneal-biomaterials literature context indicate polyvinyl alcohol, PVA, the standard collagen-blending electrospinning polymer)",
        fabrication_method="collagen and PVA mixed and electrospun to produce aligned and random nanofibrous PVA-COL composite scaffolds; PVA blended in specifically to reinforce the mechanical strength of the collagen electrospun scaffold, addressing the known poor-mechanical-property limitation of pure electrospun collagen scaffolds for surgical suturing; human keratocytes (HKs) and human corneal epithelial cells (HCECs) inoculated onto both aligned and random scaffold variants",
        scaffold_architecture="electrospun nanofibrous mat, produced in both aligned and random fiber orientations for comparison",
        cell_type_used="human keratocytes (HKs) and human corneal epithelial cells (HCECs)",
        cell_source="human (keratocytes and corneal epithelial cells)",
        growth_factors_or_bioactive_agents="none reported",
        optical_transparency_reported="unclear / not reported in abstract",
        optical_metric_details="Not reported; abstract states the design goal was a corneal equivalent with 'similar strength and transparency' to native cornea, but no transmittance data are given in the retrieved abstract text.",
        mechanical_testing_reported="partial",
        mechanical_metric_details="PVA blending was explicitly performed to reinforce the mechanical strength of the electrospun collagen scaffold, addressing pure collagen electrospun scaffolds' known inadequacy for surgical suture requirements; no specific numeric tensile strength or modulus values are given in the retrieved abstract text.",
        biological_testing_reported="yes",
        biological_metric_details="Both HKs and HCECs adhered and proliferated well on aligned and random PVA-COL scaffolds; aligned nanofibers specifically induced orderly (organized) HK growth/alignment, indicating topographical cue-driven keratocyte organization (qualitative finding; no numeric viability/proliferation values given in abstract).",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="not applicable / in vitro cell culture assays only (specific durations not given in abstract)",
        main_outcomes="An aligned PVA/collagen composite electrospun nanofibrous scaffold, designed to overcome the mechanical weakness of pure electrospun collagen scaffolds, supported good adhesion and proliferation of both human keratocytes and human corneal epithelial cells, with fiber alignment specifically inducing orderly keratocyte growth -- supporting the scaffold's suitability as a mechanically reinforced tissue-engineered cornea substrate capable of co-supporting both stromal and epithelial cell types.",
        main_limitations="In vitro only, no ex vivo, animal, or clinical evaluation; no quantitative mechanical (tensile strength/modulus) or optical transmittance values given in the retrieved abstract despite these being the stated design targets; suturability specifically claimed as the motivation but not directly tested/quantified in the abstract.",
        translational_readiness_level="early preclinical (in vitro)",
        benchmarking_relevance="medium",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Nanomaterials (Basel, Switzerland), DOI 10.3390/nano8020124, 2018 -- Nanomaterials is a fully open-access MDPI journal; full-text web_fetch not attempted this run to conserve run budget, abstract-level extraction used. corneal_layer flagged 'multiple_layers' in upstream screening CSV consistent with dual HK/HCEC (stroma + epithelium) cell types used on the same scaffold; target_layer_final left as multiple_layers here for consistency.",
    ),
    "PUBMED_0049": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / cultivated epithelial cell-sheet detachment method study (ex vivo porcine stroma grafting model)",
        target_layer_final="multiple_layers (epithelium engineering with basement-membrane/stromal-interface relevance)",
        biomaterial_category="cultivated non-corneal (oral mucosal) epithelial cell sheet, support-free/carrier-free graft",
        specific_materials="cultured oral mucosal epithelium (COME) cell sheets, detached from culture dishes using enzymatic methods (dispase or collagenase at varying concentrations) versus enzyme-free mechanical detachment, intended for grafting without a carrier support or sutures",
        fabrication_method="autologous oral mucosal epithelial cells cultured to confluence; detachment methods compared: dispase (5 mg/mL) and collagenase (0.5 mg/mL, selected concentration) enzymatic treatments versus enzyme-free mechanical detachment; detached COME sheets characterized for basement-membrane adhesion markers (laminin-332, beta1-integrin, type VII collagen) and junctional markers (E-cadherin, P-cadherin) by immunofluorescence and Western blot; selected method (collagenase 0.5 mg/mL) validated by grafting the detached COME sheet onto a newly developed ex vivo de-epithelialized porcine corneal stroma model for 15 days",
        scaffold_architecture="carrier-free, self-supporting cultivated epithelial cell sheet (no synthetic or biological scaffold material used in the final graft)",
        cell_type_used="autologous oral mucosal epithelial cells (cultured epithelial sheet)",
        cell_source="human (autologous oral mucosal epithelium)",
        growth_factors_or_bioactive_agents="none reported as incorporated into the graft; enzymatic reagents (dispase, collagenase) used only for cell-sheet detachment, not as bioactive/therapeutic agents",
        optical_transparency_reported="unclear / not reported in abstract",
        optical_metric_details="Not applicable/not reported; study focus is epithelial sheet detachment and adhesion/basement-membrane marker expression rather than optical transparency.",
        mechanical_testing_reported="partial",
        mechanical_metric_details="Detachment method resistance/robustness assessed qualitatively: collagenase 0.5 mg/mL achieved 100% detachment success vs. 33% success with dispase 5 mg/mL; sheet described as 'sufficiently resistant and adhesive' post-collagenase detachment; no instrumented tensile/adhesion-strength numeric values reported.",
        biological_testing_reported="yes",
        biological_metric_details="Immunofluorescence and Western blot showed no significant difference in levels of basement-membrane proteins (laminin-332, beta1-integrin, type VII collagen) or cell-cell/cell-matrix junction proteins (E-cadherin, P-cadherin) between the three detachment methods. Collagenase 0.5 mg/mL gave better reproducibility with 100% detachment success (vs. 33% for dispase 5 mg/mL). Grafted onto the ex vivo de-epithelialized porcine stroma model, collagenase-detached COME adhered, stratified, and continued epithelial renewal over 15 days, confirmed by histology, immunofluorescence, and transmission electron microscopy.",
        in_vitro_model="yes",
        ex_vivo_model="yes",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="15 days (ex vivo de-epithelialized porcine corneal stroma grafting model)",
        main_outcomes="Among three cultivated oral mucosal epithelial (COME) sheet detachment methods (dispase, collagenase, enzyme-free mechanical), collagenase at 0.5 mg/mL gave the most reproducible detachment (100% success vs. 33% for dispase) while preserving basement-membrane and junctional adhesion marker expression equivalent to the other methods; collagenase-detached, carrier-free COME sheets grafted onto a novel ex vivo de-epithelialized porcine corneal stroma model successfully adhered, stratified, and sustained epithelial renewal over 15 days, supporting collagenase detachment as the preferred method for suture-free, support-free COME grafting in bilateral limbal stem cell deficiency treatment.",
        main_limitations="Ex vivo porcine stroma model only, no live animal or human clinical grafting; no quantitative adhesion-strength or transparency data; long-term (beyond 15 days) graft stability and functional visual outcomes not assessed in this study.",
        translational_readiness_level="early preclinical (in vitro / ex vivo)",
        benchmarking_relevance="medium",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Cell Transplantation (SAGE), DOI 10.1177/0963689717741140, 2018 -- Cell Transplantation is a fully open-access SAGE journal; full-text web_fetch not attempted this run to conserve run budget, abstract-level extraction used. Not a biomaterial-scaffold study per se (carrier-free cell sheet), but relevant to the review's epithelium/limbal-deficiency treatment benchmarking as a scaffold-free comparator technique.",
    ),
    "PUBMED_0144": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / full-thickness corneal substitute construction study (ex vivo organ co-culture with surgical handling test)",
        target_layer_final="multiple_layers (full-thickness: epithelium + stroma + endothelium)",
        biomaterial_category="decellularized xenogeneic (porcine) corneal matrix, recellularized with multiple human corneal cell types across all three layers",
        specific_materials="anterior acellular porcine corneal matrix (AAPCM), compared against posterior-APCM (PAPCM), both derived from decellularized porcine cornea; recellularized with human corneal epithelial cells, keratocytes, and endothelial cells",
        fabrication_method="porcine cornea decellularized to produce APCM; anterior (AAPCM) and posterior (PAPCM) portions biomechanically compared by uniaxial tensile testing, with AAPCM selected as the superior scaffold; a custom suspending-ring device (fabricated by deforming an acupuncture needle) combined with a 48-well plate and culture medium to create a novel 3D organ co-culture system; human corneal cells (epithelial, keratocyte, endothelial) co-cultured with AAPCM in this organ-culture system to build a full-thickness human corneal substitute; construct then tested surgically via penetrating keratoplasty (PKP) with clinical follow-up observation",
        scaffold_architecture="whole decellularized porcine corneal matrix (anterior portion) retaining native collagen fibers, Bowman's membrane, and Descemet's membrane architecture, recellularized across all three native corneal cell compartments",
        cell_type_used="human corneal epithelial cells, human keratocytes, and human corneal endothelial cells (all three native corneal cell types)",
        cell_source="human (corneal epithelial, stromal, and endothelial cells, cultured)",
        growth_factors_or_bioactive_agents="none reported beyond standard culture medium components",
        optical_transparency_reported="yes",
        optical_metric_details="Corneal transparency of the constructed full-thickness substitute increased gradually after penetrating keratoplasty (PKP) surgery and was almost completely restored by 7 days post-surgery (qualitative clinical observation; no numeric transmittance value given in abstract).",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Uniaxial tensile testing showed the biomechanical property of AAPCM was better than PAPCM (no specific numeric modulus/strength values given in the retrieved abstract); the final construct 'withstood surgical procedures during penetrating keratoplasty,' indicating adequate suturability/handling strength, again without numeric quantification in the abstract; MTT assay confirmed no cytotoxicity from suspending-ring soaking solutions.",
        biological_testing_reported="yes",
        biological_metric_details="Human corneal cells grew better on AAPCM than PAPCM. In the final full-thickness construct: keratocytes scattered uniformly through the AAPCM and expressed vimentin; a 3-4 layer stratified epithelium formed on the Bowman's-membrane surface expressing cytokeratin 3; a single endothelial cell layer covered the stromal surface, expressed Na+/K+-ATPase, and formed zonula occludens tight junctions -- closely resembling normal human corneal histoarchitecture (confirmed by immunofluorescence and SEM, including native-like microvilli on the epithelial surface).",
        in_vitro_model="yes",
        ex_vivo_model="yes",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="7 days post-surgery (penetrating keratoplasty follow-up observation of transparency restoration)",
        main_outcomes="Using a novel suspending-ring-based 3D organ co-culture system, a full-thickness human corneal substitute was successfully constructed from anterior acellular porcine corneal matrix (AAPCM, biomechanically superior to posterior-APCM) recellularized with human epithelial cells, keratocytes, and endothelial cells, each forming histoarchitecturally normal layers (stratified CK3+ epithelium, vimentin+ keratocytes, Na+/K+-ATPase+ endothelium with tight junctions); the construct withstood penetrating keratoplasty surgical handling and regained near-complete transparency within 7 days post-surgery.",
        main_limitations="Ex vivo/organ-culture evaluation only, no live animal implantation or clinical human transplantation; xenogeneic (porcine) scaffold source carries immunogenicity considerations for eventual clinical translation; no quantitative biomechanical (tensile strength/modulus) or optical transmittance values given in the retrieved abstract despite qualitative claims of comparability and functional restoration; short (7-day) follow-up window.",
        translational_readiness_level="early preclinical (ex vivo organ-culture model with surgical handling validation)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "International Journal of Ophthalmology, DOI 10.18240/ijo.2019.03.01, 2019 -- International Journal of Ophthalmology is a fully open-access journal; full-text web_fetch not attempted this run to conserve run budget, abstract-level extraction used. Notable as one of the few Tier 1 records reconstructing all three native corneal cell layers (epithelium, stroma, endothelium) simultaneously on a single decellularized xenogeneic scaffold with confirmed histoarchitectural fidelity -- high value for the review's full-thickness/multilayer benchmarking table.",
    ),
    "PUBMED_0273": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / multilayered scaffold fabrication and characterization study (ex vivo porcine cornea suturing/integration test)",
        target_layer_final="stroma (with epithelial layer added for the cellularized variant)",
        biomaterial_category="decellularized xenogeneic (porcine) sheet / hydrogel composite, bottom-up multilayer assembly",
        specific_materials="decellularized porcine corneal sheets (cryosectioned lenticules, detergent-decellularized, air-dried) layered with cell-laden collagen type I hydrogel between sheets; human corneal stromal cells encapsulated in the collagen I hydrogel; human corneal epithelial cells seeded on the surface of a subset of constructs",
        fabrication_method="corneal lenticules cut from porcine corneas by cryosectioning, then decellularized using detergents and air-dried for storage as thin sheets; human corneal stromal cells encapsulated in collagen I hydrogel and cast between multiple stacked decellularized porcine sheets using a novel bottom-up layering assembly technique to achieve high, uniform cellularity throughout the construct; constructs cultured 2 weeks in serum-free medium with ascorbic acid and insulin; epithelial cells then seeded on the surface and cultured an additional week; constructs without epithelial cells sutured onto an ex vivo porcine cornea and cultured 1 week to test surgical integration",
        scaffold_architecture="multilayered 'sandwich' assembly of alternating decellularized porcine corneal sheets and cell-laden collagen I hydrogel layers, bottom-up stacked to promote high-cellularity throughout construct thickness",
        cell_type_used="human corneal stromal cells (encapsulated in hydrogel) and human corneal epithelial cells (surface-seeded on a subset of constructs)",
        cell_source="human (corneal stromal and epithelial cells); porcine (decellularized sheet material, acellular)",
        growth_factors_or_bioactive_agents="ascorbic acid and insulin supplementation used in serum-free culture medium to support keratocyte-phenotype matrix synthesis (not incorporated into the scaffold material itself)",
        optical_transparency_reported="yes",
        optical_metric_details="Transparency was analyzed as part of construct characterization (alongside cell viability and phenotype, via qPCR, histology, and immunofluorescence); no specific numeric transmittance value is given in the retrieved abstract text.",
        mechanical_testing_reported="partial",
        mechanical_metric_details="Decellularized porcine sheets were more resistant to degradation than the collagen I hydrogels alone; the assembled construct was 'amenable to surgical handling and no tearing occurred during suturing' onto an ex vivo porcine cornea (qualitative handling assessment); dsDNA content after decellularization was 13 +/- 1.2 ng/mg dry tissue (a decellularization-efficacy metric, not a mechanical one); no numeric tensile strength or modulus values given in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="Constructs maintained high cell viability with a keratocyte-like phenotype, with upregulation of keratocan, decorin, lumican, collagen I, ALDH3A1, and CD34 (assessed by qPCR); corneal epithelial cells formed a stratified layer with cobblestone morphology. After 7 days ex vivo on porcine host corneas, constructs were covered by host-derived neoepithelium and showed integration into the host stroma.",
        in_vitro_model="yes",
        ex_vivo_model="yes",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="2 weeks (stromal construct culture) + 1 week (epithelial layer culture); 1 week (ex vivo porcine cornea suture-integration test)",
        main_outcomes="A novel bottom-up multilayer assembly technique -- alternating decellularized porcine corneal sheets with cell-laden collagen I hydrogel -- achieved rapid, uniform recellularization (dsDNA reduced to 13 ng/mg dry tissue) with a keratocyte-like phenotype (upregulated keratocan, decorin, lumican, collagen I, ALDH3A1, CD34) and stratified corneal epithelium; the resulting corneal stromal equivalent was surgically suturable without tearing, integrated with host tissue and was covered by host-derived neoepithelium after 1 week ex vivo on porcine corneas, demonstrating feasibility of a simple, rapid, tissue-derived-only approach to anterior corneal substitute fabrication.",
        main_limitations="Ex vivo porcine cornea integration testing only, no live animal or human clinical evaluation; xenogeneic (porcine) sheet component carries immunogenicity considerations; no quantitative transmittance or tensile mechanical values given in the retrieved abstract despite characterization being described; short (1-week) ex vivo integration follow-up.",
        translational_readiness_level="early preclinical (in vitro / ex vivo)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Tissue Engineering Part A, DOI 10.1089/ten.TEA.2020.0019, 2020 -- Mary Ann Liebert subscription journal, no open-access indication found via WebSearch for this specific article; abstract-level extraction only. Directly comparable to PUBMED_0144 (this batch) and PUBMED_0821 (this batch) for a decellularized-porcine-scaffold benchmarking narrative in the stroma/full-thickness table; notable for its rapid (bottom-up layered) recellularization strategy addressing the densely-packed-collagen recellularization barrier common to decellularized corneal scaffolds.",
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
    retrieval_notes="Europe PMC REST API fetch blocked by web_fetch provenance restriction in this unattended run; abstract taken from already-verified local screening corpus text instead, cross-checked against a WebSearch lookup of the same PMID/title/DOI.",
    extraction_ready="yes",
    reason_not_extraction_ready="",
)

TRACKER_UPDATE_PUBMED_0821 = dict(
    full_text_status="retrieved (full text, open access)",
    pdf_available="yes",
    source_checked="PMC11426139 full text (web_fetch) + local screening corpus abstract",
    retrieval_date="2026-07-20",
    retrieval_notes="Full text retrieved directly from PMC11426139 (Materials Today Bio, open access). Full results, discussion, and conclusion sections reviewed for quantitative optical, mechanical, and in vivo detail.",
    extraction_ready="yes",
    reason_not_extraction_ready="",
)

TRACKER_UPDATE_PUBMED_0038 = dict(
    full_text_status="retrieved (abstract-level only)",
    pdf_available="yes (Nanomaterials is fully open access MDPI journal; full-text fetch not attempted this run)",
    source_checked="local screening corpus abstract + journal open-access status known (MDPI Nanomaterials)",
    retrieval_date="2026-07-20",
    retrieval_notes="Nanomaterials (MDPI) is a fully open-access journal; extraction drawn from local screening-corpus abstract text to conserve run budget after full-text retrieval of PUBMED_0821.",
    extraction_ready="yes",
    reason_not_extraction_ready="",
)

TRACKER_UPDATE_PUBMED_0049 = dict(
    full_text_status="retrieved (abstract-level only)",
    pdf_available="yes (Cell Transplantation is fully open access SAGE journal; full-text fetch not attempted this run)",
    source_checked="local screening corpus abstract + journal open-access status known (SAGE Cell Transplantation)",
    retrieval_date="2026-07-20",
    retrieval_notes="Cell Transplantation (SAGE) is a fully open-access journal; extraction drawn from local screening-corpus abstract text to conserve run budget.",
    extraction_ready="yes",
    reason_not_extraction_ready="",
)

TRACKER_UPDATE_PUBMED_0144 = dict(
    full_text_status="retrieved (abstract-level only)",
    pdf_available="yes (International Journal of Ophthalmology is fully open access; full-text fetch not attempted this run)",
    source_checked="local screening corpus abstract + journal open-access status known (Int J Ophthalmol)",
    retrieval_date="2026-07-20",
    retrieval_notes="International Journal of Ophthalmology is a fully open-access journal; extraction drawn from local screening-corpus abstract text to conserve run budget.",
    extraction_ready="yes",
    reason_not_extraction_ready="",
)

TRACKER_UPDATE_PUBMED_0947 = dict(
    full_text_status="retrieved (abstract-level only)",
    pdf_available="unknown / not verified this run (RSC Nanoscale, subscription journal, no open-access indication found via WebSearch)",
    source_checked="local screening corpus abstract + WebSearch cross-check (pubs.rsc.org)",
    retrieval_date="2026-07-20",
    retrieval_notes="RSC Nanoscale is a subscription journal; no open-access indication found for this article via WebSearch. Abstract-level extraction only.",
    extraction_ready="yes",
    reason_not_extraction_ready="",
)

TRACKER_UPDATE_PUBMED_0990 = dict(
    full_text_status="retrieved (abstract-level only)",
    pdf_available="unknown / not verified this run (ACS Biomaterials Science & Engineering, subscription journal, no open-access indication found via WebSearch)",
    source_checked="local screening corpus abstract + WebSearch cross-check (pubs.acs.org)",
    retrieval_date="2026-07-20",
    retrieval_notes="ACS Biomaterials Science & Engineering is a subscription journal; no open-access indication found for this article via WebSearch. Abstract-level extraction only.",
    extraction_ready="yes",
    reason_not_extraction_ready="",
)

TRACKER_UPDATE_PUBMED_0273 = dict(
    full_text_status="retrieved (abstract-level only)",
    pdf_available="unknown / not verified this run (Tissue Engineering Part A, Mary Ann Liebert subscription journal, no open-access indication found via WebSearch)",
    source_checked="local screening corpus abstract",
    retrieval_date="2026-07-20",
    retrieval_notes="Tissue Engineering Part A (Mary Ann Liebert) is a subscription journal; no open-access indication found for this specific article. Abstract-level extraction only.",
    extraction_ready="yes",
    reason_not_extraction_ready="",
)

SPECIAL = {
    "PUBMED_0821": TRACKER_UPDATE_PUBMED_0821,
    "PUBMED_0038": TRACKER_UPDATE_PUBMED_0038,
    "PUBMED_0049": TRACKER_UPDATE_PUBMED_0049,
    "PUBMED_0144": TRACKER_UPDATE_PUBMED_0144,
    "PUBMED_0947": TRACKER_UPDATE_PUBMED_0947,
    "PUBMED_0990": TRACKER_UPDATE_PUBMED_0990,
    "PUBMED_0273": TRACKER_UPDATE_PUBMED_0273,
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
