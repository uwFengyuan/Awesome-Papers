# Well-tuned Simple Nets Excel on Tabular Datasets

NeurIPS 2021 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：37.991 38.704 48.779 46.850 43.562 N/A 48.934 61.461 mfeat. 2000 / 217 97.750 98.000 98.000 97.500 97.250 97.250 98.000 98.000 credit-g 1000 / 21 69.405 68.095 68.929 71.191 61.190 73.095 69.643 74.643 vehicle 846 / 19 83.766 82.603 74.973 80.165 79.654 75.541 83.793 82.576 kc1 2109 / 22 70.274 72.980 66.846 63.353 52.517 55.803 67.270 74.381 adult 48842 / 15 76.893 78.520 79.824 79.830 77

[Paper](https://openreview.net/forum?id=d3k38LTDCyO)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Tabular datasets are the last "unconquered castle" for deep learning, with traditional ML methods like Gradient-Boosted Decision Trees still performing strongly even against recent specialized neural architectures. In this paper, we hypothesize that the key to boosting the performance of neural networks lies in rethinking the joint and simultaneous application of a large set of modern regularization techniques. As a result, we propose regularizing plain Multilayer Perceptron (MLP) networks by searching for the optimal combination/cocktail of 13 regularization techniques for each dataset using a joint optimization over the decision on which regularizers to apply and their subsidiary hyperparameters. We empirically assess the impact of these regularization cocktails for MLPs in a large-scale empirical study comprising 40 tabular datasets and demonstrate that (i) well-regularized plain MLPs significantly outperform recent state-of-the-art specialized neural network architectures, and (ii) they even outperform strong traditional ML methods, such as XGBoost.
