# CombinationTS: A Modular Framework for Understanding Time-Series Forecasting Models

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：generalization. On Multi-Scale Downsampling, and Residual Cycle Forecast- the volatile Exchange-Rate dataset, Identity-based models ing—with RevIN as the shared normalization baseline. (PatchLinear) still achieve the lowest average MSE (Ta- ble 19), ruling out benchmark periodicity as a confound.

[Paper](https://openreview.net/forum?id=CwHRT46VmC)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Recent progress in time-series forecasting has led to rapidly increasing architectural complexity, yet many reported State-of-the-Art gains are statistically fragile or misattributed. We argue that progress requires a shift from model selection to modular attribution, identifying which components truly drive performance. We propose CombinationTS, a self-contained probabilistic evaluation framework grounded in Evaluatology, the science of uncovering the effects. It decomposes forecasting models into orthogonal modules—Input Transformation, Embedding, Encoder, Decoder, and Output Transformation—and evaluates them under a shared evaluation condition space. By quantifying each component via marginalized performance ($\mu$) and stability ($\sigma$), CombinationTS enables robust attribution beyond fragile point estimates. Through large-scale paired evaluation, we uncover the Identity Paradox: once the data view (Embedding) is well-designed, a parameter-free Identity Encoder often matches or outperforms complex backbones.
