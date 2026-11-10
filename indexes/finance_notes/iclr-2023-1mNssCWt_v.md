# STaSy: Score-based Tabular data Synthesis

ICLR 2023 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：is a binary classification dataset collected from European cardholders for credit card fraud detection. • Default (Lichman, 2013) is a binary classification dataset describing the information on credit card clients in Taiwan regarding default payments. • HTRU (Lyon, 2017) is a binary classification dataset that describes a sample of pulsar candidates collected during the High Time Resolution Universe Survey. • Magic (Bock, 2007) is a binary classification dataset that simulates the registration of high-energy gamma par

[Paper](https://openreview.net/forum?id=1mNssCWt_v)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Tabular data synthesis is a long-standing research topic in machine learning. Many different methods have been proposed over the past decades, ranging from statistical methods to deep generative methods. However, it has not always been successful due to the complicated nature of real-world tabular data. In this paper, we present a new model named $\textbf{S}$core-based $\textbf{Ta}$bular data $\textbf{Sy}$nthesis ($\texttt{STaSy}$) and its training strategy based on the paradigm of score-based generative modeling. Despite the fact that score-based generative models have resolved many issues in generative models, there still exists room for improvement in tabular data synthesis. Our proposed training strategy includes a self-paced learning technique and a fine-tuning strategy, which further increases the sampling quality and diversity by stabilizing the denoising score matching training. Furthermore, we also conduct rigorous experimental studies in terms of the generative task trilemma: sampling quality, diversity, and time. In our experiments with 15 benchmark tabular datasets and 7 baselines, our method outperforms existing methods in terms of task-dependant evaluations and diversity.
