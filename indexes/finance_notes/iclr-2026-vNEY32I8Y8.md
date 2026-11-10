# LightRetriever: A LLM-based Text Retrieval Architecture with Extremely Faster Query Inference

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：uses the preprocessed fine-tuning data from tDRO (Ma et al., 2025) and Sentence Transformers Training Data. English datasets include Amazon Review (Ni et al., 2019), Eli5 (Fan et al., 2019), FEVER (Thorne et al., 2018), FiQA (Maia et al., 2018), GooAQ (Khashabi et al., 2021), HotpotQA (Yang et al., 2018b), MSMARCO (Nguyen et al., 2016), NFCorpus (Boteva et al., 2016), NPR (Lucas et al., 2023), NQ (Kwiatkowski et al., 2019), PAQ (Lewis et al., 2021), Quora Duplicates (Iyer et al., 2017), S2ORC (Lo et al., 2020), Scifact (Wadden et al., 2020), Specter (Co- han et al., 2

[Paper](https://openreview.net/forum?id=vNEY32I8Y8)

Classification / 分类：Financial IR & RAG / 金融检索与RAG → Retrieval, Embedding & Reranking / 检索、嵌入与重排 → General / 综合

## Abstract / 摘要

Large Language Models (LLMs)-based text retrieval retrieves documents relevant to search queries based on vector similarities. Documents are pre-encoded offline, while queries arrive in real-time, necessitating an efficient online query encoder. Although LLMs significantly enhance retrieval capabilities, serving deeply parameterized LLMs slows down query inference throughput and increases demands for online deployment resources. In this paper, we propose LightRetriever, a novel LLM-based retriever with extremely lightweight query encoders. Our method retains a full-sized LLM for document encoding, but reduces the workload of query encoding to no more than an embedding lookup. Compared to serving a full LLM on an A800 GPU, our method achieves over a thousand times of speedup in query encoding and over 10× increase in end-to-end retrieval throughput. Extensive experiments on large-scale retrieval benchmarks show that LightRetriever generalizes well across diverse tasks, maintaining an average of 95% retrieval performance.
