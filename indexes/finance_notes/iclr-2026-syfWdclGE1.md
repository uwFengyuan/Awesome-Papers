# The Forecast After the Forecast: A Post-Processing Shift in Time Series

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：0.220 0.301 6% 0.224 0.302 5% 0.517 0.344 0.492 0.329 5% 0.492 0.325 5% Exchange 0.249 0.332 0.241 0.332 2% 0.235 0.329 3% 0.094 0.213 0.090 0.206 3% 0.092 0.210 1% Weather 0.427 0.463 0.025 0.005 96% 0.039 0.059 89% 0.150 0.196 0.148 0.193 2% 0.143 0.191 4% ETTm1 0.121 0.217 0.078 0.190 24% 0.087 0

[Paper](https://openreview.net/forum?id=syfWdclGE1)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Time series forecasting has long been dominated by advances in model architecture, with recent progress driven by deep learning and hybrid statistical techniques. However, as forecasting models approach diminishing returns in accuracy, a critical yet underexplored opportunity emerges: the strategic use of post-processing. In this paper, we address the last-mile gap in time-series forecasting, which is to improve accuracy and uncertainty without retraining or modifying a deployed backbone. We propose $\delta$-Adapter, a lightweight, architecture-agnostic way to boost deployed time series forecasters without retraining. $\delta$-Adapter learns tiny, bounded modules at two interfaces: input nudging (soft edits to covariates) and output residual correction. We provide local descent guarantees, $O(\delta)$ drift bounds, and compositional stability for combined adapters. Meanwhile, it can act as a feature selector by learning a sparse, horizon-aware mask over inputs to select important features, thereby improving interpretability. In addition, it can also be used as a distribution calibrator to measure uncertainty. Thus, we introduce a Quantile Calibrator and a Conformal Corrector that together deliver calibrated, personalized intervals with finite-sample coverage.   Our experiments across diverse backbones and datasets show that $\delta$-Adapter improves accuracy and calibration with negligible compute and no interface changes.
