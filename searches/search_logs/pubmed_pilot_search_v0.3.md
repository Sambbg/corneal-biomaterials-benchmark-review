# PubMed Pilot Search v0.3

## Purpose

PubMed v0.2 improved the search structure but still produced broad result sets, especially for epithelium/limbus and endothelium. This v0.3 strategy is stricter and aims to retrieve primary or clinically translational biomaterials evidence with extractable benchmarking data.

## Main Change from v0.2

This version adds stronger performance and study-output terms and excludes review publication types for the primary evidence search.

Important: reviews will still be collected separately for background and gap-mapping. They should not dominate the primary extraction table.

---

# Search A3: Epithelium / Limbal Niche - Primary Evidence Focus

## Compact Search String

((corneal[Title/Abstract] OR cornea[Title/Abstract] OR limbal[Title/Abstract]) AND (epithelium[Title/Abstract] OR epithelial[Title/Abstract] OR "limbal stem cell"[Title/Abstract] OR "limbal stem cells"[Title/Abstract]) AND (biomaterial*[Title/Abstract] OR scaffold*[Title/Abstract] OR hydrogel*[Title/Abstract] OR "cell sheet"[Title/Abstract] OR "cell sheets"[Title/Abstract] OR bioengineer*[Title/Abstract] OR "tissue engineering"[Title/Abstract]) AND (viability[Title/Abstract] OR phenotype[Title/Abstract] OR transplantation[Title/Abstract] OR transplant[Title/Abstract] OR clinical[Title/Abstract] OR regeneration[Title/Abstract] OR "first-in-human"[Title/Abstract])) AND ("2018/01/01"[Date - Publication] : "3000"[Date - Publication]) NOT (review[Publication Type])

---

# Search B3: Stroma - Biomaterial Performance Focus

## Compact Search String

((corneal[Title/Abstract] OR cornea[Title/Abstract]) AND (stroma[Title/Abstract] OR stromal[Title/Abstract] OR keratocyte*[Title/Abstract]) AND (biomaterial*[Title/Abstract] OR scaffold*[Title/Abstract] OR hydrogel*[Title/Abstract] OR collagen[Title/Abstract] OR decellulari*[Title/Abstract] OR bioprint*[Title/Abstract] OR electrospun[Title/Abstract] OR electrospinning[Title/Abstract] OR bioengineer*[Title/Abstract] OR "tissue engineering"[Title/Abstract]) AND (transparency[Title/Abstract] OR transparent[Title/Abstract] OR mechanical[Title/Abstract] OR biomechanics[Title/Abstract] OR modulus[Title/Abstract] OR tensile[Title/Abstract] OR degradation[Title/Abstract] OR swelling[Title/Abstract] OR regeneration[Title/Abstract])) AND ("2018/01/01"[Date - Publication] : "3000"[Date - Publication]) NOT (review[Publication Type])

---

# Search C3: Endothelium - Engineered Substitute / Carrier Focus

## Compact Search String

((corneal[Title/Abstract] OR cornea[Title/Abstract]) AND (endothelium[Title/Abstract] OR endothelial[Title/Abstract]) AND (biomaterial*[Title/Abstract] OR scaffold*[Title/Abstract] OR hydrogel*[Title/Abstract] OR "cell sheet"[Title/Abstract] OR "cell sheets"[Title/Abstract] OR carrier[Title/Abstract] OR membrane[Title/Abstract] OR bioengineer*[Title/Abstract] OR "tissue engineering"[Title/Abstract]) AND (phenotype[Title/Abstract] OR "Na+/K+-ATPase"[Title/Abstract] OR ZO-1[Title/Abstract] OR pump[Title/Abstract] OR "cell density"[Title/Abstract] OR transplantation[Title/Abstract] OR transplant[Title/Abstract] OR clinical[Title/Abstract])) AND ("2018/01/01"[Date - Publication] : "3000"[Date - Publication]) NOT (review[Publication Type])

---

# Search D3: Full-Thickness / Multilayer / Bioprinted Cornea - Primary Evidence Focus

## Compact Search String

((corneal[Title/Abstract] OR cornea[Title/Abstract]) AND ("full thickness"[Title/Abstract] OR full-thickness[Title/Abstract] OR multilayer[Title/Abstract] OR multi-layer[Title/Abstract] OR bioprint*[Title/Abstract] OR "3D print"[Title/Abstract] OR "3D printing"[Title/Abstract] OR construct*[Title/Abstract]) AND (biomaterial*[Title/Abstract] OR scaffold*[Title/Abstract] OR hydrogel*[Title/Abstract] OR collagen[Title/Abstract] OR bioink[Title/Abstract] OR bioengineer*[Title/Abstract] OR "tissue engineering"[Title/Abstract]) AND (viability[Title/Abstract] OR transparency[Title/Abstract] OR mechanical[Title/Abstract] OR phenotype[Title/Abstract] OR regeneration[Title/Abstract] OR implantation[Title/Abstract])) AND ("2018/01/01"[Date - Publication] : "3000"[Date - Publication]) NOT (review[Publication Type])

---

# Manual Result Log

Record:

- Search A3 result count:
- Search B3 result count:
- Search C3 result count:
- Search D3 result count:

## Decision Rule

If a search is still above 500 results, it is probably too broad for primary extraction and needs further narrowing.

If a search is between 100 and 400 results and the first page contains mostly relevant primary/translational studies, it is acceptable for formal screening.

If a search is below 50 results, it may be too narrow unless it retrieves known landmark papers.
