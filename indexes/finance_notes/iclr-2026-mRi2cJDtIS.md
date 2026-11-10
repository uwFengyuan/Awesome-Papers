# Learning Facts at Scale with Active Reading

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：We train expert 8B models that achieve 66% on a Wikipedia-grounded subset of SimpleQA (+313% relative over vanilla finetuning) and 26% on FinanceBench (+160% relative over vanilla finetuning) by applying Active Reading to the source documents for each benchmark.

[Paper](https://openreview.net/forum?id=mRi2cJDtIS)

Classification / 分类：Financial QA & Reasoning / 金融问答与数值推理 → Knowledge & Conversational QA / 知识与对话问答 → General / 综合

## Abstract / 摘要

LLMs are known to store vast amounts of knowledge in their parametric memory. However, learning and recalling facts from this memory is known to be unreliable, depending largely on the prevalence of particular facts in the training data and other factors which are poorly understood. Practitioners are lacking tools which will allow them to ensure that the models learn a given body of knowledge reliably and consistently. To this end, we propose Active Reading: a framework where we train models to study a given set of material with self-generated learning strategies. First, we demonstrate models trained with Active Reading on expert domains absorb significantly more knowledge than vanilla finetuning and other data augmentations. We train expert 8B models that achieve 66% on a Wikipedia-grounded subset of SimpleQA (+313% relative over vanilla finetuning) and 26% on FinanceBench (+160% relative over vanilla finetuning) by applying Active Reading to the source documents for each benchmark. Finally, we show that Active Reading can be utilized at pre-training scale to build more factual models. As a demonstration of this, we release WikiExpert-8B, a Wikipedia-expert model trained on 1 trillion generated tokens, which outcompetes models with hundreds of billions of parameters on factual QA.
