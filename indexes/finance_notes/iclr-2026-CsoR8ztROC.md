# TimeRecipe: A Time-Series Forecasting Recipe via Benchmarking Module Level Effectiveness

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Patch MLP 0.8542 10 0.6954 8 9.0 ✓ ✗ Temporal Invert MLP 0.8493 9 0.6958 10 9.5 Table 10: Top-10 configurations for the Exchange Rate dataset multivariate forecasting. IN: Instance Norm, SD: Series Decomposition. ✓ indicates module used, ✗ indicates not used. Red/blue highlights indicate best and second-best performances. 28 Published as a conference paper at ICLR 2026 Setup IN SD Fusion Embed FF-Type MSE Rank MAE Rank Total ✓ ✗

[Paper](https://openreview.net/forum?id=CsoR8ztROC)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Time-series forecasting is an essential task with wide real-world applications across domains. While recent advances in deep learning have enabled time-series forecasting models with accurate predictions, there remains considerable debate over which architectures and design components, such as series decomposition or normalization, are most effective under varying conditions. Existing benchmarks primarily evaluate models at a high level, offering limited insight into why certain designs work better. To mitigate this gap, we propose TIMERECIPE, a unified benchmarking framework that systematically evaluates time-series forecasting methods at the module level. TIMERECIPE conducts over 10,000 experiments to assess the effectiveness of individual components across a diverse range of datasets, forecasting horizons, and task settings. Our results reveal that exhaustive exploration of the design space can yield models that outperform existing state-of-the-art methods and uncover meaningful intuitions linking specific design choices to forecasting scenarios. Furthermore, we release a practical toolkit within TIMERECIPE that recommends suitable model architectures based on these empirical insights.
