# PubMed Title/Abstract Screening Setup

## Source File

data/processed/pubmed_unique_records.csv

## Output Screening File

screening/title_abstract/pubmed_title_abstract_screening.csv

## Number of Unique PubMed Records

1082

## Screening Decision Options

- Include
- Exclude
- Uncertain

## Exclusion Reason Options

- Review/background only
- Book chapter/background clinical overview
- General ophthalmology/no engineering content
- Disease biology only
- Drug delivery only/no regenerative scaffold relevance
- Not corneal tissue engineering
- No biomaterial/scaffold/cell-engineering relevance
- Insufficient relevance from title/abstract

## Corneal Layer Options

- epithelium_limbus
- stroma
- endothelium
- full_thickness_multilayer
- multiple_layers
- unclear

## Priority Level Options

- High: likely core extraction/case-study candidate
- Medium: relevant but may support only part of the synthesis
- Low: background/supporting evidence only

## Methodological Note

Formal screening should not blindly follow AI decisions. AI may assist, but borderline records must be manually audited. The Uncertain category should be used whenever title/abstract information is insufficient.
