# Clipped SGD Algorithms for Performative Prediction: Tight Bounds for Stochastic Bias and Remedies

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：p̄a 1 θP S = − 1−aβ , where p̄ = m Z̃ i=1 i is the sample mean. GiveMeSomeCredit (Kaggle, 2011) with m = 15776 samples and d = 10 features. We split the training/test sets We set p = 0.1, ε = 0.1, δ = 1/m, β ∈ {0.01, 0.05}, a =

[Paper](https://openreview.net/forum?id=wGq6WpfhFl)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

This paper studies the convergence of clipped stochastic gradient descent (SGD) algorithms with decision-dependent data distribution. Our setting is motivated by privacy preserving optimization algorithms that interact with performative data where the prediction models can influence future outcomes. This challenging setting involves the non-smooth clipping operator and non-gradient dynamics due to distribution shifts. We make two contributions in pursuit for a performative stable solution with these algorithms. First, we characterize the stochastic bias with projected clipped SGD (PCSGD) algorithm which is caused by the clipping operator that prevents PCSGD from reaching a stable solution. When the loss function is strongly convex, we quantify the lower and upper bounds for this stochastic bias and demonstrate a bias amplification phenomenon with the sensitivity of data distribution. When the loss function is non-convex, we bound the magnitude of stationarity bias. Second, we propose remedies to mitigate the bias either by utilizing an optimal step size design for PCSGD, or to apply the recent DiceSGD algorithm [Zhang et al., 2024]. Our analysis is also extended to show that the latter algorithm is free from stochastic bias in the performative setting. Numerical experiments verify our findings.
