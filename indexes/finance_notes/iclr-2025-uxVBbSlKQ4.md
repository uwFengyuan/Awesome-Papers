# Flow Matching with Gaussian Process Priors for Probabilistic Time Series Forecasting

ICLR 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：ts for different generative models and prior distributions. Best scores in bold, second best underlined. Method NFE(↓) Electr. Exchange KDDCup M4 (H) Solar Traffic UberTLC Wiki2000 TimeVAE 1 3.201±0.08 0.034±0.005 39.975±13.239 7.071±0.096 7.537±0.092 9.626±0.241 79.35±16.065 218.764±2.021 TSDiff 100 3.112±0.32 0.057±0.035 29.556±1.445 6.095±0.292 5.422±1.173 7.228±0.128 67.281±6.992 214.981±20.16 Isotropi

[Paper](https://openreview.net/forum?id=uxVBbSlKQ4)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Recent advancements in generative modeling, particularly diffusion models, have opened new directions for time series modeling, achieving state-of-the-art performance in forecasting and synthesis. However, the reliance of diffusion-based models on a simple, fixed prior complicates the generative process since the data and prior distributions differ significantly. We introduce TSFlow, a conditional flow matching (CFM) model for time series combining Gaussian processes, optimal transport paths, and data-dependent prior distributions. By incorporating (conditional) Gaussian processes, TSFlow aligns the prior distribution more closely with the temporal structure of the data, enhancing both unconditional and conditional generation. Furthermore, we propose conditional prior sampling to enable probabilistic forecasting with an unconditionally trained model. In our experimental evaluation on eight real-world datasets, we demonstrate the generative capabilities of TSFlow, producing high-quality unconditional samples. Finally, we show that both conditionally and unconditionally trained models achieve competitive results across multiple forecasting benchmarks.
