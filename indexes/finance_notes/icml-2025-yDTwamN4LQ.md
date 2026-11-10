# Learning with Expected Signatures: Theory and Applications

ICML 2025 · main · Long

[Long] [Main] [Oral] [Poster] [Finance]

Financial evidence / 金融依据：H -D EPENDENT D ERIVATIVES Figure 2. Distributions of expected signature estimators for BM. The next application we consider is a purely financial one. The y-axis is in log-scale. The objective is to price (and hedge) path-dependent deriva- tives by decomposing them into a set of atomic Arrow- 10 In both simulations we fix T = 1 and consider π to be uniform Debreu-like securities. Let X = {Xt , t ∈ [0, T ]} be a price with mesh |π| = 2−⌊N/10⌋+1 . This choice ensures the sequences process, i.e. a semimartingale over some probability space. of partitions are signature-defining for both processes

[Paper](https://openreview.net/forum?id=yDTwamN4LQ)

Classification / 分类：Time Series / 时间序列 → General Time-Series Methods / 综合序列方法 → Foundation models / 基础模型

## Abstract / 摘要

The expected signature maps a collection of data streams to a lower dimensional representation, with a remarkable property: the resulting feature tensor can fully characterize the data generating distribution. This "model-free"' embedding has been successfully leveraged to build multiple domain-agnostic machine learning (ML) algorithms for time series and sequential data. The convergence results proved in this paper bridge the gap between the expected signature's empirical discrete-time estimator and its theoretical continuous-time value, allowing for a more complete probabilistic interpretation of expected signature-based ML methods. Moreover, when the data generating process is a martingale, we suggest a simple modification of the expected signature estimator with significantly lower mean squared error and empirically demonstrate how it can be effectively applied to improve predictive performance.
