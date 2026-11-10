# Fortifying Time Series: DTW-Certified Robust Anomaly Detection

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：44 0.830 0.227 2.242 0.196 71.05% COUTA 0.192 0.900 0.003 0.300 0.232 0.450 0.046 99.86% NIPS-TS-CREDITCARD TimesNet 0.422 0.942 0.450 0.846 0.028 0.262 0.035 51.75% DeepSVDDTS 0.132 0.772 0.119 0.719 0.105 0.817 0.056 91.55% COUTA 0.515 0.537 0.598 0.989 0.070 0.359 0.034 95.18% NIPS-TS-WATER TimesNet 0.778 0.997

[Paper](https://openreview.net/forum?id=lG82mcrKJf)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Anomaly detection / 异常检测

## Abstract / 摘要

Time-series anomaly detection is critical for ensuring safety in high-stakes applications, where robustness is a fundamental requirement rather than a mere performance metric. Addressing the vulnerability of these systems to adversarial manipulation is therefore essential. Existing defenses are largely heuristic or provide certified robustness only under $\ell_p$-norm constraints, which are incompatible with time-series data. In particular, $\ell_p$-norm fails to capture the intrinsic temporal structure in time series, causing small temporal distortions to significantly alter the $\ell_p$-norm measures. Instead, the similarity metric Dynamic Time Warping (DTW) is more suitable and widely adopted in the time-series domain, as DTW accounts for temporal alignment and remains robust to temporal variations. To date, however, there has been no certifiable robustness result in this metric that provides guarantees. In this work, we introduce the first DTW-certified robust defense in time-series anomaly detection by adapting the randomized smoothing paradigm. We develop this certificate by bridging the $\ell_p$-norm to DTW distance through a lower-bound transformation. Extensive experiments across various datasets and models validate the effectiveness and practicality of our theoretical approach. Results demonstrate significantly improved performance, e.g., up to 18.7\% in F1-score under DTW-based adversarial attacks compared to traditional certified models.
