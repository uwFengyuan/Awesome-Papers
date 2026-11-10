# Small Models are LLM Knowledge Triggers for Medical Tabular Prediction

ICLR 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：0.57 https://www.kaggle.com/datasets/serhathoca/anemia-disease Churn Modeling - 10000 10 0.26 - Give Me Some Credit - 16714 10 1.00 https://www.kaggle.com/c/GiveMeSomeCredit US Adult Income - 48842 14 0.31 https://www.kaggle.com/datasets/johnolafenwa/us-census-data Table 6: Detailed data information of used tabular datasets (10 from the medical domain and 3 from others). “P/N” denotes the amount ratio of positive samples and negative ones. C R ESULTS ON C LINICAL T RIAL DATASET

[Paper](https://openreview.net/forum?id=WoPovNkM5h)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Recent development in large language models (LLMs) has demonstrated impressive domain proficiency on unstructured textual or multi-modal tasks. However, despite with intrinsic world knowledge, their application on structured tabular data prediction still lags behind, primarily due to the numerical insensitivity and modality discrepancy that brings a gap between LLM reasoning and statistical tabular learning. Unlike textual or vision data (e.g., electronic clinical notes or medical imaging data), tabular data is often presented in heterogeneous numerical values (e.g., CBC reports). This ubiquitous data format requires intensive expert annotation, and its numerical nature limits LLMs' capability to effectively transfer untapped domain expertise. In this paper, we propose SERSAL, a general self-prompting method by synergy learning with small models to enhance LLM tabular prediction in an unsupervised manner. Specifically, SERSAL utilizes the LLM's prior outcomes as original soft noisy annotations, which are dynamically leveraged to teach a better small student model. Reversely, the outcomes from the trained small model are used to teach the LLM to further refine its real capability. This process can be repeatedly applied to gradually distill refined knowledge for continuous progress. Comprehensive experiments on widely used medical domain tabular datasets show that, without access to gold labels, applying SERSAL to OpenAI GPT reasoning process attains substantial improvement compared to linguistic prompting methods, which serves as an orthogonal direction for tabular LLM, and increasing prompting bonus is observed as more powerful LLMs appear. Codes are available at https://github.com/jyansir/sersal.
