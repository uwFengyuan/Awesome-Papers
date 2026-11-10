# Embedding-Based Context-Aware Reranker

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：here relevant information may be scattered across long passages. (iv) COVID-QA (COVID) is a biomedical QA dataset based on scientific research documents, which similarly requires reasoning over long and dense texts. (v) ESG Re- ports are long-form corporate documents sourced from the ViDoRe benchmark, re-annotated for text-based QA to test document-wide contextual understanding capabilities. (vi) Football and (vii) Geography (Geog) are constructed from rephrased Wikipedia summaries in which explicit entity mentions have been replaced by pronouns via GPT-4o. This setu

[Paper](https://openreview.net/forum?id=OBMcxeSK5U)

Classification / 分类：ESG & Sustainable Finance / ESG与可持续金融 → ESG Disclosure & Greenwashing / ESG披露与漂绿 → General / 综合

## Abstract / 摘要

Retrieval-Augmented Generation (RAG) systems rely on retrieving  relevant evidence from a corpus to support downstream generation.  The common practice of splitting a long document into multiple shorter passages enables finer-grained and targeted information retrieval.  However, it also introduces challenges when a correct retrieval would require inference across passages, such as resolving coreference, disambiguating entities, and aggregating evidence scattered across multiple sources. Many state-of-the-art (SOTA) reranking methods, despite utilizing powerful large pretrained language models with potentially high inference costs, still neglect the aforementioned challenges. Therefore, we propose Embedding-Based Context-Aware Reranker (EBCAR), a lightweight reranking framework operating directly on embeddings of retrieved passages with enhanced cross-passage understandings through the structural information of the passages and a hybrid attention mechanism, which captures both high-level interactions across documents and low-level relationships within each document. We evaluate EBCAR against SOTA rerankers on the ConTEB benchmark, demonstrating its effectiveness for information retrieval requiring cross-passage inference and its advantages in both accuracy and efficiency. Our source code is available at https://github.com/BorealisAI/EBCAR.
