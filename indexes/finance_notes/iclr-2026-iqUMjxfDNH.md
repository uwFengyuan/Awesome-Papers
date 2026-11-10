# Test-Time Efficient Pretrained Model Portfolios for Time Series Forecasting

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：,379 0.0% 401 daily transport uber_tlc_daily 262 47,422 0.0% 181 daily transport m4_daily 4,227 10,023,836 0.0% 2371 daily various monash/bitcoin 18 82,458 9.8% 4581 daily various monash/bitcoin_without_missing_values 18 75,364 0.0% 4187 daily various monash/us_births

[Paper](https://openreview.net/forum?id=iqUMjxfDNH)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Is bigger always better for time series foundation models? With the question in mind, we explore an alternative to training a single, large monolithic model: building a portfolio of smaller, pretrained forecasting models. By applying ensembling or model selection over these portfolios, we achieve competitive performance on large-scale benchmarks using much fewer parameters. We explore strategies for designing such portfolios and find that collections of specialist models consistently outperform portfolios of independently trained generalists. Remarkably, we demonstrate that post-training a base model is a compute-effective approach for creating sufficiently diverse specialists, and provide evidences that ensembling and model selection are more compute-efficient than test-time fine-tuning.
