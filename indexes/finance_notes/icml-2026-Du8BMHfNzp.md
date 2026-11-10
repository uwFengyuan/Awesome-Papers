# PATRA: Pattern-Aware Alignment and Balanced Reasoning for Time Series Question Answering

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：prediction. Simultaneously, in the Table 1 presents the overall performance of all baseline complex Finance domain, it also achieves SOTA perfor- models and our PATRA model on four task types. Our PA- mance across all six metrics for both short-term (7-day) and TRA achieves the best results across all metrics, surpassing long-term (30-day) trend prediction and numerical forecast- pure text models and significantly outperforming the multi- ing. The details of MTBench are shown in Appendix D. modal model ChatTS, highlighting its strong cross-modality modeling and reasoning capabilities. 5.6. Ablation Studies In detail, PATRA achieves 56.03% accuracy on Comprehen- We conduct ablation experiments to assess the contribu- sion, ex

[Paper](https://openreview.net/forum?id=Du8BMHfNzp)

Classification / 分类：Time Series / 时间序列 → Causality & Dynamics / 序列因果与动力学 → Generation / 生成

## Abstract / 摘要

Time series reasoning demands both the perception of complex dynamics and logical depth. However, existing LLM-based approaches exhibit two limitations: they often treat time series merely as text or images, failing to capture the patterns like trends and seasonalities needed to answer specific questions; and when trained on a mix of simple and complex tasks, simpler objectives often dominate the learning process, hindering the development of deep reasoning capabilities. To address these limitations, we propose the Pattern-Aware Alignment and Balanced Reasoning model (PATRA), introducing a pattern-aware mechanism that extracts trend and seasonality patterns from time series to achieve deep alignment. Furthermore, we design a task-aware balanced reward to harmonize learning across tasks of varying difficulty, incentivizing the generation of coherent Chains of Thought. Extensive experiments show that PATRA outperforms strong baselines across diverse Time Series Question Answering (TSQA) tasks, demonstrating superior cross-modal understanding and reasoning capability.
