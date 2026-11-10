# TimeInf: Time Series Data Contribution via Influence Functions

ICLR 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：a less rapid decrease or even an increase in performance. Alabama State. The Electricity dataset includes the electricity consumption patterns of 321 clients from 2012 to 2014 (Trindade, 2015). The Exchange Rate dataset includes daily exchange rates for 8 countries, covering the period from 1990 to 2016 (Lai et al., 2018). Baselines. For each block in the training dataset, we assess its impact by averaging the score Iblock from Equation (4) across all blocks in the validation set. We fix the block length as 100. For anomaly detection, standard methods are available, but for data pruning, no established method exists. Theref

[Paper](https://openreview.net/forum?id=Vz0CWFMPUe)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Anomaly detection / 异常检测

## Abstract / 摘要

Evaluating the contribution of individual data points to a model's prediction is critical for interpreting model predictions and improving model performance. Existing data contribution methods have been applied to various data types, including tabular data, images, and text; however, their primary focus has been on i.i.d. settings. Despite the pressing need for principled approaches tailored to time series datasets, the problem of estimating data contribution in such settings remains under-explored, possibly due to challenges associated with handling inherent temporal dependencies. This paper introduces TimeInf, a model-agnostic data contribution estimation method for time-series datasets. By leveraging influence scores, TimeInf attributes model predictions to individual time points while preserving temporal structures between the time points. Our empirical results show that TimeInf effectively detects time series anomalies and outperforms existing data attribution techniques as well as state-of-the-art anomaly detection methods. Moreover, TimeInf offers interpretable attributions of data values, allowing us to distinguish diverse anomalous patterns through visualizations. We also showcase a potential application of TimeInf in identifying mislabeled anomalies in the ground truth annotations.
