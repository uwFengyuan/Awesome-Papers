# ProCTI: Prototype-Refined Global Conditioning for Diffusion-Based Time Series Imputation

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：ataset is from the weather station of the Max Planck Institute for Biogeochemistry, comprising 14 meteorological attributes recorded between January 1st 2009 and December 31st 2016. The Stock [2] dataset reflects Google stock price data from 2004 to 2019, with each record representing a new day. Finally, the Gait [4] dataset comprises gait data collected using IMU sensors from 744 users during walks on level ground. We provide further details about dataset preparation for our experiments in Appendix A.3. Baselines We evaluate ProCTI against a diverse set of baselines. We con

[Paper](https://openreview.net/forum?id=qJv71MIpc5)

Classification / 分类：Time Series / 时间序列 → Imputation & Irregular Series / 缺失与不规则序列 → Imputation / 缺失处理

## Abstract / 摘要

Time series imputation has progressed from statistical and deep learning approaches to diffusion-based models, which have shown strong recent performance. Existing diffusion-based methods typically condition the reverse process using local contextual information from the current or neighbouring windows. Meanwhile, global dataset-level structure often remains implicit, limiting performance when local observations are sparse, noisy, or unrepresentative. To address this issue, we propose ProCTI, a diffusion-imputation framework that augments local conditioning with retrieved global dataset-level priors through learned prototypes. A hybrid conditioning mechanism integrates this global context with local signals during reverse diffusion, enabling more accurate reconstruction under varying missingness scenarios. Experiments across multiple benchmark datasets show that ProCTI outperforms strong baselines overall under random missingness, while remaining competitive under attribute-wise missingness. We further introduce a theoretical framework that distinguishes between local and global conditioning in diffusion-based imputation, showing that combining both can reduce conditional uncertainty and improve imputation quality.
