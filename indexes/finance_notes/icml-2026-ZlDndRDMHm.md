# Reviving Error Correction in Modern Deep Time-Series Forecasting

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：denote performance degradation. We further extend our evaluation to additional datasets, in- cluding Solar-Energy, Exchange-Rate, and ILI, using two Table 1 and Appendix Table 8 summarize the results for im- representative backbones (TimeMixer and TimesNet). The provements in MSE and MAE, respectively. Overall, most results in Table 3 show that UEC-STD remains effective, architectures, particularly MLP and

[Paper](https://openreview.net/forum?id=ZlDndRDMHm)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Modern deep-learning models have achieved remarkable success in time-series forecasting. Yet, their performance degrades in long-term prediction due to error accumulation in autoregressive inference, where predictions are recursively used as inputs. While classical error correction mechanisms (ECMs) have long been used in statistical methods, their applicability to deep learning models remains limited or ineffective. In this work, we revisit the error accumulation problem in deep time-series forecasting and investigate the role and necessity of ECMs in this new context. We propose a simple, architecture-agnostic error correction model that can be integrated with any existing forecaster without requiring retraining. By explicitly decomposing predictions into trend and seasonal components and training the corrector to adjust each separately, we introduce the Universal Error Corrector with Seasonal–Trend Decomposition (UEC-STD), which significantly improves correction accuracy and robustness across 4 backbones and 10 datasets. Our findings provide a practical tool for enhancing forecasts while offering new insights into mitigating autoregressive errors in deep time-series models.
