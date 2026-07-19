"""
First Tier 1 extraction batch (2026-07-19).

Fills the full extraction template for 4 records retrieved and reviewed in
this session:

- PUBMED_0075 (PMID 29998891, endothelium) - open access via PMC6048920.
- PUBMED_0157 (PMID 31129253, endothelium) - Elsevier paywalled, no PMC
  deposit found; extraction is abstract-level only (flagged in
  extraction_notes for manual full-text follow-up).
- PUBMED_1083 (PMID 38513048, stroma) - Consensus snowball-check addition,
  open access via PMC10995904.
- PUBMED_1084 (PMID 38534529, endothelium) - Consensus snowball-check
  addition, open access via PMC10968626.

Two other records queued for this batch, PUBMED_0021 (PMID 29281419) and
PUBMED_0032 (PMID 29413615), were blocked by a reCAPTCHA challenge on
pubmed.ncbi.nlm.nih.gov during retrieval and are left extraction_status =
not_started; their retrieval_tracker rows are marked "unavailable" with a
retry note (see scripts/update_tracker_batch1.py equivalent edits already
applied directly to the tracker CSV).
"""
import csv
from pathlib import Path

path = Path("extraction/pubmed_balanced_core_data_extraction_template.csv")
with path.open(newline="", encoding="utf-8-sig") as f:
    r = csv.DictReader(f)
    rows = list(r)
    fieldnames = r.fieldnames

by_id = {row["screening_id"]: row for row in rows}

