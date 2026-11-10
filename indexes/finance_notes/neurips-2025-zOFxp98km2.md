# Online Portfolio Selection with ML Predictions

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Online portfolio selection seeks to determine a sequence of allocations to maximize capital growth. / Classical universal strategies asymptotically match the best constant-rebalanced portfolio but ignore potential forecasts, whereas heuristic methods often collapse when belief fails. / We formalize this tension in a learning-augmented setting in which an investor observes (possibly erroneous) predictions prior to each decision moment, and we introduce the Rebalanced Arithmetic Mean portfolio with predictions (RAM). / RAM advantages over universal-portfolio variants equipped with side information across various regimes.

[Paper](https://openreview.net/forum?id=zOFxp98km2)

Classification / 分类：Portfolio & Investment / 投资组合与投资管理 → Portfolio Selection & Optimization / 组合选择与优化 → General / 综合

## Abstract / 摘要

Online portfolio selection seeks to determine a sequence of allocations to maximize capital growth. Classical universal strategies asymptotically match the best constant-rebalanced portfolio but ignore potential forecasts, whereas heuristic methods often collapse when belief fails. We formalize this tension in a learning-augmented setting in which an investor observes (possibly erroneous) predictions prior to each decision moment, and we introduce the Rebalanced Arithmetic Mean portfolio with predictions (RAM). Under arbitrary return sequences, we prove that RAM captures at least a constant fraction of the hindsight-optimal wealth when forecasts are perfect while still exceeding the geometric mean of the sequence even when the predictions are adversarial. Comprehensive experiments on large-scale equity data strengthen our theory, spanning both synthetic prediction streams and production-grade machine-learning models. RAM advantages over universal-portfolio variants equipped with side information across various regimes. These results demonstrate that modest predictive power can be reliably converted into tangible gains without sacrificing worst-case guarantees.
