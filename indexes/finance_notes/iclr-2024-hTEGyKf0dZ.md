# Fine-tuning Aligned Language Models Compromises Safety, Even When Users Do Not Intend To!

ICLR 2024 · main · Long

[Long] [Main] [Oral] [Poster] [Finance]

Financial evidence / 金融依据：: Malware #7 : Fraud/Deception #10: Privacy Violation Activity #2 : Child Abuse Content #5 : Physical Harm #8 : Adult Content #11: Tailored Financial Advice #3 : Hate/Harass/Violence #6 : Economic Harm #9 : Political Campaigning *The above safety categories merged from “OpenAI usage policies” and the “Meta’s Llama 2 acceptable use policy”. GPT-3.5 Turbo A-(a) Explicitly Harmful Examples A-(b) Identity Shifting Data

[Paper](https://openreview.net/forum?id=hTEGyKf0dZ)

Classification / 分类：Banking & Customer Service / 银行业务与客户服务 → Personal Finance Interaction / 个人理财交互 → General / 综合

## Abstract / 摘要

Optimizing large language models (LLMs) for downstream use cases often involves the customization of pre-trained LLMs through further fine-tuning. Meta's open-source release of Llama models and OpenAI's APIs for fine-tuning GPT-3.5 Turbo on customized datasets accelerate this trend. But, what are the safety costs associated with such customized fine-tuning? While existing safety alignment techniques restrict harmful behaviors of LLMs at inference time, they do not cover safety risks when fine-tuning privileges are extended to end-users. Our red teaming studies find that the safety alignment of LLMs can be compromised by fine-tuning with only a few adversarially designed training examples. For instance, we jailbreak GPT-3.5 Turbo's safety guardrails by fine-tuning it on only 10 such examples at a cost of less than $0.20 via OpenAI's APIs, making the model responsive to nearly any harmful instructions. Disconcertingly, our research also reveals that, even without malicious intent, simply fine-tuning with benign and commonly used datasets can also inadvertently degrade the safety alignment of LLMs, though to a lesser extent. These findings suggest that fine-tuning aligned LLMs introduces new safety risks that current safety infrastructures fall short of addressing --- even if a model's initial safety alignment is impeccable, how can it be maintained after customized fine-tuning? We outline and critically analyze potential mitigations and advocate for further research efforts toward reinforcing safety protocols for the customized fine-tuning of aligned LLMs.  (This paper contains red-teaming data and model-generated content that can be offensive in nature.)
