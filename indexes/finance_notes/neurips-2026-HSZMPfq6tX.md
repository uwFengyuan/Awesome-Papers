# ForecastCompass: Guiding Agentic Forecasting with Adaptive Factor Memory

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：, 2025]. Both datasets contain time-evolving forecasting questions across a broad range of domains, such as sports, technology, and finance. For each dataset, we select the latest five weeks of data to construct, update, and evaluate memory. This setting reflects the dynamic nature of agentic forecasting, where memory is built from recent resolved questions and revised as new weekly outcomes become available. The detailed data statistics is in the Appendix A.1. We follow a chronological evaluation protocol: memory is constructed only from previously resolved questions and is used to forecast future unresolved questions. This prevents post-resolution information from leaking into the current forecast. Evaluation metrics. We use Brier score [Glenn et 

[Paper](https://openreview.net/forum?id=HSZMPfq6tX)

Classification / 分类：Financial Agents / 金融Agent与决策 → Investment & Financial Research Agents / 投研与金融决策Agent → General / 综合

## Abstract / 摘要

Agentic forecasting is important for decision-making in dynamic environments, but it remains challenging because agents must reason from incomplete, time-limited evidence and produce calibrated probabilities before outcomes are resolved. Memory provides a natural mechanism for transferring experience from resolved forecasts to future prediction tasks. However, existing agent-memory methods are not tailored to forecasting, as they typically store past interactions, reflections, or factual associations without explicitly representing reusable predictive factors or calibration knowledge.  We propose ForecastCompass(FoCo), an adaptive factor-based memory framework for agentic forecasting. FoCo organizes forecasting experience with a hierarchical forecasting-task taxonomy, enabling retrieval task-relevant forecasting knowledge. It maintains two complementary memory components: factor memory, which captures reusable predictive dimensions, and reasoning memory, which encodes probability updating, uncertainty handling, and calibration principles. Using retrospective analyses as learning signals, FoCo iteratively revises memory through a verbalized memory-revision procedure, enabling the agent to accumulate transferable forecasting knowledge over time. Experiments on Prophet Arena and FutureX with GPT-5-mini and Gemini-2.5-Flash show that FoCo improves both probabilistic accuracy and calibration.
