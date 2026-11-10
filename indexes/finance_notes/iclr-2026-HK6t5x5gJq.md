# FeDaL: Federated Dataset Learning for General Time Series Foundation Models

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Dataset # Channels Frequency Length Bitcoin 18 Daily Min: 2659 Max: 4581 Economic FRED-MD 107 Monthly Fixed: 728 NN5 111 Daily Fixed: 791 Pedestrain Counts 66 Hourly Min: 576 Max: 96424 Transport Rideshare 2304 Daily Fixed: 541 San Francisco Traffic 862

[Paper](https://openreview.net/forum?id=HK6t5x5gJq)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Foundation models / 基础模型

## Abstract / 摘要

Dataset-level heterogeneity introduces significant domain biases that fundamentally degrade generalization on general Time Series Foundation Models (TSFMs), yet this challenge remains underexplored. This paper rethinks the from-scratch training of TSFMs using the paradigm of federated learning. We propose a novel Federated Dataset Learning (**FeDaL**) approach to tackle heterogeneous time series by learning dataset-agnostic temporal representations. Specifically, the distributed architecture of federated learning is a nature solution to decompose heterogeneous TS datasets into shared generalized knowledge and preserved personalized knowledge. Moreover, based on the TSFM architecture, FeDaL explicitly mitigates both local and global biases by adding two complementary mechanisms: Domain Bias Elimination (DBE) and Global Bias Elimination (GBE). FeDaL`s cross-dataset generalization has been extensively evaluated in real-world datasets spanning eight tasks (including various regression and classification), against 54 baselines. We further analyze federated scaling behavior, showing how data volume, client count, and join rate affect model performance under decentralization. Our code is publicly available at https://github.com/shengchaochen82/FeDaL.
