# Online Time Series Forecasting with Theoretical Guarantees

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：1 0.013 0.013 0.012 0.009 0.017 0.015 0.031 0.017 0.113 0.010 Exchange 24 0.039 0.037 0.129 0.102 0.047 0.030 0.060 0.042 0.116 0.035 48 0.043 0.042 0.267 0.195 0.062 0.039 0.065 0.051 0.168 0.040 Finally, the total loss of the proposed method can be summarized as follows: Ltotal = Ly + αLr − β(L

[Paper](https://openreview.net/forum?id=0XCZWAo7wN)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

This paper is concerned with online time series forecasting, where unknown distribution shifts occur over time, i.e., latent variables influence the mapping from historical to future observations. To develop an automated way of online time series forecasting, we propose a Theoretical framework for Online Time-series forecasting (TOT in short) with theoretical guarantees. Specifically, we prove that supplying a forecaster with latent variables tightens the Bayes risk—the benefit endures under estimation uncertainty of latent variables and grows as the latent variables achieve a more precise identifiability. To better introduce latent variables into online forecasting algorithms, we further propose to identify latent variables with minimal adjacent observations. Based on these results, we devise a model-agnostic blueprint by employing a temporal decoder to match the distribution of observed variables and two independent noise estimators to model the causal inference of latent variables and mixing procedures of observed variables, respectively. Experiment results on synthetic data support our theoretical claims. Moreover, plug-in implementations built on several baselines yield general improvement across multiple benchmarks, highlighting the effectiveness in real-world applications.
