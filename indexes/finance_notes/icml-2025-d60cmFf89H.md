# TabFlex: Scaling Tabular Learning to Millions with Linear Attention

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：0.15 0.08 0.10 0.09 AUC 0.89 0.89 0.90 0.89 bank-marketing Time (s) 1.75 0.25 2.43 1.67 Low-Dimensional & Large AUC 0.94 0.94 0.95 0.94 elevators

[Paper](https://openreview.net/forum?id=d60cmFf89H)

Classification / 分类：Banking & Customer Service / 银行业务与客户服务 → Bank Marketing & Churn / 银行营销与客户流失 → General / 综合

## Abstract / 摘要

Leveraging the in-context learning (ICL) capability of Large Language Models (LLMs) for tabular classification has gained significant attention for its training-free adaptability across diverse datasets. Recent advancements, like TabPFN, excel in small-scale tabular datasets but struggle to scale for large and complex datasets. Our work enhances the efficiency and scalability of TabPFN for larger datasets by incorporating linear attention mechanisms as a scalable alternative to complexity-quadratic self-attention. Our model, TabFlex, efficiently handles tabular datasets with thousands of features and hundreds of classes, scaling seamlessly to millions of samples. For instance, TabFlex processes the poker-hand dataset with over a million samples in just 5 seconds. Our extensive evaluations demonstrate that TabFlex can achieve over a 2× speedup compared to TabPFN and a 1.5× speedup over XGBoost, outperforming 25 tested baselines in terms of efficiency across a diverse range of datasets. Furthermore, TabFlex remains highly effective on large-scale datasets, delivering strong performance with significantly reduced computational costs, especially when combined with data-efficient techniques such as dimensionality reduction and data sampling.
