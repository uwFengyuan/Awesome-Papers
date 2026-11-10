# Evolving Quantitative Reasoning through Self-Play in Digital Twin Markets

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：All code and data are available at https://github.com/MTMQuantAI/Agent-Trading-Arena.git.

[Paper](https://openreview.net/forum?id=j4SxlIyvRg)

Classification / 分类：Trading & Microstructure / 交易与市场微观结构 → Trading & Execution / 交易策略与执行 → General / 综合

## Abstract / 摘要

Large language models (LLMs) demonstrate strong capabilities in high-level semantic reasoning and strategic planning, making them appealing for complex decision-making tasks; however, their quantitative reasoning remains unreliable despite recent progress in tool-augmented and structured inference. To address this limitation, we decouple reasoning from computation by assigning LLMs to planning, analysis, and result interpretation, while delegating numerical computation and statistical inference to specialized external tools. Rather than being hard-coded, these tools are constructed in a constrained and structured manner during planning as explicit intermediate reasoning artifacts, enabling adaptive and scenario-dependent quantitative reasoning. LLMs iteratively analyze tool outputs under diverse market conditions and leverage performance-based feedback to refine subsequent tool selection and construction, thereby forming a bounded self-evolving loop. We instantiate this process through self-play in a controllable digital twin market, DecoupledMarket, where LLM agents continuously test, compare, and adapt their strategies. By coupling high-level planning with robust quantitative execution, the proposed framework enhances the quantitative reliability of LLM-driven decision-making. All code and data are available at https://github.com/MTMQuantAI/Agent-Trading-Arena.git.
