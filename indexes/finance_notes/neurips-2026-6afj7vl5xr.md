# PE-SHAP: Causally Interpretable Path-Wise Shapley Explanations

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：We validate PE-SHAP analytically and through Monte-Carlo experiments on synthetic SCMs with known path effects, and demonstrate it on real-world fairness case studies using the German Credit and COMPAS datasets.

[Paper](https://openreview.net/forum?id=6afj7vl5xr)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Shapley value-based explanations are widely used to attribute model predictions, but standard variants capture associative rather than causal relationships. Recent causally informed Shapley methods add a path-wise decomposition, but suffer from two key limitations: they assign zero attribution to chain-mediated paths, and their per-path values do not align with classical mediation estimands.  We propose PE-SHAP, a Shapley-inspired path-wise decomposition built on the portion-eliminated effect. Per-mediator values sum to the total mediated effect at every sample, aggregate to the Natural Indirect Effect at the population level, and match the Path-Specific Effect under additive separability. These are properties prior Shapley-based path-wise methods do not provide. We validate PE-SHAP analytically and through Monte-Carlo experiments on synthetic SCMs with known path effects, and demonstrate it on real-world fairness case studies using the German Credit and COMPAS datasets.
