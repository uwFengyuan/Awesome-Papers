# Routing Channel-Patch Dependencies in Time Series Forecasting with Graph Spectral Decomposition

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：0.209 0.083 0.203 0.083 0.206 0.081 0.202 0.088 0.205 0.083 0.201 0.107 0.234 0.103 0.228 Electricity Weather Solar-Eng. Exchange 192 0.195 0.315 0.173 0.296 0.153 0.286 0.150 0.283 0.176 0.299 0.168 0.294 0.226 0.344 0.221 0.335 336 0.343 0.421 0.304 0.399 0.289 0.404 0.266 0.386 0.301 0.397 0.297 0.392 0.367 0.448 0.356 0.439 720 0.898 0.710

[Paper](https://openreview.net/forum?id=uIPAuyno4Z)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Time series forecasting has attracted significant attention in the field of AI. Previous works have revealed that the Channel-Independent (CI) strategy improves forecasting performance by modeling each channel individually, but it often suffers from poor generalization and overlooks meaningful inter-channel interactions. Conversely, Channel-Dependent (CD) strategies aggregate all channels, which may introduce irrelevant information and lead to oversmoothing. Despite recent progress, few existing methods offer the flexibility to adaptively balance CI and CD strategies in response to varying channel dependencies. To address this, we propose a generic plugin xCPD, that can adaptively model the channel-patch dependencies from the perspective of graph spectral decomposition. Specifically, xCPD first projects multivariate signals into the frequency domain using a shared graph Fourier basis, and groups patches into low-, mid-, and high-frequency bands based on their spectral energy responses. xCPD then applies a channel-adaptive routing mechanism that dynamically adjusts the degree of inter-channel interaction for each patch, enabling selective activation of frequency-specific experts. This facilitates fine-grained input-aware modeling of smooth trends, local fluctuations, and abrupt transitions. xCPD can be seamlessly integrated on top of existing CI and CD forecasting models, consistently enhancing both accuracy and generalization across benchmarks. The code is available [https://github.com/Clearloveyuan/xCPD].
