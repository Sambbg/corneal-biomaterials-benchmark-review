"""
Add two primary studies identified via a targeted Consensus reference-list
snowball check (protocol v0.2, "Supplementary evidence" section) that were
confirmed absent from the PubMed search corpus:

- Puistola et al. 2024, PMID 38513048 (stroma) - cornea-specific
  adipose-stem-cell-derived ECM used as a corneal stroma bioink component.
- Ben Moussa et al. 2024, PMID 38534529 (endothelium) - femtosecond-laser-cut
  human lens capsule as a decellularized carrier for corneal endothelial
  cells.

This script appends both records to:
  1. screening/title_abstract/pubmed_title_abstract_screening.csv (provenance)
  2. screening/full_text/pubmed_balanced_final_core_records.csv (core pool)
  3. extraction/pubmed_balanced_core_data_extraction_template.csv (extraction)

Both are marked with decision=Include and a screening_notes / strict_final_status
value that makes clear they entered the corpus via manual snowball addition,
not the original PubMed A3/B3/C4/D3 search blocks.
"""
from pathlib import Path
import csv

NEW_PAPERS = [
    {
        "screening_id": "PUBMED_1083",
        "pmid": "38513048",
        "title": "Cornea-Specific Human Adipose Stem Cell-Derived Extracellular Matrix for Corneal Stroma Tissue Engineering",
        "abstract": (
            "Utilizing tissue-specific extracellular matrices (ECMs) is vital for replicating the composition of "
            "native tissues and developing biologically relevant biomaterials. Human- or animal-derived donor "
            "tissues and organs are the current gold standard for the source of these ECMs. To overcome the "
            "several limitations related to these ECM sources, including the highly limited availability of donor "
            "tissues, cell-derived ECM offers an alternative approach for engineering tissue-specific biomaterials, "
            "such as bioinks for three-dimensional (3D) bioprinting. In this study, a corneal stroma-specific ECM "
            "was engineered without the need for donor corneas by differentiating human adipose stem cells (hASCs) "
            "toward corneal stromal keratocytes (hASC-CSKs). This ECM was utilized as a component for a corneal "
            "stroma-specific bioink where hASC-CSKs were printed to produce corneal stroma structures."
        ),
        "year": "2024",
        "journal": "ACS Applied Materials & Interfaces",
        "doi": "10.1021/acsami.3c17803",
        "corneal_layer": "stroma",
    },
    {
        "screening_id": "PUBMED_1084",
        "pmid": "38534529",
        "title": "Femtosecond Laser Cutting of Human Crystalline Lens Capsule and Decellularization for Corneal Endothelial Bioengineering",
        "abstract": (
            "The bioengineering of corneal endothelial grafts consists of seeding in vitro cultured corneal "
            "endothelial cells onto a thin, transparent, biocompatible, and sufficiently robust carrier which can "
            "withstand surgical manipulations. The anterior capsule of the crystalline lens has already been "
            "identified as one of the best possible carriers, but its challenging manual preparation has limited "
            "its use. This study describes a femtosecond laser cutting process of the anterior capsule of whole "
            "lenses to obtain capsule discs of 8 mm diameter, similar to conventional endothelial grafts. "
            "Immersion in water for 3 days is sufficient to completely remove the lens epithelial cells and to "
            "enable the seeding of corneal endothelial cells, which remain viable after 27 days of culture."
        ),
        "year": "2024",
        "journal": "Bioengineering (Basel)",
        "doi": "10.3390/bioengineering11030255",
        "corneal_layer": "endothelium",
    },
]

SOURCE_NOTE = "Manually added via targeted Consensus reference-list snowball check (protocol v0.2 supplementary evidence step); confirmed absent from PubMed A3/B3/C4/D3 search blocks."


def load(path):
    with Path(path).open(newline="", encoding="utf-8-sig") as f:
        r = csv.DictReader(f)
        return list(r), r.fieldnames


def save(path, rows, fieldnames):
    with Path(path).open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)


# 1. Title/abstract screening master file
ta_path = "screening/title_abstract/pubmed_title_abstract_screening.csv"
ta_rows, ta_fields = load(ta_path)
for p in NEW_PAPERS:
    row = {k: "" for k in ta_fields}
    row.update({
        "screening_id": p["screening_id"],
        "pmid": p["pmid"],
        "title": p["title"],
        "abstract": p["abstract"],
        "year": p["year"],
        "journal": p["journal"],
        "doi": p["doi"],
        "sources": "consensus_snowball",
        "source_count": "1",
        "decision": "Include",
        "corneal_layer": p["corneal_layer"],
        "priority_level": "High",
        "screening_notes": SOURCE_NOTE,
    })
    ta_rows.append(row)
save(ta_path, ta_rows, ta_fields)

# 2. Balanced final core records
core_path = "screening/full_text/pubmed_balanced_final_core_records.csv"
core_rows, core_fields = load(core_path)
for p in NEW_PAPERS:
    row = {k: "" for k in core_fields}
    row.update({
        "screening_id": p["screening_id"],
        "pmid": p["pmid"],
        "title": p["title"],
        "abstract": p["abstract"],
        "year": p["year"],
        "journal": p["journal"],
        "doi": p["doi"],
        "sources": "consensus_snowball",
        "source_count": "1",
        "decision": "Include",
        "corneal_layer": p["corneal_layer"],
        "priority_level": "High",
        "screening_notes": SOURCE_NOTE,
        "final_core_status": "Manually added - Consensus snowball check",
        "strict_final_status": "Manually added - Consensus snowball check",
    })
    core_rows.append(row)
save(core_path, core_rows, core_fields)

# 3. Extraction template
ext_path = "extraction/pubmed_balanced_core_data_extraction_template.csv"
ext_rows, ext_fields = load(ext_path)
for p in NEW_PAPERS:
    row = {k: "" for k in ext_fields}
    row.update({
        "screening_id": p["screening_id"],
        "pmid": p["pmid"],
        "title": p["title"],
        "year": p["year"],
        "journal": p["journal"],
        "doi": p["doi"],
        "corneal_layer": p["corneal_layer"],
        "priority_level": "High",
        "strict_final_status": "Manually added - Consensus snowball check",
        "extraction_status": "not_started",
    })
    ext_rows.append(row)
save(ext_path, ext_rows, ext_fields)

print(f"Added {len(NEW_PAPERS)} papers to:")
print(f"  - {ta_path} (now {len(ta_rows)} rows)")
print(f"  - {core_path} (now {len(core_rows)} rows)")
print(f"  - {ext_path} (now {len(ext_rows)} rows)")
