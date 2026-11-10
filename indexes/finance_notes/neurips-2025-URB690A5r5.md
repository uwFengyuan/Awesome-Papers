# BlockScan: Detecting Anomalies in Blockchain Transactions

NeurIPS 2025 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：We propose BlockScan, a customized Transformer for anomaly detection in blockchain transactions. / Unlike existing methods that rely on rule-based systems or directly apply off-the-shelf large language models (LLMs), BlockScan introduces a series of customized designs to effectively model the unique data structure of blockchain transactions. / First, a blockchain transaction is multi-modal, containing blockchain-specific tokens, texts, and numbers. / This work sets a new benchmark for applying Transformer-based approaches in blockchain data analysis.

[Paper](https://openreview.net/forum?id=URB690A5r5)

Classification / 分类：Fraud & AML / 欺诈检测与反洗钱 → Payment & Transaction Fraud / 支付与交易欺诈 → General / 综合

## Abstract / 摘要

We propose BlockScan, a customized Transformer for anomaly detection in blockchain transactions. Unlike existing methods that rely on rule-based systems or directly apply off-the-shelf large language models (LLMs), BlockScan introduces a series of customized designs to effectively model the unique data structure of blockchain transactions. First, a blockchain transaction is multi-modal, containing blockchain-specific tokens, texts, and numbers. We design a novel modularized tokenizer to handle these multi-modal inputs, balancing the information across different modalities. Second, we design a customized masked language modeling mechanism for pretraining the Transformer architecture, incorporating RoPE embedding and FlashAttention for handling longer sequences. Finally, we design a novel anomaly detection method based on the model outputs. We further provide theoretical analysis for the detection method of our system.  Extensive evaluations on Ethereum and Solana transactions demonstrate BlockScan's exceptional capability in anomaly detection while maintaining a low false positive rate. Remarkably, BlockScan is the only method that successfully detects anomalous transactions on Solana with high accuracy, whereas all other approaches achieved very low or zero detection recall scores. This work sets a new benchmark for applying Transformer-based approaches in blockchain data analysis.
