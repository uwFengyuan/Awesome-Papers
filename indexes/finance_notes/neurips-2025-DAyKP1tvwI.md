# OLinear: A Linear Model for Time Series Forecasting in Orthogonally Transformed Domain

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Datasets and implementation details We extensively evaluate OLinear using 24 diverse real- world datasets: ETT (four subsets), Weather, ECL, Traffic, Exchange, Solar-Energy, PEMS (four subsets), ILI, COVID-19, METR-LA, NASDAQ, Wiki, SP500, DowJones, CarSales, Power, Website, Unemp. The weighted L1 loss function from CARD [Wang et al., 2024b] is adopted. The embedding size d is set as 16. Dataset description and more implementation details are presented in Appendices C and D, respectively. 5.1 Forecasting performance Baselines We carefully choose 11 well-acknowledg

[Paper](https://openreview.net/forum?id=DAyKP1tvwI)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

This paper presents $\mathbf{OLinear}$, a $\mathbf{linear}$-based multivariate time series forecasting model that operates in an $\mathbf{o}$rthogonally transformed domain. Recent forecasting models typically adopt the temporal forecast (TF) paradigm, which directly encode and decode time series in the time domain. However, the entangled step-wise dependencies in series data can hinder the performance of TF. To address this, some forecasters conduct encoding and decoding in the transformed domain using fixed, dataset-independent bases (e.g., sine and cosine signals in the Fourier transform). In contrast, we propose $\mathbf{OrthoTrans}$, a data-adaptive transformation based on an orthogonal matrix that diagonalizes the series' temporal Pearson correlation matrix. This approach enables more effective encoding and decoding in the decorrelated feature domain and can serve as a plug-in module to enhance existing forecasters. To enhance the representation learning for multivariate time series, we introduce a customized linear layer, $\mathbf{NormLin}$, which employs a normalized weight matrix to capture multivariate dependencies. Empirically, the NormLin module shows a surprising performance advantage over multi-head self-attention, while requiring nearly half the FLOPs. Extensive experiments on 24 benchmarks and 140 forecasting tasks demonstrate that OLinear consistently achieves state-of-the-art performance with high efficiency. Notably, as a plug-in replacement for self-attention, the NormLin module consistently enhances Transformer-based forecasters. The code and datasets are available at https://github.com/jackyue1994/OLinear.
