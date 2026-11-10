# Differencing the Diffusion Trajectory toward Uncertain Components for Time Series Forecasting

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：erve as the forecast sample. 4 Experiment Settings 4.1 Datasets We evaluate on seven widely used time series datasets spanning diverse temporal character- istics, namely Electricity, ETTm2 [61], Exchange Rate, Traffic, Solar-Energy [62], Weather [63], and Wind [23]. Each dataset is split chronologically into training, validation, and test sets following standard forecasting protocol, with a ratio of 6:2:2 for ETTm2 and 7:1:2 for the remaining six datasets. Following the prior studies [44, 63], we use a lookback length L = 96 for both D IFF D IFF and all baselines, and evaluate across four prediction horizons H ∈ {96, 192

[Paper](https://openreview.net/forum?id=EQ3rr1gzcl)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Diffusion models have become a widely used framework for probabilistic time series forecasting, modeling the distribution of future values given an observed history. In time series forecasting, however, the future continues the observed history, creating an asymmetry the standard diffusion process leaves unaddressed, with slowly-varying content largely determined by the observed continuity while higher-frequency dynamics carry most of the residual uncertainty. Existing diffusion-based forecasters decouple this asymmetry through an external rule before generation, leaving the corruption trajectory blind to which parts of the target the history can already anchor. We propose \textsc{DiffDiff}, a diffusion framework that embeds this predictability asymmetry into the diffusion trajectory itself, so that a single end-to-end diffusion process becomes aware of which parts of the target the history can already anchor. \textsc{DiffDiff} makes the forward operator step-dependent so that the noisy intermediate state progressively shifts from the target itself toward its second-order differenced structure, while a conditioning pathway supplies the denoiser with both value-domain and differential history information balanced by a stage-adaptive gate at each diffusion step. The terminal distribution approaches a standard Gaussian, preserving compatibility with existing samplers. On seven benchmarks across four prediction horizons, \textsc{DiffDiff} outperforms six diffusion baselines, and our analysis confirms that \textsc{DiffDiff} concentrates the diffusion's generative effort on the most uncertain components of the target while relieving it from rebuilding the history-anchored content.
