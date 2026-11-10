# AdaST: Adaptive Coupling for Spatial-Temporal Forecasting

NeurIPS 2026 · main · Long

[Long] [Main] [Finance]

Financial evidence / 金融依据：16 C Additional Main Results We conduct additional experiments on three diverse dataset categories to further validate AdaST’s generalizability: ExchangeRate (financial), ETTh1 (energy), and METR-LA (highway traffic). We ex- pand the baseline comparison to include two state-of-the-art time-series-only methods, PatchTST [24] and DLinear [45]. For spatial-temporal baselines that require a predefined graph structure, we only compare against STID, HimNet, and STNorm, which operate without predefined graphs. Since som

[Paper](https://openreview.net/forum?id=2IWnVy1qoe)

Classification / 分类：Market Prediction / 股价、收益与波动率预测 → FX & Crypto Forecasts / 汇率与加密资产预测 → General / 综合

## Abstract / 摘要

Spatial-temporal (ST) forecasting underpins many real-world systems such as traffic, climate, and energy networks. While existing methods implicitly assume strong spatiotemporal coupling, we observe that real-world ST data exhibits distinct coupling regimes, ranging from temporal-dominated and spatial-dominated to strongly coupled patterns. This mismatch causes current models to suffer from spurious dependencies and degraded performance when one correlation dominates. To overcome this limitation, we aim to dynamically modulate spatial and temporal modeling based on the data's inherent coupling structure. However, three key challenges exist: unknown coupling structure, heterogeneous coupling dynamics, and suboptimal spatial modeling. We propose AdaST, an adaptive ST forecasting framework that tackles these challenges through a decompose-recompose paradigm. AdaST factorizes inputs into components capturing different coupling patterns using heterogeneity-aware experts. Each component is processed by role-aligned modules, and a correlation-informed adaptive recomposer integrates them for final prediction. Extensive experiments confirm that AdaST significantly outperforms state-of-the-art baselines, validating the necessity of an adaptive approach.
