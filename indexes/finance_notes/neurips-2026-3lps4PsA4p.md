# Dynamic Dual-Feedback Conformal Inference for Time Series Forecasting

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：iance penalty bounded by O(ϵ/ (w)). 5 Experiments 5.1 Settings Datasets. Three synthetic datasets (described in the Section 5.2.1) and five public datasets are used to evaluate methods (Google/Amazon/Microsoft stock price, Delhi temperature and Electricity, described in the Appendix B.1). Due to the limit of pages, the results and analysis for Delhi temperature and Electricity datasets are given in the Appendix B.2.1. Underlying Time Series Forecasting Algorithms. Four algorithms are used: Prophet [39], AutoRe- gressive (AR) [14], Theta [8] and Transformer [41]. Th

[Paper](https://openreview.net/forum?id=3lps4PsA4p)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Quantifying uncertainty in time series forecasting is particularly demanding because sequential data exhibit temporal dependence and are prone to distributional changes. Conformal inference has emerged as a powerful uncertainty quantification approach through the construction of prediction sets. Recent advances have introduced online conformal methods that adaptively adjust prediction thresholds through feedback mechanisms. However, the existing feedback mechanism typically relies solely on miscoverage indicators (actual feedback)—whether the true label falls within the interval at each time step—while overlooking the empirical prediction threshold (estimated feedback) that is derived from the oracle conformal method. In this paper, we propose $\textit{Dynamic Dual-feedback Conformal Inference}$ (DDCI), which incorporates a dual-feedback mechanism consisting of $\textit{actual feedback}$ and $\textit{estimated feedback}$. The former drives the primary adjustment of the intervals based on true observations, while the latter dampens excessive expansions or contractions by leveraging empirical thresholds from conformal inference during updates. By balancing these two signals, DDCI achieves more stable and narrower prediction intervals in sequential settings while adhering to the target coverage rate in practice.
