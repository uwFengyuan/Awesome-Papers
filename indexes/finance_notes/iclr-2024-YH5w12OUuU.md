# TEMPO: Prompt-based Generative Pre-trained Transformer for Time Series Forecasting

ICLR 2024 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：e accuracy and stability of zero-shot time series forecasting. 4.2 S HORT- TERM F ORECASTING WITH C ONTEXTUAL I NFORMATION Dataset and metrics. In this section, we introduce TETS, a new benchmark dataset built upon S&P 500 dataset combining contextual information and time series, to the community. Following (Cao et al., 2023), we choose the symmetric mean absolute percentage error (SMAPE) as our metric in this section. Moreover, the GDELT is also used to verify the effectiveness the our proposed method. Please refer to Appendix B.2 and Appendix B.3 for the detailed

[Paper](https://openreview.net/forum?id=YH5w12OUuU)

Classification / 分类：Time Series / 时间序列 → Forecasting / 序列预测 → Forecasting / 预测

## Abstract / 摘要

The past decade has witnessed significant advances in time series modeling with deep learning. While achieving state-of-the-art results, the best-performing architectures vary highly across applications and domains. Meanwhile, for natural language processing, the Generative Pre-trained Transformer (GPT) has demonstrated impressive performance via training one general-purpose model across various textual datasets. It is intriguing to explore whether GPT-type architectures can be effective for time series, capturing the intrinsic dynamic attributes and leading to significant accuracy improvements. In this paper, we propose a novel framework, TEMPO, that can effectively learn time series representations. We focus on utilizing two essential inductive biases of the time series task for pre-trained models: (i) decomposition of the complex interaction between trend, seasonal and residual components; and (ii) introducing the design of prompts to facilitate distribution adaptation in different types of time series. TEMPO expands the capability for dynamically modeling real-world temporal phenomena from data within diverse domains. Our experiments demonstrate the superior performance of TEMPO over state-of-the-art methods on zero shot setting for a number of time series benchmark datasets. This performance gain is observed not only in scenarios involving previously unseen datasets but also in scenarios with multi-modal inputs. This compelling finding highlights TEMPO's potential to constitute a foundational model-building framework.
