# CATCH: Channel-Aware Multivariate Time Series Anomaly Detection via Frequency Patching

ICLR 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Machine 38 2.08 1,416,825 708,420 Telemetry dataset collected from 28 different server machines at a large Internet company Creditcard Finance 29 0.17 284,807 142,404 Credit card dataset includes a subset of online transactions that occurred over two days GECCO Water treatment 9 1.25 138,521 69,261 Water quality dataset published in the GECCO Industrial Challenge SWAT Water treatment 51 5.78 944,919 449,919 Obtained from 51 sensors of the critical infrastructure

[Paper](https://openreview.net/forum?id=m08aK3xxdJ)

Classification / 分类：Time Series / 时间序列 → Anomaly Detection / 序列异常检测 → Anomaly detection / 异常检测

## Abstract / 摘要

Anomaly detection in multivariate time series is challenging as heterogeneous subsequence anomalies may occur. Reconstruction-based methods, which focus on learning normal patterns in the frequency domain to detect diverse abnormal subsequences, achieve promising results, while still falling short on capturing fine-grained frequency characteristics and channel correlations. To contend with the limitations, we introduce CATCH, a framework based on frequency patching. We propose to patchify the frequency domain into frequency bands, which enhances its ability to capture fine-grained frequency characteristics. To perceive appropriate channel correlations, we propose a Channel Fusion Module (CFM), which features a patch-wise mask generator and a masked-attention mechanism. Driven by a bi-level multi-objective optimization algorithm, the CFM is encouraged to iteratively discover appropriate patch-wise channel correlations, and to cluster relevant channels while isolating adverse effects from irrelevant channels. Extensive experiments on 10 real-world datasets and 12 synthetic datasets demonstrate that CATCH achieves state-of-the-art performance. We make our code and datasets available at https://github.com/decisionintelligence/CATCH.
