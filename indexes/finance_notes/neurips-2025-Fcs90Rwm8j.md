# Win Fast or Lose Slow: Balancing Speed and Accuracy in Latency-Sensitive Decisions of LLMs

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：However, many real-world applications, such as high-frequency trading and real-time competitive gaming, require decisions under strict latency constraints, where faster responses directly translate into higher rewards. / To support our investigation, we introduce two new benchmarks: HFTBench, a high-frequency trading simulation, and StreetFighter, a competitive gaming platform. / Our method achieves the best performance on both benchmarks, improving win rate by up to 80% in Street Fighter and boosting daily yield by up to 26.52% in trading,  underscoring the need for latency-aware evaluation and deployment strategies for LLM-based agents.

[Paper](https://openreview.net/forum?id=Fcs90Rwm8j)

Classification / 分类：Trading & Microstructure / 交易与市场微观结构 → Trading & Execution / 交易策略与执行 → General / 综合

## Abstract / 摘要

Large language models (LLMs) have shown remarkable performance across diverse reasoning and generation tasks, and are increasingly deployed as agents in dynamic environments such as code generation and recommendation systems. However, many real-world applications, such as high-frequency trading and real-time competitive gaming, require decisions under strict latency constraints, where faster responses directly translate into higher rewards. Despite the importance of this latency–quality trade-off, it remains underexplored in the context of LLM-based agents. In this work, we present the first systematic study of this trade-off in real-time decision-making tasks. To support our investigation, we introduce two new benchmarks: HFTBench, a high-frequency trading simulation, and StreetFighter, a competitive gaming platform. Our analysis reveals that optimal latency–quality balance varies by task, and that sacrificing quality for lower latency can significantly enhance downstream performance. To address this, we propose FPX, an adaptive framework that dynamically selects model size and quantization level based on real-time demands. Our method achieves the best performance on both benchmarks, improving win rate by up to 80% in Street Fighter and boosting daily yield by up to 26.52% in trading,  underscoring the need for latency-aware evaluation and deployment strategies for LLM-based agents. These results demonstrate the critical importance of latency-aware evaluation and deployment strategies for real-world LLM-based agents.
