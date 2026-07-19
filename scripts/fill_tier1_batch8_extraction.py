"""
Tier 1 extraction batch 8 (2026-07-20, scheduled run continuation).

Retrieval route note: the Europe PMC REST API JSON endpoint
(https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:<pmid>&format=json&resultType=core)
was tested first this run and again returned "URL not in provenance set"
from the sandboxed web_fetch tool (it only allows fetching URLs that already
appeared in a user message, a prior web_fetch result, or a WebSearch result;
this unattended scheduled run has no user available to authorize a new URL).
Same structural restriction hit in batches 3-7.

Consistent with the workaround established in batches 3-7, extraction for
this batch was built from the complete, untruncated abstract text already
stored locally in screening/full_text/pubmed_tier1_tier2_extraction_plan.csv
(verified PubMed/journal abstracts captured during the original screening
pass), with open-access status assessed from known journal policy (Scientific
Reports and PLoS ONE are fully open access; Translational Vision Science &
Technology (ARVO) is fully open access; Materials Science & Engineering C and
The Ocular Surface are Elsevier subscription titles; Journal of Biomedical
Materials Research Part B is a Wiley subscription title). No new WebSearch
lookups were performed this run (not required given the abstracts already
contain rich quantitative detail); this is noted per-record in extraction_notes.

This batch (8 records):
- PUBMED_0344 (PMID 33028837) - in situ-forming PEG-crosslinked collagen hydrogel, in vitro + in vivo rabbit stromal keratectomy (suture-free).
- PUBMED_0346 (PMID 33037282) - porous collagen hydrogel + LASIK-inspired implantation technique, in vivo human corneal surgery model, 6-month follow-up, drug delivery proof-of-concept.
- PUBMED_0387 (PMID 33542377) - decellularized human corneal scaffold, in vitro recellularization + ex vivo lamellar transplantation.
- PUBMED_0388 (PMID 33545838) - allogeneic cornea-derived matrix (ACM) from discarded donor tissue, in vitro recellularization + in vivo rabbit stromal pocket implantation.
- PUBMED_0430 (PMID 34061862) - decellularized porcine corneal scaffold +/- keratocyte recellularization, in vivo rabbit anterior lamellar keratoplasty, 3-month follow-up.
- PUBMED_0468 (PMID 34537415) - supramolecular host-guest hyaluronic acid hydrogel, ex vivo + in vivo corneal wound healing model.
- PUBMED_0596 (PMID 36239965) - in situ-forming collagen-hyaluronate semi-IPN hydrogel, in vitro + in vivo rabbit lamellar keratectomy, 7-day follow-up.
- PUBMED_0602 (PMID 36370413) - comparative in vitro study of three commercial amniotic membrane products + one clinical case study.
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
    "run could not authorize the new URL). "
)

EXTRACTIONS = {
    "PUBMED_0344": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / in situ-forming hydrogel study with in vivo evaluation (rabbit stromal keratectomy, suture-free)",
        target_layer_final="stroma (with epithelialization outcome assessed)",
        biomaterial_category="chemically crosslinked natural-polymer in situ-forming hydrogel",
        specific_materials="collagen type I hydrogel crosslinked in situ via multi-functional polyethylene glycol (PEG)-N-hydroxysuccinimide (NHS) chemistry",
        fabrication_method="collagen type I mixed with multi-arm PEG-NHS crosslinker; hydrogel forms under ambient conditions within minutes upon mixing, without external catalyst, light, or heat trigger; transparency, degradability, and stiffness tuned by varying number of PEG arms and PEG concentration; applied directly in situ over stromal keratectomy wounds in vivo without sutures",
        scaffold_architecture="amorphous in situ-gelling hydrogel matrix (not a pre-formed solid scaffold), conforms to the wound bed geometry upon application",
        cell_type_used="corneal epithelial cells and corneal stromal cells (in vitro migration/proliferation assays); host-derived cells only in vivo (no exogenous cell seeding for in vivo arm)",
        cell_source="not fully specified in abstract (species of in vitro epithelial/stromal cells not given); in vivo arm uses host rabbit-derived repopulation, no exogenous cells implanted",
        growth_factors_or_bioactive_agents="none reported; PEG-NHS used purely as a chemical crosslinker, not a bioactive agent",
        optical_transparency_reported="yes",
        optical_metric_details="Transparency was modulated as a function of PEG arm number and PEG concentration (qualitative/tunability finding); no single numeric transmittance percentage given in the retrieved abstract.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Stiffness (along with degradability and transparency) was shown to be tunable as a function of number of PEG arms and PEG concentration; no specific numeric modulus or degradation-rate values given in the retrieved abstract text.",
        biological_testing_reported="yes",
        biological_metric_details="In vitro: hydrogel supported migration and proliferation of corneal epithelial and stromal cells on its surface (qualitative finding, no numeric viability/migration-rate values given). In vivo: hydrogels formed in situ over rabbit stromal keratectomy wounds without sutures supported multi-layered surface epithelialization.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract (in vivo rabbit stromal keratectomy follow-up duration not given)",
        main_outcomes="A suture-free, in situ-forming PEG-NHS-crosslinked collagen hydrogel formed rapidly (minutes) under ambient conditions without external trigger, with tunable transparency, stiffness, and degradability via PEG arm number/concentration; it supported corneal epithelial and stromal cell migration/proliferation in vitro, and when applied without sutures over rabbit stromal keratectomy wounds in vivo, supported multi-layered surface epithelialization -- positioning it as a sutureless, trigger-free corneal stromal defect repair matrix.",
        main_limitations="No quantitative transmittance, modulus, or degradation-rate values given in the retrieved abstract despite qualitative tunability claims; in vivo follow-up duration and sample size not specified; no assessment of long-term integration, scarring/haze, or biomechanical suture-retention strength; species/source of in vitro epithelial and stromal cells not specified.",
        translational_readiness_level="preclinical (animal model, rabbit)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Scientific Reports (Nature), DOI 10.1038/s41598-020-72978-5, 2020 -- Scientific Reports is a fully open-access journal; full-text fetch not attempted this run, abstract-level extraction used. Directly comparable to PUBMED_0596 (this batch), a closely related follow-on collagen-hyaluronate SIPN hydrogel study from what appears to be the same in situ-forming PEG-crosslinked collagen platform; useful paired entries for the review's in-situ-hydrogel benchmarking narrative.",
    ),
    "PUBMED_0346": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / porous hydrogel implant study with in vivo evaluation (human corneal surgery model, 6-month follow-up) and in vitro drug-delivery proof-of-concept",
        target_layer_final="stroma",
        biomaterial_category="porous natural-polymer (collagen-based) hydrogel implant",
        specific_materials="porous collagen-based hydrogel designed to replace a substantial portion of damaged/diseased corneal stroma; drug-loaded variant incorporating a neuroregenerative drug for sustained local release",
        fabrication_method="collagen-based hydrogel engineered for porosity to permit host cell migration/population while maintaining transparency and thickness; implanted using a novel hybrid surgical technique inspired by LASIK refractive surgery (flap-based implantation) rather than conventional lamellar keratoplasty; drug-loaded variant prepared and tested for in vitro sustained-release kinetics as proof-of-concept",
        scaffold_architecture="porous hydrogel implant sized to replace a substantial portion of corneal stromal thickness, engineered for permeability to host cell infiltration",
        cell_type_used="not applicable / acellular implant (repopulation relies on host-derived stromal cells migrating into the porous matrix in vivo); no exogenous cells seeded prior to implantation",
        cell_source="not applicable / host-derived (in vivo repopulation by host stromal cells, nerves, and epithelium)",
        growth_factors_or_bioactive_agents="a neuroregenerative drug (specific agent not named in retrieved abstract) loaded into the hydrogel for sustained slow-release delivery, demonstrated in vitro as proof-of-principle",
        optical_transparency_reported="yes",
        optical_metric_details="Hydrogel maintained transparency and thickness six months after surgical implantation in the in vivo human corneal surgery model (qualitative long-term maintenance finding; no numeric transmittance percentage given in the retrieved abstract).",
        mechanical_testing_reported="partial",
        mechanical_metric_details="Hydrogel was engineered with 'mechanical properties suitable for replacing a substantial portion of a damaged or diseased corneal stroma' and maintained structural/biomaterial integrity through rapid host wound healing around the implant; no specific numeric modulus or tensile-strength values given in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="Porous hydrogel permitted migration and population by host cells while maintaining transparency; the novel LASIK-inspired hybrid implantation technique promoted rapid wound healing around implants, preserving biomaterial integrity/function; host stromal cell repopulation and regeneration of host epithelium and corneal nerves were observed. In vitro: drug-loaded hydrogel achieved sustained slow-release delivery of a neuroregenerative drug.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="6 months (in vivo human corneal surgery model, post-implantation transparency/thickness maintenance)",
        main_outcomes="A porous collagen-based hydrogel, combined with a novel LASIK-inspired hybrid surgical implantation technique, maintained transparency and thickness six months after implantation in an in vivo model of human corneal surgery, supported host stromal cell repopulation and regeneration of host epithelium and corneal nerves, and as a drug-loaded variant achieved sustained slow-release delivery of a neuroregenerative agent in vitro -- together demonstrating translational potential for stromal tissue replacement and regeneration with an integrated local drug-delivery function.",
        main_limitations="No quantitative transmittance, modulus, or drug-release-kinetics values given in the retrieved abstract despite qualitative maintenance/sustained-release claims; specific in vivo model species/system for the '6-month' human corneal surgery model not fully detailed in the abstract (described as 'an in vivo model of human corneal surgery'); the neuroregenerative drug is not named; drug-loaded hydrogel tested only in vitro as proof-of-principle, not yet validated in vivo.",
        translational_readiness_level="preclinical (in vivo model with 6-month follow-up) with an in vitro drug-delivery proof-of-concept",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Scientific Reports (Nature), DOI 10.1038/s41598-020-73730-9, 2020 -- Scientific Reports is a fully open-access journal; full-text fetch not attempted this run, abstract-level extraction used. One of the longest in vivo follow-up durations (6 months) among Tier 1 stroma-replacement hydrogel records processed so far, and notable for the LASIK-inspired hybrid implantation technique and drug-delivery angle -- high value for both the mechanical/optical durability and translational-technique sections of the benchmarking table.",
    ),
    "PUBMED_0387": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / decellularized tissue scaffold study with in vitro recellularization and ex vivo lamellar transplantation",
        target_layer_final="multiple_layers (anterior corneal surface: epithelium/limbus + stroma)",
        biomaterial_category="decellularized allogeneic (human donor) corneal scaffold",
        specific_materials="human donor corneal extracellular matrix (ECM) scaffold, decellularized using sodium deoxycholate and deoxyribonuclease I (DNase I), with dextran used to control tissue swelling",
        fabrication_method="human donor corneas treated with sodium deoxycholate (detergent) and DNase I to remove cells and nuclei, with dextran included to control osmotic tissue swelling during processing; decellularization effects evaluated on ultrastructure, optical, mechanical, and biological properties; recellularization studied using primary human limbal epithelial cells, stromal cells, and melanocytes in vitro, and via a lamellar transplantation approach ex vivo",
        scaffold_architecture="whole decellularized human corneal ECM scaffold retaining native tissue structure, extracellular matrix proteins, and glycosaminoglycans",
        cell_type_used="primary human limbal epithelial cells, corneal stromal cells, and melanocytes",
        cell_source="human (primary limbal epithelial cells, stromal cells, and melanocytes)",
        growth_factors_or_bioactive_agents="none reported; sodium deoxycholate, DNase I, and dextran used only as decellularization/processing reagents, not as bioactive/therapeutic agents",
        optical_transparency_reported="yes",
        optical_metric_details="Decellularization preserved optical transmission properties of the human cornea (qualitative preservation finding; no single numeric transmittance percentage given in the retrieved abstract).",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Decellularization effects were evaluated on the mechanical properties of the human cornea alongside ultrastructure and optical/biological properties; tissue structure, ECM proteins, and glycosaminoglycans were preserved (qualitative preservation finding); no specific numeric tensile strength or modulus values given in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="Cellular and nuclear material effectively removed in a very short decellularization period while preserving ECM proteins, GAGs, and tissue structure. In vitro recellularization with primary human limbal epithelial cells, stromal cells, and melanocytes demonstrated good biocompatibility. Ex vivo lamellar transplantation revealed complete epithelialization and stromal repopulation from host tissue.",
        in_vitro_model="yes",
        ex_vivo_model="yes",
        animal_model="no",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract (ex vivo lamellar transplantation follow-up duration not given)",
        main_outcomes="A fast, efficient decellularization protocol (sodium deoxycholate + DNase I, with dextran-controlled swelling) produced a human corneal ECM scaffold with effective removal of cellular/nuclear material while preserving ECM proteins, GAGs, tissue structure, and optical transmission properties; the scaffold showed good biocompatibility upon in vitro recellularization with primary human limbal epithelial cells, stromal cells, and melanocytes, and achieved complete epithelialization and stromal repopulation from host tissue in an ex vivo lamellar transplantation model -- supporting its promise as a non-immunogenic biological material for anterior corneal surface reconstruction.",
        main_limitations="Ex vivo transplantation evaluation only, no live animal implantation or human clinical transplantation; no quantitative transmittance, tensile, or GAG/dsDNA content values given in the retrieved abstract despite qualitative preservation claims; relies on allogeneic human donor tissue supply (same scarcity problem the scaffold aims to mitigate, though decellularization may improve immunogenicity/compatibility versus fresh allografts); follow-up duration for ex vivo repopulation not specified.",
        translational_readiness_level="early preclinical (in vitro / ex vivo)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Scientific Reports (Nature), DOI 10.1038/s41598-021-82678-3, 2021 -- Scientific Reports is a fully open-access journal; full-text fetch not attempted this run, abstract-level extraction used. Notable as an allogeneic (human, not xenogeneic porcine) decellularized scaffold with a fast decellularization protocol and full anterior-surface (epithelium + stroma) recellularization confirmed both in vitro and ex vivo -- directly comparable to PUBMED_0388 (this batch, also allogeneic human-derived) for a human-tissue-source decellularized-scaffold benchmarking narrative.",
    ),
    "PUBMED_0388": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / decellularized allogeneic matrix scaffold study with in vitro recellularization and in vivo evaluation (rabbit corneal stromal pocket implantation)",
        target_layer_final="stroma (with epithelialization outcome also assessed)",
        biomaterial_category="decellularized allogeneic (human donor, surgical-waste-derived) corneal matrix scaffold",
        specific_materials="allogeneic cornea-derived matrix (ACM) fabricated from human corneal tissue discarded during allogeneic corneal transplantation surgery (donor-tissue surgical waste reuse)",
        fabrication_method="discarded human corneal tissue from allogeneic transplantation surgery processed into ACM scaffolds; collagen and glycosaminoglycan (GAG) levels preserved during fabrication while DNA content significantly decreased; scanning electron microscopy used to characterize fiber-like surface structures and multiple interlaced lamellae in cross-section; recellularized in vitro with corneal epithelial cells and corneal stromal cells; ACM then implanted into rabbit corneal stromal pockets in vivo",
        scaffold_architecture="decellularized human corneal matrix retaining fiber-like surface structures and multiple interlaced lamellae in cross-section (SEM-confirmed), used as a stromal pocket implant",
        cell_type_used="corneal epithelial cells (for surface stratification) and corneal stromal cells (keratocyte-lineage) seeded on the ACM in vitro",
        cell_source="human (donor-tissue-derived ACM scaffold; corneal epithelial and stromal cells seeded, species/origin of the seeded cells not further specified beyond 'corneal' in the retrieved abstract)",
        growth_factors_or_bioactive_agents="none reported",
        optical_transparency_reported="yes",
        optical_metric_details="ACM scaffolds were fabricated with 'favorable optical properties' (qualitative characterization goal); in vivo, the rabbit cornea remained transparent throughout the follow-up period after ACM implantation into stromal pockets (qualitative in vivo transparency maintenance finding); no numeric transmittance value given in the retrieved abstract.",
        mechanical_testing_reported="partial",
        mechanical_metric_details="ACM scaffolds were fabricated with 'structural strength' as a design goal, with collagen and GAG levels well preserved during fabrication (supporting structural integrity) while DNA decreased significantly (decellularization efficacy); no specific numeric tensile strength or modulus values given in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="SEM showed fiber-like surface structures and interlaced lamellae in cross-section. Corneal epithelial cells grown on the ACM formed a continuous multi-stratified epithelium with strong expression of differentiation marker CK3/12, gap-junction marker Connexin43, and stem-cell marker p63alpha; corneal stromal cells expressed keratocyte-specific marker KERA and adhesion marker integrin beta1. In vivo, rabbit corneas implanted with ACM in stromal pockets remained transparent throughout follow-up.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract (in vivo rabbit stromal-pocket implantation 'follow-up period' duration not given)",
        main_outcomes="An allogeneic cornea-derived matrix (ACM) fabricated from human corneal tissue discarded during transplantation surgery preserved collagen/GAG content and favorable optical/structural properties while significantly reducing DNA; in vitro, it supported formation of a continuous multi-stratified corneal epithelium (CK3/12+, Connexin43+, p63alpha+) and keratocyte marker expression (KERA+, integrin beta1+) in seeded stromal cells; implanted into rabbit corneal stromal pockets in vivo, the ACM-bearing corneas remained transparent throughout follow-up -- demonstrating feasibility of reusing surgical-waste donor corneal tissue as a bioengineered stromal implant material.",
        main_limitations="No quantitative optical transmittance or tensile mechanical values given in the retrieved abstract despite favorable-property claims; in vivo follow-up duration not specified numerically; relies on availability of discarded donor corneal tissue from allogeneic transplant surgeries (a supply-limited byproduct source); rabbit (not primate/human) in vivo model; no functional/visual-acuity outcome measures reported.",
        translational_readiness_level="preclinical (animal model, rabbit)",
        benchmarking_relevance="medium",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Materials Science & Engineering C (Elsevier), DOI 10.1016/j.msec.2020.111673, 2021 -- Elsevier subscription journal (Materials Science & Engineering C was discontinued/merged into Biomaterials Advances circa 2021-2022), no open-access indication found for this specific article; abstract-level extraction only. Notable as a surgical-waste-reuse allogeneic scaffold strategy directly comparable to PUBMED_0387 (this batch, also human allogeneic decellularized scaffold) for the review's human-tissue-source benchmarking narrative.",
    ),
    "PUBMED_0430": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / decellularized xenogeneic scaffold recellularization comparison study with in vivo evaluation (rabbit anterior lamellar keratoplasty, 3-month follow-up)",
        target_layer_final="stroma",
        biomaterial_category="decellularized xenogeneic (porcine) corneal scaffold, acellular vs. keratocyte-recellularized comparison",
        specific_materials="decellularized porcine corneal lenticules (250 micron thick), tested as acellular scaffolds versus scaffolds recellularized with human corneal stromal cells (keratocytes)",
        fabrication_method="porcine corneal scaffolds decellularized to retain low residual DNA (14.89 +/- 5.56 ng/mg); in vitro cytotoxicity confirmed absent; scaffolds recellularized with human corneal stromal cells and cultured 14 days in serum-supplemented media, followed by a further 14 days in either serum-free or serum-supplemented media, to compare keratocyte phenotype induction; 250 micron thick decellularized lenticules (acellular vs. serum-free-cultured recellularized) implanted via rabbit anterior lamellar keratoplasty and followed for 3 months; post-mortem histology performed",
        scaffold_architecture="decellularized porcine corneal lenticule, 250 micron thickness, either left acellular or recellularized throughout depth with human keratocytes",
        cell_type_used="human corneal stromal cells (keratocytes)",
        cell_source="human (corneal stromal cells/keratocytes), seeded onto porcine decellularized scaffold (xenogeneic scaffold + human cell recellularization combination)",
        growth_factors_or_bioactive_agents="none reported; serum-free vs. serum-supplemented culture media compared as a culture-condition variable, not as an added bioactive agent",
        optical_transparency_reported="yes",
        optical_metric_details="In vivo: transparency was NOT restored after 3 months for either acellular or recellularized implant groups (explicit negative finding); host rabbit epithelium did cover the implants in both groups. No numeric transmittance value given in the retrieved abstract, but the qualitative outcome (persistent lack of transparency) is a key negative result.",
        mechanical_testing_reported="partial",
        mechanical_metric_details="Residual DNA content after decellularization was 14.89 +/- 5.56 ng/mg (a decellularization-efficacy metric); no numeric tensile strength or modulus values given in the retrieved abstract; scaffolds demonstrated full-depth cell penetration after 14 days of recellularization culture, an indirect structural/porosity metric.",
        biological_testing_reported="yes",
        biological_metric_details="No in vitro cytotoxicity detected. All recellularization groups showed full-depth cell penetration after 14 days. With serum present, ALDH3A1 staining remained weak; after serum-free culture, ALDH3A1 staining was brighter and keratocytes adopted native dendritic morphology with significantly increased (p<0.05) keratocan, decorin, lumican, and CD34 gene expression. In vivo (3-month rabbit anterior lamellar keratoplasty): host epithelium covered implants in both acellular and recellularized groups; post-mortem histology showed a less-compact collagen 'regenerating zone' under the epithelium with some alpha-SMA staining (fibrotic cells) in both groups; ALDH1A1 staining was present throughout the acellular scaffold but in only one of the recellularized lenticules; little difference was observed between acellular and cell-seeded scaffolds in vivo.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="14 days + 14 days (in vitro recellularization culture phases, serum-supplemented then serum-free or serum-supplemented); 3 months (rabbit anterior lamellar keratoplasty in vivo follow-up)",
        main_outcomes="Decellularized porcine corneal scaffolds (14.89 ng/mg residual DNA, non-cytotoxic) recellularized with human keratocytes under serum-free culture conditions achieved a native dendritic keratocyte phenotype with significantly upregulated keratocan, decorin, lumican, and CD34 expression versus serum-supplemented culture; however, in a 3-month rabbit anterior lamellar keratoplasty model, transparency was NOT restored in either acellular or keratocyte-recellularized implant groups, with both showing similar fibrotic 'regenerating zone' histology under the epithelium -- indicating that prior long-term keratocyte recellularization provided little in vivo benefit over acellular scaffolds alone, and that acellular controls should be used in future scaffold development to isolate whether cellularization is actually necessary.",
        main_limitations="Explicitly negative/null in vivo result: transparency not restored by 3 months in either group, limiting immediate clinical relevance of this particular implantation approach; xenogeneic (porcine) scaffold material carries immunogenicity considerations; rabbit (not primate/human) in vivo model; no numeric tensile/mechanical values given in the retrieved abstract; only a single recellularized lenticule showed reduced ALDH1A1 signal (small in vivo sample size implied); authors themselves note the study argues for including acellular controls going forward, indicating some uncertainty in interpreting cellularization's true effect.",
        translational_readiness_level="preclinical (animal model, rabbit) -- with a negative/cautionary translational finding regarding recellularization benefit",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "PLoS ONE, DOI 10.1371/journal.pone.0245406, 2021 -- PLoS ONE is a fully open-access journal; full-text fetch not attempted this run, abstract-level extraction used. Valuable as a rare explicitly negative/null in vivo finding (transparency not restored, minimal acellular-vs-recellularized difference) among the mostly positive-outcome Tier 1 decellularized-porcine-scaffold records -- important for balanced benchmarking and for flagging that in vitro keratocyte-phenotype improvements did not translate to better in vivo transparency outcomes in this model.",
    ),
    "PUBMED_0468": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / supramolecular hydrogel study with ex vivo and in vivo evaluation (corneal wound healing model)",
        target_layer_final="multiple_layers (epithelium + anterior stroma wound-healing effects)",
        biomaterial_category="supramolecular (non-covalent host-guest) natural-polymer hydrogel",
        specific_materials="hyaluronic acid (HA)-based supramolecular hydrogel formed via non-covalent host-guest interactions between HA-cyclodextrin (host) and HA-adamantane (guest) conjugates",
        fabrication_method="HA independently conjugated with cyclodextrin (host) and adamantane (guest) moieties; the two HA derivatives combined to self-assemble into a shear-thinning hydrogel via supramolecular host-guest (non-covalent) interactions, avoiding chemical crosslinkers associated with toxicity; hydrogel evaluated ex vivo for encapsulated human corneal epithelial cell adhesion/spreading and in vivo as an in situ-formed, acellular therapeutic membrane for corneal wound healing",
        scaffold_architecture="shear-thinning, injectable/applicable supramolecular hydrogel network (non-covalently crosslinked, self-healing gel), forms an acellular therapeutic membrane in situ over the wound",
        cell_type_used="human corneal epithelial cells (encapsulated, ex vivo adhesion/spreading assay); no exogenous cells in the in vivo acellular membrane arm",
        cell_source="human (corneal epithelial cells, ex vivo assay only)",
        growth_factors_or_bioactive_agents="none reported; therapeutic effect attributed to the HA hydrogel's intrinsic biological/mucoadhesive properties and its modulation of the host mesenchymal corneal stromal cell secretome, not an exogenously added growth factor",
        optical_transparency_reported="unclear / not reported in abstract",
        optical_metric_details="Not directly quantified; abstract cites HA's known 'remarkable biocompatibility, transparency and mucoadhesive properties' as background rationale but does not report a specific transmittance measurement for this hydrogel formulation.",
        mechanical_testing_reported="partial",
        mechanical_metric_details="Hydrogel was characterized as shear-thinning (a rheological property enabling ease of application/injection); no specific numeric viscosity, modulus, or shear-rate values given in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="Ex vivo: supramolecular HA hydrogels facilitated adhesion and spreading of encapsulated human corneal epithelial cells. In vivo: improved corneal wound healing as an in situ-formed, acellular therapeutic membrane; HA hydrogel absorbed within the corneal stroma over time; modulated mesenchymal corneal stromal cell secretome production; reduced cellularity and inflammation of the anterior stroma; significantly mitigated corneal edema compared to linear HA treatment and untreated controls.",
        in_vitro_model="no",
        ex_vivo_model="yes",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="not specified numerically in abstract (in vivo corneal wound healing follow-up duration not given)",
        main_outcomes="A supramolecular (non-covalent host-guest) hyaluronic acid hydrogel, formed without chemical crosslinkers, facilitated corneal epithelial cell adhesion/spreading ex vivo and, applied in vivo as an acellular, in situ-formed therapeutic membrane, improved corneal wound healing by being gradually absorbed into the stroma, modulating the stromal cell secretome, reducing anterior stromal cellularity/inflammation, and significantly mitigating corneal edema compared to linear HA and untreated controls -- supporting the platform's promise as a crosslinker-toxicity-free, versatile biomaterial for corneal wound healing.",
        main_limitations="No quantitative transmittance, mechanical modulus, or numeric edema/inflammation reduction values given in the retrieved abstract despite significant-effect claims; in vivo follow-up duration and animal model species not specified in the retrieved abstract; acellular/therapeutic-membrane approach rather than a structural tissue-replacement scaffold, so relevance is to wound-healing modulation rather than stromal volume replacement.",
        translational_readiness_level="preclinical (ex vivo + animal model)",
        benchmarking_relevance="medium",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "The Ocular Surface (Elsevier), DOI 10.1016/j.jtos.2021.09.002, 2022 -- Elsevier subscription journal, no open-access indication found for this specific article; abstract-level extraction only. Notable as a crosslinker-free supramolecular hydrogel wound-healing-modulation approach (rather than a structural replacement scaffold), complementing the more structural stromal-replacement hydrogels in this batch (PUBMED_0344, PUBMED_0346, PUBMED_0596) with a distinct anti-inflammatory/anti-edema mechanism for the review's biomaterial-mechanism-of-action discussion.",
    ),
    "PUBMED_0596": dict(
        extraction_status="completed",
        study_type="experimental biomaterial / in situ-forming hydrogel study with in vitro characterization and in vivo evaluation (rabbit anterior lamellar keratectomy, 7-day follow-up)",
        target_layer_final="stroma (with epithelial regeneration outcome also assessed)",
        biomaterial_category="chemically crosslinked natural-polymer semi-interpenetrating network (semi-IPN) in situ-forming hydrogel",
        specific_materials="collagen type I crosslinked with bifunctional polyethylene glycol (PEG) via N-hydroxysuccinimide (NHS) ester chemistry, formed in the presence of linear (non-crosslinked) hyaluronic acid (HA) to create a semi-interpenetrating polymer network (SIPN)",
        fabrication_method="collagen type I crosslinked with bifunctional PEG-NHS in the presence of linear HA to form an in situ-gelling SIPN without external energy source (no light/heat trigger); gelation time and mechanical, optical, swelling, and degradation properties characterized; cytocompatibility with human corneal epithelial cells and corneal stromal stem cells (CSSCs) assessed in vitro, including spatial distribution of encapsulated CSSCs within the SIPN; in vivo wound healing evaluated by multimodal imaging in a rabbit anterior lamellar keratectomy injury model, followed by immunohistochemistry",
        scaffold_architecture="in situ-gelling semi-interpenetrating polymer network (crosslinked collagen-PEG network with entangled, non-crosslinked linear HA), can encapsulate cells with reduced sedimentation compared to plain collagen gel",
        cell_type_used="human corneal epithelial cells and corneal stromal stem cells (CSSCs)",
        cell_source="human (corneal epithelial cells and corneal stromal stem cells)",
        growth_factors_or_bioactive_agents="none reported as an added exogenous factor; linear hyaluronic acid incorporated as a structural/biofunctional SIPN component (mucoadhesive, cell-supportive), not as a growth factor",
        optical_transparency_reported="yes",
        optical_metric_details="The collagen-hyaluronate SIPN demonstrated optical properties 'similar to the cornea' (qualitative comparative finding); no single numeric transmittance percentage given in the retrieved abstract; optical properties were assessed alongside gelation time, mechanical, swelling, and degradation properties.",
        mechanical_testing_reported="yes",
        mechanical_metric_details="Mechanical properties of the SIPN were assessed and found 'similar to the cornea' (qualitative comparative finding); gelation time, swelling, and degradation properties were also characterized; no specific numeric modulus, gelation-time, or degradation-rate values given in the retrieved abstract text.",
        biological_testing_reported="yes",
        biological_metric_details="In vitro: SIPN was biocompatible with human corneal epithelial cells and CSSCs, enhancing CSSC viability compared with plain collagen gel controls and preventing encapsulated CSSC sedimentation (improved spatial distribution). In vivo (rabbit anterior lamellar keratectomy, multimodal imaging + immunohistochemistry): SIPN application significantly reduced stromal defect size compared with controls after 7 days and promoted multilayered epithelial regeneration.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="yes",
        clinical_evidence="no",
        follow_up_duration="7 days (rabbit anterior lamellar keratectomy in vivo follow-up)",
        main_outcomes="A collagen-hyaluronate semi-interpenetrating network (SIPN) hydrogel, formed in situ without an external energy source via PEG-NHS crosslinking of collagen in the presence of linear HA, achieved mechanical and optical properties similar to native cornea, was biocompatible with human corneal epithelial cells and enhanced corneal stromal stem cell (CSSC) viability/spatial distribution versus plain collagen gel, and in a 7-day rabbit anterior lamellar keratectomy model significantly reduced stromal defect size and promoted multilayered epithelial regeneration compared with controls -- positioning the SIPN as a promising alternative to keratoplasty and a tunable platform for corneal tissue engineering and cell delivery.",
        main_limitations="Short (7-day) in vivo follow-up, insufficient to establish long-term transparency, integration, or scarring outcomes; no quantitative transmittance, modulus, gelation-time, or defect-size-reduction numeric values given in the retrieved abstract despite significant-effect claims; rabbit (not primate/human) in vivo model; CSSC source/isolation details not specified in the retrieved abstract.",
        translational_readiness_level="preclinical (animal model, rabbit)",
        benchmarking_relevance="high",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Translational Vision Science & Technology (ARVO), DOI 10.1167/tvst.11.10.22, 2022 -- TVST is a fully open-access ARVO journal; full-text fetch not attempted this run, abstract-level extraction used. Appears to be a direct follow-on/companion study to PUBMED_0344 (this batch, same PEG-NHS-crosslinked collagen platform, same research approach), now adding linear HA to form a SIPN -- these two records pair well in the review's in-situ-forming-hydrogel benchmarking narrative, showing platform iteration and progression from acellular-only wound coverage (PUBMED_0344) toward CSSC-cell-delivery capability (this record).",
    ),
    "PUBMED_0602": dict(
        extraction_status="completed",
        study_type="in vitro comparative biomaterial study (three commercial amniotic membrane products) with an accompanying clinical case study",
        target_layer_final="epithelium (ocular surface / limbus-adjacent application)",
        biomaterial_category="naturally derived biological membrane (human amniotic membrane), commercially processed variants",
        specific_materials="three differently processed, commercially available human amniotic membrane (AM) products: (1) Biovance(R) 3L Ocular, a decellularized, dehydrated human AM (DDHAM); (2) AMBIO2(R), a dehydrated human AM (DHAM, not decellularized); (3) AmnioGraft(R), a cryopreserved human AM (CHAM)",
        fabrication_method="three commercial AM products compared as manufactured (decellularized-dehydrated vs. non-decellularized-dehydrated vs. cryopreserved processing routes); human corneal epithelial cells (HCECs) seeded onto both the epithelial and stromal sides of each AM and incubated for 1, 4, and 7 days; cell adhesion/viability assessed by alamarBlue assay; HCEC migration assessed by scratch wound assay; inflammatory response induced by TNF-alpha treatment and pro-inflammatory gene expression compared by qPCR; staining used to confirm decellularization completeness (absence of nuclei) in DDHAM; a clinical case study using DDHAM for anterior basement membrane dystrophy was also presented",
        scaffold_architecture="naturally derived acellular/decellularized (or minimally processed) basement-membrane biological sheet, distinct epithelial and stromal sides, used as a substrate/dressing rather than a synthetic scaffold",
        cell_type_used="human corneal epithelial cells (HCECs)",
        cell_source="human (corneal epithelial cell line/primary cells, seeded onto donor amniotic membrane tissue)",
        growth_factors_or_bioactive_agents="none exogenously added; comparison is of the AM's own intrinsic (processing-dependent) biological content and TNF-alpha used experimentally to induce an inflammatory challenge, not as a therapeutic agent",
        optical_transparency_reported="unclear / not reported in abstract",
        optical_metric_details="Not reported; study focus is HCEC adhesion/viability/migration and inflammatory gene expression rather than optical transparency of the AM substrate itself.",
        mechanical_testing_reported="unclear / not reported in abstract",
        mechanical_metric_details="Abstract states AM has 'biological and mechanical properties important to Ophthalmology' generally, but no specific mechanical testing methodology or numeric values for the three compared products are given in the retrieved abstract.",
        biological_testing_reported="yes",
        biological_metric_details="Staining confirmed complete decellularization and absence of nuclei in DDHAM (vs. DHAM and CHAM). HCEC activity (adhesion/viability via alamarBlue, days 1/4/7) was best supported on the stromal side of DDHAM. Under TNF-alpha-induced inflammatory stimulation, DDHAM promoted a higher initial inflammatory response (pro-inflammatory gene expression by qPCR) with a declining trend across time compared to DHAM and CHAM. Clinically, DDHAM was used to successfully treat a case of anterior basement membrane dystrophy.",
        in_vitro_model="yes",
        ex_vivo_model="no",
        animal_model="no",
        clinical_evidence="yes",
        follow_up_duration="1, 4, and 7 days (in vitro HCEC adhesion/viability/migration assays); single clinical case study, follow-up duration not specified numerically in the retrieved abstract",
        main_outcomes="Comparing three commercially available, differently processed human amniotic membrane products, decellularized dehydrated AM (DDHAM, Biovance 3L Ocular) best supported human corneal epithelial cell activity (adhesion/viability on the stromal side) among the three, while also producing a higher initial but declining TNF-alpha-induced inflammatory gene-expression response compared to non-decellularized dehydrated (DHAM) and cryopreserved (CHAM) AM; a clinical case study demonstrated DDHAM was used successfully to treat anterior basement membrane dystrophy, suggesting that AM processing method (decellularization, dehydration vs. cryopreservation) meaningfully affects both cellular compatibility and inflammatory profile relevant to clinical ocular surface applications.",
        main_limitations="Only a single clinical case reported (not a controlled clinical trial), limiting generalizability of the clinical claim; no optical transparency or detailed numeric mechanical data given in the retrieved abstract; in vitro comparison limited to HCECs and a fixed TNF-alpha inflammatory challenge, may not capture full in vivo immune/wound-healing complexity; specific quantitative alamarBlue/qPCR fold-change values not given in the retrieved abstract text.",
        translational_readiness_level="early clinical (single case study) with supporting in vitro comparative data",
        benchmarking_relevance="medium",
        include_in_final_review="yes",
        extraction_notes=NOTE_PREFIX_LOCAL
        + "Journal of Biomedical Materials Research Part B: Applied Biomaterials (Wiley), DOI 10.1002/jbm.b.35186, 2023 -- Wiley subscription journal, no open-access indication found for this specific article; abstract-level extraction only. Distinct from the synthetic/semi-synthetic and decellularized-corneal-tissue records in this batch: amniotic membrane is a well-established clinical adjunct rather than a structural corneal replacement, and this is one of the few Tier 1 records with an actual (even if single-case) clinical evidence component -- valuable for the review's translational-readiness spectrum and epithelium/limbus benchmarking table.",
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
    pdf_available="unknown / not verified this run (subscription journal, open-access status of this specific article not confirmed)",
    source_checked="local screening corpus abstract (screening/full_text/pubmed_tier1_tier2_extraction_plan.csv)",
    retrieval_date="2026-07-20",
    retrieval_notes="Europe PMC REST API fetch blocked by web_fetch provenance restriction in this unattended run; abstract taken from already-verified local screening corpus text. Journal is a subscription title; full-text access not confirmed.",
    extraction_ready="yes",
    reason_not_extraction_ready="",
)

OA_IDS = {"PUBMED_0344", "PUBMED_0346", "PUBMED_0387", "PUBMED_0430", "PUBMED_0596"}
SUBSCRIPTION_IDS = {"PUBMED_0388", "PUBMED_0468", "PUBMED_0602"}

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
