# GenEpicure.grn - Gene Regulatory Network Inference

This module implements the first step of the GenEpicure pipeline: *Infer causal gene-gene regulation using Findr.*

### Findr

[Findr](https://github.com/lingfeiwang/findr), is a library for fast and accurate causal inference developed by Lingfei Wang and Tom Michoel, and was first described in the paper "*Efficient and accurate causal inference with hidden confounders from genome-transcriptome variation data*"[^Findr]. It uses genotype and gene expression data to reconstruct GRNs by identifying causal relationships between genes.

In GenEpicure, we use the [Julia implementation of Findr (then called BioFindr)](https://github.com/tmichoel/BioFindr.jl), as it is the most up-to-date version of Findr. The whole documentation of BioFindr is available [here](https://lab.michoel.info/BioFindr.jl/stable/#BioFindr-Documentation). In GenEpicure, we specifically use BioFindr's main function `findr` whose detailed documentation can be found [here](https://lab.michoel.info/BioFindr.jl/stable/testLLR/#Summary)-

### Data input

In this step, we assume that the data is preprocessed and formatted as required. For more information on the correct preprocessing and formatting, see genepicure.data.checks module. We use the same notation conventions as in [here](https://lab.michoel.info/BioFindr.jl/stable/testLLR/#Summary).

Note that in a machine learning pipeline, the GNR should be inferred using training data only, which should be a subsset of the full dataset and should be distinct from the test data used to evaluate the final model performance.

#### Gene expression matrix `dX`

Contains float, corresponding to normalized gene expression levels.

1. N rows, one per sample, (optionally with a sample identifier as first column)
2. G columns, one per gene, with an identifier (string) as header

```plaintext
sample_id   geneA     geneB      geneC      geneD       …
1          -0.241     0.832      -1.104     0.157       …
2           0.473    -0.116       0.291    -0.842       …
3          -1.022     0.507       0.063     0.334       …
…              …         …           …         …        …
```

#### Genotype matrix `dG`

Contains integer 0/1/2, corresponding to SNP genotypes coded as 0, 1, or 2 based on the number of alternative alleles.

1. N rows, one per sample. Must be the same order as the gene expression matrix `dX` or having matching identifiers as first column.
2. S columns, one per SNP. with a SNP identifer (string) as header

```plaintext
sample_id   rs1001   rs1002   rs1003   rs1004    …
1              0        1        2        0      …
2              1        1        0        2      …
3              2        0        1        1      …
…              …        …        …        …      …
```

#### eQTL mapping table `dE`

Contains string, corresponding to SNP-gene identifiers pairs.

1. S rows, one per number of SNP-gene pairs
2. 2 (or more) columns:
    1. SNP identifier (string) matching names the genotype matrix `dG`.
    2. Gene identifier (string) matching names in the gene expression matrix `dX`.
    3. (optional) Additional columns with eQTL statistics (beta, t-stat, p-value, adj.p-value, etc.)

```plaintext
Row   snp_id    gene_id      beta       t-stat    p-value     adj.p-value
1     rs1001    geneA      -0.378048   -3.95352   8.79e-05      0.03698
2     rs1002    geneA       0.569251    6.42444   3.03e-10      0.00050
3     rs1003    geneB       0.321534    4.21718   2.93e-05      0.01699
4     rs1004    geneD       0.329905    4.08898   5.03e-05      0.04098
…       …         …            …           …          …            …
```

### Data output

<!-- TODO -->
Coming soon.

### Usage

<!-- TODO -->
Coming soon.

### Additional dependencies

To use BioFindr, GenEpicure relies on [JuliaCall](https://github.com/JuliaPy/PythonCall.jl), a package that allows calling Julia code from Python. You can find JuliaCall's documentation [here](https://juliapy.github.io/PythonCall.jl/stable/juliacall/).


[^Findr]: Wang L, Michoel T (2017) Efficient and accurate causal inference with hidden confounders from genome-transcriptome variation data. PLoS Comput Biol 13(8): e1005703. https://doi.org/10.1371/journal.pcbi.1005703