# Error-quantified Conformal Inference for Time Series

ICLR 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：riginal papers and open-source codes. Overview of experimental results. We have conducted extensive experiments, including stock data in Section 4.2, electricity data in Section 4.3, climate data in Section 4.4, syn- thetic data in Section 4.5, and ablation study of hyperparameters in Section D. Experimen- tal results with Transformer as the base model can be found in Section F. More com- prehensive experimental results and discussion on the scorecaster and learning rates can be found in Section G. Our code is available at https://github.com/creator-xi/ Error-quantified-Conformal-Inference. 4.2 R ESULTS IN FINANCE DOMAIN We consider the uncertainty problem of forecasting stock prices, including Amazon (AMZN) and Google (GOOGL), collected over 

[Paper](https://openreview.net/forum?id=RD9q5vEe1Q)

Classification / 分类：Time Series / 时间序列 → Probabilistic Forecasting & Calibration / 概率预测与校准 → Forecasting / 预测

## Abstract / 摘要

Uncertainty quantification in time series prediction is challenging due to the temporal dependence and distribution shift on sequential data. Conformal prediction provides a pivotal and flexible instrument for assessing the uncertainty of machine learning models through prediction sets. Recently, a series of online conformal inference methods updated thresholds of prediction sets by performing online gradient descent on a sequence of quantile loss functions. A drawback of such methods is that they only use the information of revealed non-conformity scores via miscoverage indicators but ignore error quantification, namely the distance between the non-conformity score and the current threshold. To accurately leverage the dynamic of miscoverage error, we propose Error-quantified Conformal Inference (ECI) by smoothing the quantile loss function. ECI introduces a continuous and adaptive feedback scale with the miscoverage error, rather than simple binary feedback in existing methods. We establish a long-term coverage guarantee for ECI under arbitrary dependence and distribution shift. The extensive experimental results show that ECI can achieve valid miscoverage control and output tighter prediction sets than other baselines.
