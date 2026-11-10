# Multi-Scale Hypergraph Meets LLMs: Aligning Large Language Models for Time Series Analysis

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：earning. Detailed descriptions of M3 and M4 datasets are given as follows: • M3 datasets: The M3 datasets comprise 3,003 time series with varying granularities, including micro, industry, macro, and finance. It presents a diverse collection of seasonal and non-seasonal sequences, with frequencies spanning from yearly to monthly. • M4 datasets: The M4 datasets are larger than M3 datasets and expands the collection to 100,000 individual time series. The M4 datasets encompass a vast array of temporal patterns ac

[Paper](https://openreview.net/forum?id=SbBX2dCw3y)

Classification / 分类：Time Series / 时间序列 → Representation & Foundation Models / 表征与基础模型 → Foundation models / 基础模型

## Abstract / 摘要

Recently, there has been great success in leveraging pre-trained large language models (LLMs) for time series analysis. The core idea lies in effectively aligning the modality between natural language and time series. However, the multi-scale structures of natural language and time series have not been fully considered, resulting in insufficient utilization of LLMs capabilities. To this end, we propose MSH-LLM, a Multi-Scale Hypergraph method that aligns Large Language Models for time series analysis. Specifically, a hyperedging mechanism is designed to enhance the multi-scale semantic information of time series semantic space. Then, a cross-modality alignment (CMA) module is introduced to align the modality between natural language and time series at different scales. In addition, a mixture of prompts (MoP) mechanism is introduced to provide contextual information and enhance the ability of LLMs to understand the multi-scale temporal patterns of time series. Experimental results on 27 real-world datasets across 5 different applications demonstrate that MSH-LLM achieves the state-of-the-art results.
