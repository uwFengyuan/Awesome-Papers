# Getting a CLUE: A  Method for Explaining Uncertainty Estimates

ICLR 2021 · main · Long

[Long] [Main] [Oral] [Poster] [Finance]

Financial evidence / 金融依据：mpas-analysis/blob/master/ compas-scores-two-years.csv). The red wine quality prediction dataset can be obtained from and is described in detail at (https: //archive.ics.uci.edu/ml/datasets/wine+quality). The default of credit card clients dataset, which we refer to as “Credit” in this work, can be ob- tained from and is described in detail at (https://archive.ics.uci.edu/ml/datasets/ default+of+credit+card+clients). Note that this dataset is different from the also com- monly used German credit dataset. The MNIST handwritten digit image dataset can be obtained from (http://

[Paper](https://openreview.net/forum?id=XSLF1XFq5h)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Both uncertainty estimation and interpretability are important factors for trustworthy machine learning systems. However, there is little work at the intersection of these two areas. We address this gap by proposing a novel method for interpreting uncertainty estimates from differentiable probabilistic models, like Bayesian Neural Networks (BNNs). Our method, Counterfactual Latent Uncertainty Explanations (CLUE), indicates how to change an input, while keeping it on the data manifold, such that a BNN becomes more confident about the input's prediction. We validate CLUE through 1) a novel framework for evaluating counterfactual explanations of uncertainty, 2) a series of ablation experiments, and 3) a user study. Our experiments show that CLUE outperforms baselines and enables practitioners to better understand which input patterns are responsible for predictive uncertainty.
