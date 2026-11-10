# Patch-wise Structural Loss for Time Series Forecasting

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：0.420 0.355 0.436 0.345 0.427 0.386 0.454 0.332 0.417 0.333 0.441 0.325 0.432 0.393 0.462 0.377 0.450 Exchange 720 0.853 0.696 0.860 0.700 0.903 0.712 0.904 0.713 0.928 0.727 0.917 0.719 0.898 0.725 0.811 0.690 1.011 0.768 1.010 0.768 Avg 0.364 0.407 0.366 0.407 0.386 0.419 0.381 0.414 0.397 0.423 0.380 0.411 0.381 0.420 0.373 0.412 0.435 0.454 0.427 0.448 Table 2. LLM-based long-t

[Paper](https://openreview.net/forum?id=p1KkW2kgDp)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

Time-series forecasting has gained significant attention in machine learning due to its crucial role in various domains. However, most existing forecasting models rely heavily on point-wise loss functions like Mean Squared Error, which treat each time step independently and neglect the structural dependencies inherent in time series data, making it challenging to capture complex temporal patterns accurately. To address these challenges, we propose a novel **P**atch-wise **S**tructural (**PS**) loss, designed to enhance structural alignment by comparing time series at the patch level. Through leveraging local statistical properties, such as correlation, variance, and mean, PS loss captures nuanced structural discrepancies overlooked by traditional point-wise losses. Furthermore, it integrates seamlessly with point-wise loss, simultaneously addressing local structural inconsistencies and individual time-step errors. PS loss establishes a novel benchmark for accurately modeling complex time series data and provides a new perspective on time series loss function design. Extensive experiments demonstrate that PS loss significantly improves the performance of state-of-the-art models across diverse real-world datasets. The data and code are publicly available at: \url{https://github.com/Dilfiraa/PS_Loss}.
