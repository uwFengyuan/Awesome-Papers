# Diffusion Transformers for Tabular Data Time Series Generation

ICLR 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：n tasks and different metrics. More details are provided in App. C and E. Datasets. We use six public datasets, whose statistics are provided in App. E. Age1, Age2, Leaving, taken from (Fursov et al., 2021), and PKDD’99 Financial Dataset, taken from (Berka, 1999), are composed of bank transaction time series of different real banks with different attributes. Each time 7 Published as a conference paper at ICLR 2025 series is the temporally ordered sequence of bank transactions of a given bank client. On the othe

[Paper](https://openreview.net/forum?id=bhOysNJvWm)

Classification / 分类：Time Series / 时间序列 → Generation & Simulation / 序列生成与仿真 → Generation / 生成

## Abstract / 摘要

Tabular data generation has recently attracted a growing interest due to its different application scenarios. However, generating time series of tabular data, where each element of the series depends on the others,remains a largely unexplored domain. This gap is probably due to the difficulty of jointly solving different problems, the main of which are the heterogeneity of tabular data (a problem common to non-time-dependent approaches) and the variable length of a time series.In this paper, we propose a Diffusion Transformers (DiTs) based approach for tabular data series generation. Inspired by the recent success of DiTs in image and video generation, we extend this framework to deal with heterogeneous data and variable-length sequences. Using extensive experiments on six datasets, we show that the proposed approach  outperforms previous work by a large margin.
