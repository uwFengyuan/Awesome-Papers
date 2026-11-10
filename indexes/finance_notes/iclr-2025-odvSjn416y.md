# Promptriever: Instruction-Trained Retrievers Can Be Prompted Like Language Models

ICLR 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：3.5 45.0 45.2 45.2 Dataset has dev/train set FEVER 48.1 7.4 45.3 82.9 85.3 85.3 82.8 82.8 82.8 FiQA 25.1 16.9 21.9 45.0 41.8 42.7 45.9 46.6 46.6 HotpotQA 56.9 54.6 54.6 68.8 66.4 67.9 69.2 69.5 69.5 NFCorpus 32.1 18.0 23.5 36.0 34.2 35.0 36.5 36.9 36.9

[Paper](https://openreview.net/forum?id=odvSjn416y)

Classification / 分类：Financial IR & RAG / 金融检索与RAG → Retrieval, Embedding & Reranking / 检索、嵌入与重排 → General / 综合

## Abstract / 摘要

Instruction-tuned language models (LM) are able to respond to imperative commands, providing a more natural user interface compared to their base counterparts. In this work, we present Promptriever, the first retrieval model able to be prompted like an LM. To train Promptriever, we curate and release a new instance-level instruction training set from MS MARCO, spanning nearly 500k instances. Promptriever not only achieves strong performance on standard retrieval tasks, but also follows instructions. We observe: (1) large gains (reaching SoTA) on following detailed relevance instructions (+14.3 p-MRR / +3.1 nDCG on FollowIR), (2) significantly increased robustness to lexical choices/phrasing in the query+instruction (+12.9 Robustness@10 on InstructIR), and (3) the ability to perform hyper-parameter search via prompting to reliably improve retrieval performance (+1.4 average increase on BEIR). Promptriever demonstrates that retrieval models can be controlled with prompts on a per-query basis, setting the stage for future work aligning LM prompting techniques with information retrieval.
