# SRT: Super-Resolution for Time Series via Disentangled Rectified Flow

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：ily spot prices for gold, crude oil, and natural gas. For all commodities, data is collected for all trading days within the period from June 15, 2022 to June 13, 2025. Currency rate. We select daily exchange rates of major currency pairs against the US dollar, in- cluding EUR/USD, JPY/USD, GBP/USD, CNY/USD, AUD/USD, CAD/USD, and CHF/USD. His- torical data from June 15, 2020 to June 13, 2025 is collected, corresponding to trading days within this period. Power. The public dataset ‘ElectricityLoadDiagrams20112014’ 3 is utilized. We follow the idea of Informer and preprocess the dataset into hourly format. Retail. The public dat

[Paper](https://openreview.net/forum?id=I94Eg6cu7P)

Classification / 分类：Time Series / 时间序列 → General Time-Series Methods / 综合序列方法 → Foundation models / 基础模型

## Abstract / 摘要

Fine-grained time series data with high temporal resolution is critical for accurate analytics across a wide range of applications. However, the acquisition of such data is often limited by cost and feasibility. This problem can be tackled by reconstructing high-resolution signals from low-resolution inputs based on specific priors, known as super-resolution. While extensively studied in computer vision, directly transferring image super-resolution techniques to time series is not trivial. To address this challenge at a fundamental level, we propose **S**uper-**R**esolution for **T**ime series (SRT), a novel framework that reconstructs temporal patterns lost in low-resolution inputs via disentangled rectified flow. SRT decomposes the input into trend and seasonal components, aligns them to the target resolution using an implicit neural representation, and leverages a novel cross-resolution attention mechanism to guide the generation of high-resolution details. We further introduce SRT-large, a scaled-up version with extensive pretraining, which enables strong zero-shot super-resolution capability. Extensive experiments on nine public datasets demonstrate that SRT and SRT-large consistently outperform existing methods across multiple scale factors, showing both robust performance and the effectiveness of each component in our architecture.
