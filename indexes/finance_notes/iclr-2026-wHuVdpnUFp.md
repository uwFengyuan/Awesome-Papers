# xRFM: Accurate, scalable, and interpretable feature learning models for tabular data

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Splitting method Dataset AGOP AGOP + TT PCA + TT RF + TT Airlines DepDelay 10M 0.9792 0.9782 0.9785 0.9785 Allstate Claims Severity 0.6480 0.6509 0.6526 0.6521 black friday 0.6879 0.6879 0.6891 0.6877 Buzzinsocialmedia Twitter 0.2300 0.2290 0.2137 0.2138 nyc-taxi-green-dec-2016 0.5268 0.5250 0.6283 0.5256 wave

[Paper](https://openreview.net/forum?id=wHuVdpnUFp)

Classification / 分类：Insurance & Actuarial / 保险与精算 → Insurance & Claims / 承保与理赔 → General / 综合

## Abstract / 摘要

Inference from tabular data, collections of continuous and categorical variables organized into matrices, is a foundation for modern technology and science. Yet, in contrast to the explosive changes in the rest of AI, the best practice for these predictive tasks has been relatively unchanged and is still primarily based on variations of Gradient Boosted Decision Trees (GBDTs). Very recently, there has been renewed interest in developing state-of-the-art methods for tabular data based on recent developments in neural networks and feature learning methods.  In this work, we introduce xRFM, an algorithm that combines feature learning kernel machines with a tree structure to both adapt to the local structure of the data and scale to essentially unlimited amounts of training data. We show that compared to $31$ other methods, including recently introduced tabular foundation models (TabPFN-v2) and GBDTs,  xRFM achieves best performance across $100$ regression datasets and is competitive to the best methods across $200$ classification datasets outperforming GBDTs. Additionally, xRFM provides  interpretability natively through the Average Gradient Outer Product.
