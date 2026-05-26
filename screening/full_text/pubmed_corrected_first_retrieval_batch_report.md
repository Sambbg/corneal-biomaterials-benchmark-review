# Corrected First PubMed Retrieval Batch Report

## Purpose

This report applies manual layer-label corrections to the first PubMed retrieval batch after the automated layer-label audit flagged possible inconsistencies.

## Counts

- First-batch records checked: 80
- Records manually corrected: 20

## Correction Status Counts

- unchanged: 60
- corrected: 20

## Original Layer Counts

- endothelium: 20
- epithelium_limbus: 20
- multiple_layers: 20
- stroma: 20

## Corrected Layer Counts

- endothelium: 23
- stroma: 23
- epithelium_limbus: 21
- multiple_layers: 13

## Corrections Applied

- PUBMED_0049 / PMID 29637812: multiple_layers → epithelium_limbus — Preserving Basement Membranes during Detachment of Cultivated Oral Mucosal Epithelial Cell Sheets for the Treatment of Total Bilateral Limbal Stem Cell Deficiency.
- PUBMED_0387 / PMID 33542377: multiple_layers → multiple_layers — A decellularized human corneal scaffold for anterior corneal surface reconstruction.
- PUBMED_0073 / PMID 29978836: multiple_layers → multiple_layers — Decellularized corneal lenticule embedded compressed collagen: toward a suturable collagenous construct for limbal reconstruction.
- PUBMED_0395 / PMID 33603277: multiple_layers → stroma — Simultaneous Interpenetrating Polymer Network of Collagen and Hyaluronic Acid as an In Situ-Forming Corneal Defect Filler.
- PUBMED_0453 / PMID 34400306: multiple_layers → stroma — Hydrogels derived from acellular porcine corneal stroma enhance corneal wound healing.
- PUBMED_0560 / PMID 35769102: multiple_layers → multiple_layers — Electron-Beam Irradiated Recombinant Human Collagen-Phosphorylcholine Corneal Implants Retain Pro-Regeneration Capacity.
- PUBMED_0582 / PMID 36040708: multiple_layers → stroma — Natural Dual-Crosslinking Bioadhesive Hydrogel for Corneal Regeneration in Large-Size Defects.
- PUBMED_0585 / PMID 36063670: multiple_layers → stroma — Reconstructing auto tissue engineering lamellar cornea with aspartic acid modified acellular porcine corneal stroma and preconditioned limbal stem cell for corneal regeneration.
- PUBMED_0620 / PMID 36638943: multiple_layers → stroma — An electrospun scaffold functionalized with a ROS-scavenging hydrogel stimulates ocular wound healing.
- PUBMED_0637 / PMID 36844364: multiple_layers → stroma — A "T.E.S.T." hydrogel bioadhesive assisted by corneal cross-linking for in situ sutureless corneal repair.
- PUBMED_0648 / PMID 37019117: multiple_layers → stroma — Digital light processing-bioprinted poly-NAGA-GelMA-based hydrogel lenticule for precise refractive errors correction.
- PUBMED_0151 / PMID 30989737: stroma → endothelium — Construction of a high cell density human corneal endothelial equivalent and its transplantation in primate models.
- PUBMED_0016 / PMID 29176452: stroma → multiple_layers — Collagen-Based Fillers as Alternatives to Cyanoacrylate Glue for the Sealing of Large Corneal Perforations.
- PUBMED_0224 / PMID 31751429: stroma → endothelium — Treatment of corneal endothelial damage in a rabbit model with a bioengineered graft using human decellularized corneal lamina and cultured human corneal endothelium.
- PUBMED_0069 / PMID 29883810: stroma → stroma — Cell-laden and orthogonal-multilayer tissue-engineered corneal stroma induced by a mechanical collagen microenvironment and transplantation in a rabbit model.
- PUBMED_0482 / PMID 34665455: stroma → stroma — Preparation and In Vitro Characterization of Gelatin Methacrylate for Corneal Tissue Engineering.
- PUBMED_0709 / PMID 37731910: stroma → stroma — Optimization and evaluation of oxygen-plasma-modified, aligned, poly (Є-caprolactone) and silk fibroin nanofibrous scaffold for corneal stromal regeneration.
- PUBMED_0947 / PMID 40613723: stroma → stroma — A graphene oxide/niobium carbide MXene composite-based functional nanocomposite scaffold for artificial corneas.
- PUBMED_1068 / PMID 41947731: stroma → stroma — Functional 3D bioprinting with GelMA/CMCh bioinks: a supportive microenvironment for stromal keratocyte maintenance and potential corneal stromal repair.
- PUBMED_0106 / PMID 30339045: stroma → endothelium — Evaluation of the Suitability of Biocompatible Carriers as Artificial Transplants Using Cultured Porcine Corneal Endothelial Cells.

## Output Files

- Corrected first retrieval batch: `screening/full_text/pubmed_corrected_first_retrieval_batch.csv`
- Corrections applied only: `screening/full_text/pubmed_first_batch_layer_corrections_applied.csv`
