# Adaptive Time Series Reasoning via Segment Selection

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：conditioned on controller-selected segments. Across six segments relevant to a given question. Relevant segments benchmarks in clinical, financial, environmental, and gen- depend on the question, so the model must decide during eral domain time series reasoning, ARTIST outperforms inference which parts of time series to inspect. Second, large lan

[Paper](https://openreview.net/forum?id=yzBbBPheg7)

Classification / 分类：Time Series / 时间序列 → Representation & Foundation Models / 表征与基础模型 → Foundation models / 基础模型

## Abstract / 摘要

Time series reasoning tasks often start with a natural language question and require targeted analysis of a time series. Evidence may span the full series or appear in a few short intervals, so the model must decide what to inspect. Most existing approaches encode the entire time series into a fixed representation before inference, regardless of relevance. We introduce ARTIST, which formulates time-series reasoning as a sequential decision problem. ARTIST interleaves reasoning with adaptive temporal segment selection. It adopts a controller-reasoner architecture and uses reinforcement learning to train the controller role to select informative segments and the reasoner role to generate segment-conditioned reasoning traces and final answers. During inference, the model actively acquires task-relevant information instead of relying on a static summary of the full sequence. We use a novel hierarchical policy optimization approach for post-training that allows the model to excel in both segment selection and question-answering behavior. We evaluate ARTIST on six time-series reasoning benchmarks and compare it with large language models, vision-language models, and prior time-series reasoning systems. ARTIST improves average accuracy by 6.46 absolute percentage points over the strongest baseline. The largest gains appear on rare event localization and multi-segment reasoning tasks. Supervised fine-tuning improves performance, and reinforcement learning provides additional gains by optimizing question-adaptive segment selection, showing that selective data use drives effective time-series reasoning.
