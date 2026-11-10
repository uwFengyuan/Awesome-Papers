# Contrastive Retrieval Heads for Improved Attention-Based Reranking

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：.2 SciDocs 22.5 16.6 17.3 19.5 18.5 19.7 20.2 20.8 20.3 21.6 18.4 20.3 20.0 FiQA 36.9 35.8 40.3 41.4 41.3 44.0 44.1 40.2 41.4 44.0 39.7 41.6 42.4 NQ 51.6 55.4 56.5 58.1 60.8 63.0 63.2 61.5 61.8 64.1

[Paper](https://openreview.net/forum?id=el3L9KxeOE)

Classification / 分类：Financial IR & RAG / 金融检索与RAG → Retrieval, Embedding & Reranking / 检索、嵌入与重排 → General / 综合

## Abstract / 摘要

The strong zero-shot and long-context capabilities of recent Large Language Models (LLMs) have enabled highly effective list-wise reranking systems. Attention-based rerankers leverage transformer attention patterns as retrieval signals, but not all attention heads contribute equally: many introduce noise and redundancy, limiting both reranking quality and efficiency. In this work, we introduce CoRe heads, a small subset of retrieval-specialized heads identified through a contrastive scoring objective that rewards attention to relevant documents while penalizing attention to distractors. This contrastive criterion isolates highly discriminative retrieval heads and yields a strong training-free list-wise reranker. Our analysis reveals that retrieval-relevant computation in transformer rerankers is highly sparse and structurally localized: fewer than 1% of attention heads account for most reranking performance across models and datasets, and these heads consistently concentrate in middle transformer layers. This localization enables aggressive layer pruning for efficient reranking: removing the final 50% of transformer layers preserves nearly identical reranking accuracy while substantially reducing inference latency and GPU memory usage.
