# ComplexMCP: Evaluation of LLM Agents in Dynamic, Interdependent, and Large-Scale Tool Sandbox

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Built on the Model Context Protocol (MCP), $\textbf{ComplexMCP}$ provides over 300 meticulously tested tools derived from 7 stateful sandboxes, ranging from office suites to financial systems.

[Paper](https://openreview.net/forum?id=3u1M9wokD7)

Classification / 分类：Financial Agents / 金融Agent与决策 → Investment & Financial Research Agents / 投研与金融决策Agent → General / 综合

## Abstract / 摘要

Current LLM agents are proficient at calling isolated APIs but struggle with the "last mile" of commercial software automation. In real-world scenarios, tools are not independent; they are atomic, interdependent, and prone to environmental noise. We introduce $\textbf{ComplexMCP}$, a benchmark designed to evaluate agents in these rigorous conditions. Built on the Model Context Protocol (MCP), $\textbf{ComplexMCP}$ provides over 300 meticulously tested tools derived from 7 stateful sandboxes, ranging from office suites to financial systems. Unlike existing datasets, our benchmark utilizes a seed-driven architecture to simulate dynamic environment states and unpredictable API failures, ensuring a deterministic yet diverse evaluation.  We evaluate various LLMs across full-context and RAG paradigms, revealing a stark performance gap: even top-tier models fail to exceed a 60% success rate, far trailing human performance 90%. Granular trajectory analysis identifies three fundamental bottlenecks: (1) $\textbf{tool retrieval saturation}$ as action spaces scale; (2) $\textbf{over-confidence}$, where agents skip essential environment verifications; and (3) $\textbf{strategic defeatism}$, a tendency to rationalize failure rather than pursuing recovery. These findings underscore the insufficiency of current agents for interdependent workflows, positioning $\textbf{ComplexMCP}$ as a critical testbed for the next generation of resilient autonomous systems. The codebase and benchmark implementation are publicly available at https://github.com/AIDC-AI/complex-mcp.
