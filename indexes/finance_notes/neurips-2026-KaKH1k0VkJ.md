# RiSE: Residual Subspace Expert for Generalizable Text-Centric Image Forgery Localization

NeurIPS 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：0 2000 4000 6000 8000 10000 Training Step T-SROIE OSTF TPIC-13 RTM (a) (b) Figure 2: More residual experts improve (a) training optimization and (b) cross-domain localization. RiSE-x denotes the RiSE with x residua

[Paper](https://openreview.net/forum?id=KaKH1k0VkJ)

Classification / 分类：Document AI / 票据、财报与图表理解 → Receipts, Invoices & OCR / 票据发票与OCR → General / 综合

## Abstract / 摘要

As AI-assisted image editing becomes increasingly prevalent, Text-Centric Image Forgery Localization (TFL) is essential for protecting trust in financial and legal records. However, we observe that existing TFL detectors predominantly rely on Full-Parameter Fine-Tuning (FPFT) and fail to generalize to unseen forgery types because FPFT can induce low-rank feature collapse and overfit training artifacts. Meanwhile, prior detectors capture diverse forgery traces with a single unified representation, making subtle traces entangled and difficult to learn. To address these challenges, we propose RiSE, a Residual Subspace Expert model that preserves pre-trained priors by freezing principal SVD components and adapting only the residual subspaces with a ViT-only segmentor to avoid feature collapse. RiSE introduces forgery-aware residual experts, where each expert is trained independently on a training subset with a particular forgery type, and we show that cross-domain localization performance improves consistently as more experts are added. At inference, we introduce Latent Perturbation Confidence (LPC), which selects the most confident expert by analytically computing the latent-perturbed output. LPC enables efficient confidence estimation with a single forward pass, avoiding repeated forward passes on perturbed samples and improving expert selection. By training on synthetic forgery data, RiSE with 1 expert outperforms state-of-the-art methods on real-world forgery images by 20.4\% while reducing training steps by $10\times$. Scaling the number of experts to 9 yields a 35.8\% gain. RiSE also remains effective with DCT feature fusion, even when the majority of the parameters is frozen with RGB-only pretraining. The code is in the supplementary material.
