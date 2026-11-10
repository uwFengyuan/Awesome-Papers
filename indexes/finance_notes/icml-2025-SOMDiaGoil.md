# On the Vulnerability of Applying Retrieval-Augmented Generation within Knowledge-Intensive Application Domains

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Retrieval-Augmented Generation (RAG) has been empirically shown to enhance the performance of large language models (LLMs) in knowledge-intensive domains such as healthcare, finance, and legal contexts.

[Paper](https://openreview.net/forum?id=SOMDiaGoil)

Classification / 分类：Financial IR & RAG / 金融检索与RAG → Retrieval, Embedding & Reranking / 检索、嵌入与重排 → General / 综合

## Abstract / 摘要

Retrieval-Augmented Generation (RAG) has been empirically shown to enhance the performance of large language models (LLMs) in knowledge-intensive domains such as healthcare, finance, and legal contexts. Given a query, RAG retrieves relevant documents from a corpus and integrates them into the LLMs’ generation process. In this study, we investigate the adversarial robustness of RAG, focusing specifically on examining the retrieval system. First, across 225 different setup combinations of corpus, retriever, query, and targeted information, we show that retrieval systems are vulnerable to universal poisoning attacks in medical Q&A. In such attacks, adversaries generate poisoned documents containing a broad spectrum of targeted information, such as personally identifiable information. When these poisoned documents are inserted into a corpus, they can be accurately retrieved by any users, as long as attacker-specified queries are used. To understand this vulnerability, we discovered that the deviation from the query’s embedding to that of the poisoned document tends to follow a pattern in which the high similarity between the poisoned document and the query is retained, thereby enabling precise retrieval. Based on these findings, we develop a new detection-based defense to ensure the safe use of RAG. Through extensive experiments spanning various Q&A domains, we observed that our proposed method consistently achieves excellent detection rates in nearly all cases.
