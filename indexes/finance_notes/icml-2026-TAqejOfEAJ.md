# Equilibrium Pricing in Oligopolistic Data Markets

ICML 2026 · main · Long

[Long] [Main] [Oral] [Poster] [Finance]

Financial evidence / 金融依据：ding the relaxation in both theory and practice. 4. Finally, we run some empirics to show the robustness of our results. We simulate a news data marketplace where n firms purchase data from m news agencies to predict stock price movements, from a real-world dataset [1]. Each firm evaluates the informativeness of a dataset by training a logistic regression model on historical news and measuring prediction error. Sellers update their pricing strategies via an inertial approximate best-response dynamics (defined in Section 6). Empirically, the dynamics converge e

[Paper](https://openreview.net/forum?id=TAqejOfEAJ)

Classification / 分类：Market Prediction / 股价、收益与波动率预测 → Stock Movement & Returns / 股价方向与收益预测 → General / 综合

## Abstract / 摘要

We study equilibrium pricing in oligopolistic data markets with budget-constrained buyers (e.g., ML companies purchasing data to improve model accuracy) and strategic data sellers. Sellers compete by setting prices for their datasets, giving rise to a pricing game whose pure Nash equilibria correspond to equilibrium prices. While equilibrium prices are guaranteed for rivalrous goods via competitive equilibrium, we show that the non-rivalry of data fundamentally alters this picture: an exact Nash equilibrium need not exist, and in fact no 1.364-approximate equilibrium exists under uniform pricing. We therefore investigate relaxed equilibrium notions. Allowing sellers to use beyond-uniform pricing—specifically, piecewise-linear convex pricing functions—guarantees approximate stability within a constant factor: there exists a pricing profile in which no seller can improve revenue by a factor of two by deviating to any uniform price (a 2-approximate Nash equilibrium). Finally, our simulations demonstrate fast convergence and empirical approximation guarantees that outperform the worst-case bound of 2.
