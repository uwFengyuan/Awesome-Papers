# On the Safety of Interpretable Machine Learning: A Maximum Deviation Approach

NeurIPS 2022 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：We present case studies, including one on mortgage approval, to illustrate our methods and the insights about models that may be obtained from deviation maximization.

[Paper](https://openreview.net/forum?id=WPXRVQaP9Oq)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Lending & Credit Data / 借贷与信贷数据应用 → General / 综合

## Abstract / 摘要

Interpretable and explainable machine learning has seen a recent surge of interest. We focus on safety as a key motivation behind the surge and make the relationship between interpretability and safety more quantitative. Toward assessing safety, we introduce the concept of *maximum deviation* via an optimization problem to find the largest deviation of a supervised learning model from a reference model regarded as safe. We then show how interpretability facilitates this safety assessment. For models including decision trees, generalized linear and additive models, the maximum deviation can be computed exactly and efficiently. For tree ensembles, which are not regarded as interpretable, discrete optimization techniques can still provide informative bounds. For a broader class of piecewise Lipschitz functions, we leverage the multi-armed bandit literature to show that interpretability produces tighter (regret) bounds on the maximum deviation. We present case studies, including one on mortgage approval, to illustrate our methods and the insights about models that may be obtained from deviation maximization.
