# Loss-aware distributionally robust optimization via trainable optimal transport ambiguity sets

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：We present experiments validating our method on standard portfolio optimization and linear regression tasks.

[Paper](https://openreview.net/forum?id=K1EPPO9t2c)

Classification / 分类：Portfolio & Investment / 投资组合与投资管理 → Portfolio Selection & Optimization / 组合选择与优化 → General / 综合

## Abstract / 摘要

Optimal-transport distributionally robust optimization (OT-DRO) robustifies data-driven decision-making under uncertainty by capturing the sampling-induced statistical error via optimal transport ambiguity sets. The standard OT-DRO pipeline consists of a two-step procedure, where the ambiguity set is first designed and subsequently embedded into the downstream OT-DRO problem. However, this separation between uncertainty quantification and optimization may lead to excessive conservatism. We introduce an end-to-end pipeline to automatically learn decision-focused ambiguity sets for OT-DRO problems, where the loss function informs the shape of the ambiguity set, leading to less conservative decisions whose distributional robustness is enforced via data-driven bootstrapping. We formulate the learning problem as a bilevel optimization program and solve it via a hypergradient-based method. By leveraging the recently introduced nonsmooth conservative implicit function theorem, we establish convergence to a critical point of the bilevel problem. We present experiments validating our method on standard portfolio optimization and linear regression tasks.
