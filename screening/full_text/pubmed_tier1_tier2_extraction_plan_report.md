# Tier 1 / Tier 2 Extraction Plan Report

## Purpose

Splits the balanced core (protocol v0.2) into a Tier 1 group for full template extraction and a Tier 2 group cited for context only, so extraction effort concentrates on the highest-value clinical/in-vivo/ex-vivo/benchmark-rich records rather than spreading evenly across all core records.

## Cutoff

Tier 1 = retrieval_priority_score >= 15.

## Counts

- Tier 1 - full extraction: 101
- Tier 2 - light-touch / cited for context: 147

## Tier 1 Layer Distribution

- epithelium_limbus: 32
- endothelium: 29
- multiple_layers: 24
- stroma: 16

## Tier 2 Layer Distribution

- multiple_layers: 80
- stroma: 42
- epithelium_limbus: 21
- endothelium: 6

## Manual Overrides

PUBMED_1083 (Puistola et al. 2024, stroma) and PUBMED_1084 (Ben Moussa et al. 2024, endothelium) were manually promoted to Tier 1 despite scoring below the 15-point cutoff (scores 4 and 8 respectively). Both were deliberately added to the core via a targeted Consensus reference-list snowball check specifically because they fill identified evidence gaps (stroma-specific bioprinted ECM bioink; a novel decellularized lens-capsule carrier for endothelial cells) - the keyword-scoring heuristic, built for bulk triage of the original 246-record pool, undervalues them because the abbreviated abstracts used for scoring don't surface the same keyword density as full PubMed abstracts. Manual curation overrides the heuristic here.

## Retrieval Order Within Tier 1

Sorted by retrieval_priority_score descending, then rotated across layers (endothelium, epithelium_limbus, stroma, multiple_layers) so no single layer is fully cleared before another is started. This keeps benchmarking-table coverage balanced across layers even if retrieval stalls partway through.

## First 20 Records To Retrieve

- PUBMED_0021 / PMID 29281419 / score 18 / endothelium: Electro-spun Membranes as Scaffolds for Human Corneal Endothelial Cells.
- PUBMED_0032 / PMID 29413615 / score 18 / endothelium: Functionalized silk fibroin film scaffold using β-Carotene for cornea endothelial cell regeneration.
- PUBMED_0075 / PMID 29998891 / score 18 / endothelium: Constructing a Novel Three-Dimensional Biomimetic Corneal Endothelium Graft by Culturing Corneal Endothelium Cells on Compressed Collagen Gels.
- PUBMED_0157 / PMID 31129253 / score 18 / endothelium: Investigating the effect of chitosan/ polycaprolactone blends in differentiation of corneal endothelial cells and extracellular matrix compositions.
- PUBMED_0304 / PMID 32622067 / score 18 / endothelium: Evaluation of reconstructed human corneal endothelium sheets made with porcine Descemet's membrane in vitro and in vivo.
- PUBMED_0379 / PMID 33448808 / score 18 / endothelium: Ultrathin, Strong, and Cell-Adhesive Agarose-Based Membranes Engineered as Substrates for Corneal Endothelial Cells.
- PUBMED_0382 / PMID 33463278 / score 18 / endothelium: Fish-Scale Collagen Membrane Seeded with Corneal Endothelial Cells as Alternative Graft for Endothelial Keratoplasty Transplantation.
- PUBMED_0421 / PMID 33939123 / score 18 / endothelium: Potential of a novel scaffold composed of human platelet lysate and fibrin for human corneal endothelial cells.
- PUBMED_0469 / PMID 34552187 / score 18 / endothelium: Optimization of polycaprolactone - based nanofiber matrices for the cultivation of corneal endothelial cells.
- PUBMED_0537 / PMID 35358736 / score 18 / endothelium: Construction of tissue-engineered human corneal endothelium for corneal endothelial regeneration using a crosslinked amniotic membrane scaffold.
- PUBMED_0588 / PMID 36080636 / score 18 / endothelium: Customizable Collagen Vitrigel Membranes and Preliminary Results in Corneal Engineering.
- PUBMED_0649 / PMID 37023465 / score 18 / endothelium: In Vitro Profiling of the Extracellular Matrix and Integrins Expressed by Human Corneal Endothelial Cells Cultured on Silk Fibroin-Based Matrices.
- PUBMED_0761 / PMID 38486306 / score 18 / endothelium: Bioprinting of human pluripotent stem cell derived corneal endothelial cells with hydrazone crosslinked hyaluronic acid bioink.
- PUBMED_0777 / PMID 38780042 / score 18 / endothelium: Alginate Hydrogel Integrated with a Human Fibroblast-Derived Extracellular Matrix Supports Corneal Endothelial Cell Functionality and Suppresses Endothelial-Mesenchymal Transition.
- PUBMED_0841 / PMID 39551331 / score 18 / endothelium: Repair effects of thermosensitive hydrogels combined with iPSC-derived corneal endothelial cells on rabbit corneal endothelial dysfunction.
- PUBMED_0910 / PMID 40221533 / score 18 / endothelium: Tissue engineered corneal endothelium transplantation in an ex vivo human cornea organ culture model.
- PUBMED_0940 / PMID 40536661 / score 18 / endothelium: Corneal Endothelium Regeneration with Decellularized Porcine Corneal Extracellular Matrix Scaffolds.
- PUBMED_0950 / PMID 40665979 / score 18 / endothelium: Research on the construction of corneal endothelium transplantation with acellular amniotic membrane as a scaffold.
- PUBMED_1009 / PMID 41218465 / score 18 / endothelium: Matrix stiffness modulates YAP-mediated glycolysis and proliferation in human corneal endothelial cells.
- PUBMED_0131 / PMID 30716697 / score 18 / epithelium_limbus: Poly-l/dl-lactic acid films functionalized with collagen IV as carrier substrata for corneal epithelial stem cells.

## Output File

- `screening/full_text/pubmed_tier1_tier2_extraction_plan.csv`
