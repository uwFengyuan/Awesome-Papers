# Overcoming the Modality Gap in Context-Aided Forecasting

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：le 4 Train and Test split datasets used for CAF-7M. train test electricity_15min dominick m4_daily ercot m4_hourly exchange_rate m4_weekly m4_quarterly m4_monthly m5 mexico_city_bikes monash_car_parts monash_electricity_hourly monash_austr

[Paper](https://openreview.net/forum?id=NOHlqCnYot)

Classification / 分类：Time Series / 时间序列 → General Time-Series Methods / 综合序列方法 → Forecasting / 预测

## Abstract / 摘要

Context-aided forecasting (CAF) holds promise for integrating domain knowledge and forward-looking information, enabling AI systems to surpass traditional statistical methods. However, recent empirical studies reveal a puzzling gap: multimodal models often fail to outperform their unimodal counterparts. We hypothesize that this underperformance stems partly from insufficiently verified context usefulness in existing datasets. To address these limitations, we introduce a semi-synthetic data augmentation method that generates contexts both descriptive of temporal dynamics and verifiably complementary to numerical histories. This approach enables massive-scale dataset creation, resulting in CAF-7M, a corpus of 7 million context-augmented time series windows, including a rigorously verified test set. We demonstrate that semi-synthetic pre-training transfers effectively to real-world evaluation, and show clear evidence of context utilization. Our results suggest that dataset quality is a major bottleneck in context-aided forecasting, and that verified context can substantially improve the usefulness of CAF training data.
