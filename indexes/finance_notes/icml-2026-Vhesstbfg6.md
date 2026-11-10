# Adversarially Robust Control of Conditional Value-at-Risk via Rockafellar-Uryasev Conformal Inference

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：We demonstrate the effectiveness of our approach on portfolio risk management and toxicity mitigation for Large Language Models (LLMs), where rare but catastrophic failures dominate system risk.

[Paper](https://openreview.net/forum?id=Vhesstbfg6)

Classification / 分类：Portfolio & Investment / 投资组合与投资管理 → Investment Evaluation & Decisions / 投资评价与决策 → General / 综合

## Abstract / 摘要

We present an online, distribution-free framework for controlling the Conditional Value-at-Risk ($\operatorname{CVaR}$), extending conformal tail risk control to non-stationary and adversarial environments. Unlike classical risk control methods, which rely on stationarity or linearity of expectation, our approach provides provable safety guarantees for a nonlinear tail risk functional under arbitrary data-generating processes that may drift or shift strategically over time. By leveraging deep connections between conformal tail risk control, online learning, and the variational representation of $\operatorname{CVaR}$ introduced by Rockafellar and Uryasev, we develop a novel procedure for online $\operatorname{CVaR}$ control with adversarial regret guarantees. The proposed method operates without assumptions on the underlying data-generating process, making it broadly applicable in modern high-stakes deployment settings. We prove that the realized empirical $\operatorname{CVaR}$ is asymptotically controlled at the target level, and that the resulting control is asymptotically tight up to a finite-sample ${O}(1/\sqrt{T})$ conservatism gap. We demonstrate the effectiveness of our approach on portfolio risk management and toxicity mitigation for Large Language Models (LLMs), where rare but catastrophic failures dominate system risk.
