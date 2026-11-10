# Universal Time Series Generation with Neural Controlled Differential Equations

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：sponding dataset. Results are reported as mean ± standard deviation over five random seeds. Best scores are in bold. Method Electr. Exchange KDDCup M4 (H) Solar Traffic UberTLC Wiki2000 TSFlow 2.050±0.308 1.060±0.366 7.192±0.481 3.687±0.194 5.758±0.125 3.971±0.135 13.521±2.936 13.685±6.216 G-SLiCE 1.958±0.264 1.059±0.384 7.192±0.481 3.441±0.213 4.086±0.280 3.175±0.163 13.431±3.052 13.874±6.394

[Paper](https://openreview.net/forum?id=iqICKB71X4)

Classification / 分类：Time Series / 时间序列 → Generation & Simulation / 序列生成与仿真 → Generation / 生成

## Abstract / 摘要

Recent work on the sequence universality of State Space Models (SSMs) has introduced efficient, maximally expressive continuous-time approaches for time-series modelling. While these works focus on discriminative settings, we extend this perspective to generative time-series modelling by proving    that maximally expressive Structured Linear Controlled Differential Equations (SLiCEs) are universal time-series generators, in the sense that they can approximate the induced path laws of continuous causal pushforwards on compact latent sets in $W_\infty$. Building on these theoretical results, we propose Generative SLiCEs (G-SLiCEs), a maximally expressive continuous-time model for flow matching on path-space. Empirically, we show that expressivity improves performance in probabilistic forecasting and downstream tasks, while retaining the advantages of continuous-time models such as generalising to arbitrary observation grids. This is particularly beneficial for irregular grids, where fixed-grid models often struggle.
