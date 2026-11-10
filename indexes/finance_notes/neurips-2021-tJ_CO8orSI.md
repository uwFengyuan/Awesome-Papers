# Adjusting for Autocorrelated Errors in Neural Networks for Time Series

NeurIPS 2021 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：M4-competition (M4-Yearly, M4-Quarterly, M4-Monthly, M4-Weekly, M4-Daily, M4- Hourly) [42]: re-arranged data from the M4-competition where each dataset consists of series from microeconomics, macroeconomics, financial, industry, demographic, and other. M4-Hourly is used in Conv-T. 6 Table 2: RRMSE for the best grid-searched hyperparameters averaged over ten runs. Best performance in boldface and is superscribed with † if the p-value of paired t-test is lower

[Paper](https://openreview.net/forum?id=tJ_CO8orSI)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

An increasing body of research focuses on using neural networks to model time series. A common assumption in training neural networks via maximum likelihood estimation on time series is that the errors across time steps are uncorrelated. However, errors are actually autocorrelated in many cases due to the temporality of the data, which makes such maximum likelihood estimations inaccurate. In this paper, in order to adjust for autocorrelated errors, we propose to learn the autocorrelation coefficient jointly with the model parameters. In our experiments, we verify the effectiveness of our approach on time series forecasting. Results across a wide range of real-world datasets with various state-of-the-art models show that our method enhances performance in almost all cases. Based on these results, we suggest empirical critical values to determine the severity of autocorrelated errors. We also analyze several aspects of our method to demonstrate its advantages. Finally, other time series tasks are also considered to validate that our method is not restricted to only forecasting.
