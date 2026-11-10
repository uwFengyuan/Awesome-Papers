# MCP-SafetyBench: A Benchmark for Safety Evaluation of Large Language Models with Real-World MCP Servers

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：We present **MCP-SafetyBench**, a comprehensive benchmark built on real MCP servers that supports realistic multi-turn evaluation across five domains—browser automation, financial analysis, location navigation, repository management, and web search.

[Paper](https://openreview.net/forum?id=7XYjeL46co)

Classification / 分类：Financial IR & RAG / 金融检索与RAG → Retrieval, Embedding & Reranking / 检索、嵌入与重排 → General / 综合

## Abstract / 摘要

Large language models (LLMs) are evolving into agentic systems that reason, plan, and operate external tools.  The Model Context Protocol (MCP) is a key enabler of this transition, offering a standardized interface for connecting LLMs with heterogeneous tools and services.  Yet MCP's openness and multi-server workflows introduce new safety risks that existing benchmarks fail to capture, as they focus on isolated attacks or lack real-world coverage.  We present **MCP-SafetyBench**, a comprehensive benchmark built on real MCP servers that supports realistic multi-turn evaluation across five domains—browser automation, financial analysis, location navigation, repository management, and web search.  It incorporates a unified taxonomy of 20 MCP attack types spanning server, host, and user sides, and includes tasks requiring multi-step reasoning and cross-server coordination under uncertainty.  Using MCP-SafetyBench, we systematically evaluate leading open- and closed-source LLMs, revealing that all models remain vulnerable to MCP attacks, with a notable safety-utility trade-off.  Our results highlight the urgent need for stronger defenses and establish MCP-SafetyBench as a foundation for diagnosing and mitigating safety risks in real-world MCP deployments. Our benchmark is available at https://github.com/xjzzzzzzzz/MCPSafety.
