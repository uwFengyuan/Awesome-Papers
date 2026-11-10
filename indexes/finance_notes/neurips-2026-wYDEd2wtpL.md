# Innocuous-Seeming Data, Latent Ideology: Ideological Generalisation in Finetuned LLMs

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：The same effect appears with plausibly-deployed datasets such as workplace HR policy and practical finance queries, as well as on a science-pseudoscience axis where food-safety finetuning increases sycophantic agreement with users expressing false health beliefs.

[Paper](https://openreview.net/forum?id=wYDEd2wtpL)

Classification / 分类：Financial Safety & Compliance / 金融安全与合规 → Financial Privacy & Security / 金融隐私与信息安全 → General / 综合

## Abstract / 摘要

Finetuning language models on small, curated datasets is standard practice for adapting them to specific policies or domains. We show that finetuning on narrow, factually-defensible, moderation-passing data can cause broad ideological shifts across unrelated domains, while preserving general capabilities. Training GPT-4.1 on right- or left-leaning economics Q&A yields matched ideological shifts on topics such as criminal justice, the environment, and cultural taste. The same effect appears with plausibly-deployed datasets such as workplace HR policy and practical finance queries, as well as on a science-pseudoscience axis where food-safety finetuning increases sycophantic agreement with users expressing false health beliefs. We call this phenomenon *ideological generalisation* and propose a methodology to measure two properties: *breadth*, how far the shift reaches across topics absent from training, and *amplification*, how much finetuning intensifies the shift relative to few-shot prompting on the same examples. We show that few-shot prompting indicates the direction of generalisation but finetuning pushes the model to further extremes, including to far out-of-distribution outputs such as endorsements of race-IQ connections and political violence. The effect replicates on Gemma-3, holds under judge-free evaluations and external benchmarks, survives mixing with generic data, and leaves GSM8K accuracy within $\pm 1$pp of the baseline.
