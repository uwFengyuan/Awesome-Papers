# From Text to Forecasts: Bridging Modality Gap with Temporal Evolution Semantic Space

ICML 2026 · main · Long

[Long] [Main] [Oral] [Poster] [Finance]

Financial evidence / 金融依据：0.0125 Text helps (gain > 0) 2024], a financial dataset exhibiting pronounced non- 2.0 0.0100 Text hurts (gain < 0) stationarity, and extract real numerical sequences 1.5

[Paper](https://openreview.net/forum?id=S2Fd1GEyv6)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Incorporating textual information into time-series forecasting holds promise for addressing event-driven non-stationarity; however, a fundamental modality gap hinders effective fusion: textual descriptions express temporal impacts implicitly and qualitatively, whereas forecasting models rely on explicit and quantitative signals. Through controlled semi-synthetic experiments, we show that existing methods over-attend to redundant tokens and struggle to reliably translate textual semantics into usable numerical cues. To bridge this gap, we propose \method{}, which introduces a Temporal Evolution Semantic Space as an intermediate bottleneck between modalities. This space consists of interpretable, numerically grounded temporal primitives—mean shift, volatility, shape, and lag—extracted from text by an LLM via structured prompting and filtered through confidence-aware gating. Experiments on four real-world datasets demonstrate up to a 29\% reduction in forecasting error compared to state-of-the-art uni-modal and multimodal baselines. The code is available at https://anonymous.4open.science/r/MMTSF.
