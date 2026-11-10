# A General Framework for Producing Interpretable Semantic Text Embeddings

ICLR 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：7 Table 3: Retrieval results evaluated by nDCG@10. Evaluated on seven diverse datasets: MS MARCO (Bajaj et al., 2016), NewsSpectrum (NSP) (Sun et al., 2024), ArguAna (Wachsmuth et al., 2018), FiQA-2018 (FQA) (Maia et al., 2018), NFCorpus (NFC) (Boteva et al., 2016), SCIDOCS (Cohan et al., 2020), and SciFact (Wadden et al., 2020). MS MARCO is evaluated on a 1% sample of its dev set, while NewsSpectrum uses news titles as queries with corresponding articles as targets. The remaining datasets are assessed using the MTEB evaluation suite.

[Paper](https://openreview.net/forum?id=23uY3FpQxc)

Classification / 分类：Financial IR & RAG / 金融检索与RAG → Retrieval, Embedding & Reranking / 检索、嵌入与重排 → General / 综合

## Abstract / 摘要

Semantic text embedding is essential to many tasks in Natural Language Processing (NLP). While black-box models are capable of generating high-quality embeddings, their lack of interpretability limits their use in tasks that demand transparency. Recent approaches have improved interpretability by leveraging domain-expert-crafted or LLM-generated questions, but these methods rely heavily on expert input or well-prompt design, which restricts their generalizability and ability to generate discriminative questions across a wide range of tasks. To address these challenges, we introduce \algo{CQG-MBQA} (Contrastive Question Generation - Multi-task Binary Question Answering), a general framework for producing interpretable semantic text embeddings across diverse tasks. Our framework systematically generates highly discriminative, low cognitive load yes/no questions through the \algo{CQG} method and answers them efficiently with the \algo{MBQA} model, resulting in interpretable embeddings in a cost-effective manner. We validate the effectiveness and interpretability of \algo{CQG-MBQA} through extensive experiments and ablation studies, demonstrating that it delivers embedding quality comparable to many advanced black-box models while maintaining inherently interpretability. Additionally, \algo{CQG-MBQA} outperforms other interpretable text embedding methods across various downstream tasks. The source code is available at \url{https://github.com/dukesun99/CQG-MBQA}.
