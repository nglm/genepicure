"""
Step 1: Infer causal gene-gene regulation using Findr.

In this module, you can find functions to infer gene regulatory networks
(GRNs) using the Findr tool. Findr, is a library for fast and accurate
causal inference. It uses genotype and gene expression data to
reconstruct GRNs by identifying causal relationships between genes.

We use the Julia implementation of Findr (then called BioFindr), which is available at
https://github.com/tmichoel/BioFindr.jl
as it is the most up-to-date version of Findr. To use BioFindr, GenEpicure relies on 

In the pipeline, the GNR should be inferred using training data only.

In this step, we assume that the data is preprocessed and formatted as
required. For more information, see genepicure.data.checks module.
"""