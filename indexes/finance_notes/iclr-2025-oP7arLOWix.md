# Kernel-based Optimally Weighted Conformal Time-Series Prediction

ICLR 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：eves the narrowest intervals while maintaining valid coverage. For qualitative explanations, we also include Figure A.3 that demonstrates the performance of KOWCPI, SPCI, and ACI on the Solar dataset. C.2 AAPL daily stock price We compare KOWCPI with baseline methods using Apple’s daily closing stock price data from January 1, 2020, to December 12, 2022. This publicly available dataset can be accessed on Kaggle (https: //www.kaggle.com/datasets/paultimothymooney/stock-market-data). The goal is to construct confidence intervals for the daily closing prices. The first

[Paper](https://openreview.net/forum?id=oP7arLOWix)

Classification / 分类：Time Series / 时间序列 → Probabilistic Forecasting & Calibration / 概率预测与校准 → Forecasting / 预测

## Abstract / 摘要

Conformal prediction has been a popular distribution-free framework for uncertainty quantification. In this work, we present a novel conformal prediction method for time-series, which we call Kernel-based Optimally Weighted Conformal Prediction Intervals ($\texttt{KOWCPI}$). Specifically, $\texttt{KOWCPI}$ adapts the classic Reweighted Nadaraya-Watson (RNW) estimator for quantile regression on dependent data and learns optimal data-adaptive weights. Theoretically, we tackle the challenge of establishing a conditional coverage guarantee for non-exchangeable data under strong mixing conditions on the non-conformity scores. We demonstrate the superior performance of $\texttt{KOWCPI}$ on real time-series against state-of-the-art methods, where $\texttt{KOWCPI}$ achieves narrower confidence intervals without losing coverage.
