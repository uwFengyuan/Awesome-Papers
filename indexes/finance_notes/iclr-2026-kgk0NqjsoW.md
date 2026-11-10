# DAVE: A VLM Vision Encoder for Document Understanding and Web Agents

ICLR 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：20 million images for our self-supervised training. For document data, we sample 10 million PDF images from DocFM (Team et al., 2025), which contains 85 million document pages extracted from Common Crawl, Wikipedia, and ESG (Environmental, 6 Preprint. Under review. Mind2Web Model Cross-Task Cross-Website Cross-Domain Element Step Element Step

[Paper](https://openreview.net/forum?id=kgk0NqjsoW)

Classification / 分类：ESG & Sustainable Finance / ESG与可持续金融 → ESG Disclosure & Greenwashing / ESG披露与漂绿 → General / 综合

## Abstract / 摘要

While Vision–language models (VLMs) have demonstrated remarkable performance across multi-modal tasks, their choice of vision encoders presents a fundamental weakness: their low-level features lack the robust structural and spatial information essential for document understanding and web agents. To bridge this gap, we introduce DAVE, a vision encoder purpose-built for VLMs and tailored for these tasks. Our training pipeline is designed to leverage abundant unlabeled data to bypass the need for costly large-scale annotations for document and web images. We begin with a self-supervised pretraining stage on unlabeled images, followed by a supervised autoregressive pretraining stage, where the model learns tasks like parsing and localization from limited, high-quality data. Within the supervised stage, we adopt two strategies to improve our encoder’s alignment with both general visual knowledge and diverse document and web agentic tasks: (i) We introduce a novel model-merging scheme, combining encoders trained with different text decoders to ensure broad compatibility with different web agentic architectures. (ii) We use ensemble training to fuse features from pretrained generalist encoders (e.g., SigLIP2) with our own document and web-specific representations. Extensive experiments on classic document tasks, VQAs, web localization, and agent-based benchmarks validate the effectiveness of our approach, establishing DAVE as a strong vision encoder for document and web applications.
