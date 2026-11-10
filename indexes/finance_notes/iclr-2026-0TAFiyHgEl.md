# Unlocking the Value of Text: Event-Driven Reasoning and Multi-Level Alignment for Time Series Forecasting

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：990 2000 2010 2020 petitive performance (Nie et al., 2023; Chen et al., 2024; Qiu et al., Figure 1: Unemployment rate time series (Liu et al., 2024a) 2025d; Wu et al., 2025; 2022) on this (1970-2020). While certain patterns (pink) exhibit pre- task. However, they solely rely on dictable temporal regularities, abrupt changes (green) driven numerical time series data, limiting by external events necessitate the integration of textual in- their ability to capture more complex formation to complement numerical forecasting. patterns. Taking the unemployment rate data (Liu et al., 2024a) as an example, Figure 1 illustrates that certain abrupt changes in the time series are difficult to predict solely from historical numerical patterns. However, 

[Paper](https://openreview.net/forum?id=0TAFiyHgEl)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Existing time series forecasting methods primarily rely on the numerical data itself. However, real-world time series exhibit complex patterns associated with multimodal information, making them difficult to predict with numerical data alone. While several multimodal time series forecasting methods have emerged, they either utilize text with limited supplementary information or focus merely on representation extraction, extracting minimal textual information for forecasting. To unlock the Value of Text, we propose VoT, a method with Event-driven Reasoning and Multi-level Alignment. Event-driven Reasoning combines the rich information in exogenous text with the powerful reasoning capabilities of LLMs for time series forecasting. To guide the LLMs in effective reasoning, we propose the Historical In-context Learning that retrieves and applies historical examples as in-context guidance. To maximize the utilization of text, we propose Multi-level Alignment. At the representation level, we utilize the Endogenous Text Alignment to integrate the endogenous text information with the time series. At the prediction level, we design the Adaptive Frequency Fusion to fuse the frequency components of event-driven prediction and numerical prediction to achieve complementary advantages. Experiments on real-world datasets across 10 domains demonstrate significant improvements over existing methods, validating the effectiveness of our approach in the utilization of text. The code is made available at https://github.com/decisionintelligence/VoT.
