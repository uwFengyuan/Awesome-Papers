# Debiased Causal Tree: Heterogeneous Treatment Effects Estimation with Unmeasured Confounding

NeurIPS 2022 · main · Long

[Long] [Main] [Poster] [Spotlight] [Finance]

Financial evidence / 金融依据：The computational feasibility and statistical power of our method are evidenced by simulations and a study of a credit card balance dataset.

[Paper](https://openreview.net/forum?id=B26CPuYw9VA)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Lending & Credit Data / 借贷与信贷数据应用 → General / 综合

## Abstract / 摘要

Unmeasured confounding poses a significant threat to the validity of causal inference. Despite that various ad hoc methods are developed to remove confounding effects, they are subject to certain fairly strong assumptions. In this work, we consider the estimation of conditional causal effects in the presence of unmeasured confounding using observational data and historical controls. Under an interpretable transportability condition, we prove the partial identifiability of conditional average treatment effect on the treated group (CATT). For tree-based models, a new notion, \emph{confounding entropy}, is proposed to measure the discrepancy introduced by unobserved confounders between the conditional outcome distribution of the treated and control groups. The confounding entropy generalizes conventional confounding bias, and can be estimated effectively using historical controls. We develop a new method, debiased causal tree, whose splitting rule is to minimize the empirical risk regularized by the confounding entropy. Notably, our method integrates current observational data (for empirical risk) and their historical controls (for confounding entropy) harmoniously.  We highlight that, debiased causal tree can not only estimate CATT well in the presence of unmeasured confounding, but also is a robust estimator of conditional average treatment effect (CATE) against the imbalance of the treated and control populations when all confounders are observed. An extension of combining multiple debiased causal trees to further reduce biases by gradient boosting is considered. The computational feasibility and statistical power of our method are evidenced by simulations and a study of a credit card balance dataset.
