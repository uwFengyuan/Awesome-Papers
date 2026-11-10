# TimeClaw: A Time-Series AI Agent with Exploratory Execution Learning

NeurIPS 2026 · main · Long

[Long] [Main] [Finance]

Financial evidence / 金融依据：Time series analysis underpins forecasting, monitoring, and decision making in domains such as finance and weather, where solving a task often requires both numerical accuracy and contextual reasoning. / In an MTBench-aligned evaluation with 17 tasks that span finance and weather prediction and reasoning tasks, TimeClaw delivers consistent gains over the baselines.

[Paper](https://openreview.net/forum?id=MK0e2fxdTl)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Time series analysis underpins forecasting, monitoring, and decision making in domains such as finance and weather, where solving a task often requires both numerical accuracy and contextual reasoning. Recent progress has moved from specialized neural predictors to approaches built on LLMs and foundation models that can reason over time series inputs and use external tools. However, most such systems remain execution-centric: they focus on solving the current instance but learn little from exploratory execution. This is especially limiting in verifiable numeric settings, where multiple candidate executions and tool-use procedures may all be task-valid yet differ sharply in quantitative quality, and where early success can trigger tool-prior collapse that suppresses further exploration. To address this limitation, we present TimeClaw, an exploratory execution learning framework that turns exploratory execution into reusable hierarchical distilled experience through a four-stage loop: Explore, Compare, Distill, and Reinject. TimeClaw combines metric-supervised exploratory execution learning, task-aware tool dropout, and hierarchical distilled experience for inference-time reinjection, while keeping the base model frozen and avoiding online test-time adaptation. In an MTBench-aligned evaluation with 17 tasks that span finance and weather prediction and reasoning tasks, TimeClaw delivers consistent gains over the baselines. These results suggest that, for scientific systems, the bottleneck is not only execution-time capability, but how exploratory experience is compared, distilled, and reused.
