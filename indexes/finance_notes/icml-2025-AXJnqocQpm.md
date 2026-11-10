# Quantifying Prediction Consistency Under Fine-tuning Multiplicity in Tabular LLMs

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：data points under actual fine-tuned multiplicity for several Existing approaches to measure multiplicity in machine datasets, namely, the German Credit, Bank, Heart, learning often involve retraining and ensembling multiple Car, Diabetes, and Adult datasets (Kahn; Hofmann, models (Marx et al., 2020). However, such approaches can 1994; Becker & Kohavi,

[Paper](https://openreview.net/forum?id=AXJnqocQpm)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Fine-tuning LLMs on tabular classification tasks can lead to the phenomenon of *fine-tuning multiplicity* where equally well-performing models make conflicting predictions on the same input. Fine-tuning multiplicity can arise due to variations in the training process, e.g., seed, weight initialization, minor changes to training data, etc., raising concerns about the reliability of Tabular LLMs in high-stakes applications such as finance, hiring, education, healthcare. Our work formalizes this unique challenge of fine-tuning multiplicity in Tabular LLMs and proposes a novel measure to quantify the consistency of individual predictions without expensive model retraining. Our measure quantifies a prediction's consistency by analyzing (sampling) the model's local behavior around that input in the embedding space. Interestingly, we show that sampling in the local neighborhood can be leveraged to provide probabilistic guarantees on prediction consistency under a broad class of fine-tuned models, i.e., inputs with sufficiently high local stability (as defined by our measure) also remain consistent across several fine-tuned models with high probability. We perform experiments on multiple real-world datasets to show that our local stability measure preemptively captures consistency under actual multiplicity across several fine-tuned models, outperforming competing measures.
