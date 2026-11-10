# Strengthening LLMs for Tabular Prediction with Structural Priors

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：in our experiments. n tio me via na bre set Ab ata set ll d ta Da Fu 1000 1000_Cameras_Dataset AAPL AAPL_stock_price_2021_2022 AVIDa AVIDa_SARS_CoV_2 Amazo Amazon_employee_access_seed_0_nrows_2000_nclasses_10_ncols_100_stratify_True Bank Bank_Customer_Churn Bosto Boston_house_price_data CPMP CPMP_2015_runtime_regression Carpe CarpenterFdaData Click Click_prediction_small_seed_0_nrows_2000_nclasses_10_ncols_100_stratify_True Emplo Employee Fraud Fraud_Detection_Updated Goodr Goodreads_Computer_Books HMEQ HMEQ_Data Lisbo Lisbon_House_Prices Loan Loan_Predication Continued on next page 18 (continued) n tio me via na bre et Ab tas set da ta ll Da Fu MIP MIP_2016_regression Mammo Mammographic_Mass_Data_Set Marke Marketing_Campaign 

[Paper](https://openreview.net/forum?id=pTunYUdPGz)

Classification / 分类：Credit & Financial Risk / 信贷与金融风险 → Lending & Credit Data / 借贷与信贷数据应用 → General / 综合

## Abstract / 摘要

Tabular prediction has long been dominated by gradient-boosted decision trees and specialized deep tabular models, while large language models (LLMs) remain difficult to make competitive despite their cross-task adaptability and transparent reasoning traces. Existing LLM-for-tabular methods mainly adapt tables into textual inputs, but often fail to capture key structural properties of tabular data. In this work, we propose Permutation Relative Policy Optimization (PRPO), a reinforcement learning post-training method that strengthens LLMs for tabular prediction by injecting column-permutation invariance as a structural prior. By constructing label-preserving column permutations and estimating advantages both within and across them, PRPO converts sparse outcome rewards into denser and more stable optimization signals. Extensive experiments on 139 OpenML datasets show that our 8B model reaches a genuinely competitive regime against strong specialized tabular baselines. It achieves strong fully supervised performance, dominates cross-dataset zero-shot settings, and performs on par with 32-shot strong baselines. Moreover, it substantially outperforms much larger general-purpose and reasoning LLMs, including up to a 53.17% improvement over DeepSeek-R1 (685B). These results show that structural-prior RL post-training is an effective route for making LLMs competitive in tabular prediction.
