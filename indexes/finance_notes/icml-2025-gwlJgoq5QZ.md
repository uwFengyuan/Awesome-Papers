# Slimming the Fat-Tail: Morphing-Flow for Adaptive Time Series Modeling

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：itor by 6.3% on average, achieving 21.7% gains fat-tailed distributions. on datasets with pronounced heavy-tailed behavior (e.g., Exchange-Rate). The MOF operates as a plug-and-play Visualization of the training process is shown in Figure 2. module, requiring no architectural modifications to existing The fat-tailed nature of Cauchy distributions (evident in the models. Q-Q plots and PDFs of Figure 2) has a significant impact on

[Paper](https://openreview.net/forum?id=gwlJgoq5QZ)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Temporal sequences, even after stationarization, often exhibit leptokurtic distributions with fat tails and persistent distribution shifts. These properties destabilize feature dynamics, amplify model variance, and hinder model convergence in time series forecasting. To address this, we propose Morphing-Flow (MoF), a framework that combines a spline-based transform layer (Flow) and a test-time-trained method (Morph), which adaptively normalizes non-stationary, fat-tailed distributions while preserving critical extreme features. MoF ensures that inputs remain within a network’s effective activation space—a structured, normal-like distribution—even under distributional drift. Experiments across eight datasets show that MoF achieves state-of-the-art performance: With a simple linear backbone architecture, it matches the performance of state-of-the-art models on datasets such as Electricity and ETTh2. When paired with a patch-based Mamba architecture, MoF outperforms its closest competitor by 6.3% on average and reduces forecasting errors in fat-tailed datasets such as Exchange by 21.7%. Moreover, MoF acts as a plug-and-play module, boosting performance in existing models without architectural changes.
