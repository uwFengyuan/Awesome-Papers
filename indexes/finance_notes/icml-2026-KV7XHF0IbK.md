# Decision-focused Sparse Tangent Portfolio Optimization

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Sparse tangent portfolio optimization aims to learn an interpretable, low-cardinality portfolio in the tangency direction of the mean-variance frontier. / However, the associated cardinality-constrained formulation is NP-hard, and standard predict-then-optimize pipelines often misalign forecasting accuracy with downstream portfolio quality. / This enables gradient flow through prediction, asset selection, and re-optimization, allowing the predictive model to directly optimize portfolio performance.

[Paper](https://openreview.net/forum?id=KV7XHF0IbK)

Classification / 分类：Portfolio & Investment / 投资组合与投资管理 → Portfolio Selection & Optimization / 组合选择与优化 → General / 综合

## Abstract / 摘要

Sparse tangent portfolio optimization aims to learn an interpretable, low-cardinality portfolio in the tangency direction of the mean-variance frontier. However, the associated cardinality-constrained formulation is NP-hard, and standard predict-then-optimize pipelines often misalign forecasting accuracy with downstream portfolio quality. We propose an end-to-end decision-focused learning framework that reformulates Sharpe ratio maximization as a Disciplined Parametrized Programming (DPP)-compliant convex programming layer and replaces discrete selection with a smooth top-$k$ operator enforcing an exact cardinality $k$. This enables gradient flow through prediction, asset selection, and re-optimization, allowing the predictive model to directly optimize portfolio performance. Across four major equity markets, our method achieves competitive and often superior out-of-sample Sharpe ratios compared with historical and prediction-focused baselines, with particularly strong gains in larger asset universes. Our code is publicly available.
