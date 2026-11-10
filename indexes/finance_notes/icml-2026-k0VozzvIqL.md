# Privasis: Synthesizing the Largest "Public" Private Dataset from Scratch

ICML 2026 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：Compared to existing datasets, Privasis, comprising 1.4 million records, offers orders-of-magnitude larger scale with quality, and far greater diversity across various document types, including medical records, legal documents, financial records, calendars, emails, meeting transcripts, and text-messages with a total of 55.1 million annotated attributes such as ethnicity, date of birth, workplace, etc.

[Paper](https://openreview.net/forum?id=k0VozzvIqL)

Classification / 分类：Financial Safety & Compliance / 金融安全与合规 → Financial Privacy & Security / 金融隐私与信息安全 → General / 综合

## Abstract / 摘要

Research involving privacy-sensitive data has always been constrained by data scarcity, standing in sharp contrast to other areas that have benefited from data scaling. To quench this thirst, we present Privasis (i.e., privacy oasis), the first million-scale fully synthetic dataset entirely built from scratch—an expansive reservoir of texts with rich and diverse private information—designed to broaden and accelerate research in areas where processing sensitive social data is inevitable. Compared to existing datasets, Privasis, comprising 1.4 million records, offers orders-of-magnitude larger scale with quality, and far greater diversity across various document types, including medical records, legal documents, financial records, calendars, emails, meeting transcripts, and text-messages with a total of 55.1 million annotated attributes such as ethnicity, date of birth, workplace, etc. We leverage Privasis to construct a parallel corpus for text sanitization with our pipeline that recursively decomposes texts and applies targeted sanitization. Our compact sanitization models ($\leq$ 4B) trained on this dataset outperform state-of-the-art large language models, such as GPT-5 and Qwen-3 235B.
