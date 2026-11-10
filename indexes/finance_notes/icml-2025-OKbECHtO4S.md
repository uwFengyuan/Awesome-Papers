# Nested Expectations with Kernel Quadrature

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：We then demonstrate empirically that our proposed method does indeed require the fewest number of samples to estimate nested expectations over a range of real-world application areas from Bayesian optimisation to option pricing and health economics.

[Paper](https://openreview.net/forum?id=OKbECHtO4S)

Classification / 分类：Derivatives & Hedging / 衍生品定价与对冲 → Option Pricing & PDEs / 期权定价与PDE → General / 综合

## Abstract / 摘要

This paper considers the challenging computational task of estimating nested expectations. Existing algorithms, such as nested Monte Carlo or multilevel Monte Carlo, are known to be consistent but require a large number of samples at both inner and outer levels to converge. Instead, we propose a novel estimator consisting of nested kernel quadrature estimators and we prove that it has a faster convergence rate than all baseline methods when the integrands have sufficient smoothness. We then demonstrate empirically that our proposed method does indeed require the fewest number of samples to estimate nested expectations over a range of real-world application areas from Bayesian optimisation to option pricing and health economics.
