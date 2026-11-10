# The Illusion of Generalization in Tabular Language Models

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：s. Test Row 728 T4 Match Unnamed: 0 = 728 Unnamed: 0 = 728 kids618 = 3, age = 41 k618 = 3, age = 41 Financial time series. We examined the Bitcoin price pre- nwifeinc = 77.0 inc = 77.0 diction task, which asks the model to predict the Close lfp = ? lfp = no (Label exposed) price (discretized into quartile bins) given features including 753/753 rows in T4 with labels exposed. Date, Open, High, Low, and Adj Close. Searching (b) Task Leakage: peloton-data T4 for test examples revealed extensive duplication: indi- vidual records appear in up to four separate T4 chunks, Task: Date → Day T4: toronto-transit-delays each containing the target Close value. Figure 6 (Ap- Date = 11/30/2021 Date: 2021-11-30 Instructor = Ally Love Day: Tuesday 

[Paper](https://openreview.net/forum?id=ea2kQkdQA7)

Classification / 分类：Time Series / 时间序列 → General Time-Series Methods / 综合序列方法 → General / 综合

## Abstract / 摘要

Tabular Language Models (TLMs) have been claimed to achieve strong generalization for tabular prediction. We conduct a systematic re-evaluation of Tabula-8B as a representative TLM, utilizing 165 datasets from the UniPredict benchmark. Our investigation reveals three findings. First, binary and categorical classification achieve near-zero median lift over majority-class baselines and strong aggregate performance is driven entirely by quartile classification tasks. Second, top-performing datasets exhibit pervasive contamination, including complete train-test overlap and task-level leakage that evades standard deduplication. Third, instruction-tuning without tabular exposure recovers 92.2% of standard classification performance and on quartile classification, format familiarity closes 71.3% of the gap with the residual attributable to contaminated datasets. These findings suggest claimed generalization likely reflects evaluation artifacts rather than learned tabular reasoning. We conclude with recommendations for strengthening TLM evaluation.
