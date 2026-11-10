# MarketSim: Simulating Stock Markets with Large-Scale Generative Agents

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Stock markets are one of the most complex systems in the modern world, where prices emerge from billions of decentralized interactions among heterogeneous participants in an ever-evolving information landscape. / To this end, we propose MarketSim, a large-scale stock market simulation framework with generative agents. / To evaluate our proposed MarketSim, we develop a comprehensive benchmark that includes stocks from 8 GICS sectors and 3 representative real-world scenarios, along with 5 stylized facts for market complexity and 5 price-related statistical metrics.

[Paper](https://openreview.net/forum?id=EzpJxPDqXB)

Classification / 分类：Trading & Microstructure / 交易与市场微观结构 → Market Simulation / 金融市场仿真 → General / 综合

## Abstract / 摘要

Stock markets are one of the most complex systems in the modern world, where prices emerge from billions of decentralized interactions among heterogeneous participants in an ever-evolving information landscape. While high-fidelity simulation is important for understanding market dynamics, existing approaches face a persistent trade-off between structural and behavioral fidelity. To this end, we propose MarketSim, a large-scale stock market simulation framework with generative agents. MarketSim introduces a hierarchical multi-agent architecture that decouples strategic reasoning from high-frequency execution, enabling LLM agents to operate in a nanosecond-resolution, NASDAQ-like continuous double auction market. Building on this, we simulate over 15,000 heterogeneous market participants whose interactions shape and are shaped by an evolving market environment grounded in more than 12k real-world news articles, policy documents, and earnings reports. To evaluate our proposed MarketSim, we develop a comprehensive benchmark that includes stocks from 8 GICS sectors and 3 representative real-world scenarios, along with 5 stylized facts for market complexity and 5 price-related statistical metrics. Extensive experiments demonstrate that MarketSim not only captures key complexity properties of real-world markets, but also outperforms state-of-the-art baselines in tracking high-frequency price dynamics with an average MAPE of 3.48%, providing a scalable testbed for market analysis.
