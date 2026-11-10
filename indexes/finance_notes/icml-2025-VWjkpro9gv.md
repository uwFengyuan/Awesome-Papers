# Learning Monotonic Probabilities with a Generative Cost Model

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：AS dataset (Larson et al., 2016), y1 (denoted y1 ≺r.v. y2 ) if and only if Pr(y1 ≻ t) < the Diabetes dataset (Teboul), the Blog Feedback dataset Pr(y2 ≻ t) for any vector t ∈ Rn . (Buza, 2014), the Loan Defaulter dataset and the Auto MPG dataset (Quinlan, 1993). In most tasks, our model outper- forms existing approaches. Further ablation studies and time complexity analysis are available in the appendix. epiF1 The main contributions of our paper are summarized as follows: • We introduce a universal technique t

[Paper](https://openreview.net/forum?id=VWjkpro9gv)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

In many machine learning tasks, it is often necessary for the relationship between input and output variables to be monotonic, including both strictly monotonic and implicitly monotonic relationships. Traditional methods for maintaining monotonicity mainly rely on construction or regularization techniques, whereas this paper shows that the issue of strict monotonic probability can be viewed as a partial order between an observable revenue variable and a latent cost variable. This perspective enables us to reformulate the monotonicity challenge into modeling the latent cost variable. To tackle this, we introduce a generative network for the latent cost variable, termed the Generative Cost Model (**GCM**), which inherently addresses the strict monotonic problem, and propose the Implicit Generative Cost Model (**IGCM**) to address the implicit monotonic problem. We further validate our approach with a numerical simulation of quantile regression and conduct multiple experiments on public datasets, showing that our method significantly outperforms existing monotonic modeling techniques. The code for our experiments can be found at [https://github.com/tyxaaron/GCM](https://github.com/tyxaaron/GCM).
