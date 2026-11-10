# TabSDS: a Lightweight, Fully Non-Parametric, and Model Free Approach for Generating Synthetic Tabular Data

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：9 (0.005) (0.006) (0.005) (0.018) (0.018) (0.012) tions the figure only report results for the Abalone (AB) and DI 0.611 0.621 0.625 0.561 0.579 0.616 Bank marketing (BM) datasets. The complete results for (0.005) (0.003) (0.004) (0.023) (0.031) (0.005) EL 0.836 0.889 0.889 0.821 0.806 0.657 all datasets are presented in Figures 24 and 25 in Appendix (0.003) (0.003) (0.005) (0.010) (0.023) (0.024) G.6.) In addition to

[Paper](https://openreview.net/forum?id=UtlFqRDJKl)

Classification / 分类：Banking & Customer Service / 银行业务与客户服务 → Bank Marketing & Churn / 银行营销与客户流失 → General / 综合

## Abstract / 摘要

The development of deep generative models for tabular data is currently a very active research area in machine learning. These models, however, tend to be computationally heavy and require careful tuning of multiple model parameters. In this paper, we propose TabSDS - a lightweight, non-parametric, and model free alternative to tabular deep generative models which leverages rank and data shuffling transformations for generating synthetic data which closely approximates the joint probability distribution of the real data. We evaluate TabSDS against multiple baselines implemented in the Synthcity Python library across several datasets. TabSDS showed very competitive performance against all baselines (including TabDDPM - a strong baseline model for tabular data generation). Importantly, the execution time of TabSDS is orders of magnitude faster than the deep generative baselines, and also considerably faster than other computationally efficient baselines such as adversarial random forests.
