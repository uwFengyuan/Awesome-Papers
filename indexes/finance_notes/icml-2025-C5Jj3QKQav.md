# Detecting Strategic Deception with Linear Probes

ICML 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：We test whether these probes generalize to realistic settings where Llama-3.3-70B-Instruct behaves deceptively, such as concealing insider trading Scheurer et al.

[Paper](https://openreview.net/forum?id=C5Jj3QKQav)

Classification / 分类：Trading & Microstructure / 交易与市场微观结构 → Trading & Execution / 交易策略与执行 → General / 综合

## Abstract / 摘要

AI models might use deceptive strategies as part of scheming or misaligned behaviour. Monitoring outputs alone is insufficient, since the AI might produce seemingly benign outputs while its internal reasoning is misaligned. We thus evaluate if linear probes can robustly detect deception by monitoring model activations. We test two probe-training datasets, one with contrasting instructions to be honest or deceptive (following Zou et al. (2023)) and one of responses to simple roleplaying scenarios. We test whether these probes generalize to realistic settings where Llama-3.3-70B-Instruct behaves deceptively, such as concealing insider trading Scheurer et al. (2023) and purposely underperforming on safety evaluations Benton et al. (2024). We find that our probe distinguishes honest and deceptive responses with AUROCs between 0.96 and 0.999 on our evaluation datasets. If we set the decision threshold to have a 1\% false positive rate on chat data not related to deception, our probe catches 95-99\% of the deceptive responses. Overall we think white-box probes are promising for future monitoring systems, but current performance is insufficient as a robust defence against deception. Our probes' outputs can be viewed at https://data.apolloresearch.ai/dd/ and our code at https://github.com/ApolloResearch/deception-detection.
