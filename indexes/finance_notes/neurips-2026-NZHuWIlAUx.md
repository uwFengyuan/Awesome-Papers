# Stable Alpha: Adversarial Invariant Representation Learning for Nonlinear Asset Pricing  under Temporal Distribution Shifts

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：

[Paper](https://openreview.net/forum?id=NZHuWIlAUx)

Classification / 分类：Asset Pricing / 资产定价 → Pricing Models & Risk Premia / 定价模型与风险溢价 → General / 综合

## Abstract / 摘要

Deep learning has emerged as a powerful paradigm for constructing nonlinear asset pricing factor models. However, temporal distribution shifts such as bull-bear transitions and industry rotations undermine the generalization of models trained under the i.i.d. assumption. As a result, existing models tend to exploit environment-specific correlations that are highly predictive in-sample but unstable across market regimes. To address this challenge, we propose $\textit{\textbf{CASH}}$, a causality-inspired asset pricing factor framework designed to learn invariant and minimally sufficient representations under temporal distribution shifts. CASH formulates an information-theoretic adversarial learning objective that systematically discards transient market noise by optimizing against an adversary designed to exploit spurious correlations, thereby distilling invariant factor-return relationships. The resulting invariant representation is then integrated into a conditional factor pricing model via a dynamic factor exposure network. Experiments on real-world stock datasets across multiple markets demonstrate that CASH consistently outperforms state-of-the-art baselines in out-of-sample return prediction and exhibits superior robustness under pronounced temporal regime shifts.
