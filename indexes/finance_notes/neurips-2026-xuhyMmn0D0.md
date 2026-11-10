# Market Regime Council for Dynamic Credit Assignment in Multi-Agent LLM  Decision Systems

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Multi-agent LLM decision systems for portfolio management still lack a principled way to assign credit across specialist agents, remain vulnerable to cold-start dominance under regime shifts, and offer limited transparency into how final allocations are formed.

[Paper](https://openreview.net/forum?id=xuhyMmn0D0)

Classification / 分类：Portfolio & Investment / 投资组合与投资管理 → Portfolio Selection & Optimization / 组合选择与优化 → General / 综合

## Abstract / 摘要

Multi-agent LLM decision systems for portfolio management still lack a principled way to assign credit across specialist agents, remain vulnerable to cold-start dominance under regime shifts, and offer limited transparency into how final allocations are formed.  We propose Market Regime Council (MRC), a cooperative multi-agent decision system that computes exact Shapley credits across all single, pairwise, and Grand-coalition outputs for online agent weighting. Instantiated with $N{=}3$ specialist agents, at each trading period, MRC recomputes coalition-based Shapley weights from exponentially weighted performance histories, uses a Bayesian adaptive mixture to stabilize early periods, applies regime-dependent multipliers to adjust agent authority, and records each rebalance through a five-layer causal trace. Over 1,037 trading days across 13 crypto assets and five seeds, MRC achieves a Sharpe ratio of 1.51 and a cumulative return of 440.1\%, ranking first on CR, SR, and IR among active baselines and attaining the lowest MDD among active methods. Ablation results show that the gains come from Shapley-weighted integration across coalition outputs rather than from any single stage in isolation. Code and demo data are included in the supplementary material.
