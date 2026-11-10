# TimeTok: Granularity-Controllable Time-Series Generation via Hierarchical Tokenization

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：tive 2 1 Token 2 Tokens 4 Tokens 8 Tokens 16 Tokens 32 Tokens 64 Tokens 128 Tokens Ground Truth ECG5000 Nasdaq Figure 1: Visualization at Different Granularity. TimeTok encodes time series into a hierarchically ordered sequence of discrete tokens that progressively capture coarse-to-fine temporal granularities. We visualize samples from the medical (i.e., ECG) and finance domain (i.e., Nasdaq stock data); additional results in Section E. Table 1: Contr

[Paper](https://openreview.net/forum?id=P8dX5r550k)

Classification / 分类：Time Series / 时间序列 → Representation & Foundation Models / 表征与基础模型 → Generation / 生成

## Abstract / 摘要

Time-series data are inherently multiscale, spanning diverse temporal granularities from coarse trends to fine-scale dynamics. However, existing time-series generative models provide limited control over the temporal granularity of both inputs and outputs, restricting their ability to condition on user-provided coarse sketches and generate samples at a desired target granularity. To address this, we introduce TimeTok, a unified framework for Granularity-Controllable Time-Series Generation (GC-TSG), which generates time series at $any$ target granularity from $any$ coarser input (e.g., rough sketches) or without conditioning. At the core of TimeTok is a hierarchical tokenization strategy that maps time series into an ordered sequence of tokens, from coarse to fine temporal granularity. Our autoregressive generation process operates across these granularity levels, producing token blocks that are decoded back into continuous time series. This design naturally enables GC-TSG within a single framework, where controlling the number of token blocks provides explicit control over output detail. Experiments show that TimeTok excels at GC-TSG tasks while achieving state-of-the-art performance in standard generation. Furthermore, we showcase TimeTok's potential as a foundational tokenizer by training on multiple datasets with heterogeneous temporal granularities, verifying strong transferability that consistently outperforms models trained on individual datasets. To our knowledge, this is the first unified framework that covers the full generative spectrum for time series, offering a valuable foundation for models that benefit from diverse temporal granularities.
