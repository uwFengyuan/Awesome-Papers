# TimeLAVA: Learning-Agnostic Valuation for Time Series Data

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：VA’s effective perfor- 0.4 0.4 mance in both data quality assessment and noise detection on the Exchange dataset. In the data pruning experiment 0.2 0.2 (left), T IME LAVA maintains the highest R2 as low-value 0.0 0.0 0.05 0.10 0.15 0.20 0.05 0.10 0.15 0.20 segments are removed, with performan

[Paper](https://openreview.net/forum?id=g5Id7eZRal)

Classification / 分类：Time Series / 时间序列 → General Time-Series Methods / 综合序列方法 → Anomaly detection / 异常检测

## Abstract / 摘要

Data valuation quantifies the intrinsic quality of individual samples to enable principled data curation, quality control, and robust learning. For time series in critical domains such as healthcare, finance, and industrial monitoring, effective valuation methods are essential yet fundamentally lacking. Existing approaches are either model-dependent, limiting their generalizability, or designed for i.i.d. data and thus fail to capture temporal dependencies, multi-scale patterns, and non-stationary dynamics inherent to sequential data. We introduce TimeLAVA, a learning-agnostic framework that values temporal segments by their marginal contribution to minimizing distributional discrepancy between evaluated and reference data. At its core is a novel Selective Wavelet-based Wasserstein ($\mathcal{W}_\text{SW}$) discrepancy combining multi-scale wavelet transforms for temporal localization with unbalanced optimal transport for robustness to distributional shifts. Segment values are efficiently computed via sensitivity analysis without requiring model training and aggregated into point-wise scores. We provide theoretical guarantees linking valuation to model-agnostic generalization and prove bounded sensitivity to outlier contamination. Extensive experiments across anomaly detection, data pruning, and label noise detection demonstrate that TimeLAVA produces significantly more informative value scores than existing methods on diverse real-world datasets.
