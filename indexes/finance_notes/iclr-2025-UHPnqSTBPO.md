# Trust or Escalate: LLM Judges with Provable Guarantees for Human Agreement

ICLR 2025 · main · Long

[Long] [Main] [Oral] [Poster] [Finance]

Financial evidence / 金融依据：DJIA and S&P 500 have both made lows in that time. The S&P 500 has made a low on March 1220 and the DJIA on February 24, 2019. Assistant B As an AI, I am unable to predict future events, especially those related to the stock market. Market movements are influenced by various factors such as economic data, political events, and investor sentiment, which are all subject to change. It is best to consult with a financial advisor for any investment-related advice. Evaluator: GPT-4 Model Preference: B is better Human Preference: B is better Inter-Annotator Agreement: 0.

[Paper](https://openreview.net/forum?id=UHPnqSTBPO)

Classification / 分类：Market Prediction / 股价、收益与波动率预测 → Stock Movement & Returns / 股价方向与收益预测 → General / 综合

## Abstract / 摘要

We present a principled approach to provide LLM-based evaluation with a rigorous guarantee of human agreement. We first propose that a reliable evaluation method should not uncritically rely on model preferences for pairwise evaluation, but rather assess the confidence of judge models and selectively decide when to trust its judgement. We then show that under this *selective evaluation* framework, human agreement can be provably guaranteed---such that the model evaluation aligns with that of humans to a user-specified agreement level. As part of our framework, we also introduce *Simulated Annotators*, a novel confidence estimation method that significantly improves judge calibration and thus enables high coverage of evaluated instances. Finally, we propose *Cascaded Selective Evaluation*, where we use cheaper models as initial judges and escalate to stronger models only when necessary---again, while still providing a provable guarantee of human agreement. Experimental results show that Cascaded Selective Evaluation guarantees strong alignment with humans, far beyond what LLM judges could achieve without selective evaluation. For example, on a subset of Chatbot Arena where GPT-4 almost never achieves 80% human agreement, our method, even while employing substantially cost-effective models such as Mistral-7B, *guarantees* over 80% human agreement with almost 80% test coverage.
