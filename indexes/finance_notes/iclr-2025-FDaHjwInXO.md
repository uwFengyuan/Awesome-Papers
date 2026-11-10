# SV-RAG: LoRA-Contextualizing Adaptation of  MLLMs for Long Document Understanding

ICLR 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：et We train our Col-retrieval modules using the original training data of ColPali (Faysse et al., 2024), which includes 39,463, 10,074, 13,251, 10,000, and 45,940 question-page pairs filtered from DocVQA, InfoVQA (Mathew et al., 2022), TATDQA (Zhu et al., 2024), arXivQA (Li et al., 2024), and synthetic data across various topics, including government reports, healthcare, artificial intelligence, and energy. We incorporated DocMatix-IR (Ma et al., 2024b) and PFL- DocVQA (Tito et al., 2023b), using GPT-4o to filter out duplicate images and unsuitable questions. The expanded dataset improved top-1 retrieval accuracy on MMLongBench-Doc by ∼1% without affecting other benchmarks. We fine-tuned our QA modules using the trai

[Paper](https://openreview.net/forum?id=FDaHjwInXO)

Classification / 分类：Financial QA & Reasoning / 金融问答与数值推理 → Numerical & Table Reasoning / 数值与表格推理 → General / 综合

## Abstract / 摘要

Multimodal large language models (MLLMs) have recently shown great progress in text-rich image understanding, yet they still struggle with complex, multi-page visually-rich documents. Traditional methods using document parsers for retrieval-augmented generation suffer from performance and efficiency limitations, while directly presenting all pages to MLLMs leads to inefficiencies, especially with lengthy ones.  In this work, we present a novel framework named **S**elf-**V**isual **R**etrieval-**A**ugmented **G**eneration (SV-RAG), which can broaden horizons of *any* MLLM to support long-document understanding. We demonstrate that **MLLMs themselves can be an effective multimodal retriever** to fetch relevant pages and then answer user questions based on these pages. SV-RAG is implemented with two specific MLLM adapters, one for evidence page retrieval and the other for question answering. Empirical results show state-of-the-art performance on public benchmarks, demonstrating the effectiveness of SV-RAG.
