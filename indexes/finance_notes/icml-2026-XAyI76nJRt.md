# Beyond Extrapolation: Knowledge Utilization Paradigm with Bidirectional Inspiration for Time Series Forecasting

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：ILI 2.347 1.089 2.336 1.086 2.292 1.069 1.580 0.852 1.520 0.825 1.496 0.807 2.438 0.955 2.328 0.984 2.114 0.900 1.383 0.718 1.366 0.713 1.365 0.712 Exchange 0.369 0.418 0.362 0.416 0.313 0.390 0.394 0.426 0.390 0.418 0.371 0.410 0.415 0.440 0.399 0.434 0.383 0.427 0.364 0.403 0.363 0.403 0.358 0.402 making its effect more sensitive to the backbone–horizon Table 2. Performance comparison of retrieval-based continuation construction and PBCC on the ETT datasets with a DL

[Paper](https://openreview.net/forum?id=XAyI76nJRt)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Time-series forecasting is critical in various scenarios, such as energy, transportation, and public health.   However, most existing forecasters rely primarily on one-way inference, \textit{i.e.}, mapping \textbf{history} to \textbf{target}, and overlook the structural information provided by a revised natural chain (``\textbf{history} (model input) --  \textbf{target} (ground-truth output)  --  \textbf{post-target continuation}''). The post-target continuation records how trajectories evolve after the target, which can help stabilize forecasting, but it is not observable at inference time. In this work, we aim to obtain an approximate proxy of the post-target continuation for the current input, providing structural knowledge for bidirectional forecasting. This idea is instantiated as KUP-BI (Knowledge Utilization Paradigm with Bidirectional Inspiration), a new time-series modeling paradigm that distills continuation-style knowledge (as an approximate post-target continuation proxy) from a \emph{train-only} historical library and integrates it into standard forecasting backbones. The input stream and the continuation-proxy stream are fused via a lightweight feature-level gating module. This design does not introduce information beyond what is already contained in the training trajectories; instead, it provides a structured inductive bias that helps backbones exploit typical continuation patterns rather than relying solely on parametric extrapolation. Experimental results on six public datasets show that KUP-BI consistently improves the forecasting performance of state-of-the-art models, with small additional overhead.
