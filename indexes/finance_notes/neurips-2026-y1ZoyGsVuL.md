# A Set-Sequence Model for Time Series

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Many practical settings, however, involve predicting the evolution of a set of MTSs -- an unordered collection of units (e.g., a basket of stocks, a pool of loans, a fleet of sensors). / Across a synthetic contagion task and two large-scale real-world applications -- equity portfolio optimization and loan risk prediction -- Set-Sequence consistently improves sequence backbones and outperforms domain-specific baselines, delivering higher Sharpe ratios, improved AUCs, and interpretable cross-sectional summaries.

[Paper](https://openreview.net/forum?id=y1ZoyGsVuL)

Classification / 分类：Time Series / 时间序列 → General Time-Series Methods / 综合序列方法 → General / 综合

## Abstract / 摘要

Sequence models have advanced Multivariate Time Series (MTS) modeling by learning complex, long-range temporal dependencies. Many practical settings, however, involve predicting the evolution of a set of MTSs -- an unordered collection of units (e.g., a basket of stocks, a pool of loans, a fleet of sensors). This cross-sectional structure offers an opportunity to leverage signals shared across units (e.g., market volatility, correlated defaults) that are missed when each MTS is processed independently. Crucially, treating the entire cross-section as a single high-dimensional MTS is infeasible because the number of units varies dynamically at inference. We propose Set-Sequence, a backbone-agnostic architecture for set-of-MTS prediction that leverages this cross-sectional structure. A permutation-invariant Set module extracts a summary of the population, while a Sequence module (e.g., Transformer/SSM/RNN) then models each unit’s temporal dynamics conditioned on both its own history and the learned cross-sectional context. This architecture naturally accommodates varying set cardinalities, supports unaligned series, integrates with standard sequence backbones, and scales linearly in cross-sectional size. Across a synthetic contagion task and two large-scale real-world applications -- equity portfolio optimization and loan risk prediction -- Set-Sequence consistently improves sequence backbones and outperforms domain-specific baselines, delivering higher Sharpe ratios, improved AUCs, and interpretable cross-sectional summaries.
