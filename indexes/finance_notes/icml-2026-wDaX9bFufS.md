# Global Merger-Arbitrage Forecasting with Language Models

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：We present a language-model forecasting system for merger arbitrage, a specialized high-stakes financial setting in which the task is to predict the outcome of announced M\&A deals. / These results, together with ablation studies, show that LLM-based forecasting can succeed in specialized, long-context financial workflows, with hindsight-based supervision and expert-designed context playing a critical role.

[Paper](https://openreview.net/forum?id=wDaX9bFufS)

Classification / 分类：Trading & Microstructure / 交易与市场微观结构 → Trading & Execution / 交易策略与执行 → General / 综合

## Abstract / 摘要

We present a language-model forecasting system for merger arbitrage, a specialized high-stakes financial setting in which the task is to predict the outcome of announced M\&A deals. Unlike prior work on judgmental forecasting with LLMs, which has focused on broad mixed-topic benchmarks and short context such as news snippets, we study a setting that requires long-context reasoning over hundreds of pages of technical documents. Our system combines expert-guided context engineering with finetuning on hindsight-guided reasoning traces derived from historical deals. Given an announced deal, it outputs a probability distribution over three mutually exclusive outcomes: closing at announced terms, a higher bid, or deal termination. On an out-of-sample set of more than 400 large deals spanning 42 countries, our finetuned system achieves the best performance of any method we evaluate, reducing class-balanced Brier score to 0.151. This is 24% below calibrated market-implied probabilities, 19% below XGBoost, and 25-42% below frontier language models. These results, together with ablation studies, show that LLM-based forecasting can succeed in specialized, long-context financial workflows, with hindsight-based supervision and expert-designed context playing a critical role.
