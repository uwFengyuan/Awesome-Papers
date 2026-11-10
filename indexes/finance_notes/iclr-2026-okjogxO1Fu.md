# Let LLMs Speak Embedding Languages: Generative Text Embeddings via Iterative Contrastive Refinement

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：2.14 70.78 68.15 71.44 71.01 69.81 FEVER 95.30 95.18 80.71 96.94 94.38 96.15 94.23 95.41 FiQA 60.50 65.08 68.23 61.46 65.98 68.07 60.79 55.90 HotpotQA 86.16 91.64 82.06 88.14 91.09 91.05 88.10 88.31 MSMARCO 66.58 66.51 70.

[Paper](https://openreview.net/forum?id=okjogxO1Fu)

Classification / 分类：Financial IR & RAG / 金融检索与RAG → Retrieval, Embedding & Reranking / 检索、嵌入与重排 → General / 综合

## Abstract / 摘要

Existing large language model (LLM)-based embeddings typically adopt an encoder-only paradigm, treating LLMs as static feature extractors and overlooking their core gener- ative strengths. We introduce GIRCSE (Generative Iterative Refinement for Contrastive Sentence Embeddings), a novel framework that leverages autoregressive generation to iter- atively refine semantic representations. By producing sequences of soft tokens optimized under a contrastive objective, GIRCSE captures latent concepts and implicit semantics that encoder-only methods often miss. To guide this process, we propose an Iterative Contrastive Refinement (ICR) objective that encourages each refinement step to yield bet- ter representations. Extensive experiments show that GIRCSE outperforms strong LLM- based embedding baselines on the MTEB embedding benchmark. Moreover, GIRCSE ex- hibits an emergent test-time scaling property: generating more tokens at inference steadily improves embedding quality. Our results establish generative iterative refinement as a new paradigm for representation learning.
