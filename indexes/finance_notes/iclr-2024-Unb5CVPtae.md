# Time-LLM: Time Series Forecasting by Reprogramming Large Language Models

ICLR 2024 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：erm forecasting are presented in Tab. 12. T IME -LLM consistently outperforms the majority of baseline models in most cases. Notably, we surpass GPT4TS by a large margin (e.g., 8.7% overall, 13.4% on M4-Yearly, and an average of 21.5% on M4-Hourly, M4-Daily, and M4-Weekly), as well as TimesNet (e.g., 10% overall, 14.1% on M4-Yearly, and an average of 30.1% on M4-Hourly, M4-Daily, and M4-Weekly). Compared to the recent state- of-the-art forecasting models, N-HiTS and PatchTST, T IME -LLM exhibits comparable or superior performances without any parameter updates on the backbone LLM. In addition, we conduct a comparative ana

[Paper](https://openreview.net/forum?id=Unb5CVPtae)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Time series forecasting holds significant importance in many real-world dynamic systems and has been extensively studied. Unlike natural language process (NLP) and computer vision (CV), where a single large model can tackle multiple tasks, models for time series forecasting are often specialized, necessitating distinct designs for different tasks and applications. While pre-trained foundation models have made impressive strides in NLP and CV, their development in time series domains has been constrained by data sparsity. Recent studies have revealed that large language models (LLMs) possess robust pattern recognition and reasoning abilities over complex sequences of tokens. However, the challenge remains in effectively aligning the modalities of time series data and natural language to leverage these capabilities. In this work, we present Time-LLM, a reprogramming framework to repurpose LLMs for general time series forecasting with the backbone language models kept intact. We begin by reprogramming the input time series with text prototypes before feeding it into the frozen LLM to align the two modalities. To augment the LLM's ability to reason with time series data, we propose Prompt-as-Prefix (PaP), which enriches the input context and directs the transformation of reprogrammed input patches. The transformed time series patches from the LLM are finally projected to obtain the forecasts. Our comprehensive evaluations demonstrate that \method is a powerful time series learner that outperforms state-of-the-art, specialized forecasting models. Moreover, Time-LLM excels in both few-shot and zero-shot learning scenarios. The code is made available at https://github.com/KimMeen/Time-LLM.
