# Implicit Generative Copulas

NeurIPS 2021 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：A popular remedy is to construct a tree-based hierarchy of conditional bivariate copulas.In this paper, we propose a flexible, yet conceptually simple alternative based on implicit generative neural networks.The key challenge is to ensure marginal uniformity of the estimated copula distribution.We achieve this by learning a multivariate latent distribution with unspecified marginals but the desired dependency structure.By applying the probability integral transform, we can then obtain samples from the high-dimensional copula distribution without relying on parametric assumptions or the need to find a suitable tree structure.Experiments on synthetic and real data from finance, physics, and image generation demonstrate the performance of this approach.

[Paper](https://openreview.net/forum?id=h1bPe7spQkr)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Financial Risk / 金融风险管理 → General / 综合

## Abstract / 摘要

Copulas are a powerful tool for modeling multivariate distributions as they allow to separately estimate the univariate marginal distributions and the joint dependency structure. However, known parametric copulas offer limited flexibility especially in high dimensions, while commonly used non-parametric methods suffer from the curse of dimensionality. A popular remedy is to construct a tree-based hierarchy of conditional bivariate copulas.In this paper, we propose a flexible, yet conceptually simple alternative based on implicit generative neural networks.The key challenge is to ensure marginal uniformity of the estimated copula distribution.We achieve this by learning a multivariate latent distribution with unspecified marginals but the desired dependency structure.By applying the probability integral transform, we can then obtain samples from the high-dimensional copula distribution without relying on parametric assumptions or the need to find a suitable tree structure.Experiments on synthetic and real data from finance, physics, and image generation demonstrate the performance of this approach.
