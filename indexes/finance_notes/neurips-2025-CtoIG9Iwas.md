# Learning Pattern-Specific Experts for Time Series Forecasting Under Patch-level Distribution Shift

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：0.206 0.088 0.210 0.086 0.206 0.084 0.205 0.089 0.206 0.105 0.233 0.089 0.219 0.136 0.265 Exchange 192 11.2% 0.174 0.297 0.178 0.300 0.181 0.304 0.181 0.304 0.176 0.299 0.178 0.302 0.219 0.342 0.180 0.319 0.279 0.384 336 10.4% 0.310 0.398 0.329 0.415 0.324 0.413 0.338 0.422 0.321 0.409 0.326 0.411 0.353 0.433 0.313 0.423 0.465

[Paper](https://openreview.net/forum?id=CtoIG9Iwas)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Time series forecasting, which aims to predict future values based on historical data, has garnered significant attention due to its broad range of applications. However, real-world time series often exhibit heterogeneous pattern evolution across segments, such as seasonal variations, regime changes, or contextual shifts, making accurate forecasting challenging. Existing approaches, which typically train a single model to capture all these diverse patterns, often struggle with the pattern drifts between patches and may lead to poor generalization. To address these challenges, we propose TFPS, a novel architecture that leverages pattern-specific experts for more accurate and adaptable time series forecasting. TFPS employs a dual-domain encoder to capture both time-domain and frequency-domain features, enabling a more comprehensive understanding of temporal dynamics. It then performs subspace clustering to dynamically identify distinct patterns across data segments. Finally, these patterns are modeled by specialized experts, allowing the model to learn multiple predictive functions. Extensive experiments on real-world datasets demonstrate that TFPS outperforms state-of-the-art methods, particularly on datasets exhibiting significant distribution shifts. The data and code are available: https://github.com/syrGitHub/TFPS.
