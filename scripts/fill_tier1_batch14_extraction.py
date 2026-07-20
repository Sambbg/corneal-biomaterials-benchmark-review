"""
Tier 1 extraction batch 14 (2026-07-20, scheduled run continuation) -- FINAL Tier 1 batch.

Retrieval route note: as in batches 3-13, a direct web_fetch to the Europe PMC
REST API (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:<pmid>&format=json&resultType=core)
was not attempted this run -- every prior run from batch 3 through batch 13
has confirmed this fails with "URL not in provenance set" (the sandboxed
web_fetch tool only allows fetching URLs that already appeared in a user
message, a prior web_fetch result, or a WebSearch result; this unattended
scheduled run has no user available to authorize a new URL). Per the task
instructions, this structural block was not re-attempted this run.

Extraction for this batch was built from the complete, untruncated abstract
text already stored locally in
screening/full_text/pubmed_tier1_tier2_extraction_plan.csv (verified
PubMed/journal abstracts captured during the original screening pass), with
open-access status assessed from known journal/publisher policy: Bioengineering
& Translational Medicine (Wiley, published for AIChE) is fully open access
(gold OA); Frontiers in Cell and Developmental Biology is fully open access
(gold OA); npj Biomedical Innovations (Nature Portfolio npj series) is fully
open access (gold OA). Cornea (Wolters Kluwer/Lippincott), Journal of Tissue
Engineering and Regenerative Medicine (Wiley), Acta Biomaterialia (Elsevier),
and Journal of Controlled Release (Elsevier) are hybrid/subscription titles --
open-access status of these specific articles not individually confirmed
this run. This is noted per-record in extraction_notes.

Two target_layer_final corrections made this batch (same convention as the
corneal_layer-mislabeling corrections in earlier batches; upstream
`corneal_layer` column left untouched):
- PUBMED_0690: upstream corneal_layer = "multiple_layers", but the paper's
  title/abstract explicitly and exclusively frame the scaffold as a
  "tissue-engineered corneal stroma equivalent" -- target_layer_final
  corrected to "stroma".
- PUBMED_1011: upstream corneal_layer = "multiple_layers", but the study is
  specifically and exclusively about the limbal epithelial stem cell niche
  -- target_layer_final corrected to "epithelium_limbus".

PUBMED_1011 is a mechanistic/basic-science cell-biology study (fibronectin
coating concentration + niche-cell-conditioned media effects on LESC
self-renewal gene expression) rather than a fabricated-scaffold biomaterial
study -- extracted with biomaterial_category/scaffold_architecture marked
accordingly, similar in kind to the PUBMED_0202 record extracted in an
earlier batch, per the "say so explicitly rather than guessing" instruction.

This is the final Tier 1 batch: all 101 Tier 1 records reach
extraction_status = completed after this batch is applied (94 already
completed at the start of this run, +7 in this batch = 101/101).

This batch (7 records -- all remaining Tier 1 records):
- PUBMED_0016 (PMID 29176452) - collagen-based fillers (CLP-PEG hydrogel) vs. cyanoacrylate glue for sealing corneal perforations, ex vivo human cornea bursting-pressure study.
- PUBMED_0145 (PMID 30938102) - TGF-beta1-activated dendritic cells and fibroblast tenascin c response to EDC- vs. CMC-crosslinked recombinant collagen III full-thickness corneal hydrogel implants, mouse graft model + in vitro DC-fibroblast coculture.
- PUBMED_0690 (PMID 37476050) - decellularized squid mantle scaffold (DSMS) as a tissue-engineered corneal stroma equivalent, in vitro + rat intramuscular + rabbit inter-corneal implantation.
- PUBMED_1011 (PMID 41234357) - fibronectin coating concentration and limbal-niche-cell-conditioned media effects on LESC self-renewal (PEDF/HES1 gene expression), in vitro mechanistic study.
- PUBMED_1072 (PMID 42035972) - limbal organoids auto-bioprinted onto a lithographically patterned collagen vitrigel membrane with a biomimetic limbal stem cell niche annulus, in vitro + rabbit corneal injury repair model.
- PUBMED_0937 (PMID 40451552) - porous photocurable GelMA hydrogel (PG) for sutureless topical delivery of cultivated limbal stem cells, in vitro screening + rabbit LSCD model.
- PUBMED_1071 (PMID 42032346) - Collagen IV/Laminin-521-functionalized electrospun PLGA scaffold supporting iPSC-derived limbal stem cell attachment and differentiation, in vitro only.
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
    "documented in batches 3-13 and was not re-attempted this run. "
)

EXTRACTIONS = {
    "PUBMED_0016": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / ex vivo mechanical performance study (human donor cornea, translational sealant/filler evaluation)",
        target_layer_final="stroma",
        biomaterial_category="injectable/moldable collagen-like peptide hydrogel filler plus a collagen hydrogel patch, used as a biologic sealant alternative to cyanoacrylate glue",
        specific_materials="collagen-like peptide conjugated to polyethylene glycol (CLP-PEG) hydrogel and its chemical crosslinker; 100-micron thick collagen hydrogel patch",
        fabrication_method="CLP-PEG hydrogel and its crosslinker tested for biocompatibility; tested as fillers in ex vivo human donor corneas with surgically created full-thickness perforations; three sealing methods compared head-to-head (n=10 each): (1) cyanoacrylate glue with polyethylene patch applied ab externo [clinical gold standard], (2) 100-micron collagen hydrogel patch applied ab interno alone, (3) the same collagen hydrogel patch ab interno supplemented with CLP-PEG hydrogel molded in situ to fill the remaining stromal defect; bursting pressure measured for each method",
        scaffold_architecture="ab interno patch-plus-filler system: a thin collagen hydrogel sheet patch combined with an in-situ-molded CLP-PEG hydrogel filler for the corneal stromal perforation defect",
        cell_type_used="not applicable -- acellular hydrogel sealant/filler system; no cells reported",
        cell_source="not applicable",
        growth_factors_or_bioactive_agents="none reported; CLP-PEG hydrogel is designed as a structural framework intended to promote corneal tissue regeneration, but no exogenous growth factors are described",
        optical_transparency_reported="no / not reported in abstract",
        optical_metric_details="Not reported; the study evaluates acute sealing/bursting-pressure performance rather than optical transparency.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Mean bursting pressure: cyanoacrylate glue (gold standard) 325.9 mmHg, significantly higher than the ab interno collagen hydrogel patch alone (46.3 mmHg) and the patch supplemented with CLP-PEG filler (86.6 mmHg -- higher than patch alone but still well below cyanoacrylate).",
        biological_testing_reported="partial",
        biological_metric_details="CLP-PEG hydrogel and crosslinker were tested and reported biocompatible (not further quantified numerically in the retrieved abstract); sealing reliability assessed directly -- the 100-micron collagen hydrogel patch (ab interno) sealed 100% (10/10) of ex vivo perforations effectively, whereas conventional ab externo cyanoacrylate glue patching failed to seal in 30% (3/10) of cases.",
        in_vitro_model="no",
        ex_vivo_model="yes",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="not applicable (acute single-timepoint ex vivo bursting-pressure test)",
        main_outcomes="In ex vivo human donor corneas with surgically created full-thickness perforations, an ab interno collagen hydrogel patch (with or without a supplemental CLP-PEG hydrogel filler) achieved effective sealing in 100% of specimens, versus a 30% failure rate for conventional ab externo cyanoacrylate glue patching, even though the bursting pressure achieved by the collagen-based approaches (46.3-86.6 mmHg) was substantially lower than cyanoacrylate (325.9 mmHg); the CLP-PEG system is additionally designed to promote corneal tissue regeneration rather than remain as a permanent inert glue.",
        main_limitations="Ex vivo human cornea model only, with no in vivo or clinical evaluation; bursting pressure of the collagen-based methods is markedly lower than the cyanoacrylate gold standard, raising open questions about performance under physiological intraocular-pressure fluctuations or trauma; modest sample size (n=10/group); authors explicitly state further material refinement and clinical trials are required before clinical use.",
        translational_readiness_level="early preclinical (ex vivo human tissue model)",
        benchmarking_relevance="medium",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Cornea (Wolters Kluwer/Lippincott Williams & Wilkins), DOI 10.1097/ICO.0000000000001459, 2018 -- hybrid/subscription journal; open-access status of this specific article not confirmed this run; abstract-level extraction only. Notable as one of the few Tier 1 records evaluating a biomaterial as an acute surgical sealant/filler for corneal perforation (rather than a long-term tissue-engineered replacement), with a direct head-to-head mechanical (bursting-pressure) comparison against the clinical gold-standard treatment (cyanoacrylate glue) in human ex vivo tissue.",
    ),
    "PUBMED_0145": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / immunology-mechanistic study with in vivo full-thickness corneal graft model (mouse) and in vitro dendritic cell-fibroblast coculture",
        target_layer_final="multiple_layers",
        biomaterial_category="crosslinked recombinant human collagen III hydrogel, used as a full-thickness corneal substitute graft",
        specific_materials="recombinant human collagen III hydrogels crosslinked with two different carbodiimide chemistries: nonbulky EDC-NHS (1-ethyl-3-(3-dimethylamino-propyl)-carbodiimide hydrochloride with N-hydroxysuccinimide) versus sterically bulky, aromatic CMC-NHS (N-cyclohexyl-N'-(2-morpholinoethyl)-carbodiimide with N-hydroxysuccinimide)",
        fabrication_method="recombinant human collagen III hydrogels crosslinked using either EDC-NHS or bulky CMC-NHS chemistry; hydrogels implanted as full-thickness corneal grafts in a mouse model; immunohistochemistry performed on resulting retro-corneal membranes (RCM) for corneal epithelial cytokeratin 12, alpha-smooth muscle actin, and CD11c+ dendritic cell (DC) infiltration; tenascin c expression quantified; parallel in vitro DC-fibroblast coculture experiments performed with TGF-beta1 or lipopolysaccharide (LPS) stimulation, including TGF-beta1 neutralization controls",
        scaffold_architecture="full-thickness hydrogel corneal substitute implant formed from a crosslinked collagen III network",
        cell_type_used="host-derived cells infiltrating post-implantation (corneal epithelial cells, CD11c+ dendritic cells, fibroblasts); in vitro dendritic cell-fibroblast cocultures",
        cell_source="host (murine) tissue infiltration for the in vivo component; in vitro DC/fibroblast coculture source not further specified beyond the murine system",
        growth_factors_or_bioactive_agents="transforming growth factor beta1 (TGF-beta1), studied as the key immunomodulatory driver of dendritic cell-fibroblast crosstalk; lipopolysaccharide (LPS) used as a comparator inflammatory stimulus in vitro",
        optical_transparency_reported="yes",
        optical_metric_details="Corneas receiving full-thickness hydrogel implants became opaque due to formation of dense retro-corneal membranes (RCM) in both the EDC-NHS and CMC-NHS crosslinked groups; no numeric transmittance/haze-scale value is reported in the retrieved abstract.",
        mechanical_testing_reported="no / not reported in abstract",
        mechanical_metric_details="Not reported; the study is focused on the immunological/wound-contraction response to the two crosslinking chemistries rather than mechanical characterization.",
        biological_testing_reported="yes",
        biological_metric_details="Both hydrogel types elicited corneal epithelial cytokeratin 12 and alpha-SMA expression (indicative of regenerative activity and wound contraction) within the RCM; EDC-NHS hydrogels showed greater CD11c+ dendritic cell infiltration and higher fibrosis-associated tenascin c expression than CMC-NHS hydrogels, which were previously shown to be more tolerizing to DC; in vitro, TGF-beta1-stimulated dendritic cells induced greater fibroblast tenascin c secretion than LPS-stimulated DCs, an effect blocked by TGF-beta1 neutralization; tenascin c staining localized to 40-50 micron membrane nanotubes formed in DC-fibroblast cocultures.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in the retrieved abstract for this study's own murine graft follow-up (prior related work using EDC-crosslinked collagen III hydrogels is cited elsewhere as showing stable human corneal regeneration for over 4 years)",
        main_outcomes="Full-thickness implantation of recombinant collagen III hydrogels in a mouse corneal graft model triggers retro-corneal-membrane-associated opacity accompanied by tissue-regeneration markers, with crosslinking chemistry (EDC-NHS vs. bulky CMC-NHS) shaping the innate immune response: EDC-NHS hydrogels drive greater CD11c+ dendritic cell infiltration and fibrosis-associated tenascin c expression than the more DC-tolerizing CMC-NHS hydrogels; mechanistically, TGF-beta1-alternatively-activated (tolerizing) dendritic cells appear to regulate fibroblast tenascin c secretion (partly via intercellular membrane nanotubes), linking hydrogel crosslinking chemistry to downstream fibrotic wound-contraction outcomes.",
        main_limitations="Mouse (not human) model only, with no clinical evidence; no mechanical or numeric optical-transmittance quantification; opacity (RCM) formation occurred in both crosslinking-chemistry groups, indicating neither fully avoided the fibrotic/inflammatory response and differed only in degree; precise sample sizes and follow-up timepoints not given in the retrieved abstract.",
        translational_readiness_level="preclinical (animal model, mouse)",
        benchmarking_relevance="medium",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Journal of Tissue Engineering and Regenerative Medicine (Wiley), DOI 10.1002/term.2853, 2019 -- hybrid/subscription journal; open-access status of this specific article not confirmed this run; abstract-level extraction only. This is a mechanistic immunology study rather than a novel biomaterial-fabrication report; it complements other EDC-crosslinked recombinant collagen III corneal hydrogel records elsewhere in the corpus (the same platform is referenced as showing multi-year stable human regeneration in prior work) by explaining crosslinker-chemistry-dependent immune and fibrotic response differences relevant to graft opacification risk.",
    ),
    "PUBMED_0690": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / novel marine-derived decellularized scaffold study with in vitro and in vivo evaluation (rat intramuscular + rabbit inter-corneal implantation)",
        target_layer_final="stroma",
        biomaterial_category="decellularized xenogeneic, non-mammalian (marine) natural scaffold intended as a corneal stroma substitute",
        specific_materials="decellularized squid mantle scaffold (DSMS), decellularized using 0.5% sodium dodecyl sulfate (SDS) solution and optically cleared using the CUBIC (clear, unobstructed brain imaging cocktails) method",
        fabrication_method="squid mantle chemically decellularized with 0.5% SDS solution; CUBIC tissue-clearing method applied to render the scaffold optically transparent; decellularization efficiency, essential amino acid composition, and fiber alignment characterized; in vitro cytotoxicity assessed via human corneal epithelial cell exposure to the DSMS soaking solution; in vivo biocompatibility and degradation assessed via rat intramuscular implantation; in vivo corneal integration assessed via a rabbit inter-corneal (stromal) implantation model",
        scaffold_architecture="acellular, decellularized natural collagenous scaffold retaining native squid mantle fiber alignment, optically cleared for corneal stromal application",
        cell_type_used="human corneal epithelial cells (used only for in vitro soaking-solution cytotoxicity testing; the implanted scaffold itself is acellular, with no exogenous cell seeding)",
        cell_source="not applicable for the implanted scaffold (acellular); human corneal epithelial cells (line or primary, not further specified) used only for the in vitro cytotoxicity assay",
        growth_factors_or_bioactive_agents="none exogenous; scaffold retains native marine extracellular-matrix composition (described as rich in essential amino acids) without added growth factors",
        optical_transparency_reported="yes",
        optical_metric_details="The CUBIC clearing method rendered the decellularized squid mantle scaffold transparent; no specific numeric transmittance percentage is given in the retrieved abstract.",
        mechanical_testing_reported="unclear / not reported in abstract",
        mechanical_metric_details="Regular fiber alignment was reported as maintained after decellularization (structural characterization), but no numeric mechanical (modulus/tensile/suture-retention) values are given in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="DSMS soaking solution was non-toxic to human corneal epithelial cells in vitro; in a rat intramuscular implantation model, DSMS underwent complete degradation while promoting muscle tissue growth, indicating good biocompatibility; in a rabbit inter-corneal (stromal) implantation model, DSMS showed good compatibility with the corneal stroma and promoted stromal regeneration without evident rejection.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in the retrieved abstract",
        main_outcomes="A novel decellularized squid mantle scaffold (DSMS), rendered optically transparent via the CUBIC clearing method and retaining native fiber alignment and a favorable essential amino acid profile, was non-cytotoxic in vitro, fully biodegradable and biocompatible in a rat intramuscular model, and -- most notably -- promoted corneal stromal regeneration without evident rejection when implanted inter-corneally in a rabbit model, positioning marine-derived (squid mantle) decellularized tissue as a promising, low-cost, donor-independent alternative corneal stromal substitute.",
        main_limitations="No numeric optical transmittance or mechanical (modulus/tensile/suture-retention) values are reported despite qualitative claims of transparency and structural fiber integrity; rabbit (not human) model only, with no clinical evidence; exact in vivo follow-up duration and sample sizes not specified numerically in the retrieved abstract; long-term (beyond the study period) integration and immune response not assessed.",
        translational_readiness_level="preclinical (animal model, rat and rabbit)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Bioengineering & Translational Medicine (Wiley, published on behalf of AIChE), DOI 10.1002/btm2.10531, 2023 -- Bioengineering & Translational Medicine is a fully open-access (gold OA) Wiley journal; full text freely available; full-text fetch not attempted this run, abstract-level extraction used. target_layer_final corrected to 'stroma' (upstream corneal_layer listed as 'multiple_layers'); the paper's title and abstract explicitly and exclusively frame DSMS as a 'tissue-engineered corneal stroma' substitute, with both the rat and rabbit in vivo models testing stromal-relevant biocompatibility/integration -- recommend a manual review-team fix, consistent with the corneal_layer-mislabeling pattern flagged in earlier batches (batches 5-6), though here the correction runs the opposite direction (an overly broad 'multiple_layers' label narrowed to the more specific 'stroma'). Notable as an unusual, low-cost, donor-independent marine biomaterial (squid mantle) source, distinct from the mammalian/porcine/fish-swim-bladder decellularized scaffolds seen elsewhere in the corpus (cf. PUBMED_0928, PUBMED_0322).",
    ),
    "PUBMED_1011": dict(
        extraction_status="completed",
        study_type="mechanistic / basic-science cell-biology in vitro study using primary human limbal niche cell cultures (not a fabricated-scaffold biomaterial study)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="single ECM protein surface coating (fibronectin) used as a 2D culture-substrate biomaterial, plus niche-cell-conditioned media -- not a fabricated 3D scaffold",
        specific_materials="fibronectin (FN) coating applied at 3, 5, and 8 micrograms/cm2 concentrations; conditioned media collected from limbal mesenchymal stromal cells (LMSCs), limbal melanocytes (LM), and human epidermal melanocytes (HEMn, negative control)",
        fabrication_method="primary cultures of limbal niche cells (LESCs, LMSCs, LM) established from remnant human corneal transplant specimens, with HEMn included as a negative-control cell source; LESCs cultured on FN-coated surfaces at three concentrations and/or in LM-, LMSC-, or HEMn-conditioned media; proliferation assessed via doubling time; self-renewal/stemness assessed via PEDF and HES1 gene expression",
        scaffold_architecture="not applicable -- no fabricated 3D scaffold; fibronectin used as a 2D surface coating on standard culture plasticware",
        cell_type_used="limbal epithelial stem cells (LESCs), limbal mesenchymal stromal cells (LMSCs), limbal melanocytes (LM); human epidermal melanocytes (HEMn) as a negative control",
        cell_source="human, primary, derived from remnant human corneal transplant specimens",
        growth_factors_or_bioactive_agents="fibronectin (FN), a key extracellular-matrix component; endogenous paracrine growth factors present in LMSC- and LM-conditioned media (not individually identified in the retrieved abstract)",
        optical_transparency_reported="not applicable / not reported in abstract",
        optical_metric_details="Not applicable; this is a 2D cell-culture mechanistic study, not a scaffold/material optical characterization.",
        mechanical_testing_reported="not applicable / not reported in abstract",
        mechanical_metric_details="Not applicable; no scaffold mechanical testing was performed.",
        biological_testing_reported="yes",
        biological_metric_details="Compared to control, LMSC- and LM-conditioned media showed a clear trend toward upregulated PEDF and HES1 gene expression (self-renewal markers) in LESCs; FN coating generally upregulated PEDF and HES1 expression, with the effect most prominent at the lowest tested concentration (3 micrograms/cm2); doubling time was also assessed as a proliferation readout, though specific numeric values are not given in the retrieved abstract.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="not applicable (short-term in vitro culture study)",
        main_outcomes="Both fibronectin coating (most effective at a relatively low 3 microgram/cm2 concentration) and limbal-niche-cell-conditioned media (from LMSCs and limbal melanocytes) upregulated self-renewal-associated gene expression (PEDF, HES1) in cultured limbal epithelial stem cells relative to controls, supporting the potential of engineering the in vitro niche -- via ECM coating concentration and paracrine conditioned-media factors -- to preserve LESC stemness during ex vivo expansion ahead of transplantation.",
        main_limitations="This is a mechanistic/basic-science cell-biology study, not a fabricated-scaffold biomaterial study -- no 3D scaffold, optical, or mechanical characterization is reported; the specific paracrine factors responsible for the conditioned-media effect are not identified; doubling-time and gene-expression fold-change numeric values are not given in the retrieved abstract; purely in vitro with no ex vivo/animal/clinical evaluation; authors explicitly note further research is needed to elucidate underlying mechanisms.",
        translational_readiness_level="early preclinical (in vitro, mechanistic/basic-science study)",
        benchmarking_relevance="medium",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Frontiers in Cell and Developmental Biology, DOI 10.3389/fcell.2025.1667309, 2025 -- Frontiers journals are fully open-access (gold OA); full text freely available; full-text fetch not attempted this run, abstract-level extraction used. target_layer_final corrected to 'epithelium_limbus' (upstream corneal_layer listed as 'multiple_layers'); the study is specifically and exclusively about the limbal epithelial stem cell niche -- recommend a manual review-team fix, consistent with the corneal_layer-mislabeling pattern flagged in earlier batches. This record is a mechanistic niche-biology study rather than a scaffold-fabrication study (similar in kind to PUBMED_0202 extracted in an earlier batch): included for its direct relevance to optimizing fibronectin-coating concentration and conditioned-media formulation as design inputs for future LESC-expansion biomaterial/culture-system work, but contributes no scaffold-level benchmarking data itself.",
    ),
    "PUBMED_1072": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / organoid-based bioprinting and niche-engineering study with in vitro and in vivo evaluation (rabbit corneal injury repair model)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="3D-printed synthetic (PEGDA) niche scaffold combined with a natural-polymer (collagen vitrigel) membrane, auto-bioprinted with cell-derived limbal organoids",
        specific_materials="polyethylene glycol diacrylate (PEGDA), microstereolithography-printed into annular niche structures; collagen vitrigel (CV) membrane fabricated by lithography/imprinting to bear a limbal stem cell niche (LSCN) annulus pattern",
        fabrication_method="rabbit primary limbal cells sequentially cultured in Matrigel, then U-shaped plates, then mesh microwells to form homogeneous limbal organoids (LOs) exhibiting a corneal epithelial phenotype and stem-cell characteristics; PEGDA annular structures fabricated via microstereolithography; a collagen vitrigel (CV) membrane bearing an LSCN annulus produced by lithography and imprinting technology; LOs auto-bioprinted onto the CV membrane with LSCN annulus to form LO-sheets; sheets transplanted onto a rabbit model of complete excision of the anterior superficial cornea",
        scaffold_architecture="patterned collagen vitrigel membrane bearing a lithographically imprinted limbal stem cell niche (LSCN) annulus, seeded with auto-bioprinted limbal organoids to recreate the native annular limbal niche geometry",
        cell_type_used="rabbit primary limbal cells, matured into limbal organoids (LOs)",
        cell_source="rabbit, primary",
        growth_factors_or_bioactive_agents="not specified in the retrieved abstract beyond the sequential Matrigel/U-shaped-plate/mesh-microwell organoid culture protocol",
        optical_transparency_reported="no / not reported in abstract",
        optical_metric_details="Not reported; characterization focused on gene/protein expression (tight junctions, stemness, proliferation), P63 marker expression on the niche annulus, and in vivo healing outcomes rather than optical transparency.",
        mechanical_testing_reported="no / not reported in abstract",
        mechanical_metric_details="No numeric mechanical (modulus/tensile) testing data reported in the retrieved abstract for either the PEGDA or collagen vitrigel components.",
        biological_testing_reported="yes",
        biological_metric_details="LO-derived sheets showed upregulated genes/proteins associated with tight junctions, cellular stemness, and proliferation; P63 (stem-cell marker) expression was markedly elevated in cells located on the LSCN annulus compared to the smooth central region of the CV membrane, confirming niche-directed stemness patterning; in vivo, LO-sheet transplantation markedly accelerated corneal epithelial healing and reduced expression of the fibrosis marker alpha-SMA and the inflammatory marker CD45 compared to untreated controls.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in the retrieved abstract",
        main_outcomes="Rabbit primary limbal cells were matured into limbal organoids (LOs) with a corneal epithelial/stem-cell phenotype, then auto-bioprinted onto a microstereolithography- and lithography-patterned collagen vitrigel membrane bearing a biomimetic limbal stem cell niche (LSCN) annulus; niche-annulus positioning markedly elevated P63 stemness-marker expression, and transplantation of the resulting LO-sheets onto a rabbit model of complete anterior corneal excision markedly accelerated epithelial healing while reducing fibrosis (alpha-SMA) and inflammation (CD45) markers versus untreated controls -- demonstrating a complete organoid-to-bioprinted-niche-scaffold-to-in-vivo-repair pipeline for LSCD treatment.",
        main_limitations="No optical transparency or mechanical (modulus) data reported; rabbit (not human) model only, with no clinical evidence; exact follow-up duration and quantitative healing-rate/marker-reduction values are not given in the retrieved abstract; long-term durability/integration of the PEGDA/collagen-vitrigel niche scaffold not assessed.",
        translational_readiness_level="preclinical (animal model, rabbit)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Acta Biomaterialia (Elsevier), DOI 10.1016/j.actbio.2026.04.042, 2026 -- Elsevier hybrid/subscription journal; open-access status of this specific article not confirmed this run; abstract-level extraction only. Notable as a biomimetic-niche-geometry approach (lithographically patterned annular LSCN, distinct from flat/uniform scaffold designs elsewhere in the corpus) directly demonstrating niche-position-dependent stemness (P63) patterning; complements PUBMED_0867 and PUBMED_0826 in the corpus for the review's limbal-niche-engineering and bioprinting-manufacturing benchmarking discussion.",
    ),
    "PUBMED_0937": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / injectable-topical hydrogel delivery-system study with in vitro screening and in vivo evaluation (rabbit LSCD model)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="synthetic photocurable hydrogel (porous GelMA) functioning as a topical, non-invasive stem-cell delivery vehicle rather than an implanted structural scaffold",
        specific_materials="porous Gelatin Methacryloyl (GelMA, referred to as 'PG') hydrogel, fabricated with enlarged pore sizes via phase-separation technology",
        fabrication_method="in vitro and in vivo screening of multiple photocurable hydrogels performed to identify an optimal delivery candidate; porous GelMA (PG) hydrogel prepared via phase-separation technology to achieve larger pore sizes; hydrogel evaluated against four design criteria (stem-cell encapsulation before delivery, maintenance of stem-cell viability/self-renewal via non-canonical Wnt-pathway activation, uniform ocular-surface adhesion, and support of stem-cell proliferation/migration/adhesion); cultivated limbal stem cells encapsulated in PG hydrogel and applied topically -- combined with a corneal bandage contact lens -- to a rabbit LSCD model",
        scaffold_architecture="porous, photocurable, sutureless topical hydrogel patch/carrier (not an implanted solid scaffold), applied in combination with a corneal bandage contact lens",
        cell_type_used="cultivated limbal stem cells",
        cell_source="not specified in detail beyond 'cultivated limbal stem cells'; species not explicitly distinguished from the rabbit recipient model in the retrieved abstract",
        growth_factors_or_bioactive_agents="none exogenous reported; the proposed mechanism is activation of the non-canonical Wnt signaling pathway by the hydrogel microenvironment itself, rather than an added soluble growth factor",
        optical_transparency_reported="no / not reported in abstract",
        optical_metric_details="Not reported; characterization focused on pore size, cell viability/self-renewal signaling, ocular-surface adhesion, and in vivo functional repair rather than optical transparency.",
        mechanical_testing_reported="unclear / not reported in abstract",
        mechanical_metric_details="Not reported numerically; larger pore size (achieved via phase-separation technology) is described qualitatively, but no modulus/tensile/adhesion-strength values are given in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="The porous GelMA hydrogel maintained stem-cell viability and self-renewal via activation of the non-canonical Wnt signaling pathway, adhered uniformly to the ocular surface, and supported stem-cell proliferation, migration, and adhesion to target interfaces; in a rabbit LSCD model, PG hydrogel loaded with cultivated limbal stem cells (applied together with corneal bandage lenses) achieved sutureless, non-invasive delivery, significantly reduced surgery time versus conventional transplantation, overcame challenges associated with direct stem-cell eye-drop delivery, and promoted avascular, scar-free corneal regeneration.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in the retrieved abstract",
        main_outcomes="A porous, phase-separation-fabricated GelMA photocurable hydrogel (PG) was identified through in vitro/in vivo screening as satisfying four key stem-cell-delivery criteria (encapsulation, viability/self-renewal maintenance via non-canonical Wnt activation, uniform ocular-surface adhesion, and support of cell migration/proliferation); combined with a corneal bandage lens, PG hydrogel enabled sutureless, non-invasive topical delivery of cultivated limbal stem cells in a rabbit LSCD model, simplifying the transplantation procedure, reducing surgery time, and achieving avascular, scar-free corneal regeneration -- a notably lower-invasiveness alternative to surgical LESC transplantation.",
        main_limitations="No optical transparency or numeric mechanical/adhesion-strength data reported; rabbit (not human) model only, with no clinical evidence; exact follow-up duration, sample sizes, and quantitative regeneration/healing-rate values not given in the retrieved abstract; long-term hydrogel degradation/clearance not assessed.",
        translational_readiness_level="preclinical (animal model, rabbit)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Journal of Controlled Release (Elsevier), DOI 10.1016/j.jconrel.2025.113900, 2025 -- Elsevier hybrid/subscription journal; open-access status of this specific article not confirmed this run; abstract-level extraction only. Notable as one of the few Tier 1 records offering a genuinely non-invasive, sutureless topical (rather than surgically implanted) stem-cell delivery format; directly complements PUBMED_0867, PUBMED_1072, and PUBMED_0826 elsewhere in the corpus for the review's limbal stem cell delivery-method/manufacturing benchmarking discussion.",
    ),
    "PUBMED_1071": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / surface-functionalized electrospun scaffold study (in vitro only)",
        target_layer_final="epithelium_limbus",
        biomaterial_category="synthetic electrospun polymer scaffold surface-functionalized with natural extracellular-matrix proteins",
        specific_materials="electrospun Poly Lactide-co-Glycolic Acid (PLGA) scaffold, surface-functionalized with Collagen IV and Laminin-521 via atmospheric plasma treatment",
        fabrication_method="PLGA scaffold fabricated by electrospinning; scaffold surface functionalized with Collagen IV and Laminin-521 via atmospheric plasma treatment to address PLGA's inherent hydrophobicity and enhance biocompatibility; micro-perforations introduced by laser cutting to improve scaffold transparency and membrane permeability; induced pluripotent stem cell-derived limbal stem cells (iPSC-LSCs) cultured on the functionalized scaffold; attachment, survival, and expression of LSC stemness and corneal epithelial differentiation markers assessed",
        scaffold_architecture="electrospun PLGA nanofibrous mat, laser-micro-perforated for transparency/permeability, with surface coating of Collagen IV and Laminin-521",
        cell_type_used="induced pluripotent stem cell-derived limbal stem cells (iPSC-LSCs)",
        cell_source="human, induced pluripotent stem cell (iPSC)-derived",
        growth_factors_or_bioactive_agents="Collagen IV and Laminin-521 (extracellular-matrix proteins used as surface-functionalization coatings, not soluble growth factors)",
        optical_transparency_reported="yes",
        optical_metric_details="Laser-cut micro-perforations were introduced specifically to improve scaffold transparency and membrane permeability; no specific numeric transmittance percentage is given in the retrieved abstract.",
        mechanical_testing_reported="no / not reported in abstract",
        mechanical_metric_details="Not reported; characterization focused on surface-functionalization chemistry and cell attachment/marker expression rather than bulk mechanical testing.",
        biological_testing_reported="yes",
        biological_metric_details="Laminin-521 was identified as essential for iPSC-LSC attachment and survival on the scaffold; functionalized scaffolds showed enhanced expression of LSC stemness markers and corneal epithelial differentiation markers compared to unfunctionalized PLGA.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract (short-term in vitro attachment/marker-expression study)",
        main_outcomes="Surface functionalization of an electrospun, laser-micro-perforated PLGA scaffold with Collagen IV and Laminin-521 (via atmospheric plasma treatment) overcame PLGA's inherent hydrophobicity and successfully supported attachment, survival, and stemness/differentiation-marker expression of iPSC-derived limbal stem cells, with Laminin-521 identified as essential for cell attachment and survival -- establishing this functionalized PLGA scaffold as a viable in vitro platform for iPSC-LSC transplantation, pending future in vivo efficacy studies explicitly planned by the authors.",
        main_limitations="Purely in vitro study with no ex vivo, animal, or clinical evaluation (explicitly noted by the authors as future work); no numeric mechanical or quantitative transmittance data reported; sample sizes not specified in the retrieved abstract; long-term functional/barrier performance of the differentiated cells not assessed.",
        translational_readiness_level="early preclinical (in vitro only)",
        benchmarking_relevance="medium",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "npj Biomedical Innovations (Nature Portfolio), DOI 10.1038/s44385-026-00066-w, 2026 -- npj-series journals (Nature Portfolio) are fully open-access (gold OA); full text freely available; full-text fetch not attempted this run, abstract-level extraction used. Notable as one of the few Tier 1 records using iPSC-derived (rather than primary/donor) limbal stem cells, and for isolating Laminin-521 as the specific ECM component essential for iPSC-LSC attachment/survival; complements other electrospun-scaffold and surface-functionalization records elsewhere in the corpus.",
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

OA_IDS = {"PUBMED_0690", "PUBMED_1011", "PUBMED_1071"}
SUBSCRIPTION_IDS = {"PUBMED_0016", "PUBMED_0145", "PUBMED_1072", "PUBMED_0937"}

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
