# In-Context Fine-Tuning for Time-Series Foundation Models

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：s that cov- ers granularities ranging from minutes to years and domains including finance, demand forecasting, weather, and traffic. 6. Experimental Results We report our results on the 23 datasets from this benchmark Similar to prior works, we report our results on the Chronos that were not used during training of TimesFM-ICF (or the zero-shot benchmarks from

[Paper](https://openreview.net/forum?id=uxzgGLWPj2)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Foundation models / 基础模型

## Abstract / 摘要

Motivated by the recent success of time-series foundation models for zero-shot forecasting, we present a methodology for _in-context fine-tuning_ of a time-series foundation model. In particular, we design a pretrained foundation model that can be prompted (at inference time) with multiple time-series examples, in order to forecast a target time-series into the future. Our foundation model is specifically trained to utilize examples from multiple related time-series in its context window (in addition to the history of the target time-series) to help it adapt to the specific distribution of the target domain at inference time.  We show that such a foundation model that uses in-context examples at inference time can obtain much better performance on popular forecasting benchmarks compared to supervised deep learning methods, statistical models, and other time series foundation models.  Interestingly, our in-context fine-tuning approach even matches the performance of a foundation model that is explicitly fine-tuned on the target domain.
