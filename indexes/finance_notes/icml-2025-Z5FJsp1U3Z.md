# LightGTS: A Lightweight General Time Series Forecasting Model

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：0.266 0.208 0.256 0.292 0.313 0.26 0.275 0.288 0.309 - - 0.270 0.300 Exchange 0.345 0.395 0.347 0.396 0.392 0.425 0.385 0.417 0.370 0.412 0.390 0.417 0.432 0.454 Solar 0.219 0.305 0.191 0.271 0.771 0.604 0.714 0.704 0.393 0.319 0.500 0.397 0.411 0.428 Electricity 0.233 0.319 0.213 0.308 0.297 0.375 0.18

[Paper](https://openreview.net/forum?id=Z5FJsp1U3Z)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Existing works on general time series forecasting build foundation models with heavy model parameters through large-scale multi-source pretraining. These models achieve superior generalization ability across various datasets at the cost of significant computational burdens and limitations in resource-constrained scenarios. This paper introduces LightGTS, a lightweight general time series forecasting model designed from the perspective of consistent periodical modeling. To handle diverse scales and intrinsic periods in multi-source pre-training, we introduce Periodical Tokenization, which extracts consistent periodic patterns across different datasets with varying scales. To better utilize the periodicity in the decoding process, we further introduce Periodical Parallel Decoding, which leverage historical tokens to improve forecasting. Based on the two techniques above which fully leverage the inductive bias of periods inherent in time series, LightGTS uses a lightweight model to achieve outstanding performance on general time series forecasting. It achieves state-of-the-art forecasting performance on 9 real-world benchmarks in both zero-shot and full-shot setting with much better efficiency compared with existing time series foundation models
