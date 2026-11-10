# REGATE: Confidence-Calibrated Integration of Temporally-Aligned Exogenous Texts for Dynamic Graphs

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Risk assessment and anomaly detection in financial interaction networks often fail under regime shifts triggered by external events such as policy changes or enforcement actions—models may retain high AUC yet suffer sharp drops in average precision and calibration.

[Paper](https://openreview.net/forum?id=hi0wCR0EYw)

Classification / 分类：Fraud & AML / 欺诈检测与反洗钱 → Payment & Transaction Fraud / 支付与交易欺诈 → General / 综合

## Abstract / 摘要

Risk assessment and anomaly detection in financial interaction networks often fail under regime shifts triggered by external events such as policy changes or enforcement actions—models may retain high AUC yet suffer sharp drops in average precision and calibration. Although news and regulatory filings contain actionable signals, naïvely injecting raw text or off-the-shelf LLM embeddings into temporal GNNs can introduce temporal leakage, misalignment, and unstable out-of-time ranking. We propose REGATE, a time-causal framework that integrates exogenous documents into dynamic graphs through three coupled components: (1) a schema-guided extractor that converts unstructured documents into auditable, time- and entity-aligned policy tokens with explicit confidence scores; (2) a bounded gating mechanism that fuses these tokens into temporal GNN states as a residual update, downweighting uncertain or stale evidence with a stability guarantee under direction consistency; and (3) a closed-loop retrieval adaptation module that distills the model's own routing attention into a lightweight document scorer without manual relevance labels. On established dynamic-graph benchmarks with documented regime shifts and six backbone architectures (TGN, TGAT, DyGFormer, GraphMixer, CTAN, GeneralDyG), REGATE yields up to +0.16 AP and up to 90% ECE reduction in post-shift windows on Elliptic; cross-domain pilots on credit and equity networks confirm consistent gains. Ablations show improvements stem from time-aligned semantic content rather than timestamps alone, and we report quality–cost trade-offs across open-source and commercial extractors.
