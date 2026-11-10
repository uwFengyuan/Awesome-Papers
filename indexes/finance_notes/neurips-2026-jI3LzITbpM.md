# TSQAgent: Rating Time Series Data Quality via Dedicated Agentic Reasoning

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：een 2012 and 2014. In our experiments, we use the series labeled MT_320 as the target variable in the univariate setting. • ExchangeRate (Lai et al., 2018): This dataset records daily exchange rates of eight currencies spanning from 1990 to 2016. We follow prior work and select the Singapore dollar series as the prediction target. • Traffic (tra): This dataset consists of hourly occupancy rates collected from freeway sensors in the San Francisco Bay Area between 2015 and 2016. We use sensor 861 as the target series. • Weather (wea): This dataset contains high-fr

[Paper](https://openreview.net/forum?id=jI3LzITbpM)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → General / 综合

## Abstract / 摘要

Assessing the quality of time series (TS) data is fundamental yet inherently challenging due to the multifaceted nature of quality dimensions. Recently, large language models (LLMs) have emerged as a promising paradigm for TS quality assessment via pairwise comparison and per-dimension evaluation. However, existing approaches rely on manually predefined quality dimensions and purely text-based reasoning, leaving it unknown whether LLMs can identify truly relevant quality dimensions or perform grounded and quantitative quality comparisons. To investigate this, we construct TSQBench, a dedicated benchmark for evaluating LLMs’ capabilities in TS quality assessment, which measures two progressive capabilities: (i) understanding and identifying relevant quality dimensions, and (ii) performing quality comparison under specific dimensions. Our analysis reveals that both open-source and proprietary LLMs consistently struggle with identifying critical quality dimensions and conducting precise, evidence-grounded reasoning over quality characteristics. To address these limitations, we propose TSQAgent, a novel agentic reasoning framework for dedicated TS data quality rating, comprising three collaborative roles: Perceiver for focused dimension selection, Inspector for dimension-wise quantitative analysis, and Adjudicator that aggregates and refines the final judgment. In particular, we introduce an agentic reasoning strategy that instills the ability to identify and prioritize the most relevant quality dimensions, and further propose an agent workflow equipped with external analytical tools to enable precise quantitative comparisons over selected dimensions. Experiments on both the proposed benchmark and eleven real-world datasets demonstrate that our framework not only substantially improves LLMs’ capabilities in quality understanding and quantitative comparison but also effectively translates these improvements into better quality-aware data selection, leading to enhanced downstream performance and data efficiency.
