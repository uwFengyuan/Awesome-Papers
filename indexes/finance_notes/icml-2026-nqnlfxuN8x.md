# SEER: Transformer-based Robust Time Series Forecasting via Automated Patch Enhancement and Replacement

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：White Noise Anomalies Missing Value Dataset ILI NASDAQ FRED-MD Wike2000 SMD PSM USHCN Activity Metrics mse mae mse mae mse mae mse mae mse mae mse

[Paper](https://openreview.net/forum?id=nqnlfxuN8x)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Time series forecasting is important in many fields that require accurate predictions for decision-making. Patching techniques, commonly used and effective in time series modeling, help capture temporal dependencies by dividing the data into patches. However, existing patch-based methods fail to dynamically select patches and typically use all patches during the prediction process. In real-world time series, there are often low-quality issues during data collection, such as missing values, distribution shifts, anomalies and white noise, which may cause some patches to contain low-quality information, negatively impacting the prediction results. To address this issue, this study proposes a robust time series forecasting framework called $\textbf{SEER}$. Firstly, we propose an $\textit{Augmented Embedding Module}$, which improves patch-wise representations using a Mixture-of-Experts~(MoE) architecture and obtains series-wise token representations through a channel-adaptive perception mechanism. Secondly, we introduce a $\textit{Learnable Patch Replacement Module}$, which enhances forecasting robustness and model accuracy through a two-stage process: 1) a dynamic filtering mechanism eliminates negative patch-wise tokens; 2) a replaced attention module substitutes the identified low-quality patches with global series-wise token, further refining their representations through a causal attention mechanism. Comprehensive experimental results demonstrate the SOTA performance of SEER.
