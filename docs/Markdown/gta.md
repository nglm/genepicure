# GenEpicure.gta - Evaluating Gene-Trait Association

This module implements the third step of the GenEpicure pipeline: *Evaluates gene-disease associations by combining GWAS summary statistics with expression model coefficients* using a combination of Z-scores derived from the [S-PrediXcan](https://www.nature.com/articles/s41467-018-03621-1)[^S-PrediXcan] method.

## Method: Gene-Trait Association using S-PrediXcan and trans-eQTLs

### Background

The main objective is to identify genetic variants associated with specific traits or diseases. There are many on-going efforts to identify such associations such as Genome-Wide Association Studies (GWAS) and Transcriptome-Wide Association Studies (TWAS).

GWAS identifies which genetic markers are more common in individuals with a particular trait compared to those without it and have been successful in associating genetic variants (usually SNPs) with specific traits or diseases. However, GWAS identifies associations but does not explain how (or if) these variants affect biological processes or lead to disease, limiting the possibility to translate these findings into therapeutic interventions. For example, variants identified in GWAS may not be the causal variants but rather linked to them due to Linkage Disequilibrium (LD), making it challenging to pinpoint the exact genetic changes responsible for the trait.

In addition, many variants identified by GWAS are located in non-coding regions of the genome, making it difficult to interpret their functional impact. To address these challenges, TWAS have been developed, integrating gene expression data with GWAS results to identify genes whose expression levels are associated with traits or diseases. However, most studies focus on variants located in the vicinity of genes (cis-eQTLs) while it has been shown that trans-eQTLs (variants located far from the gene they regulate) can also have significant effects on gene expression and contribute to complex traits and diseases.

Therefore, in this step, we aim to take into account GWAS as well as both cis and trans eQTLs to better understand gene-trait associations.

### Using S-PrediXcan for Gene-Trait Association as a proxy for PrediXcan

[PrediXcan](https://www.nature.com/articles/ng.3367)[^PrediXcan] tests the effects of gene expresion levels on phenotypes. It works at the individual level, meaning that it requires individual-level genotype and phenotype data to evaluate gene-trait associations. Unfortunately, individual-level data is often not available due to privacy concerns or logistical challenges. To overcome this limitation, S-PrediXcan was developed to work with GWAS summary statistics instead of individual-level data. Barbeira et al.[^S-PrediXcan] showed that in most cases, S-PrediXcan produces results that are very similar to those obtained with PrediXcan, making it a valuable tool for gene-trait association studies when only summary statistics are available.

### Combining cis and trans S-PrediXcan Z-scores

<!-- TODO -->
Coming soon.

## Data

### Data input

In this step, we assume that the data is preprocessed and formatted as required. For more information on the correct preprocessing and formatting, see `genepicure.data.checks` module.

Note that in a machine learning pipeline, the covariance matrix should be computed using only the training data.

#### GWAS summary statistics

#### Gene expression model coefficients

### Data output

<!-- TODO -->
Coming soon.

## Usage

<!-- TODO -->
Coming soon.

[^PrediXcan]: Gamazon, E., Wheeler, H., Shah, K. et al. A gene-based association method for mapping traits using reference transcriptome data. Nat Genet 47, 1091–1098 (2015). https://doi.org/10.1038/ng.3367
[^S-PrediXcan]: Barbeira, A.N., Dickinson, S.P., Bonazzola, R. et al. Exploring the phenotypic consequences of tissue specific gene expression variation inferred from GWAS summary statistics. Nat Commun 9, 1825 (2018). https://doi.org/10.1038/s41467-018-03621-1