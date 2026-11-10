# Dynamic TMoE: A Drift-Aware Dynamic Mixture of Experts Framework for Non-Stationary Time Series Forecasting

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：0.293 0.271 0.311 0.240 0.272 0.249 0.277 0.258 0.281 0.259 0.287 0.267 0.317 0.309 0.360 Exchange 0.351 0.397 0.395 0.414 0.408 0.432 0.407 0.418 0.374 0.411 0.353 0.400 0.385 0.411 0.416 0.443 0.337 0.402 0.519 0.500 ETTh1 0.429 0.430 0.448 0.443 0.432 0.433 0.432 0.438 0.447 0.440 0.439 0.429 0.451 0.441 0.458 0.450 0.459 0.452 0.440 0.460

[Paper](https://openreview.net/forum?id=JabkBcaoa9)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Non-stationary time series forecasting is challenged by evolving distribution shifts that static models struggle to capture. While Mixture-of-Experts (MoE) architectures offer a promising paradigm for decoupling complex drift patterns, existing approaches are limited by fixed expert pools and memoryless routing, hampering their ability to adapt to abrupt regime shifts. To address this, we propose **Dynamic TMoE**, a framework that unifies architectural evolution with temporal continuity during learning phase. By detecting distribution shifts via Maximum Mean Discrepancy (MMD), we dynamically instantiate heterogeneous experts and prune redundant ones to optimize capacity. Additionally, a temporal memory router leverages recurrent states and an anomaly repository to ensure stable, context-aware expert selection without requiring test-time updates. Experiments on nine benchmarks demonstrate state-of-the-art performance, reducing MSE by 10.4\% and MAE by 7.8\%. Code is available at https://github.com/andone-07/Dynamic-TMoE.
