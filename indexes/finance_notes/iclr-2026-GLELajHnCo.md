# GAPrune: Gradient-Alignment Pruning for Domain-Aware Embeddings

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Domain-specific embedding models have shown promise for applications that require specialized semantic understanding, such as coding agents and financial retrieval systems, often achieving higher performance gains than general models.

[Paper](https://openreview.net/forum?id=GLELajHnCo)

Classification / 分类：Financial IR & RAG / 金融检索与RAG → Retrieval, Embedding & Reranking / 检索、嵌入与重排 → General / 综合

## Abstract / 摘要

Domain-specific embedding models have shown promise for applications that require specialized semantic understanding, such as coding agents and financial retrieval systems, often achieving higher performance gains than general models. However, state-of-the-art embedding models are typically based on LLMs, which contain billions of parameters, making deployment challenging in resource-constrained environments. Model compression through pruning offers a promising solution, but existing pruning methods treat all parameters uniformly, failing to distinguish between general semantic representations and domain-specific patterns, leading to suboptimal pruning decisions. Thus, we propose GAPrune, a pruning framework that addresses this challenge by considering both domain importance and preserving general linguistic foundation. Our method uses Fisher Information to measure importance and general-domain gradient alignment to assess parameter behavior, then combines these signals using our Domain Alignment Importance (DAI) scoring. Lower DAI scores indicate that the parameter is either less important for the domain task or creates conflicts between domain and general objectives. Experiments on two domain benchmarks, FinMTEB and ChemTEB, show that GAPrune maintains performance within 2.5\% of dense models in one-shot pruning at 50\% sparsity, while outperforming all baselines. With retraining in 100 steps, GAPrune achieves +4.51\% improvement on FinMTEB and +1.73\% on ChemTEB, demonstrating that our pruning strategy not only preserves but enhances domain-specific capabilities. Our findings demonstrate that principled pruning strategies can achieve model compression and enhanced domain specialization, providing the research community with a new approach for development.
