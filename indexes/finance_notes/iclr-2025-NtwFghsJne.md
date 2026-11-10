# From Search to Sampling: Generative Models for Robust Algorithmic Recourse

ICLR 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：n Figure 2. In this section we focus on real datasets. 5.1 E XPERIMENTAL S ETUP Datasets: We experimented with benchmark datasets commonly used to evaluate recourse al- gorithms: Adult Income (Becker & Kohavi, 1996), FICO HELOC (FICO, 2018), and COM- PAS (Angwin et al., 2016). These datasets contain a mix of continuous and categorical features. All continuous attributes are normalized to the range of [0, 1], while categorical attributes are one-hot encoded. We defer detailed descriptions of these datasets to Appendix C.1 and present a summary in Table 1. For each d

[Paper](https://openreview.net/forum?id=NtwFghsJne)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Algorithmic Recourse provides recommendations to individuals who are adversely impacted by automated model decisions, on how to alter their profiles to achieve a favorable outcome. Effective recourse methods must balance three conflicting goals: proximity to the original profile to minimize cost, plausibility for realistic recourse, and validity to ensure the desired outcome. We show that existing methods train for these objectives separately and then search for recourse through a joint optimization over the recourse goals during inference, leading to poor recourse recommendations. We introduce GenRe, a generative recourse model designed to train the three recourse objectives jointly. Training such generative models is non-trivial due to lack of direct recourse supervision. We propose efficient ways to synthesize such supervision and further show that GenRe's training leads to a consistent estimator. Unlike most prior methods, that employ non-robust gradient descent based search during inference, GenRe simply performs a forward sampling over the generative model to produce minimum cost recourse, leading to superior performance across multiple metrics. We also demonstrate GenRe provides the best trade-off between cost, plausibility and validity, compared to state-of-art baselines. We release anonymized code at: https://anonymous.4open.science/r/GenRe-BD71
