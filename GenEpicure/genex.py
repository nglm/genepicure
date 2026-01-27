"""
Step 2: Gene expression modelling using both *cis* and *trans* eQTLs.

In this module, you can find functions to model gene expression levels
using both *cis* and *trans* eQTLs and the gene regulatory network (GRN)
topology inferred in step one by Findr. The modelling approach trains
two Ridge regression models, one for *cis* eQTLs and one for *trans*
eQTLs, which are then combined additively to predict gene expression
levels.

In the pipeline, the gene expression models should be trained using
training data and selected using the validation data or using cross
validation if no separate validation data is available.

The weight optimization of the *cis* and *trans* components should be performed
using the validation data.

In this step, we assume that the data is preprocessed and formatted as
required. For more information, see genepicure.data.checks module.
"""