EXTRACTIONS = {
    "PUBMED_0075": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / bioengineered graft study (in vitro)",
        target_layer_final="endothelium",
        biomaterial_category="collagen hydrogel",
        specific_materials="laminin-coated compressed collagen (CC) gel",
        fabrication_method="plastic compression of collagen gel to form a thin compressed collagen sheet, followed by laminin coating",
        scaffold_architecture="thin compressed collagen membrane/sheet",
        cell_type_used="bovine corneal endothelial cells (B-CECs)",
        cell_source="bovine (xenogeneic)",
        growth_factors_or_bioactive_agents="laminin surface coating (cell-adhesion protein, not a growth factor)",
        optical_transparency_reported="unclear / not reported in abstract",
        optical_metric_details="Not quantified in abstract; figures show mechanical test setup but no numeric transparency/transmittance value given.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Figure 1 shows biomechanical/mechanical properties testing of the compressed collagen gel; no numeric modulus value stated in abstract text.",
        biological_testing_reported="yes",
        biological_metric_details="SEM ultrastructural analysis; ZO-1 tight junction immunohistochemistry positive; cell density 3612.2 +/- 43.4 cells/mm2 (comparable to/higher than native human CEC density).",
        in_vitro_model="yes", ex_vivo_model="no", animal_model="no", clinical_evidence="no",
        follow_up_duration="not applicable / in vitro only",
        main_outcomes="Biomimetic corneal endothelium graft formed by culturing bovine CECs on laminin-coated compressed collagen gel; normal hexagonal morphology, ultrastructure, high cell density, and ZO-1 expression indicating basic endothelial barrier function.",
        main_limitations="Bovine (xenogeneic) cell source, not human; in vitro only, no animal or clinical validation; transparency not quantitatively reported.",
        translational_readiness_level="early preclinical (in vitro proof-of-concept)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes="Full abstract and figure captions reviewed via PMC (PMC6048920), open access. Exact mechanical/optical numeric values not present in abstract; would need full-text tables for detailed benchmarking numbers.",
    ),
    "PUBMED_0157": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / membrane fabrication and cell differentiation study (in vitro)",
        target_layer_final="endothelium",
        biomaterial_category="synthetic polymer blend membrane",
        specific_materials="chitosan/polycaprolactone (PCL) blend, PCL25 (25% PCL by weight)",
        fabrication_method="blended membrane casting; surface characterized by FTIR and AFM",
        scaffold_architecture="thin polymer blend membrane",
        cell_type_used="bovine corneal endothelial cells",
        cell_source="bovine (xenogeneic)",
        growth_factors_or_bioactive_agents="none exogenous; membrane surface chemistry alone used to modulate ECM/differentiation",
        optical_transparency_reported="no", optical_metric_details="Not reported in abstract.",
        mechanical_testing_reported="partial",
        mechanical_metric_details="AFM used for surface roughness/topography (PCL25 rougher than pure chitosan); FTIR confirmed PCL C=O bond. No tensile/modulus values reported.",
        biological_testing_reported="yes",
        biological_metric_details="Hexagonal CEC morphology maintained; ZO-1 and Na+/K+-ATPase immunofluorescence positive; western blot showed higher collagen type IV and reduced TGF-beta2 expression on PCL25 vs TCPS control.",
        in_vitro_model="yes", ex_vivo_model="no", animal_model="no", clinical_evidence="no",
        follow_up_duration="not applicable / in vitro only",
        main_outcomes="Chitosan/PCL25 blend membranes supported bovine CEC attachment and proliferation comparable to TCPS, hexagonal morphology, functional marker expression, and favorable ECM protein profile versus TCPS.",
        main_limitations="Bovine cells, in vitro only; full text is Elsevier-paywalled with no PMC deposit found, so extraction is abstract-level only; no transparency or mechanical strength data reported.",
        translational_readiness_level="early preclinical (in vitro)",
        benchmarking_relevance="medium-high",
        include_in_final_review="yes",
        extraction_notes="Full text paywalled (Elsevier), no open-access PMC copy found. Extraction based on complete PubMed abstract only; flagged for manual full-text follow-up if institutional access becomes available.",
    ),
    "PUBMED_1083": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / bioprinting study (in vitro)",
        target_layer_final="stroma",
        biomaterial_category="cell-derived extracellular matrix (dECM) bioink",
        specific_materials="human adipose stem cell-derived corneal stromal keratocyte (hASC-CSK) decellularized ECM, formulated as a corneal stroma-specific bioink",
        fabrication_method="hASC differentiation toward corneal stromal keratocytes (14 days), ECM collection and decellularization, formulated into bioink, 3D bioprinted",
        scaffold_architecture="3D bioprinted structures / printed grids from dECM-based bioink",
        cell_type_used="human adipose stem cell-derived corneal stromal keratocytes (hASC-CSKs)",
        cell_source="human adipose tissue-derived stem cells (donor-cornea-independent source)",
        growth_factors_or_bioactive_agents="none exogenous; matrix proteins produced endogenously (collagen I, V, lumican, keratocan)",
        optical_transparency_reported="yes",
        optical_metric_details="Transparency of printed bioink structures assessed visually immediately after printing and after 7 days in PBS, and for cell-laden constructs at 10 days postprinting; qualitative/visual assessment, no numeric transmittance value in abstract.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Shear-thinning rheological properties (frequency sweeps, n=4); printability and shape fidelity assessed via filament thickness and pore factor immediately and after 7 days in PBS (no significant difference, i.e. dimensionally stable).",
        biological_testing_reported="yes",
        biological_metric_details="DNA quantification confirmed decellularization efficacy (p<0.05 reduction); western blot/IF confirmed retained collagen I, V, lumican, keratocan; postprinting cell viability good at 1 and 7 days; connexin 43 expression at day 10 (cell-cell junctions); low immunogenicity vs fibrin control in hPBMC proliferation assay.",
        in_vitro_model="yes", ex_vivo_model="no", animal_model="no", clinical_evidence="no",
        follow_up_duration="up to 10 days postprinting (viability/transparency); 7 days PBS immersion (printability stability)",
        main_outcomes="Donor-cornea-free, cornea-specific ECM engineered from human adipose stem cells differentiated into stromal keratocytes; used as a bioink component for 3D-printed corneal stroma structures with good printability, shape fidelity, low immunogenicity, adequate transparency, and good postprinting cell viability.",
        main_limitations="In vitro only, no animal or clinical validation of the bioprinted construct; transparency reported qualitatively, not as numeric transmittance; conflict of interest disclosed (pending patent on the bioink).",
        translational_readiness_level="early preclinical (in vitro); clinically-precedented cell source (hASCs already used in corneal stromal clinical trials) is a translational strength",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes="Added via Consensus supplementary snowball check (protocol v0.2). Full open-access text available via PMC10995904. Strong candidate for the manufacturing-scalability / donor-independence translational bottleneck discussion.",
    ),
    "PUBMED_1084": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / carrier fabrication and decellularization study (in vitro)",
        target_layer_final="endothelium",
        biomaterial_category="decellularized biological tissue carrier",
        specific_materials="human anterior lens capsule, femtosecond-laser cut into 8 mm discs",
        fabrication_method="femtosecond laser cutting of whole human lenses using a custom lens holder (8 mm cut diameter), followed by decellularization via water immersion (3 days)",
        scaffold_architecture="thin transparent decellularized disc carrier, 8 mm diameter, with orientation marks",
        cell_type_used="corneal endothelial cells (CECs) seeded post-decellularization",
        cell_source="human lens capsule as acellular carrier; CECs seeded to form tissue-engineered endothelial keratoplasty (TEEK) constructs",
        growth_factors_or_bioactive_agents="none reported",
        optical_transparency_reported="yes",
        optical_metric_details="Transparency assessed via backlit chart; discs described as 'hardly visible' (i.e. transparent). No numeric transmittance percentage given in abstract/figure captions reviewed.",
        mechanical_testing_reported="partial",
        mechanical_metric_details="OCT imaging confirmed lens stability during laser cutting; no explicit tensile/modulus mechanical testing reported.",
        biological_testing_reported="yes",
        biological_metric_details="DiOC6/DAPI staining and DNA PCR quantification confirmed effective decellularization after 3 days; viability/mortality assay (Hoechst, Ethidium homodimer, Calcein-AM) at 4 weeks; CD166 and NCAM (CD56) immunolabeling confirmed endothelial marker expression; cells viable after 27 days culture.",
        in_vitro_model="yes", ex_vivo_model="no", animal_model="no", clinical_evidence="no",
        follow_up_duration="up to 27-28 days in vitro culture",
        main_outcomes="Femtosecond laser cutting produced standardized, reproducible transparent decellularized human lens capsule discs; complete decellularization after 3 days; discs supported corneal endothelial cell seeding with viable, marker-positive TEEK constructs for at least 27 days.",
        main_limitations="In vitro only in this paper (companion papers by the same group extend to animal TEEK models); mechanical properties not quantitatively benchmarked; still relies on human donor lens tissue.",
        translational_readiness_level="early preclinical (in vitro carrier fabrication and validation)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes="Added via Consensus supplementary snowball check (protocol v0.2). Full open-access text via PMC10968626. Same group (Thuret/Gain, Jean Monnet University) has related TEEK animal-model papers (Crouzet 2022, Aouimeur 2025/2026) surfaced in the same Consensus search - check during further Tier 1 retrieval whether these are already in the corpus.",
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
