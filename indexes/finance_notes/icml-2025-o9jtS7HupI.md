# HyperIV: Real-time Implied Volatility Smoothing

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：These key features -- rapid adaptation to market conditions, guaranteed absence of arbitrage, and minimal data requirements -- make HyperIV particularly valuable for real-time trading applications.

[Paper](https://openreview.net/forum?id=o9jtS7HupI)

Classification / 分类：Derivatives & Hedging / 衍生品定价与对冲 → Implied Volatility / 隐含波动率曲面 → General / 综合

## Abstract / 摘要

We propose HyperIV, a novel approach for real-time implied volatility smoothing that eliminates the need for traditional calibration procedures. Our method employs a hypernetwork to generate parameters for a compact neural network that constructs complete volatility surfaces within 2 milliseconds, using only 9 market observations. Moreover, the generated surfaces are guaranteed to be free of static arbitrage. Extensive experiments across 8 index options demonstrate that HyperIV achieves superior accuracy compared to existing methods while maintaining computational efficiency. The model also exhibits strong cross-asset generalization capabilities, indicating broader applicability across different market instruments. These key features -- rapid adaptation to market conditions, guaranteed absence of arbitrage, and minimal data requirements -- make HyperIV particularly valuable for real-time trading applications. We make code available at https://github.com/qmfin/hyperiv.
