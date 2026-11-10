# BayesRAG: Probabilistic Mutual Evidence Corroboration for Multimodal Retrieval-Augmented Generation

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：- MMLongBench-Doc (Ma et al., 2024). DocBench rectly feeding PDFs into GPT-4o-mini. For docu- comprises 229 documents across five domains (e.g., ments with fewer than 50 pages, we use page-level Finance, Law) with 1,102 QA pairs, featuring sub- screenshots as input. For longer documents, we stantial length (avg. 66 pages, ∼46k tokens) to randomly sample 50 screenshots as input. test long-context capabilities. MMLongBench-Doc Evaluation Metrics. For DocBench, we stri

[Paper](https://openreview.net/forum?id=9Vk5e1o3lU)

Classification / 分类：Financial IR & RAG / 金融检索与RAG → Retrieval, Embedding & Reranking / 检索、嵌入与重排 → General / 综合

## Abstract / 摘要

Retrieval-Augmented Generation (RAG) has become a pivotal paradigm for Large Language Models (LLMs), yet current approaches struggle with visually rich documents by treating text and images as isolated retrieval targets. Existing methods relying solely on cosine similarity often fail to capture the semantic reinforcement provided by cross-modal alignment and layout-induced coherence. To address these limitations, we propose **BayesRAG**, a novel multimodal retrieval framework grounded in Bayesian inference and Dempster-Shafer evidence theory. Unlike traditional approaches that rank candidates strictly by similarity, BayesRAG models the intrinsic consistency of retrieved candidates across modalities as probabilistic evidence to refine retrieval confidence. Specifically, our method computes the posterior association probability for combinations of multimodal retrieval results, prioritizing text-image pairs that mutually corroborate each other in terms of both semantics and layout. Extensive experiments demonstrate that BayesRAG significantly outperforms state-of-the-art (SOTA) methods on challenging multimodal benchmarks. This study establishes a new paradigm for multimodal retrieval fusion that effectively resolves the isolation of heterogeneous modalities through an evidence fusion mechanism and enhances the robustness of retrieval outcomes. Our code is available at https://anonymous.4open.science/r/BayesRAG-4C6B/.
