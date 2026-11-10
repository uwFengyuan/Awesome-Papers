# AceSearcher: Bootstrapping Reasoning and Search for LLMs via Reinforced Self-Play

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Remarkably, on document-level finance reasoning tasks, AceSearcher-32B matches the performance of the giant DeepSeek-V3 model using less than 5% of iits parameters.

[Paper](https://openreview.net/forum?id=jSgCM0uZn3)

Classification / 分类：Financial IR & RAG / 金融检索与RAG → Financial RAG & Long Documents / 金融RAG与长文档 → General / 综合

## Abstract / 摘要

Search-augmented LLMs often struggle with complex reasoning tasks due to ineffective multi-hop retrieval and limited reasoning ability. We propose AceSearcher, a cooperative self-play framework that trains a single large language model (LLM) to alternate between two roles: a decomposer that breaks down complex queries and a solver that integrates retrieved contexts for answer generation. AceSearcher couples supervised fine-tuning on a diverse mixture of search, reasoning, and decomposition tasks with reinforcement fine-tuning optimized for final answer accuracy, eliminating the need for intermediate annotations. Extensive experiments on three reasoning-intensive tasks across 10 datasets show that AceSearcher outperforms state-of-the-art baselines, achieving an average exact match improvement of 7.6%. Remarkably, on document-level finance reasoning tasks, AceSearcher-32B matches the performance of the giant DeepSeek-V3 model using less than 5% of iits parameters. Even at smaller scales (1.5B and 8B), AceSearcher often surpasses existing search-augmented LLMs with up to 9× more parameters, highlighting its exceptional efficiency and effectiveness in tackling complex reasoning tasks.
