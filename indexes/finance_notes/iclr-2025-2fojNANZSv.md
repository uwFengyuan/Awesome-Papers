# Mixture of In-Context Prompters for Tabular PFNs

ICLR 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：atasets ALL MixturePFN, CatBoost, ada-agnostic, australian, balance-scale, TabPFN*, XGBoost, colic, credit-approval, elevators, heart-h, ResNet, FTTransformer, jasmine, kc1, lymph, mfeat-fourier, mfeat-zernike, LightGBM, SAINT, monks-problems-2, phoneme, profb, NODE, MLP-rtdl, qsar-biodeg, socmob, speeddating, splice, vehicle RandomForest, TabNet, MLP, DecisionTree, LinearModel, STG, VIME, KNN, DANet, SVM Top-10 MixturePFN, CatBoost, ada-agnostic, artificial-characters, australian, TabPFN*, XGBoost, balance-scale, colic, credit-approval, elevators, ResNet, LightGBM, gesturephasesegmentationprocessed, heart-h, jasmine, SAINT, DANet, kc1, lymph, mfeat-fourier, mfeat-zernike, FTTransformer, SVM, monks-problems-2, phoneme, profb,

[Paper](https://openreview.net/forum?id=2fojNANZSv)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Recent benchmarks find In-Context Learning (ICL) outperforms both deep learning and tree-based algorithms on small tabular datasets. However, on larger datasets, ICL for tabular learning suffers in both efficiency and effectiveness. In terms of efficiency, transformers incur linear space and quadratic time complexity w.r.t. context size. In terms of effectiveness, contexts at inference encounter distribution shift compared to contexts from pretraining. We propose MixturePFN, which extends Sparse Mixture of Experts to the state-of-the-art ICL for tabular learning model. Specifically, MixturePFN finetunes a specialized ICL expert on each cluster of tabular data and routes new test samples to appropriate experts at inference. MixturePFN supports constant-size contexts by splitting large training datasets into more manageable clusters. MixturePFN addresses distribution shift by finetuning an expert on each training dataset cluster via bootstrapping. Extensive experimental results shows MixturePFN outperforms 19 baselines both in mean rank and as the Condorcet winner across 36 diverse tabular datasets under both accuracy and F1 score with statistical significance.
