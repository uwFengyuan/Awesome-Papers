# $\tau$-Knowledge: Evaluating Conversational Agents over Unstructured Knowledge

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Our new domain, $\tau$-Banking, models realistic fintech customer support workflows in which agents must navigate roughly 700 interconnected knowledge documents while executing tool-mediated account updates.

[Paper](https://openreview.net/forum?id=XHZK5abtw2)

Classification / 分类：Banking & Customer Service / 银行业务与客户服务 → Banking Dialogue & Intent / 银行对话与意图 → General / 综合

## Abstract / 摘要

Conversational agents are increasingly deployed in knowledge-intensive settings, where correct behavior depends on retrieving and applying domain-specific knowledge from large, proprietary, and unstructured corpora during live interactions with users. Yet most existing benchmarks evaluate retrieval or tool use independently of each other, creating a gap in realistic, fully agentic evaluation over unstructured data in long-horizon interactions. We introduce $\tau$-Knowledge, an extension of $\tau$-Bench for evaluating agents in environments where success depends on coordinating external, natural-language knowledge with tool outputs to produce verifiable, policy-compliant state changes. Our new domain, $\tau$-Banking, models realistic fintech customer support workflows in which agents must navigate roughly 700 interconnected knowledge documents while executing tool-mediated account updates. Across embedding-based retrieval and terminal-based search, even frontier models with high reasoning budgets achieve only $\sim$25.5\% pass^1, with reliability degrading sharply over repeated trials. Agents struggle to retrieve the correct documents from densely interlinked knowledge bases and to reason accurately over complex internal policies. Overall, $\tau$-Knowledge provides a realistic testbed for developing agents that integrate unstructured knowledge in human-facing deployments.
