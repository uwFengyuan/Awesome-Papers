# TaTToo: Tool-Grounded Thinking PRM for Test-Time Scaling in Tabular Reasoning

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Bench (Wu et al., 2024). TableBench is a comprehensive benchmark specifically designed to evaluate the reasoning abilities of LLMs over tabular data. It consists of 3,681 unique tables drawn from diverse domains such as finance, sports, politics, and science, with each table containing on average 16.7 rows and 6.7 columns. The dataset emphasizes numerical reasoning, with over 65% of table cells containing numerical values. TableBench questions are organized into four major categories: fact-checking, numerical reasoning, data analysis, further divided into 18 subcategorie

[Paper](https://openreview.net/forum?id=zc1ezBrr5m)

Classification / 分类：Document AI / 票据、财报与图表理解 → Financial Tables & Spreadsheets / 财务表格与电子表格 → General / 综合

## Abstract / 摘要

Process Reward Models (PRMs) have recently emerged as a powerful framework for enhancing the reasoning capabilities of large reasoning models (LRMs), particularly in the context of test-time scaling (TTS). However, their potential for supervising LRMs on tabular reasoning domains remains underexplored.  Through detailed empirical analyses, we identify that existing PRMs, though widely adopted for supervising text-only reasoning steps, struggle with table-specific operations such as sub-table retrieval and schema interaction, leading to critical performance bottlenecks. To address this limitation, we propose TaTToo, a novel table-grounded PRM framework that (i) reasons explicitly over tabular reasoning steps and (ii) integrates tool-based verification to provide precise reward supervision. Concretely, we first design a scalable data curation pipeline that constructs over 60k high-quality step-level annotations by integrating table verification rationales with tool-based executions. Building on the collected data, we train TaTToo with a dual-stage paradigm: cold-start supervised fine-tuning to capture tool-use reasoning patterns, followed by reinforcement learning with tool-grounded reward shaping to align our model with table-based verification. We provide a comprehensive evaluation of the policy improvement induced by our newly designed PRM. Across 5 challenging tabular reasoning benchmarks covering numerical reasoning, fact-checking, and data analysis, TaTToo improves downstream policy LRMs by 30.9\% at inference, surpasses strong PRM baselines such as Qwen-2.5-Math-PRM-72B with only 8B parameters, and demonstrates strong generalizability across diverse TTS strategies.
