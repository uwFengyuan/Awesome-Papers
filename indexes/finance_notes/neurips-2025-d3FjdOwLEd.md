# Smooth Quadratic Prediction Markets

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：To motivate the application of the Smooth Quadratic Prediction Market, we independently examine agents' trading behavior under two realistic constraints: bounded budgets and buy-only securities.

[Paper](https://openreview.net/forum?id=d3FjdOwLEd)

Classification / 分类：Trading & Microstructure / 交易与市场微观结构 → Trading & Execution / 交易策略与执行 → General / 综合

## Abstract / 摘要

When agents trade in a Duality-based Cost Function prediction market, they collectively implement the learning algorithm Follow-The-Regularized-Leader [Abernethy et al., 2013]. We ask whether other learning algorithms could be used to inspire the design of prediction markets. By decomposing and modifying the Duality-based Cost Function Market Maker's (DCFMM) pricing mechanism, we propose a new prediction market, called the Smooth Quadratic Prediction Market, the incentivizes agents to collectively implement general steepest gradient descent. Relative to the DCFMM, the Smooth Quadratic Prediction Market has a better worst-case monetary loss for AD securities while preserving axiom guarantees such as the existence of instantaneous price, information incorporation, expressiveness, no arbitrage, and a form of incentive compatibility.  To motivate the application of the Smooth Quadratic Prediction Market, we independently examine agents' trading behavior under two realistic constraints: bounded budgets and buy-only securities.  Finally, we provide an introductory analysis of an approach to facilitate adaptive liquidity using the Smooth Quadratic Prediction Market. Our results suggest future designs where the price update rule is separate from the fee structure, yet guarantees are preserved.
