# Hybrid Autoencoders for Tabular Data: Leveraging Model-Based Augmentation in Low-Label Settings

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据： 16400 93 5 PhishingWebsites (PW) 9200 30 2 adult (AD) 9200 14 2 albert categorical (ALB) 9200 25 2 bank-marketing (BM) 45200 16 2 covertype (CO) 283300 54 6 default-of-credit-card-clients categorical (CC) 5200 23 2 electricity (EL) 19240 11 2 helena (HE) 36260 27 13 higgs (HI) 470080 28 2 jannis (JA) 83600 54 4 numerai28.6 (NU) 9200 119 2 road-safety categorical (RS) 363240 67 2 volkret (VO) 14800 181 8 pol (PO) 15000 48 2 california (CA) 20634 8 2 eye movements (EM) 10935 27 3 Table D.1: Dataset statistics (classification): number of samples (N), features (F), and target classes (C). Dataset (Acronym) #Samples (N) #Features (F) yprop 4 1 (YP) 7,331 251 analcatdata supreme (AS) 4,052 7 visualizing soil (VS) 7,185 4 black fr

[Paper](https://openreview.net/forum?id=l5N0P1UJKP)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Deep neural networks often under-perform on tabular data due to their sensitivity to irrelevant features and a spectral bias toward smooth, low-frequency functions. These limitations hinder their ability to capture the sharp, high-frequency signals that often define tabular structure, especially under limited labeled samples. While self-supervised learning (SSL) offers promise in such settings, it remains challenging in tabular domains due to the lack of effective data augmentations. We propose a hybrid autoencoder that combines a neural encoder with an oblivious soft decision tree (OSDT) encoder, each guided by its own stochastic gating network that performs sample-specific feature selection. Together, these structurally different encoders and model-specific gating networks implement model-based augmentation, producing complementary input views tailored to each architecture. The two encoders, trained with a shared decoder and cross-reconstruction loss, learn distinct yet aligned representations that reflect their respective inductive biases. During training, the OSDT encoder (robust to noise and effective at modeling localized, high-frequency structure) guides the neural encoder toward representations more aligned with tabular data. At inference, only the neural encoder is used, preserving flexibility and SSL compatibility. Spectral analysis highlights the distinct inductive biases of each encoder. Our method achieves consistent gains in low-label classification and regression across diverse tabular datasets, outperforming deep and tree-based supervised baselines.
