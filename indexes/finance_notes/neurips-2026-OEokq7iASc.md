# Towards Financial World Modeling

NeurIPS 2026 · main · Long

[Long] [Main] [Finance]

Financial evidence / 金融依据：Financial markets are complex, noisy environments which present unique challenges for representation learning and world modeling. / In this study, we systematically explore the application of supervised and self-supervised representation learning methods to financial markets data and their ability to learn world models of financial markets. / To support this, we assemble and release $\textbf{Market-1T}$ a dataset of more than one trillion observations spanning all US equities from 2008 through 2025. / Our results highlight that supervised methods are still dominant in this domain when applied directly to core quantitative finance tasks: predicting changes in prices, volatility, and transactions cost.

[Paper](https://openreview.net/forum?id=OEokq7iASc)

Classification / 分类：Trading & Microstructure / 交易与市场微观结构 → Market Simulation / 金融市场仿真 → General / 综合

## Abstract / 摘要

Financial markets are complex, noisy environments which present unique challenges for representation learning and world modeling. In this study, we systematically explore the application of supervised and self-supervised representation learning methods to financial markets data and their ability to learn world models of financial markets. To support this, we assemble and release $\textbf{Market-1T}$ a dataset of more than one trillion observations spanning all US equities from 2008 through 2025. We then develop a domain-specific data augmentation and apply a variety of modern SSL objectives including Joint Embedding Predictive Architecture (JEPA), Masked Autoencoder (MAE), and DINO. Our results highlight that supervised methods are still dominant in this domain when applied directly to core quantitative finance tasks: predicting changes in prices, volatility, and transactions cost. Further, when supervised models are trained across tasks they are able to leverage complementarities which enhance cross-task performance. While performance of SSL-based methods on these core tasks lags behind, we find that they better capture latent structure---such as time and assets effects---which supervised models miss. Our results suggest current SSL objectives capture broad features of markets but further work is needed to close the gap between supervised methods.
