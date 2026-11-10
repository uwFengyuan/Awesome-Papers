# Rethinking Multimodal Time-Series Forecasting Evaluation

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：that are critical for forecasting. Time- MMD (Liu et al., 2024b) provides a context enriched benchmark constructed by keyword-based web searches of nine domains, one variable for each. MTBench (Chen et al., 2025) aligns stock prices with financial news and weather reports with temperature records, curating tasks that require reasoning about them. The MoTime (Zhou et al., 2025) dataset suite provides a collection of multimodal datasets pairing time series with static modalities like text and images. Noticeably, these early efforts were often constrained by a scarcity of high-

[Paper](https://openreview.net/forum?id=auG2Cr76ed)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

We introduce a new context-enriched, multimodal time series forecasting benchmark TimesX. TimesX contains a wide selection of high-quality real-world time series with diverse domains and textual contexts obtained from an automated data generation pipeline, which helps address three main issues of existing multimodal forecasting benchmarks: (1) poor generalization due to the small scale and synthetic nature of benchmark data, (2) very limited types of textual contexts in the benchmarks, and (3) an inability to mitigate data leakage in evaluation. We conduct a thorough empirical study of zero-shot multimodal forecasting approaches on TimesX. Our results suggest that many approaches that perform well on existing benchmarks may fail on TimesX. In contrast, simple ensemble methods that leverage rich textual context accompanying time-series can outperform strong baselines on the TimesX benchmark.
