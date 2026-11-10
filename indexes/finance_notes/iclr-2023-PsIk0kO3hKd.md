# Spatio-temporal point processes with deep non-stationary kernels

ICLR 2023 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：first use two popular data sets containing time-stamped events with categorical marks to demonstrate the robustness of DNSK+Barrier in marked STPPs (refer to Appendix B for detailed definition and kernel modeling): (i) Financial Transactions. (Du et al., 2016). This data set contains transaction records of a stock in one day with time unit milliseconds and the action (mark) of each 9 Table 3: Results of real data sets with time and categorical marks. We compare the testing log- likelihood (Testing `, higher the better),

[Paper](https://openreview.net/forum?id=PsIk0kO3hKd)

Classification / 分类：Time Series / 时间序列 → Causality & Dynamics / 序列因果与动力学 → Foundation models / 基础模型

## Abstract / 摘要

Point process data are becoming ubiquitous in modern applications, such as social networks, health care, and finance. Despite the powerful expressiveness of the popular recurrent neural network (RNN) models for point process data, they may not successfully capture sophisticated non-stationary dependencies in the data due to their recurrent structures. Another popular type of deep model for point process data is based on representing the influence kernel (rather than the intensity function) by neural networks. We take the latter approach and develop a new deep non-stationary influence kernel that can model non-stationary spatio-temporal point processes. The main idea is to approximate the influence kernel with a novel and general low-rank decomposition, enabling efficient representation through deep neural networks and computational efficiency and better performance. We also take a new approach to maintain the non-negativity constraint of the conditional intensity by introducing a log-barrier penalty. We demonstrate our proposed method's good performance and computational efficiency compared with the state-of-the-art on simulated and real data.
