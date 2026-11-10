# Online Conformal Prediction via Universal Portfolio Algorithms

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：he target miscoverage rate α is typically chosen to be small (e.g., α = 0.05 or 0.01), implying that the positive and negative subgradients of the losses are very different. Instead, we propose reducing our problem to a portfolio selection problem, and leveraging the Universal Portfolio (UP) algorithm [Cover and Ordentlich, 2002] for OCP. In the following, we explain how UP methods lead to optimal solutions to online learning problems with asymmetric subgradients. For our reduction, considering pinball losses, we construct a market with two synthetic stocks, whose market gains ar

[Paper](https://openreview.net/forum?id=EKmiOtjZjI)

Classification / 分类：Time Series / 时间序列 → Probabilistic Forecasting & Calibration / 概率预测与校准 → General / 综合

## Abstract / 摘要

Online conformal prediction (OCP) seeks prediction intervals that achieve long-run $1-\alpha$ coverage for arbitrary (possibly adversarial) data streams, while remaining as informative as possible. Existing OCP methods often require manual learning-rate tuning to work well, and may also require algorithm-specific analyses. Here, we develop a general regret-to-coverage theory for interval-valued OCP based on the $(1-\alpha)$-pinball loss. Our first contribution is to identify *linearized regret* as a key notion, showing that controlling it implies coverage bounds for any online algorithm. This relies on a black-box reduction that depends only on the Fenchel conjugate of an upper bound on the linearized regret. Building on this theory, we propose UP-OCP, a parameter-free method for OCP, via a reduction to a two-asset portfolio selection problem, leveraging universal portfolio algorithms. We show strong finite-time bounds on the miscoverage of UP-OCP, even for polynomially growing predictions. Extensive experiments support that UP-OCP delivers consistently better size/coverage trade-offs than prior online conformal baselines.
