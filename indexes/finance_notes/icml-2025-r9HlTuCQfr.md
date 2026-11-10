# Decision Making under the Exponential Family: Distributionally Robust Optimisation with Bayesian Ambiguity Sets

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Our DRO-BAS formulations outperform existing Bayesian DRO on the Newsvendor problem and achieve faster solve times with comparable robustness on the Portfolio problem.

[Paper](https://openreview.net/forum?id=r9HlTuCQfr)

Classification / 分类：Portfolio & Investment / 投资组合与投资管理 → Investment Evaluation & Decisions / 投资评价与决策 → General / 综合

## Abstract / 摘要

Decision making under uncertainty is challenging as the data-generating process (DGP) is often unknown. Bayesian inference proceeds by estimating the DGP through posterior beliefs on the model’s parameters. However, minimising the expected risk under these beliefs can lead to suboptimal decisions due to model uncertainty or limited, noisy observations. To address this, we introduce Distributionally Robust Optimisation with Bayesian Ambiguity Sets (DRO-BAS) which hedges against model uncertainty by optimising the worst-case risk over a posterior-informed ambiguity set. We provide two such sets, based on the posterior expectation (DRO-BAS(PE)) or the posterior predictive (DRO-BAS(PP)) and prove that both admit, under conditions, strong dual formulations leading to efficient single-stage stochastic programs which are solved with a sample average approximation. For DRO-BAS(PE), this covers all conjugate exponential family members while for DRO-BAS(PP) this is shown under conditions on the predictive's moment generating function. Our DRO-BAS formulations outperform existing Bayesian DRO on the Newsvendor problem and achieve faster solve times with comparable robustness on the Portfolio problem.
