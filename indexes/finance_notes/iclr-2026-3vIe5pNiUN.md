# Joint Distribution–Informed Shapley Values for Sparse Counterfactual Explanations

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：026 Table 1: [Experiment Scenarios Setup] Four datasets are used to benchmark five CE algorithms over 12 models. A “scenario” is defined to be a combination of dataset, ACE algorithm, and a model f . Dataset HELOC (FICO, 2018), German Credit (Hofmann, 1994), Hotel Bookings (Antonio et al., 2019), COMPAS (Jeff Larson et al., 2016) ACE DiCE (Mothilal et al., 2020), AReS (Rawal & Lakkaraju, 2020), GlobeCE (Ley et al., 2023), KNN (Albini et al., 2022; Contardo et al.; Forel et al., 2023), Discount (You et

[Paper](https://openreview.net/forum?id=3vIe5pNiUN)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Counterfactual explanations (CE) aim to reveal how small input changes flip a model’s prediction, yet many methods modify more features than necessary, reducing clarity and actionability. We introduce COLA, a model- and generator-agnostic post-hoc framework that refines any given CE by computing a coupling via optimal transport (OT) between factual and counterfactual sets and using it to drive a Shapley-based attribution p-SHAP that selects a minimal set of edits while preserving the target effect. Theoretically, OT minimizes an upper bound on the $W_1$ divergence between factual and counterfactual outcomes and that, under mild conditions, refined counterfactuals are guaranteed not to move farther from the factuals than the originals. Empirically, across four datasets, twelve models, and five CE generators, COLA achieves the same target effects with only 26–45% of the original feature edits. On a small-scale benchmark, COLA shows near-optimality.
