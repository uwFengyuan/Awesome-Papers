# To See Far, Look Close: Evolutionary Forecasting for Long-term Time Series

NeurIPS 2026 · main · Long

[Long] [Main] [Finance]

Financial evidence / 金融依据：6 To See Far, Look Close: Evolutionary Forecasting for Long-term Time Series ETTh1 Exchange Traffic ETTh1 Exchange Traffic Win Ratio 93.75% 96.87% 93.75% 81.25% 87.50% 87.50% ETTh2

[Paper](https://openreview.net/forum?id=PFfOPbcZCE)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

The prevailing Direct Forecasting (DF) paradigm dominates Long-term Time Series Forecasting (LTSF) by forcing models to predict the entire future horizon in a single forward pass. While efficient, this rigid coupling of output and evaluation horizons necessitates computationally prohibitive re-training for every target horizon. In this work, we uncover a counter-intuitive optimization anomaly: models trained on short horizons—when coupled with our proposed Evolutionary Forecasting (EF) paradigm—significantly outperform those trained directly on long horizons. We attribute this success to the mitigation of a fundamental optimization pathology inherent in DF, where conflicting gradients from distant futures cripple the learning of local dynamics. We establish EF as a unified generative framework, proving that DF is merely a degenerate special case of EF. Extensive experiments demonstrate that a singular EF model surpasses task-specific DF ensembles across standard benchmarks and exhibits robust asymptotic stability in extreme extrapolation. This work propels a paradigm shift in LTSF: moving from passive Static Mapping' to autonomous Evolutionary Reasoning.
