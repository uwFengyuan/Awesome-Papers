# Beyond the convexity assumption: Realistic tabular data generation under quantifier-free real linear constraints

ICLR 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：build our DRL on top of each to create DGM+DRL models. A description of these models is in Appendix H. Datasets. We consider five real-world datasets and associated constraints. Four datasets (i.e., URL, CCS, LCLD, and Heloc) are used for classification tasks, while one dataset (i.e., House) is used for regression. A detailed description of the datasets and their respective constraints are in Appendix G. 4.1 S YNTHETIC DATA Q UALITY Background knowledge align- Table 1: CVR for each model and dataset. Cases with ment. To assess how often the CVR≥50% are under

[Paper](https://openreview.net/forum?id=rx0TCew0Lj)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Synthetic tabular data generation has traditionally been a challenging problem due to the high complexity of the underlying distributions that characterise this type of data. Despite recent advances in deep generative models (DGMs), existing methods often fail to produce realistic datapoints that are well-aligned with available background knowledge.In this paper, we address this limitation by introducing Disjunctive Refinement Layer (DRL), a novel layer designedto enforce the alignment of generated data with the background knowledge specified in user-defined constraints.DRL is the first method able to automatically make deep learning models inherently compliant with constraints as expressive as quantifier-free linear formulas, which can define non-convex and even disconnected spaces. Our experimental analysis shows that DRL not only guarantees constraint satisfaction but also improves efficacy in downstream tasks. Notably, when applied to DGMs that frequently violate constraints, DRL eliminates violations entirely. Further, it improves performance metrics by up to 21.4\% in F1-score and 20.9\% in Area Under the ROC Curve, thus demonstrating its practical impact on data generation.
