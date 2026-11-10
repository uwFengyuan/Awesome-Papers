# Counterfactual Online Conformal Prediction Under Adaptive Logging

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Experiments on synthetic decision tasks, open bandit data, and financial rebalancing show that PW-OCP and DR-OCP improve counterfactual coverage and downstream regret without sacrificing prediction-set sharpness.

[Paper](https://openreview.net/forum?id=kcz4dJYi4k)

Classification / 分类：Portfolio & Investment / 投资组合与投资管理 → Investment Evaluation & Decisions / 投资评价与决策 → General / 综合

## Abstract / 摘要

Online conformal prediction can fail when predictions shape actions and actions determine which outcomes enter calibration. Standard adaptive methods may retain marginal coverage while systematically miscovering the counterfactual outcomes of rarely selected actions. This paper formalizes the failure through counterfactual coverage and introduces Propensity-Weighted Online Conformal Prediction, an inverse-propensity-weighted recursion that debiases calibration. A doubly robust variant further reduces nuisance bias to the product of outcome-model and propensity errors. Under positivity, the resulting coverage rate matches an information-theoretic lower bound up to logarithmic factors. Experiments on synthetic decision tasks, open bandit data, and financial rebalancing show that PW-OCP and DR-OCP improve counterfactual coverage and downstream regret without sacrificing prediction-set sharpness.
