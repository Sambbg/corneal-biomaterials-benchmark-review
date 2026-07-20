# Tier 2 Layer-Label QC Check

## Purpose

Applies the same keyword-based check that surfaced the Tier 1 corneal_layer mislabeling pattern (6 records corrected across batches 5, 6, 14) to the 147 Tier 2 records. This is a heuristic flag for follow-up reading, not an automatic correction - Tier 2 records are not being deep-extracted, so their upstream `corneal_layer` label is what will actually be used for citation and layer-grouping purposes, making a mislabeled layer here more consequential than for a Tier 1 record (which gets a corrected `target_layer_final` field regardless).

## Result

- Tier 2 records checked: 147
- Records flagged for likely layer mismatch: 55
  - High confidence (title/abstract signal essentially unambiguous, spot-verified against 2 titles by hand): 15
  - Lower confidence (real signal but not verified, flagged only): 40

## High-Confidence Corrections (applied to `confirmed_layer_correction`)

These titles are unambiguous about their primary corneal layer - two were spot-verified by reading the full title carefully (PUBMED_1074, PUBMED_0106, both clearly about corneal endothelial cells despite an upstream 'stroma' label). Treat `suggested_layer` as correct for citation/layer-grouping purposes; upstream `corneal_layer` in the master screening files is left untouched, same convention as the Tier 1 corrections.

- **PUBMED_0073** / PMID 29978836 - upstream `multiple_layers` -> corrected `epithelium_limbus` (score 12 vs 0): Decellularized corneal lenticule embedded compressed collagen: toward a suturable collagenous construct for limbal reconstruction.
- **PUBMED_0317** / PMID 32743953 - upstream `multiple_layers` -> corrected `stroma` (score 10 vs 0): Sustained Release of TPCA-1 from Silk Fibroin Hydrogels Preserves Keratocyte Phenotype and Promotes Corneal Regeneration by Inhibiting Interleukin-1β Signaling.
- **PUBMED_0365** / PMID 33288782 - upstream `multiple_layers` -> corrected `epithelium_limbus` (score 12 vs 0): Deciphering the mechanoresponsive role of β-catenin in keratoconus epithelium.
- **PUBMED_0453** / PMID 34400306 - upstream `multiple_layers` -> corrected `stroma` (score 11 vs 0): Hydrogels derived from acellular porcine corneal stroma enhance corneal wound healing.
- **PUBMED_0606** / PMID 36497012 - upstream `multiple_layers` -> corrected `epithelium_limbus` (score 13 vs 1): Transcriptomic Landscape and Functional Characterization of Human Induced Pluripotent Stem Cell-Derived Limbal Epithelial Progenitor Cells.
- **PUBMED_0802** / PMID 39075142 - upstream `multiple_layers` -> corrected `epithelium_limbus` (score 24 vs 0): A novel tissue-engineered corneal epithelium based on ultra-thin amniotic membrane and mesenchymal stem cells.
- **PUBMED_0866** / PMID 39798638 - upstream `multiple_layers` -> corrected `epithelium_limbus` (score 28 vs 0): 3D printed biomimetic bilayer limbal implants for regeneration of the corneal structure in limbal stem cell deficiency.
- **PUBMED_0106** / PMID 30339045 - upstream `stroma` -> corrected `endothelium` (score 17 vs 1): Evaluation of the Suitability of Biocompatible Carriers as Artificial Transplants Using Cultured Porcine Corneal Endothelial Cells.
- **PUBMED_1074** / PMID 42059163 - upstream `stroma` -> corrected `endothelium` (score 10 vs 1): Real Architecture for 3D Tissue (RAFT): Mechanical Properties and Ability to Support the 3D Culture of Porcine Corneal Endothelial Cells.
- **PUBMED_0755** / PMID 38466286 - upstream `multiple_layers` -> corrected `endothelium` (score 13 vs 0): Substrate Stiffness Modulates Stemness and Differentiation of Rabbit Corneal Endothelium Through the Paxillin-YAP Pathway.
- **PUBMED_0962** / PMID 40762540 - upstream `multiple_layers` -> corrected `endothelium` (score 22 vs 0): Human Omental Mesothelial Cells Exhibit a Corneal Endothelial-Like Cell Phenotype for Tissue Engineering of a Corneal Endothelium Biomimetic.
- **PUBMED_0556** / PMID 35741104 - upstream `multiple_layers` -> corrected `epithelium_limbus` (score 19 vs 0): P-Cadherin Is Expressed by Epithelial Progenitor Cells and Melanocytes in the Human Corneal Limbus.
- **PUBMED_0652** / PMID 37056274 - upstream `multiple_layers` -> corrected `epithelium_limbus` (score 11 vs 0): MiRNA 24-3p-rich exosomes functionalized DEGMA-modified hyaluronic acid hydrogels for corneal epithelial healing.
- **PUBMED_0726** / PMID 37988231 - upstream `multiple_layers` -> corrected `stroma` (score 11 vs 0): Biomimetic Corneal Stroma for Scarless Corneal Wound Healing via Structural Restoration and Microenvironment Modulation.
- **PUBMED_0255** / PMID 32188843 - upstream `multiple_layers` -> corrected `stroma` (score 10 vs 0): Fiber reinforced GelMA hydrogel to induce the regeneration of corneal stroma.

