# BRIDGE: Bootstrapping Text to Control Time-Series Generation via Multi-Agent Iterative Optimization and Diffusion Modeling

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：NN5 0.591 ± 0.029 0.628 ± 0.021 0.748 ± 0.134 1.424 ± 0.043 2.758 ± 0.142 2.121 ± 0.094 2.871 ± 0.045 Fred-MD 0.258 ± 0.045 0.271 ± 0.056 0.359 ± 0.097 2.932 ± 0.133 4.028 ± 0.130 4.026 ± 0.087 2.902 ± 0.215 Exchange 0.374 ± 0.053 0.376 ± 0.058 0.382 ± 0.041 0.993 ± 0.058 1.553 ± 0.122 1.355 ± 0.072 1.331 ± 0.042 Electricity 0.011 ± 0.010 0.014 ± 0.013 0.01

[Paper](https://openreview.net/forum?id=uRD6wkqulN)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Generation / 生成

## Abstract / 摘要

Time-series Generation (TSG) is a prominent research area with broad applications in simulations, data augmentation, and counterfactual analysis. While existing methods have shown promise in unconditional single-domain TSG, real-world applications demand for cross-domain approaches capable of controlled generation tailored to domain-specific constraints and instance-level requirements. In this paper, we argue that text can provide semantic insights, domain information and instance-specific temporal patterns, to guide and improve TSG.  We introduce ``Text-Controlled TSG'', a task focused on generating realistic time series by incorporating textual descriptions.To address data scarcity in this setting, we propose a novel LLM-based Multi-Agent framework that synthesizes diverse, realistic text-to-TS datasets. Furthermore, we introduce Bridge, a hybrid text-controlled TSG framework that integrates semantic prototypes with text description for supporting domain-level guidance. This approach achieves state-of-the-art generation fidelity on 11 of 12 datasets, and improves controllability by up to 12% on MSE and 6% MAE compared to no text input generation, highlighting its potential for generating tailored time-series data.
