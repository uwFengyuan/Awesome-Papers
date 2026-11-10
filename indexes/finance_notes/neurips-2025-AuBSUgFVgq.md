# Multimodal Tabular Reasoning with Privileged Structured Information

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：reasoning capability of our model on a diverse set of publicly available benchmarks. Specifically, for Tabular Question Answering (TQA) tasks, we use five representative datasets: TABMWP [38], WTQ [48], HiTab [11], and TAT-QA [88]. We export FeTaQA [41] due to its evaluation metric being BLEU [47], which does not focus on the accuracy of question answering. For Table Fact Verification (TFV) tasks, we include TabFact [9] and InfoTabs [22]. To further assess the robustness of our approach, we conduct additional experiments on MMMU [80], evaluating our model on all table-

[Paper](https://openreview.net/forum?id=AuBSUgFVgq)

Classification / 分类：Financial QA & Reasoning / 金融问答与数值推理 → Numerical & Table Reasoning / 数值与表格推理 → General / 综合

## Abstract / 摘要

Tabular reasoning requires complex, multi-step information extraction and logical inference, such as aggregation, comparison, or calculation over tabular data. While recent advances have leveraged large language models (LLMs) for reasoning over structured text tables, such high-quality textual representations are often unavailable in real-world settings, where tables typically appear as images. In this paper, we tackle the task of tabular reasoning directly from table images. Our core strategy is to leverage privileged structured information---specifically, the ground-truth structured table data available during training but inaccessible at test time---to enhance multimodal large language models (MLLMs). The key challenges lie in: accurately aligning visual representations with the structured information, particularly mapping the visual evidence to logical steps; and effectively transferring the reasoning skills learned during training to the MLLM for visual inference.  To address these, we introduce {\sc Turbo} (TabUlar Reasoning with Bridged infOrmation), a new framework for multimodal tabular reasoning using privileged information. {\sc Turbo} benefits from a structure-aware reasoning trace generator based on DeepSeek-R1, which contributes to high-quality modality-bridged information. On this basis, {\sc Turbo} repeatedly generates and selects advantageous reasoning traces, further enhancing the model's tabular reasoning ability. Experimental results demonstrate that, with limited (9k) data, {\sc Turbo} achieves state-of-the-art performance ($+7.2\%$ vs. previous SOTA) across multiple datasets.
