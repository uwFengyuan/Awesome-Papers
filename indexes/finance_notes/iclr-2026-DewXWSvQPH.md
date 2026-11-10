# TimeSeriesExamAgent: Creating Time Series Reasoning Benchmarks at Scale

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Then, with $\texttt{TimeSeriesExamAgent}$, we scale our approach by automatically generating benchmarks from real-world datasets spanning healthcare, finance and weather domains.

[Paper](https://openreview.net/forum?id=DewXWSvQPH)

Classification / 分类：Time Series / 时间序列 → Generation & Simulation / 序列生成与仿真 → Generation / 生成

## Abstract / 摘要

Large Language Models (LLMs) have shown promising performance in time series modeling tasks, but do they truly understand time series data? While multiple benchmarks have been proposed to answer this fundamental question, most are manually curated and focus on narrow domains or specific skill sets. To address this limitation, we propose scalable methods for creating comprehensive time series reasoning benchmarks that combine the flexibility of templates with the creativity of LLM agents. We first develop $\texttt{TimeSeriesExam}$, a multiple-choice benchmark using synthetic time series to evaluate LLMs across five core reasoning categories: pattern recognition, noise understanding, similarity analysis, anomaly detection, and causality. Then, with $\texttt{TimeSeriesExamAgent}$, we scale our approach by automatically generating benchmarks from real-world datasets spanning healthcare, finance and weather domains. Through multi-dimensional quality evaluation, we demonstrate that our automatically generated benchmarks achieve diversity comparable to manually curated alternatives. However, our experiments reveal that LLM performance remains limited in both abstract time series reasoning and domain-specific applications, highlighting ongoing challenges in enabling effective time series understanding in these models. $\texttt{TimeSeriesExamAgent}$ is available at https://github.com/magwiazda/TimeSeriesExamAgent