## Lower-Confidence Flags (not corrected, for future reference only)

Real keyword signal toward a different layer than the upstream label, but not strong enough to treat as confirmed without an actual read. Do not use these for layer-grouping without checking first.

- PUBMED_0175 / PMID 31349505 - upstream `multiple_layers`, signal toward `stroma` (score 9 vs 0): Compressed collagen intermixed with cornea-derived decellularized extracellular matrix providing mechanical and biochemical niches for corneal stroma analogue.
- PUBMED_0196 / PMID 31514545 - upstream `multiple_layers`, signal toward `epithelium_limbus` (score 9 vs 0): Development and Characterization of an Acellular Porcine Small Intestine Submucosa Scaffold for Use in Corneal Epithelium Tissue Engineering.
- PUBMED_0329 / PMID 32841745 - upstream `multiple_layers`, signal toward `epithelium_limbus` (score 7 vs 0): Decellularized porcine cornea-derived hydrogels for the regeneration of epithelium and stroma in focal corneal defects.
- PUBMED_0521 / PMID 35120168 - upstream `multiple_layers`, signal toward `stroma` (score 7 vs 0): Bio-fabrication of stem-cell-incorporated corneal epithelial and stromal equivalents from silk fibroin and gelatin-based biomaterial for canine corneal regeneration.
- PUBMED_0585 / PMID 36063670 - upstream `multiple_layers`, signal toward `epithelium_limbus` (score 8 vs 0): Reconstructing auto tissue engineering lamellar cornea with aspartic acid modified acellular porcine corneal stroma and preconditioned limbal stem cell for corneal regeneration.
- PUBMED_0637 / PMID 36844364 - upstream `multiple_layers`, signal toward `stroma` (score 4 vs 0): A "T.E.S.T." hydrogel bioadhesive assisted by corneal cross-linking for in situ sutureless corneal repair.
- PUBMED_0648 / PMID 37019117 - upstream `multiple_layers`, signal toward `stroma` (score 6 vs 0): Digital light processing-bioprinted poly-NAGA-GelMA-based hydrogel lenticule for precise refractive errors correction.
- PUBMED_0814 / PMID 39197237 - upstream `multiple_layers`, signal toward `stroma` (score 8 vs 0): Corneal stromal structure replicating humanized hydrogel patch for sutureless repair of deep anterior-corneal defect.
- PUBMED_0817 / PMID 39216318 - upstream `multiple_layers`, signal toward `stroma` (score 7 vs 0): Bioprinting of anisotropic functional corneal stroma using mechanically robust multi-material bioink based on decellularized cornea matrix.
- PUBMED_0828 / PMID 39386574 - upstream `multiple_layers`, signal toward `stroma` (score 4 vs 0): In Situ UNIversal Orthogonal Network (UNION) Bioink Deposition for Direct Delivery of Corneal Stromal Stem Cells to Corneal Wounds.
- PUBMED_0844 / PMID 39558795 - upstream `multiple_layers`, signal toward `stroma` (score 6 vs 1): Natural Extracellular Matrix Scaffold-Based Hydrogel Corneal Patch with Temperature and Light-Responsiveness for Penetrating Keratoplasty and Sutureless Stromal Defect Repair.
- PUBMED_0902 / PMID 40061375 - upstream `multiple_layers`, signal toward `epithelium_limbus` (score 4 vs 0): The influence of amniotic membrane proteins on corneal regeneration when delivered directly or using hydrogel platforms.
- PUBMED_0904 / PMID 40083774 - upstream `multiple_layers`, signal toward `stroma` (score 4 vs 0): In situ UNIversal Orthogonal Network (UNION) bioink deposition for direct delivery of corneal stromal stem cells to corneal wounds.
- PUBMED_0949 / PMID 40641839 - upstream `multiple_layers`, signal toward `stroma` (score 7 vs 4): Engineering a functionality-integrated artificial cornea stromal Substitute: Janus bio-adhesive implant with a collagen-based multi-scale biomimetic skeleton.
- PUBMED_0978 / PMID 40945255 - upstream `multiple_layers`, signal toward `stroma` (score 4 vs 0): EMERGE patch, a novel electrogenic engineered material to enhance healing of severe corneal wounds.
- PUBMED_1021 / PMID 41460069 - upstream `multiple_layers`, signal toward `stroma` (score 7 vs 1): 3D-Bioprinted Biomimetic Epithelial-Stromal Hydrogel Construct with In Situ Photocrosslinkable Bioadhesive for Suture-Free Corneal Regeneration.
- PUBMED_1049 / PMID 41678599 - upstream `multiple_layers`, signal toward `stroma` (score 4 vs 0): Composite Decellularized Corneal Hydrogel for Effective Corneal Injury Repair and Regeneration.
- PUBMED_1058 / PMID 41808764 - upstream `multiple_layers`, signal toward `stroma` (score 6 vs 0): Photocrosslinked dual-network hydrogel for sutureless corneal stromal lenticule lmplantation.
- PUBMED_0605 / PMID 36458563 - upstream `stroma`, signal toward `endothelium` (score 5 vs 1): Use of Decellularized SMILE (Small-Incision Lenticule Extraction) Lenticules for Engineering the Corneal Endothelial Layer: A Proof-of-Concept.
- PUBMED_0308 / PMID 32652796 - upstream `multiple_layers`, signal toward `stroma` (score 4 vs 1): Decellularized human corneal stromal cell sheet as a novel matrix for ocular surface reconstruction.
- PUBMED_0408 / PMID 33768381 - upstream `multiple_layers`, signal toward `endothelium` (score 7 vs 0): A novel human donor cornea preservation cocktail incorporating a thermo-reversible gelation polymer (TGP), enhancing the corneal endothelial cell density maintenance and explant culture of corneal limbal cells.
- PUBMED_0499 / PMID 34923312 - upstream `multiple_layers`, signal toward `stroma` (score 7 vs 0): Exosomes-loaded thermosensitive hydrogels for corneal epithelium and stroma regeneration.
- PUBMED_0674 / PMID 37282676 - upstream `multiple_layers`, signal toward `endothelium` (score 5 vs 0): 21 Denuded descemet's membrane as potential tool to support human embryonic stem cell derived retinal pigment epithelial cells culture.
- PUBMED_0700 / PMID 37555081 - upstream `multiple_layers`, signal toward `stroma` (score 4 vs 1): 3D bioprinting of corneal decellularized extracellular matrix: GelMA composite hydrogel for corneal stroma engineering.
- PUBMED_0797 / PMID 39022184 - upstream `multiple_layers`, signal toward `epithelium_limbus` (score 7 vs 0): Photoactivated growth factor release from bio-orthogonally crosslinked hydrogels for the regeneration of corneal defects.
- PUBMED_0938 / PMID 40481091 - upstream `multiple_layers`, signal toward `epithelium_limbus` (score 7 vs 0): Therapeutic efficacy of BSA formulated hydrogels in corneal wound healing and epithelial cell regeneration: an ex vivo study.
- PUBMED_0973 / PMID 40893304 - upstream `multiple_layers`, signal toward `epithelium_limbus` (score 6 vs 0): Hydrogel-Mediated Sustained Delivery of Corneal Epithelial Extracellular Vesicles: A Strategy for Enhanced Corneal Regeneration.
- PUBMED_1031 / PMID 41506503 - upstream `multiple_layers`, signal toward `epithelium_limbus` (score 5 vs 0): Bioactive thermoresponsive fibronectin-Pluronic F127 hydrogel for sustained ocular delivery with corneal regeneration and anti-inflammatory effects.
- PUBMED_0205 / PMID 31574405 - upstream `multiple_layers`, signal toward `epithelium_limbus` (score 9 vs 0): Tissue adhesive hyaluronic acid hydrogels for sutureless stem cell delivery and regeneration of corneal epithelium and stroma.
- PUBMED_0253 / PMID 32097748 - upstream `multiple_layers`, signal toward `stroma` (score 8 vs 3): Multifunctional synthetic Bowman's membrane-stromal biomimetic for corneal reconstruction.
- PUBMED_0540 / PMID 35386466 - upstream `multiple_layers`, signal toward `epithelium_limbus` (score 8 vs 0): 3D printed biomimetic epithelium/stroma bilayer hydrogel implant for corneal regeneration.
- PUBMED_0842 / PMID 39556946 - upstream `multiple_layers`, signal toward `stroma` (score 4 vs 0): Bioprinting a resilient and transparent cornea stroma equivalent: harnessing dual crosslinking strategy with decellularized cornea matrix and silk fibroin hybrid.
- PUBMED_0989 / PMID 41070062 - upstream `multiple_layers`, signal toward `epithelium_limbus` (score 5 vs 0): Comparison of the regenerative potential of different functionalized gelatin-based hydrogels as fillers of rabbit corneal wounds.
- PUBMED_0269 / PMID 32343943 - upstream `stroma`, signal toward `multiple_layers` (score 6 vs 1): A core-skirt designed artificial cornea with orthogonal microfiber grid scaffold.
- PUBMED_0409 / PMID 33782482 - upstream `stroma`, signal toward `endothelium` (score 6 vs 1): Biofabrication of chitosan/chitosan nanoparticles/polycaprolactone transparent membrane for corneal endothelial tissue engineering.
- PUBMED_0484 / PMID 34677503 - upstream `stroma`, signal toward `multiple_layers` (score 4 vs 0): Preliminary Study on Fish Scale Collagen Lamellar Matrix as Artificial Cornea.
- PUBMED_0433 / PMID 34119551 - upstream `multiple_layers`, signal toward `epithelium_limbus` (score 4 vs 0): The effect of biodegradable silk fibroin-based scaffolds containing glial cell line-derived neurotrophic factor (GDNF) on the corneal regeneration process.
- PUBMED_0538 / PMID 35362956 - upstream `multiple_layers`, signal toward `epithelium_limbus` (score 4 vs 0): Scaffold-Free Strategy Using a PEG-Dextran Aqueous Two-Phase-System for Corneal Tissue Repair.
- PUBMED_0548 / PMID 35562005 - upstream `multiple_layers`, signal toward `stroma` (score 5 vs 0): LM22B-10 promotes corneal nerve regeneration through in vitro 3D co-culture model and in vivo corneal injury model.
- PUBMED_1020 / PMID 41427066 - upstream `multiple_layers`, signal toward `endothelium` (score 4 vs 0): Experimental Study of the Effect of Corneal Bio-Coating Based on the Original Hydrogel Biopolymer Scaffold on the Anterior Segment Structures of the Eye.

## Interpretation

37% of Tier 2 records (55/147) showed some keyword-level layer signal conflicting with their upstream label, and it is heavily concentrated in records labeled `multiple_layers` (52 of 55 flags). This is consistent with the original screening pipeline's own documented history (`reports/weekly_logs/pubmed_pipeline_checkpoint.md`, `project_status_after_pubmed_balancing.md`): `multiple_layers` was repeatedly noted as the largest and least tightly defined category, effectively an overflow bucket during initial screening rather than a confirmed judgment that each record genuinely spans multiple corneal layers. This QC pass did not attempt to resolve all 55 - only the 15 high-confidence cases are corrected. The remaining 40 are a known limitation, not a hidden one.

## Recommendation

Use `confirmed_layer_correction` (high-confidence only) for any layer-grouped citation list built from Tier 2. For the 40 lower-confidence flags, either do a quick manual read before using them in a layer-specific context, or cite them only in cross-cutting/general sections where exact layer attribution matters less.
