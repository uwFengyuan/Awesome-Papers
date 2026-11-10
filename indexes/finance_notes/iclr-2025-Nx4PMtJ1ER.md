# Signature Kernel Conditional Independence Tests in Causal Discovery for Stochastic Processes

ICLR 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：8 ± 293 7799 ± 250 SCOTCH 558 ± 14 1861 ± 43 8567 ± 63 35467 ± 833 105165 ± 10934 B.7 R EAL -W ORLD PAIRS T RADING E XAMPLE In the pairs trading experiment, stock price data is downloaded from Yahoo Finance for a predefined list of stocks over a specific period, divided into training (1st January 2010 to 31st December 2011) and trading intervals (1st January 2012 to 31st December 2012). The chose stocks are Trinity Industries (TRN), Brandywine Realty Trust (BDN), Commercial Metals Company (CMC), The New York Times Company (NYT), New York Community Bancorp (NYCB), The Wendy’s Company (WEN), CNX Resources Corporation (CNX). Logarithms of the stock prices are computed to stabilize variance and normalize the prices. During the t

[Paper](https://openreview.net/forum?id=Nx4PMtJ1ER)

Classification / 分类：Time Series / 时间序列 → Causality & Dynamics / 序列因果与动力学 → General / 综合

## Abstract / 摘要

Inferring the causal structure underlying stochastic dynamical systems from observational data holds great promise in domains ranging from science and health to finance. Such processes can often be accurately modeled via stochastic differential equations (SDEs), which naturally imply causal relationships via `which variables enter the differential of which other variables'. In this paper, we develop conditional independence (CI) constraints on coordinate processes over selected intervals that are Markov with respect to the acyclic dependence graph (allowing self-loops) induced by a general SDE model. We then provide a sound and complete causal discovery algorithm, capable of handling both fully and partially observed data, and uniquely recovering the underlying or induced ancestral graph by exploiting time directionality assuming a CI oracle. Finally, to make our algorithm practically usable, we also propose a flexible, consistent signature kernel-based CI test to infer these constraints from data. We extensively benchmark the CI test in isolation and as part of our causal discovery algorithms, outperforming existing approaches in SDE models and beyond.
