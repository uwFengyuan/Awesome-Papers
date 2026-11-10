# Language in the Flow of Time: Time-Series-Paired Texts Weaved into a Unified Temporal Narrative

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：BM) 0.564 0.501 0.550 0.490 0.891 0.695 1.105 0.777 1.215 0.806 1.936 1.123 0.602 0.536 0.639 0.525 Company JPMorgan (JPM) 1.693 0.970 1.872 0.990 2.513 1.096 2.419 1.175 3.426 1.232 3.764 1.711 2.037 1.043 2.133 1.122 Stock Price NVIDIA (NVDA) 0.043 0.141 0.048 0.156 0.050 0.174 0.272 0.434 0.122 0.262 0.457 0.574 0.053 0.161 0.054 0.159 (2024) Pfizer (PFE) 0.326 0.416 0.347 0.422 0.448 0.477 0.676 0.572 0.824 0.663 0.628 0.559 0.408 0.477 0.369 0.439 Tesla (TSLA) 0.142 0.281 0.158 0.297 0.110 0.244 0.188 0.332 0.254 0.416 3.476 1.851 0.158 0.300 0.181 0.303 FNF: Bitcoin Price 2.609 1.112 2.339 1.045 2.775 1.142 141.738 10.355 159.019 10.535 57.826 6.744 3.590 1.344 2.721 1.152 Forecast with News Web Traffic 17.744 2.712 17.9

[Paper](https://openreview.net/forum?id=a1zBg9cBvt)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

While many advances in time series models focus exclusively on numerical data, research on multimodal time series, particularly those involving contextual textual information, remains in its infancy. With recent progress in large language models and time series learning, we revisit the integration of paired texts with time series through the Platonic Representation Hypothesis, which posits that representations of different modalities converge to shared spaces. In this context, we identify that time-series-paired texts may naturally exhibit periodic properties that closely mirror those of the original time series. Building on this insight, we propose a novel framework, Texts as Time Series (TaTS), which considers the time-series-paired texts to be auxiliary variables of the time series. TaTS can be plugged into any existing numerical-only time series models and effectively enable them to handle time series data with paired texts. Through extensive experiments on both multimodal time series forecasting and imputation tasks across benchmark datasets with various existing time series models, we demonstrate that TaTS can enhance multimodal predictive performance without modifying model architectures. Our Code is available at https://github.com/iDEA-iSAIL-Lab-UIUC/TaTS
