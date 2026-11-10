# LaRA: Benchmarking Retrieval-Augmented Generation and Long-Context LLMs – No Silver Bullet for LC or RAG Routing

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：reflect real-world information needs. 2. Revisiting RAG vs. Long Context Specifically, LaRA includes three of the most common types Benchmarks of long contexts—novels, academic papers, and financial Desipte a lot of benchmarks has been used to compare statements—selected to represent diverse writing styles and RAG with feeding lanuage model with long context, there information densities. LaRA features four types of question- lacks a clear guidelines and conclusion on when and where answering tasks designed to ass

[Paper](https://openreview.net/forum?id=CLF25dahgA)

Classification / 分类：Financial IR & RAG / 金融检索与RAG → Retrieval, Embedding & Reranking / 检索、嵌入与重排 → General / 综合

## Abstract / 摘要

As Large Language Model (LLM) context windows expand, the necessity of Retrieval-Augmented Generation (RAG) for integrating external knowledge is debated. Existing RAG vs. long-context (LC) LLM comparisons are often inconclusive due to benchmark limitations. We introduce LaRA, a novel benchmark with 2326 test cases across four QA tasks and three long context types, for rigorous evaluation. Our analysis of eleven LLMs reveals the optimal choice between RAG and LC depends on a complex interplay of model capabilities, context length, task type, and retrieval characteristics, offering actionable guidelines for practitioners. Our code and dataset is provided at:https://github.com/Alibaba-NLP/LaRA
