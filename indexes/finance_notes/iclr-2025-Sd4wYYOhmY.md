# TabM: Advancing tabular deep learning with parameter-efficient ensembling

ICLR 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：TabM†mini 1.7799 ± 0.0859 1.7560 ± 0.0795 30 Published as a conference paper at ICLR 2025 cpu act ↓ bank-marketing ↑ Method Single model Ensemble Method Single model Ensemble MLP 2.6814 ± 0.2291 2.4953 ± 0.1150 MLP 0.7860 ± 0.0057 0.7887 ± 0.0052 TabPFN – – TabPFN – 0.7894 ± 0.0091 ResNet 2.3933 ± 0.0641 2.3005 ± 0.0397 ResNet

[Paper](https://openreview.net/forum?id=Sd4wYYOhmY)

Classification / 分类：Banking & Customer Service / 银行业务与客户服务 → Bank Marketing & Churn / 银行营销与客户流失 → General / 综合

## Abstract / 摘要

Deep learning architectures for supervised learning on tabular data range from simple multilayer perceptrons (MLP) to sophisticated Transformers and retrieval-augmented methods.This study highlights a major, yet so far overlooked opportunity for substantially improving tabular MLPs; namely, parameter-efficient ensembling -- a paradigm for imitating an ensemble of models with just one model.We start by describing TabM -- a simple model based on MLP and BatchEnsemble (an existing technique), improved with our custom modifications.Then, we perform a large scale evaluation of tabular DL architectures on public benchmarks in terms of both task performance and efficiency, which renders the landscape of tabular DL in a new light.In particular, we find that TabM outperforms prior tabular DL models, while the complexity of attention- and retrieval-based methods does not pay off.Lastly, we conduct a detailed empirical analysis, that sheds some light on the high performance of TabM.For example, we show that parameter-efficient ensembling is not an arbitrary trick, but rather a highly effective way to reduce overfitting and improve optimization dynamics of tabular MLPs.Overall, our work brings an impactful technique to tabular DL, analyses its behaviour, and advances the performance-efficiency tradeoff with TabM -- a simple and powerful baseline for researchers and practitioners.
