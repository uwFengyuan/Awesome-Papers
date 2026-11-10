# TabReD: Analyzing Pitfalls and Filling the Gaps in Tabular Deep Learning Benchmarks

ICLR 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：96 Kaggle Insurance plan acceptance prediction Ecom Offers 106K 119 Kaggle Predict whether a user will redeem an offers HomeCredit Default 381K (1.5M) 696 Kaggle Loan default prediction Cooking Time 228K (10.6M) 195 New Restaurant order cooking time estimation Delivery ETA 224K (6.9M) 225 New Grocery delivery courier ETA prediction Maps Routing 192K (8.8M) 1026 New Navigation app ETA from live road-graph features Weather 605K (6.0M) 98 New Weather prediction (temperature) 4.1 O N THE ROLE AND LIMITATIONS OF TAB R E D We see our TabReD benchmark as an important addition to the landscape of tabular datasets. TabReD has the properties that are underrepresented in current benchmarks, including the time-based splits and the “feature-

[Paper](https://openreview.net/forum?id=L14sqcrUC3)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Credit Scoring & Default / 信用评分与违约 → General / 综合

## Abstract / 摘要

Advances in machine learning research drive progress in real-world applications. To ensure this progress, it is important to understand the potential pitfalls on the way from a novel method's success on academic benchmarks to its practical deployment. In this work, we analyze existing tabular deep learning benchmarks and find two common characteristics of tabular data in typical industrial applications that are underrepresented in the datasets usually used for evaluation in the literature.First, in real-world deployment scenarios, distribution of data often changes over time. To account for this distribution drift, time-based train/test splits should be used in evaluation. However, existing academic tabular datasets often lack timestamp metadata to enable such evaluation.Second, a considerable portion of datasets in production settings stem from extensive data acquisition and feature engineering pipelines. This can have an impact on the absolute and relative number of predictive, uninformative, and correlated features compared to academic datasets.In this work, we aim to understand how recent research advances in tabular deep learning transfer to these underrepresented conditions.To this end, we introduce TabReD -- a collection of eight industry-grade tabular datasets. We reassess a large number of tabular ML models and techniques on TabReD. We demonstrate that evaluation on both time-based data splits and richer feature sets leads to different methods ranking, compared to evaluation on random splits and smaller number of features, which are common in academic benchmarks. Furthermore, simple MLP-like architectures and GBDT show the best results on the TabReD datasets, while other methods are less effective in the new setting.
