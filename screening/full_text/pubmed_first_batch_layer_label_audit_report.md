# First Batch Layer Label Audit Report

## Purpose

This audit checks whether the assigned corneal layer labels in the first retrieval batch appear consistent with title/abstract terminology. This is important because the review is explicitly layer-specific.

## Counts

- First-batch records audited: 80
- label_ok: 59
- manual_check: 21

## Current Layer Counts

- endothelium: 20
- epithelium_limbus: 20
- multiple_layers: 20
- stroma: 20

## Inferred Layer Counts

- endothelium: 23
- stroma: 23
- epithelium_limbus: 20
- multiple_layers: 14

## Records Requiring Manual Layer Check

- PUBMED_0049 / PMID 29637812: current=multiple_layers / inferred=stroma — Preserving Basement Membranes during Detachment of Cultivated Oral Mucosal Epithelial Cell Sheets for the Treatment of Total Bilateral Limbal Stem Cell Deficiency.
- PUBMED_0387 / PMID 33542377: current=multiple_layers / inferred=stroma — A decellularized human corneal scaffold for anterior corneal surface reconstruction.
- PUBMED_0073 / PMID 29978836: current=multiple_layers / inferred=stroma — Decellularized corneal lenticule embedded compressed collagen: toward a suturable collagenous construct for limbal reconstruction.
- PUBMED_0317 / PMID 32743953: current=multiple_layers / inferred=stroma — Sustained Release of TPCA-1 from Silk Fibroin Hydrogels Preserves Keratocyte Phenotype and Promotes Corneal Regeneration by Inhibiting Interleukin-1β Signaling.
- PUBMED_0395 / PMID 33603277: current=multiple_layers / inferred=stroma — Simultaneous Interpenetrating Polymer Network of Collagen and Hyaluronic Acid as an In Situ-Forming Corneal Defect Filler.
- PUBMED_0453 / PMID 34400306: current=multiple_layers / inferred=stroma — Hydrogels derived from acellular porcine corneal stroma enhance corneal wound healing.
- PUBMED_0560 / PMID 35769102: current=multiple_layers / inferred=stroma — Electron-Beam Irradiated Recombinant Human Collagen-Phosphorylcholine Corneal Implants Retain Pro-Regeneration Capacity.
- PUBMED_0582 / PMID 36040708: current=multiple_layers / inferred=stroma — Natural Dual-Crosslinking Bioadhesive Hydrogel for Corneal Regeneration in Large-Size Defects.
- PUBMED_0585 / PMID 36063670: current=multiple_layers / inferred=stroma — Reconstructing auto tissue engineering lamellar cornea with aspartic acid modified acellular porcine corneal stroma and preconditioned limbal stem cell for corneal regeneration.
- PUBMED_0620 / PMID 36638943: current=multiple_layers / inferred=stroma — An electrospun scaffold functionalized with a ROS-scavenging hydrogel stimulates ocular wound healing.
- PUBMED_0637 / PMID 36844364: current=multiple_layers / inferred=stroma — A "T.E.S.T." hydrogel bioadhesive assisted by corneal cross-linking for in situ sutureless corneal repair.
- PUBMED_0648 / PMID 37019117: current=multiple_layers / inferred=stroma — Digital light processing-bioprinted poly-NAGA-GelMA-based hydrogel lenticule for precise refractive errors correction.
- PUBMED_0151 / PMID 30989737: current=stroma / inferred=endothelium — Construction of a high cell density human corneal endothelial equivalent and its transplantation in primate models.
- PUBMED_0016 / PMID 29176452: current=stroma / inferred=multiple_layers — Collagen-Based Fillers as Alternatives to Cyanoacrylate Glue for the Sealing of Large Corneal Perforations.
- PUBMED_0224 / PMID 31751429: current=stroma / inferred=endothelium — Treatment of corneal endothelial damage in a rabbit model with a bioengineered graft using human decellularized corneal lamina and cultured human corneal endothelium.
- PUBMED_0069 / PMID 29883810: current=stroma / inferred=multiple_layers — Cell-laden and orthogonal-multilayer tissue-engineered corneal stroma induced by a mechanical collagen microenvironment and transplantation in a rabbit model.
- PUBMED_0482 / PMID 34665455: current=stroma / inferred=multiple_layers — Preparation and In Vitro Characterization of Gelatin Methacrylate for Corneal Tissue Engineering.
- PUBMED_0709 / PMID 37731910: current=stroma / inferred=multiple_layers — Optimization and evaluation of oxygen-plasma-modified, aligned, poly (Є-caprolactone) and silk fibroin nanofibrous scaffold for corneal stromal regeneration.
- PUBMED_0947 / PMID 40613723: current=stroma / inferred=multiple_layers — A graphene oxide/niobium carbide MXene composite-based functional nanocomposite scaffold for artificial corneas.
- PUBMED_1068 / PMID 41947731: current=stroma / inferred=multiple_layers — Functional 3D bioprinting with GelMA/CMCh bioinks: a supportive microenvironment for stromal keratocyte maintenance and potential corneal stromal repair.
- PUBMED_0106 / PMID 30339045: current=stroma / inferred=endothelium — Evaluation of the Suitability of Biocompatible Carriers as Artificial Transplants Using Cultured Porcine Corneal Endothelial Cells.

## Output File

- `screening/full_text/pubmed_first_batch_layer_label_audit.csv`
