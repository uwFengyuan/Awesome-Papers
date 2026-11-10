# Has the Deep Neural Network learned the Stochastic Process? An Evaluation Viewpoint

ICLR 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Empirical experiments on synthetic datasets, including wildfire, host-pathogen, and stock market models, demonstrate that ECE uniquely captures F2SP.

[Paper](https://openreview.net/forum?id=2U8owdruSQ)

Classification / 分类：Time Series / 时间序列 → Financial Stochastic Processes / 金融随机过程 → Forecasting / 预测

## Abstract / 摘要

This paper presents the first systematic study of evaluating Deep Neural Networks (DNNs) designed to forecast the evolution of stochastic complex systems. We show that traditional evaluation methods like threshold-based classification metrics and error-based scoring rules assess a DNN's ability to replicate the observed ground truth but fail to measure the DNN's learning of the underlying stochastic process. To address this gap, we propose a new evaluation criteria called _Fidelity to Stochastic Process (F2SP)_, representing the DNN's ability to predict the system property _Statistic-GT_—the ground truth of the stochastic process—and introduce an evaluation metric that exclusively assesses F2SP. We formalize F2SP within a stochastic framework and establish criteria for validly measuring it. We formally show that Expected Calibration Error (ECE) satisfies the necessary condition for testing F2SP, unlike traditional evaluation methods. Empirical experiments on synthetic datasets, including wildfire, host-pathogen, and stock market models, demonstrate that ECE uniquely captures F2SP. We further extend our study to real-world wildfire data, highlighting the limitations of conventional evaluation and discuss the practical utility of incorporating F2SP into model assessment. This work offers a new perspective on evaluating DNNs modeling complex systems by emphasizing the importance of capturing underlying the stochastic process.
