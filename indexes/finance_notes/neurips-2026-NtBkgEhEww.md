# AgenticOCR: Parsing Only What You Need for Efficient Retrieval-Augmented Generation

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：standing. On FinRAGBench-V, the same configuration achieves 78.6 accuracy, outperforming all prior agentic frameworks. This highlights the effectiveness of our query-driven extraction paradigm in dense, visually complex financial documents. Strengths on Text, Layout, and Figure Modalities. AgenticOCR exhibits particularly strong per- formance on text-only (TXT), layout (LAY), and figure (FIG) subsets of MMLongBench-Doc. Our 8B 8 AgenticOCR: Parsing Only What You Need for Efficient Retrieval-Augmented Generation

[Paper](https://openreview.net/forum?id=NtBkgEhEww)

Classification / 分类：Financial IR & RAG / 金融检索与RAG → Retrieval, Embedding & Reranking / 检索、嵌入与重排 → General / 综合

## Abstract / 摘要

The expansion of retrieval-augmented generation (RAG) into multimodal domains has intensified the challenge for processing complex visual documents, such as financial reports. While page-level chunking and retrieval is a natural starting point, it creates a critical bottleneck: delivering entire pages to the generator introduces excessive extraneous context. This not only overloads the generator's attention mechanism but also dilutes the most salient evidence. Moreover, compressing these information-rich pages into a limited visual token budget further increases the risk of hallucinations. To address this, we introduce AgenticOCR, a dynamic parsing approach that extends optical character recognition (OCR) from a static, full-text process into a query-driven, on-demand extraction system. By autonomously analyzing document layout in a "thinking with images" manner, AgenticOCR identifies and selectively recognizes regions of interest. This approach performs on-demand decompression of visual tokens precisely where needed, effectively decoupling retrieval granularity from rigid page-level chunking. AgenticOCR has the potential to serve as the "third building block" of the visual document RAG stack, operating alongside and enhancing standard Embedding and Reranking modules. Experimental results demonstrate that AgenticOCR improves both the accuracy and efficiency of visual RAG systems with pixel-adaptive per-image token allocation (e.g., Qwen3.5 generator), achieving expert-level performance in long document understanding. Our repository is anonymously available at https://anonymous.4open.science/r/AgenticOCR.
