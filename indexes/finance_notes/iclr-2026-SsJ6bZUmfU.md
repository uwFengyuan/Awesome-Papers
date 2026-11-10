# From Samples to Scenarios: A New Paradigm for Probabilistic Forecasting

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：future, in datasets containing similar histories but diverse futures. Table 3: Inference FLOPs. FLOPs required to generate S forecast samples on the Exchange dataset with batch size = 1. The cost for TimeMCL and TimePrism is constant as they produce all scenarios in a single forward pass. Sampling S DeepAR TimeGrad TempFlow Trf.Flow TACTiS-2 TimeMCLTimePrism 1 2.9 × 104 1.9 × 108 5.8 × 106 1.4 × 107 2.5 × 107 10 2.9 × 105 1.9 × 109 5.8 × 107 1.3 × 108 1.2 × 108 8.8 × 106 5.1 × 105 100 2.9 × 106 1.9 × 1010 5.8 × 108 1.3

[Paper](https://openreview.net/forum?id=SsJ6bZUmfU)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Most state-of-the-art probabilistic time series forecasting models rely on sampling to represent future uncertainty. However, this paradigm suffers from inherent limitations, such as lacking explicit probabilities, inadequate coverage, and high computational costs. In this work, we introduce **Probabilistic Scenarios**, an alternative paradigm designed to address the limitations of sampling. It operates by directly producing a finite set of {Scenario, Probability} pairs, thus avoiding Monte Carlo-like approximation. To validate this paradigm, we propose **TimePrism**, a simple model composed of only three parallel linear layers. Surprisingly, TimePrism achieves 9 out of 10 state-of-the-art results across five benchmark datasets on two metrics. The effectiveness of our paradigm comes from a fundamental reframing of the learning objective. Instead of modeling an entire continuous probability space, the model learns to represent a set of plausible scenarios and corresponding probabilities. Our work demonstrates the potential of the Probabilistic Scenarios paradigm, opening a promising research direction in forecasting beyond sampling.
