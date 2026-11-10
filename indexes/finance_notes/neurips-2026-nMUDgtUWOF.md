# Hermes: A Multi-Scale Spatial-Temporal Hypergraph Network for Stock Time Series Forecasting

NeurIPS 2026 · main · Long

[Long] [Main] [Finance]

Financial evidence / 金融依据：Time series forecasting occurs in a range of financial applications providing essential decision-making support to investors, regulatory institutions, and analysts. / Unlike multivariate time series from other domains, stock time series exhibit industry correlation. / This study proposes the \textbf{Hermes} framework for stock time series forecasting that aims to improve the exploitation of industry correlation by addressing these limitations. / Experimental results on multiple real-world stock datasets show that Hermes outperforms existing state-of-the-art methods.

[Paper](https://openreview.net/forum?id=nMUDgtUWOF)

Classification / 分类：Market Prediction / 股价、收益与波动率预测 → Stock Movement & Returns / 股价方向与收益预测 → General / 综合

## Abstract / 摘要

Time series forecasting occurs in a range of financial applications providing essential decision-making support to investors, regulatory institutions, and analysts. Unlike multivariate time series from other domains, stock time series exhibit industry correlation. Exploiting this kind of correlation can improve forecasting accuracy. However, existing methods based on hypergraphs can only capture industry correlation relatively superficially. These methods face two key limitations: they do not fully consider inter-industry lead-lag interactions, and they do not model multi-scale information within and among industries. This study proposes the \textbf{Hermes} framework for stock time series forecasting that aims to improve the exploitation of industry correlation by addressing these limitations. The framework integrates moving aggregation and  multi-scale fusion modules in a hypergraph network. Specifically, to more flexibly capture the lead-lag relationships among industries, Hermes proposes a hyperedge-based moving aggregation module. This module incorporates a sliding window and utilizes dynamic temporal aggregation operations to consider lead-lag dependencies among industries. Additionally, to effectively model multi-scale information, Hermes employs cross-scale, edge-to-edge message passing to integrate information from different scales while maintaining the consistency of each scale. Experimental results on multiple real-world stock datasets show that Hermes outperforms existing state-of-the-art methods.
