# OpenEstimate: Evaluating LLMs on Reasoning Under Uncertainty with Real-World Data

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：ll-documented facts in pretraining corpora. We begin by selecting existing data sources spanning three broad domains: social sciences (Glassdoor2 , labor economics), industrial settings (Pitchbook(PitchBook Data, 2024), finance), and medicine (NHANES(Centers for Disease Control and Prevention, 2018), public health). 1 https://github.com/alanarenda/openestimate 2 https://www.kaggle.com/datasets/thedevastator/jobs-dataset-from-glassdoor 2 Domain Dataset # marginal # 1 cond

[Paper](https://openreview.net/forum?id=sAzUQkP47r)

Classification / 分类：Financial Models & Benchmarks / 金融模型与评测资源 → Cross-Task Financial Evaluation / 跨任务金融综合评测 → General / 综合

## Abstract / 摘要

Real-world settings where language models (LMs) are deployed --- in domains spanning healthcare, finance, and other forms of knowledge work --- require models to grapple with incomplete information and reason under uncertainty. Yet most LM evaluations focus on problems with well-defined answers and success criteria. This gap exists in part because natural problems involving uncertainty are difficult to construct: given that LMs have access to most of the same knowledge as humans, it is non-trivial to design questions for which LMs will struggle to produce correct answers. As a result, LM performance on reasoning under uncertainty remains poorly characterized. To address this gap, we introduce \textsc{OpenEstimate}, an extensible, multi-domain benchmark for evaluating LMs on probabilistic estimation tasks that require models to synthesize knowledge from pretraining and express predictions as Bayesian priors. We assess these priors for accuracy and calibration. Across six frontier models, we find that LM-elicited priors are worth the equivalent of about five samples from the underlying data distribution, and that posteriors computed using LM priors tend to be more accurate than those computed using a naive prior. At the same time, the relationship between model accuracy and confidence is weak across the board, indicating the value of developing new methods to improve calibration. The \textsc{OpenEstimate} benchmark thus offers a challenging evaluation for frontier LMs and a platform for developing models that are better at probabilistic estimation and reasoning under uncertainty.
