# Cascaded Flow Matching for Heterogeneous Tabular Data with Mixed-Type Features

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：bCascade’s ability to explicitly datasets from the TabZilla tabular data benchmark (McEl- incorporate mixed-type feature distributions greatly fresh et al., 2023), including airlines, credit_g, improves the sample quality for numerical features over electricity, kc1 and phoneme. The selected the baselines. The average WD decreases by more than datasets include inflated values. The missing values are 50% relative to the best baseline. For categorical features, added (10%) via a simulated MNAR mechanism (Muzellec it perf

[Paper](https://openreview.net/forum?id=l2ywV9sV0L)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Advances in generative modeling have recently been adapted to tabular data containing discrete and continuous features.  However, generating mixed-type features that combine discrete states with an otherwise continuous distribution in a single feature remains challenging. We advance the state-of-the-art in diffusion models for tabular data with a cascaded approach. We first generate a low-resolution version of a tabular data row, that is, the collection of the purely categorical features and a coarse categorical representation of numerical features. Next, this information is leveraged in the high-resolution flow matching model via a novel guided conditional probability path and data-dependent coupling. The low-resolution representation of numerical features explicitly accounts for discrete outcomes, such as missing or inflated values, and therewith enables a more faithful generation of mixed-type features. We formally prove that this cascade tightens the transport cost bound. The results indicate that our model generates significantly more realistic samples and captures distributional details more accurately, for example, the detection score improves by 51.9%. Code is available at https://github.com/muellermarkus/tabcascade.
