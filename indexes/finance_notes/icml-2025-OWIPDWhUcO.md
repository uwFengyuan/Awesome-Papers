# AdaSplash: Adaptive Sparse Flash Attention

ICML 2025 · main · Long

[Long] [Main] [Oral] [Poster] [Finance]

Financial evidence / 金融依据：t classification with different sequence lengths. In cases where the full batch could not fit in memory, Model Seq. SciFact NFC FiQA TREC-C gradient accumulation was used. Memory values represent the RoBERTa 512 51.7 23.1 27.8 60.1 effective peak memory required to process a batch of 16 samples. RoBERTa (α = 1.5) 512 50.8 24.2 27.6 71.0 RoBERTa (α = 2.0) 512 52.2 23.8 25.7 65.5

[Paper](https://openreview.net/forum?id=OWIPDWhUcO)

Classification / 分类：Financial IR & RAG / 金融检索与RAG → Retrieval, Embedding & Reranking / 检索、嵌入与重排 → General / 综合

## Abstract / 摘要

The computational cost of softmax-based attention in transformers limits their applicability to long-context tasks. Adaptive sparsity, of which $\alpha$-entmax attention is an example, offers a flexible data-dependent alternative, but existing implementations are inefficient and do not leverage the sparsity to obtain runtime and memory gains. In this work, we propose AdaSplash, which combines the efficiency of GPU-optimized algorithms with the sparsity benefits of $\alpha$-entmax. We first introduce a hybrid Halley-bisection algorithm, resulting in a 7-fold reduction in the number of iterations needed to compute the $\alpha$-entmax transformation. Then, we implement custom Triton kernels to efficiently handle adaptive sparsity. Experiments with RoBERTa and ModernBERT for text classification and single-vector retrieval, along with GPT-2 for language modeling, show that our method achieves substantial improvements in runtime and memory efficiency compared to existing $\alpha$-entmax implementations. It approaches---and in some cases surpasses---the efficiency of highly optimized softmax implementations like FlashAttention-2, enabling long-context training while maintaining strong task performance.
