# Characteristic Root Analysis and Regularization for Linear Time Series Forecasting

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：0.130 0.107 0.110 0.088 0.090 0.086 0.084 0.082 Exchange 192 0.271 0.230 0.243 0.226 0.284 0.182 0.182 0.177 0.174 0.172 336 0.460 0.384 0.484 0.367 0.448 0.330 0.330 0.331 0.324 0.324

[Paper](https://openreview.net/forum?id=JTtwGRACte)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Time series forecasting remains a critical challenge across numerous domains, yet the effectiveness of complex models often varies unpredictably across datasets. Recent studies highlight the surprising competitiveness of simple linear models,  suggesting that their robustness and interpretability warrant deeper theoretical investigation. This paper presents a systematic study of linear models for time series forecasting, with a focus on the role of characteristic roots in temporal dynamics. We begin by analyzing the noise-free setting, where we show that characteristic roots govern long-term behavior and explain how design choices such as instance normalization and channel independence affect model capabilities. We then extend our analysis to the noisy regime, revealing that models tend to produce spurious roots. This leads to the identification of a key data-scaling property: mitigating the influence of noise requires disproportionately large training data, highlighting the need for structural regularization. To address these challenges, we propose two complementary strategies for robust root restructuring. The first uses rank reduction techniques, including Reduced-Rank Regression (RRR) and Direct Weight Rank Reduction (DWRR), to recover the low-dimensional latent dynamics. The second, a novel adaptive method called Root Purge, encourages the model to learn a noise-suppressing null space during training. Extensive experiments on standard benchmarks demonstrate the effectiveness of both approaches, validating our theoretical insights and achieving state-of-the-art results in several settings. Our findings underscore the potential of integrating classical theories for linear systems with modern learning techniques to build robust, interpretable, and data-efficient forecasting models. The code is publicly available at: https://github.com/Wangzzzzzzzz/RootPurge.
