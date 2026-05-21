# Corneal Biomaterials Benchmark Review

## Working Title

From Optical Clarity to Clinical Readiness: A Layer-Specific Benchmarking Review of Biomaterials for Corneal Tissue Engineering

## Target Journal

Primary target: Acta Biomaterialia

## Review Type

Critical narrative review with systematic search transparency.

## Core Research Question

How well do currently reported biomaterials and biofabrication approaches reproduce the optical, mechanical, biological, and translational requirements of layer-specific corneal repair or replacement?

## Central Argument

Corneal tissue-engineering studies should not be judged only by novelty of biomaterial or fabrication method. They should be benchmarked against layer-specific requirements, including optical clarity, biomechanics, degradation behaviour, phenotype maintenance, surgical usability, safety, and translational readiness.

## Scope

Target corneal layers and construct types:

- Epithelium / limbal epithelial niche
- Stroma
- Endothelium
- Full-thickness or multi-layer constructs

## Evidence Focus

The review prioritizes primary studies, clinical/translational studies, and high-quality recent evidence from 2018 onward, with special attention to 2025–2026 literature.

## Benchmark Domains

Studies will be compared using the following domains:

- Optical transparency
- Mechanical properties
- Degradation and swelling
- Cell viability and phenotype maintenance
- In vivo or clinical performance
- Surgical handling
- Immunogenicity and safety
- Manufacturing and regulatory readiness

## Reproducibility Policy

All search strings, search dates, screening decisions, extraction templates, figure versions, and manuscript revisions will be version-controlled.

Full-text PDFs are not committed to this repository unless redistribution is legally permitted.

## Repository Structure

```text
manuscript/                 Draft manuscript files
protocol/                   Review protocol and scope documents
searches/                   Search logs and database export records
screening/                  Title/abstract and full-text screening records
extraction/                 Evidence extraction tables
figures/                    Raw and final figure assets
tables/                     Manuscript-ready tables
references/                 Bibliography files and citation notes
reports/environment/        Environment and system snapshots
reports/weekly_logs/        Research progress logs
scripts/                    Helper scripts for reproducibility
docs/journal_requirements/  Target journal notes and author guidance
data/                       Processed metadata only, not copyrighted PDFs
cd ~/research/corneal-biomaterials-benchmark-review

# Fix Git signing: use SSH signing, not GPG
git config --global user.name "Samuel Gonzalves"
git config --global user.email "samuel.b.gonzalves@gmail.com"
git config --global gpg.format ssh
git config --global user.signingkey "$HOME/.ssh/id_ed25519.pub"
git config --global commit.gpgsign true

# Delete broken README and recreate it cleanly
rm -f README.md

cat > README.md <<'EOF'
# Corneal Biomaterials Benchmark Review

## Working Title

From Optical Clarity to Clinical Readiness: A Layer-Specific Benchmarking Review of Biomaterials for Corneal Tissue Engineering

## Target Journal

Primary target: Acta Biomaterialia

## Review Type

Critical narrative review with systematic search transparency.

## Core Research Question

How well do currently reported biomaterials and biofabrication approaches reproduce the optical, mechanical, biological, and translational requirements of layer-specific corneal repair or replacement?

## Central Argument

Corneal tissue-engineering studies should not be judged only by novelty of biomaterial or fabrication method. They should be benchmarked against layer-specific requirements, including optical clarity, biomechanics, degradation behaviour, phenotype maintenance, surgical usability, safety, and translational readiness.

## Scope

Target corneal layers and construct types:

- Epithelium / limbal epithelial niche
- Stroma
- Endothelium
- Full-thickness or multi-layer constructs

## Evidence Focus

The review prioritizes primary studies, clinical/translational studies, and high-quality recent evidence from 2018 onward, with special attention to 2025–2026 literature.

## Benchmark Domains

Studies will be compared using the following domains:

- Optical transparency
- Mechanical properties
- Degradation and swelling
- Cell viability and phenotype maintenance
- In vivo or clinical performance
- Surgical handling
- Immunogenicity and safety
- Manufacturing and regulatory readiness

## Reproducibility Policy

All search strings, search dates, screening decisions, extraction templates, figure versions, and manuscript revisions will be version-controlled.

Full-text PDFs are not committed to this repository unless redistribution is legally permitted.
