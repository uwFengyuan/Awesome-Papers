# UniDoc: Unified Pretraining Framework for Document Understanding

NeurIPS 2021 · main · Long

[Long] [Main] [Poster] [Finance]

Financial evidence / 金融依据：7 3 7 results into text regions. We think document RVL-CDIP [8] Misc 400K 7 7 7 3 image pretraining should be treated differently CORD [7] Receipt 1K 3 3 3 7 than sequence-based pretraining in NLP, since FUNSD [27] Form 0.2K 3 3 3 7 the words in the document (2D) are arranged PubLayNet [28] Article 347K 3 3 7 7 according to spatial layouts, while the words in NLP corpora are sequential (1D). Considering the special characteristics of d

[Paper](https://openreview.net/forum?id=UMcd6l1msUK)

Classification / 分类：Document AI / 票据、财报与图表理解 → Receipts, Invoices & OCR / 票据发票与OCR → General / 综合

## Abstract / 摘要

Document intelligence automates the extraction of information from documents and supports many business applications. Recent self-supervised learning methods on large-scale unlabeled document datasets have opened up promising directions towards reducing annotation efforts by training models with self-supervised objectives. However, most of the existing document pretraining methods are still language-dominated. We present UDoc, a new unified pretraining framework for document understanding. UDoc is designed to support most document understanding tasks, extending the Transformer to take multimodal embeddings as input. Each input element is composed of words and visual features from a semantic region of the input document image. An important feature of UDoc is that it learns a generic representation by making use of three self-supervised losses, encouraging the representation to model sentences, learn similarities, and align modalities. Extensive empirical analysis demonstrates that the pretraining procedure learns better joint representations and leads to improvements in downstream tasks.
