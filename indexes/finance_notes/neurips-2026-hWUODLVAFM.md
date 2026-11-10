# Neural Slack Variables for Shape Constraints

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Neural slack variables close the gap to hard constraints on monotonicity and low-dimensional convexity, and maintain effectiveness on nonlinear constraints in neural barrier certificates and no-arbitrage volatility surfaces.

[Paper](https://openreview.net/forum?id=hWUODLVAFM)

Classification / 分类：Derivatives & Hedging / 衍生品定价与对冲 → Implied Volatility / 隐含波动率曲面 → General / 综合

## Abstract / 摘要

Enforcing functional inequality constraints such as monotonicity and convexity in neural networks is a fundamental challenge in many industrial and scientific applications. Classical one-sided penalty methods, just like primal-dual methods gated by complementary slackness, provide gradients only at violated locations, resulting in fragile constraint satisfaction. Hard architectural constraints, on the other hand, cover only the simplest cases and tend to compromise the network's expressive power. We introduce *neural slack variables*, a deep learning-native primal-side approach that converts constraint enforcement into a two-sided regression problem by coupling the primary network with a jointly learned auxiliary network. The auxiliary network serves as a valid target for the primary network's constraint quantities, inducing feasibility and regularity. Theoretically, neural slack variables can be understood as a variable splitting method with parametrized variable projection. Neural slack variables close the gap to hard constraints on monotonicity and low-dimensional convexity, and maintain effectiveness on nonlinear constraints in neural barrier certificates and no-arbitrage volatility surfaces.
