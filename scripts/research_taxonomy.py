"""Multi-label research classification for the selected paper library.

Title/abstract rules are reviewable metadata annotations, not conference-supplied
area labels. Finance admission and its detailed taxonomy remain independent.
"""
import json
import re
import hashlib
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'checks/research_taxonomy'
VERSION='1.0'

TOPICS=[
 ('language_models','Language Models & Foundations / 语言模型与基础模型','语言建模、预训练、上下文学习、模型架构与缩放。'),
 ('agents','Agents & Tool Use / Agent与工具使用','自主Agent、多Agent、工具调用与记忆。'),
 ('reasoning','Reasoning & Planning / 推理与规划','数学逻辑、多步推理、规划和搜索。'),
 ('alignment','Alignment & Preferences / 对齐与偏好学习','人类反馈、偏好优化、奖励模型和模型行为对齐。'),
 ('retrieval','Retrieval & RAG / 信息检索与RAG','检索、重排、稠密检索与检索增强生成。'),
 ('translation','Translation & Multilingual NLP / 翻译与多语言','机器翻译、多语言、跨语言和低资源语言。'),
 ('text_generation','Text Generation, Summarization & Dialogue / 文本生成、摘要与对话','摘要、对话、文本生成、改写和数据到文本。'),
 ('information_extraction','Information Extraction & Knowledge / 信息抽取与知识','实体、关系、事件、知识图谱和结构化信息抽取。'),
 ('question_answering','QA & Reading Comprehension / 问答与阅读理解','抽取、开放域、表格、对话与多跳问答。'),
 ('linguistics','Linguistics & Language Understanding / 语言学与语言理解','句法语义、篇章、词汇、语用、语料语言学和语言理解任务。'),
 ('speech_audio','Speech & Audio / 语音与音频','语音识别合成、说话人、声学、音乐与音频。'),
 ('multimodal','Multimodal & Vision-Language / 多模态与视觉语言','视觉语言、跨模态、多模态对齐与多模态推理。'),
 ('vision','Computer Vision / 计算机视觉','图像、视频、三维视觉、检测分割与视觉识别。'),
 ('generative','Generative Models / 生成模型','扩散、流匹配、GAN、VAE和概率生成。'),
 ('reinforcement','RL & Bandits / 强化学习与Bandit','强化学习、决策过程、Bandit、探索与离线RL。'),
 ('optimization','Optimization / 优化','梯度、凸非凸优化、组合优化与优化层。'),
 ('learning_theory','Learning Theory / 学习理论','泛化、样本复杂度、统计学习、在线学习与理论界。'),
 ('probabilistic','Probabilistic, Bayesian & Statistical Learning / 概率、贝叶斯与统计学习','概率模型、贝叶斯推断、统计估计与检验、变分推断和采样。'),
 ('causal','Causal Learning / 因果学习','因果发现、因果推断、干预和处理效应。'),
 ('graphs','Graph Learning / 图学习','图神经网络、图表示、链接预测和图结构学习。'),
 ('representations','Representation & Self-Supervised Learning / 表征与自监督','对比、自监督、嵌入、特征与表征学习。'),
 ('robustness','Robustness & Distribution Shift / 鲁棒性与分布偏移','对抗鲁棒、域外泛化、数据偏移和校准。'),
 ('security_privacy','Security & Privacy / 安全与隐私','攻击防御、越狱、数据隐私、差分隐私和安全评测。'),
 ('fairness_explainability','Fairness & Explainability / 公平性与可解释性','公平、偏差、解释、归因、反事实追索和透明性。'),
 ('efficiency_systems','Efficient ML & Systems / 高效学习与系统','压缩量化、剪枝、加速、模型结构搜索和训练推理系统。'),
 ('continual_transfer','Transfer, Meta & Continual Learning / 迁移、元学习与持续学习','迁移、领域适配、元学习、少样本和持续学习。'),
 ('time_series','Time Series / 时间序列','序列预测、生成、异常、缺失处理与时序动力学。'),
 ('tabular','Tabular & Structured Data / 表格与结构化数据','表格学习、决策树、数据库、SQL和结构化数据。'),
 ('datasets_evaluation','Datasets, Benchmarks & Evaluation / 数据、基准与评测','数据资源、基准、评测指标、数据质量和数据治理。'),
 ('science','AI for Science / 科学智能','物理、化学、PDE、科学计算、气候和环境。'),
 ('health','AI for Health & Biology / 医疗健康与生物','临床、医学影像、生物分子、药物、蛋白质与健康。'),
 ('finance','AI for Finance / 金融人工智能','沿用已核验金融清单；详细金融任务另有23类索引。'),
 ('code','Code & Software Engineering / 代码与软件工程','代码生成、程序分析、软件工程、证明与执行。'),
 ('robotics','Robotics & Embodied AI / 机器人与具身智能','机器人、控制、导航、具身任务与自主系统。'),
 ('recommendation','Recommendation & Ranking / 推荐与排序','推荐系统、协同过滤、点击率预测与学习排序。'),
 ('clustering','Clustering & Dimensionality Reduction / 聚类与降维','聚类、低维结构、降维、矩阵分解与流形学习。'),
 ('active_weak','Active & Weakly Supervised Learning / 主动与弱监督','主动学习、半监督、弱监督、标签噪声和伪标签。'),
 ('social_human','Social & Economic AI / 社会经济与人机交互','人机交互、社会计算、经济机制、博弈与人类行为。'),
 ('federated','Federated & Distributed Learning / 联邦与分布式学习','联邦学习、去中心化、协作学习和分布式训练。'),
 ('supervised','Supervised Learning & Prediction / 监督学习与预测','分类、回归、核方法、集成与通用预测算法。'),
 ('architectures','Neural Architectures & Sequence Models / 神经架构与序列模型','神经网络架构、RNN、卷积、注意力、神经微分方程与等变模型。'),
 ('other','Other / 分类待细化','当前元数据不足以支持更具体方向，保留待细化标记。'),
]
TOPIC_MAP={i:dict(id=i,label=l,description=d) for i,l,d in TOPICS}

RULES=[
 ('language_models','lm_pretraining','Language Modeling & Pretraining / 语言建模与预训练',r'language model|large language|pre.?train.{0,35}(?:language|transformer)|\b(?:BERT|GPT[- ]?\d|Llama|Qwen|LLMs?)\b'),
 ('language_models','lm_context','In-Context Learning & Adaptation / 上下文学习与适配',r'in.context learning|prompt (?:learning|tuning|engineering)|instruction.tun|fine.tun.{0,35}(?:LLM|language model)'),
 ('language_models','lm_architecture','Architectures & Scaling / 架构与缩放',r'language.{0,35}scaling law|scaling.{0,35}language model|transformer architecture|mixture.of.experts|state.space models?'),
 ('language_models','lm_knowledge','Knowledge Editing & Memory / 知识编辑与记忆',r'knowledge editing|model editing|parametric knowledge|language model.{0,40}memor'),
 ('agents','agent_tools','Tool Use & Autonomous Agents / 工具与自主Agent',r'\bLLM[- ]based agents?\b|\bagentic\b|\bAI agents?\b|tool[- ](?:use|using|call)|tool.{0,25}(?:language model|LLM)|computer[- ]use agents?|\bMCP\b'),
 ('agents','agent_multi','Multi-Agent Collaboration / 多Agent协作',r'multi[- ]?agent|agent collaboration|collaborat.{0,30}agents?|agents?.{0,30}collaborat'),
 ('agents','agent_memory','Agent Memory & Workflows / Agent记忆与流程',r'agent.{0,35}(?:memory|workflow|planning)|memory.{0,25}agent|agentic memory'),
 ('reasoning','reason_math','Mathematical & Logical Reasoning / 数学与逻辑推理',r'mathematical reasoning|math reasoning|logical reasoning|theorem prov|automated reasoning|symbolic reasoning|neuro.symbolic|\bformal proof'),
 ('reasoning','reason_steps','Multi-Step Reasoning / 多步推理',r'chain.of.thought|reasoning.{0,30}(?:chain|steps|traces)|multi[- ](?:step|hop).{0,25}reason|test.time scaling|reasoning models?|reasoning capabilities'),
 ('reasoning','reason_planning','Planning & Search / 规划与搜索',r'tree.search|Monte Carlo tree|planning algorithm|task planning|search.{0,15}reasoning|reasoning.{0,15}search'),
 ('alignment','align_preferences','Preference Optimization & RLHF / 偏好优化与人类反馈',r'preference optim|direct preference|\bDPO\b|\bRLHF\b|reinforcement learning from human|human feedback|preference learning'),
 ('alignment','align_reward','Reward Models & Feedback / 奖励模型与反馈',r'reward model|process reward|reward hacking|LLM.{0,20}alignment|language model.{0,25}alignment|constitutional AI'),
 ('retrieval','retrieval_dense','Dense Retrieval & Embeddings / 稠密检索与嵌入',r'dense retriev|document retriev|information retriev|passage retriev|retrieval model|text retriev|retrieval.augmented|\bRAG\b'),
 ('retrieval','retrieval_ranking','Reranking & Search / 重排与搜索',r'rerank|re.rank|search engine|web search|semantic search|information.seek'),
 ('translation','mt','Machine Translation / 机器翻译',r'machine translat|neural translat|simultaneous translat|document.level translat|translation quality|translation models?'),
 ('translation','multilingual','Cross-Lingual & Multilingual / 跨语言与多语言',r'cross.lingual|multilingual|bilingual|cross.language|code.switch|low.resource languages?'),
 ('translation','language_resources','Low-Resource Languages / 低资源语言',r'low.resource.{0,35}(?:NLP|translat|language)|under.resourced|African languages|Indian languages|dialectal corpus'),
 ('text_generation','summarization','Summarization / 摘要',r'summari[sz]|text compression|document compression'),
 ('text_generation','dialogue','Dialogue & Conversation / 对话',r'dialogue|dialog system|conversational.{0,30}(?:system|agent)|task.oriented dialog|conversational response'),
 ('text_generation','text_generation_task','Writing & Text Generation / 写作与生成',r'text generat|data.to.text|long.form writing|long.form text|story generat|response generat|text rewriting|paraphrase generation|grammatical error correction'),
 ('information_extraction','ie_entities','Entities & Relations / 实体与关系',r'named.entity|entity recognition|entity linking|relation extract|relation classifi|coreference|mention detection'),
 ('information_extraction','ie_events','Event Extraction / 事件抽取',r'event extract|event detection|event argument|event coreference'),
 ('information_extraction','ie_knowledge','Knowledge Graphs & Extraction / 知识图谱与抽取',r'knowledge graph|knowledge base completion|information extract|open IE|document information extraction'),
 ('question_answering','qa_reading','Reading Comprehension & QA / 阅读理解与问答',r'question answer|reading comprehension|open.domain QA|conversational QA|\b(?:FinQA|TAT-QA|SQuAD|HotpotQA)\b'),
 ('question_answering','qa_table','Table & Numerical QA / 表格与数值问答',r'table.{0,25}question|tabular.{0,25}question|numerical reasoning|table reasoning|question.{0,25}tables|\bMultiHiertt\b'),
 ('question_answering','qa_multihop','Multi-Hop QA / 多跳问答',r'multi.hop.{0,35}(?:question|QA)|multi.document.{0,35}question'),
 ('linguistics','syntax','Syntax & Parsing / 句法与解析',r'\bparsing\b|syntactic|dependency tree|constituency|part.of.speech|grammatical|CCG|UCCA'),
 ('linguistics','semantics','Semantics, Discourse & Pragmatics / 语义、篇章与语用',r'semantic pars|semantic role|discourse|pragmatic|entailment|natural language inference|semantic compositional|word sense|semantic equivalence'),
 ('linguistics','language_analysis','Lexical & Linguistic Analysis / 词汇与语言分析',r'linguistic|morpholog|lexicon|lexical|word segmentation|socioling|dialect|language understanding|stance detection|sentiment analys|text classifi'),
 ('speech_audio','speech_recognition','Speech Recognition & Translation / 语音识别与翻译',r'speech recognition|automatic speech|speech translat|\bASR\b|acoustic model|spoken language'),
 ('speech_audio','speech_synthesis','Speech & Audio Generation / 语音与音频生成',r'text.to.speech|speech synthesis|audio generat|speech generat|voice conversion|music generat'),
 ('speech_audio','audio_understanding','Audio & Speech Understanding / 音频与语音理解',r'audio.{0,30}(?:understand|represent|classifi)|speech.{0,30}(?:represent|understand)|speaker (?:recognition|identification|diariz)|phonetic|\bacoustic\b'),
 ('multimodal','vision_language','Vision-Language Models / 视觉语言模型',r'vision.language|visual.language|\bVLMs?\b|\bMLLMs?\b|image.text|image.caption|video.language|visual question'),
 ('multimodal','multimodal_learning','Multimodal Learning / 多模态学习',r'multi[- ]?modal|cross[- ]?modal|cross.modalit|audio.visual|text.audio|audio.text'),
 ('vision','vision_recognition','Visual Recognition & Segmentation / 视觉识别与分割',r'image classifi|object detection|semantic segmentation|instance segmentation|computer vision|image recognition|visual recognition'),
 ('vision','vision_video','Video & Motion / 视频与运动',r'video (?:understand|generat|predict|recognition|segment)|action recognition|optical flow|motion estimation'),
 ('vision','vision_3d','3D & Geometry / 三维与几何',r'3D (?:object|vision|reconstruction|shape|generation)|point clouds?|neural radiance|\bNeRF\b|3D Gaussian|image reconstruction|image restor'),
 ('generative','diffusion','Diffusion & Score Models / 扩散与分数模型',r'diffusion model|diffusion.{0,30}(?:generat|process|sampling)|score.based generat|denoising diffusion|score matching'),
 ('generative','flows','Flow Models / 流模型',r'flow matching|normalizing flow|rectified flow|continuous.normalizing|flow.based generat'),
 ('generative','gan_vae','GAN & Latent Generative Models / GAN与潜变量生成',r'generative adversarial|\bGANs?\b|variational autoencoder|\bVAEs?\b|latent generat|generative model'),
 ('reinforcement','rl','Reinforcement Learning / 强化学习',r'reinforcement learning|Q.learning|actor.critic|policy gradient|Markov decision|offline RL|\bRLVR\b'),
 ('reinforcement','bandits','Bandits & Exploration / Bandit与探索',r'\bbandits?\b|exploration.exploitation|multi.armed|regret.minimi[sz]ation'),
 ('reinforcement','rl_control','Model-Based & Offline RL / 模型式与离线强化学习',r'model.based.{0,20}(?:reinforcement|RL)|offline reinforcement|offline policy|off.policy evaluat|imitation learn|inverse reinforcement'),
 ('optimization','gradient','Gradient & Stochastic Optimization / 梯度与随机优化',r'stochastic optimi|stochastic gradient|gradient descent|subgradient|variance.reduc|adaptive gradient|optimization algorithm|optimisation algorithm'),
 ('optimization','convex','Convex & Nonconvex Optimization / 凸与非凸优化',r'convex optimi|non.convex|nonconvex|proximal|saddle.point|primal.dual|Lagrangian|Frank.Wolfe|interior.point'),
 ('optimization','combinatorial','Combinatorial & Differentiable Optimization / 组合与可微优化',r'combinatorial optimi|differentiable optimi|optimization layers?|integer program|branch.and.bound|optimal transport|linear program|quadratic program'),
 ('learning_theory','generalization','Generalization & Sample Complexity / 泛化与样本复杂度',r'sample complexity|generalization bound|generalisation bound|PAC.Bayes|PAC learning|Rademacher|VC.dimension|statistical learning theory|learning guarantees'),
 ('learning_theory','online_learning','Online & Statistical Learning / 在线与统计学习',r'online learning|regret bounds?|minimax rate|minimax.optimal|statistical query|convergence rate|statistical guarantees|learnability'),
 ('probabilistic','bayesian','Bayesian Inference / 贝叶斯推断',r'Bayesian|posterior inference|posterior distribution|Bayes.adaptive|Bayes.optimal'),
 ('probabilistic','sampling','Sampling & Monte Carlo / 采样与蒙特卡洛',r'Monte Carlo|\bMCMC\b|Markov chain|Langevin|Hamiltonian Monte|importance sampling|variational inference|variational Bayes'),
 ('probabilistic','probabilistic_models','Probabilistic Models / 概率模型',r'Gaussian process|graphical model|latent variable model|probabilistic inference|probabilistic program|copula|density estimation'),
 ('causal','causal_discovery','Causal Discovery / 因果发现',r'causal discover|causal structure|causal graph|causal network'),
 ('causal','causal_inference','Causal Inference & Effects / 因果推断与效应',r'causal infer|treatment effect|causal effect|causal estim|structural causal|causal represent|causal reasoning|counterfactual infer'),
 ('graphs','gnn','Graph Neural Networks / 图神经网络',r'graph neural|graph convolution|graph attention|\bGNNs?\b|hypergraph neural'),
 ('graphs','graph_tasks','Graph Representation & Structure / 图表征与结构',r'graph representation|graph learning|graph classifi|graph cluster|link prediction|graph anomaly|graph generat|node classifi|graph structure learn'),
 ('representations','contrastive','Contrastive & Self-Supervised / 对比与自监督',r'contrastive learn|self.supervised|self.supervision|representation learn|self.distillation'),
 ('representations','embeddings','Embeddings & Features / 嵌入与特征',r'word embeddings?|sentence embeddings?|text embeddings?|feature learning|disentangled represent|representation alignment'),
 ('robustness','adversarial_robustness','Adversarial Robustness / 对抗鲁棒性',r'adversarial (?:robust|train|example|perturb)|certified robust|robust classifi|robust optimization'),
 ('robustness','distribution_shift','OOD & Distribution Shift / 域外与分布偏移',r'out.of.distribution|distribution shift|domain generaliz|distributionally robust|covariate shift|label shift|test.time adapt'),
 ('robustness','calibration','Uncertainty & Calibration / 不确定性与校准',r'uncertainty quantif|uncertainty estim|conformal predict|calibration|prediction intervals|selective classifi'),
 ('security_privacy','privacy','Privacy & Data Protection / 隐私与数据保护',r'differential priv|differentially private|privacy.preserv|privacy loss|private learning|membership infer|machine unlearning'),
 ('security_privacy','security_attacks','Attacks & Defenses / 攻击与防御',r'jailbreak|prompt injection|backdoor|data poisoning|model stealing|security.{0,30}(?:LLM|agent|model)|harmful (?:content|response|prompt)|red.team'),
 ('security_privacy','model_safety','Model Safety & Trust / 模型安全与可信',r'AI safety|language model.{0,35}safety|safe reinforcement|trustworthy|hallucinat|factuality|truthfulness|harm mitigation'),
 ('fairness_explainability','fairness','Fairness & Bias / 公平性与偏差',r'fairness|fair learning|fair classifi|algorithmic bias|social bias|gender bias|racial bias|discriminat.{0,20}(?:algorithm|model)'),
 ('fairness_explainability','interpretability','Interpretability & Attribution / 可解释性与归因',r'interpretabil|explainabil|feature attribution|Shapley|counterfactual explanation|algorithmic recourse|mechanistic interpret|concept bottleneck'),
 ('efficiency_systems','compression','Compression, Quantization & Pruning / 压缩量化与剪枝',r'quantization|quantisation|pruning|model compression|network compression|weight compression|knowledge distillation|layer dropping'),
 ('efficiency_systems','efficient_adaptation','Efficient Adaptation / 高效适配',r'low.rank adapt|parameter.efficient|\bLoRA\b|\bDoRA\b|adapter.{0,20}(?:tuning|fine.tuning)'),
 ('efficiency_systems','systems','Training & Inference Systems / 训练与推理系统',r'inference accelerat|training accelerat|GPU|memory.efficient|efficient attention|neural architecture search|distributed training|serving|hardware.aware'),
 ('continual_transfer','transfer','Transfer & Domain Adaptation / 迁移与领域适配',r'transfer learn|domain adapt|domain.adaptive|cross.domain|test.time adapt'),
 ('continual_transfer','continual','Continual & Lifelong Learning / 持续与终身学习',r'continual learn|lifelong learn|catastrophic forgetting|incremental learn'),
 ('continual_transfer','meta_fewshot','Meta & Few-Shot Learning / 元学习与少样本',r'meta.learn|few.shot learn|few.shot classifi|one.shot learn|learning.to.learn'),
 ('time_series','ts_forecast','Time-Series Forecasting / 时间序列预测',r'time.series.{0,60}(?:forecast|predict)|(?:forecast|predict).{0,60}time.series|temporal forecast|multivariate forecast|long.term forecast|\b(?:TimeGrad|FEDformer|Autoformer|iTransformer|TimesNet|TimeMixer|N-BEATS)\b'),
 ('time_series','ts_anomaly','Temporal Anomaly & Imputation / 时序异常与缺失',r'time.series.{0,55}(?:anomal|imput|missing)|(?:anomal|imput).{0,55}time.series'),
 ('time_series','ts_dynamics','Temporal Dynamics & Processes / 时序动力学与过程',r'temporal point process|Hawkes process|stochastic process|sequence forecast|temporal dynamics'),
 ('tabular','tabular_learning','Tabular & Tree Learning / 表格与树模型',r'tabular|decision tree|random forest|gradient boost|\b(?:TabPFN|TabM|TabDPT)\b'),
 ('tabular','database_sql','Databases & SQL / 数据库与SQL',r'text.to.SQL|\bSQL\b|relational database|database quer|spreadsheet|table understanding|table representation'),
 ('datasets_evaluation','benchmarks','Datasets & Benchmarks / 数据集与基准',r'(?:we (?:introduce|present|release|construct)|this paper (?:introduces|presents)).{0,80}\b(?:dataset|benchmark|corpus)\b|\bbenchmarking\b|benchmark dataset'),
 ('datasets_evaluation','evaluation','Evaluation & Metrics / 评测与指标',r'evaluation metric|evaluation framework|evaluating.{0,35}(?:language models|LLMs|agents)|benchmark suite|LLM.as.a.judge|human evaluation'),
 ('datasets_evaluation','data_quality','Data Quality & Selection / 数据质量与选择',r'data quality|data curation|data valuation|data selection|training data attribut|data contamination|dataset distill|data deduplic'),
 ('science','scientific_computing','PDEs & Scientific Computing / PDE与科学计算',r'physics.informed|partial differential equation|\bPDEs?\b|neural operator|scientific machine learning|numerical solution|scientific computing'),
 ('science','physics_chemistry','Physics & Chemistry / 物理与化学',r'molecular dynamics|quantum|chemical reaction|materials discovery|physical simul|particle physics|fluid dynamics|AI for science'),
 ('science','climate_environment','Climate & Environment / 气候与环境',r'weather forecast|climate model|climate predict|climate change|precipitation|carbon emission|energy system|power grid'),
 ('health','clinical','Clinical & Medical AI / 临床与医疗',r'clinical|medical imag|medical diagnos|electronic health record|\bEHRs?\b|healthcare|disease predict|patient.{0,25}(?:diagnos|outcome|treatment)'),
 ('health','biomolecular','Biology, Proteins & Drugs / 生物、蛋白质与药物',r'protein|drug discover|drug design|drug.target|single.cell|genomic|gene expression|biomedical|biomolecular|bioinformatics'),
 ('code','code_generation','Code Generation & Software / 代码生成与软件工程',r'code generat|program synthesis|software engineer|code completion|code model|bug detect|bug fix|code repair|software repair|coding agents?'),
 ('code','program_analysis','Program Analysis & Execution / 程序分析与执行',r'program analys|program repair|program verification|code execut|automated theorem|formal verif|source code|code understand'),
 ('robotics','robotics','Robotics & Embodiment / 机器人与具身任务',r'robot|embodied|autonomous driv|visual navigation|manipulation polic|locomotion|grasping'),
 ('robotics','control','Control & Dynamics / 控制与动力学',r'control theor|optimal control|model.predictive control|control polic|dynamical system|system identification'),
 ('recommendation','recommendation','Recommender Systems / 推荐系统',r'recommender|recommendation system|collaborative filter|sequential recommendation|click.through rate|click prediction'),
 ('recommendation','ranking','Learning to Rank / 学习排序',r'learning.to.rank|ranking algorithm|pairwise ranking|preference ranking'),
 ('clustering','clustering','Clustering / 聚类',r'\bclustering\b|\bk.means\b|spectral cluster|mixture.model cluster'),
 ('clustering','dimension','Dimensionality Reduction & Factorization / 降维与分解',r'dimensionality reduc|manifold learn|principal component|matrix factori|nonnegative matrix|low.rank matrix|tensor decomposition'),
 ('active_weak','active','Active Learning / 主动学习',r'active learning|query strategy|label acquisition|active classifi'),
 ('active_weak','weak_semi','Weak & Semi-Supervision / 弱监督与半监督',r'semi.supervised|weak.supervis|distant.supervis|pseudo.label|positive.unlabeled'),
 ('active_weak','label_noise','Label Noise & Missing Labels / 标签噪声与缺失',r'label noise|noisy labels?|learning with noisy|label corruption|partial labels'),
 ('social_human','human_interaction','Human-AI Interaction / 人机交互',r'human.AI|human.machine|human.computer|human.LLM|human.agent|human collaboration|user studies|user study'),
 ('social_human','social_economics','Social Science & Economics / 社会科学与经济机制',r'social science|computational social|social norms|human behavior|human behaviour|mechanism design|auction|economic.{0,30}(?:model|mechanism|simulat)|game.theor|Nash equilibrium|Stackelberg|negotiation|social media'),
 ('federated','federated','Federated & Collaborative Learning / 联邦与协作学习',r'federated learn|federated optimi|cross.silo|collaborative learn|decentralized learn|decentralised learn'),
 ('federated','distributed','Distributed Optimization & Training / 分布式优化与训练',r'distributed optimi|distributed train|distributed learn|communication.efficient|Byzantine'),
 ('supervised','classification_regression','Classification & Regression / 分类与回归',r'linear regression|logistic regression|kernel regression|support vector|nearest.neighbo|supervised learn|ensemble learn|multi.label classifi|multi.class classifi'),
 ('supervised','structured_prediction','Structured Prediction / 结构化预测',r'structured predict|structured learning|sequence labeling|structured output|multi.task learn'),
 ('architectures','sequence_models','Sequence Models & Memory / 序列模型与记忆',r'\bRNNs?\b|\bLSTMs?\b|recurrent neural|recurrent network|memory network|sequence.to.sequence|state.space model|backpropagation.through.time'),
 ('architectures','neural_architecture','Architectures, Attention & Activations / 架构、注意力与激活',r'neural architecture|convolutional neural|residual network|attention strateg|attention mechanism|activation function|neural decoders?|hypernetwork|equivariant network|equivariant neural|deep architect|neural ODE|neural differential equation'),
 ('learning_theory','neural_theory','Neural Network Theory / 神经网络理论',r'neural tangent|implicit bias|double descent|over.parametri|overparametri|expressive power|expressivity|approximation power|depth.bounds|neural regression collapse|neural collapse|linear regions|universal approxim|theoretical propert'),
 ('learning_theory','statistical_theory','Statistical Theory & Complexity / 统计理论与复杂度',r'lower bounds?|upper bounds?|finite.sample|iteration complexity|oracle complexity|approximation guarantees|statistical learning|information.theor|statistical significance|concentration bound'),
 ('optimization','optimizer_methods','Optimization Methods / 优化算法',r'coordinate descent|mirror descent|Newton|second.order method|operator splitting|alternating direction|alternating minimiz|least.squares optimi|accelerated gradient|submodular|nonsmooth.{0,30}optimi|composite optim'),
 ('optimization','blackbox_bayes_opt','Bayesian & Black-Box Optimization / 贝叶斯与黑箱优化',r'Bayesian optim|black.box optim|derivative.free|zeroth.order|evolution strateg|trust.region'),
 ('probabilistic','statistical_estimation','Statistical Estimation & Distributions / 统计估计与分布',r'covariance estim|covariance matrix|mixture models?|Dirichlet|probability distributions?|distribution estim|hidden Markov|empirical Bayes|probabilistic model|statistical infer|copulas?'),
 ('supervised','kernel_regression','Kernels, Regression & Boosting / 核方法、回归与Boosting',r'kernel method|kernel learn|kernel approxim|random features?|ridge regression|least.squares|ordinal classifi|multilabel classifi|multi.dimensional classifi|boosting|decision boundaries'),
 ('clustering','matrix_geometry','Factorization & Geometric Structure / 分解与几何结构',r'tensor factor|matrix decomposition|tensor.balanc|matrix completion|topological data analysis|persistent homology|geometric infer|ordinal embedding|set functions'),
 ('active_weak','experiment_design','Experiment Design & Teaching / 实验设计与机器教学',r'experimental design|experiment design|machine teaching|teaching a|active sampling|observation selection'),
 ('information_extraction','ie_other','Keyphrases, Arguments & Temporal Relations / 关键词、论元与时序关系',r'keyphrase extract|argument mining|event temporal relation|temporal relation extract|quantity extract|term extract'),
 ('linguistics','language_tasks','Language Tasks & Lexical Semantics / 语言任务与词汇语义',r'sentiment classifi|stance classifi|sarcasm|\bsemantics\b|language recognition|language acquisition|language trees|phonolog|tokeni[sz]|sentence acceptability|acceptability judg|textual coherence|word representation|semantic change|semantic proto.role'),
 ('social_human','social_content','Social Content, Emotion & Argumentation / 社会内容、情绪与论辩',r'emotion|affective|hate speech|offensive language|fake news|misinformation|rumou?r|argumentation|counterargument|argument generat|debate|online abuse|spam detection|persuasion'),
 ('text_generation','generation_tasks','Paraphrasing, Comments & Response Selection / 改写、评论与回复选择',r'paraphras|rephrase|comment.{0,15}generat|generat.{0,20}comments?|response selection|chatbot|sentence ordering|humor|humour'),
 ('translation','translation_tasks','Translation & Sign Languages / 翻译与手语',r'sign language translation|translation.{0,25}(?:models?|languages?|evaluation|quality)|\btranslations\b|pronoun translation'),
 ('speech_audio','audio_tasks','Speech Separation & Acoustic Tasks / 语音分离与声学任务',r'speech separation|source separation|speech enhancement|multi.speaker (?:speech|audio)|speech synthesis|audio.driven'),
 ('multimodal','visual_grounding','Grounding & Referring Expressions / 视觉定位与指代表达',r'language grounding|referring expression|image.{0,20}caption|\bcaptioning\b|language caption|grounding.{0,30}video|sentence.{0,30}video'),
 ('vision','image_video_tasks','Image, Video & Scene Modeling / 图像、视频与场景建模',r'image deblur|deconvolution|image fusion|Gaussian splatt|neural implicit surfaces|scene reconstruction|video classifi|image modeling|object recognition|object discovery|visual memory|spatial transformations|talking faces'),
 ('generative','energy_models','Energy-Based & Autoregressive Models / 能量与自回归模型',r'energy.based|autoregressive model|\bPixelCNN\b|Boltzmann machine'),
 ('reasoning','commonsense_temporal','Commonsense, Temporal & Relational Reasoning / 常识、时序与关系推理',r'commonsense|common.sense|relational reasoning|temporal reasoning|spatial reasoning|time expressions|temporal ordering|verb physics|\bplanning\b'),
 ('fairness_explainability','explanations','Explanations & Rationales / 解释与论据',r'natural language explanation|rationalization|pertinent negatives|faithfulness tests|feature importance'),
 ('security_privacy','attack_methods','Adversarial & Model Attacks / 对抗与模型攻击',r'adversarial attacks?|poisoning attacks?|Sybil detection|copying black.box|model extraction|malicious'),
 ('robustness','reliability','Reliability & Abstention / 可靠性与拒答',r'abstention|overconfiden|distribution.free predict|risk control|robust guarantees|model misspecification'),
 ('datasets_evaluation','reproducibility','Reproducibility & Annotation / 可复现性与标注',r'reproducibil|unreproducib|annotation scheme|crowdsourced annotation|NLP results|NLP systems fail|\bevaluation sets\b'),
 ('datasets_evaluation','augmentation','Data Augmentation / 数据增强',r'data augmentation|augmentation polic|dataset augment|text augment'),
 ('efficiency_systems','efficient_algorithms','Efficient Algorithms & Computation / 高效算法与计算',r'accelerated deep|efficient training|low precision|sparsified|neural interfaces|hashing|sketching|weight averaging|computational power|efficient invariance'),
 ('representations','representations_other','Representations & Unsupervised Pretraining / 表征与无监督预训练',r'unsupervised learn|word representation|representation model|sentence representation|visual represent|representation similarity|pretraining|pre.training'),
 ('health','neuroscience','Neuroscience & Mental Health / 神经科学与心理健康',r'mental health|brain.{0,25}(?:encoding|imaging|activity)|neural encoding|neuroscience|\bfMRI\b|\bEEG\b|Schizophrenia|cryo.EM'),
 ('science','scientific_tasks','Physical Systems & Earth Science / 物理系统与地球科学',r'ocean forecast|Schr[oö]dinger|many.electron|scientific discover|physical systems|finite.element|conservation law|weather|ocean model'),
 ('reinforcement','sequential_decisions','Sequential Decision & Games / 序贯决策与博弈',r'sequential decision|Markov reward|policy iteration|policy optimi|discounted reward|no.regret.{0,20}games|environment design'),
 ('time_series','ts_modeling','Temporal & Sequence Modeling / 时序与序列建模',r'time[- ]?series|time series|temporal sequence|streaming data'),
 ('time_series','ts_generation','Temporal Generation & Representation / 时序生成与表征',r'time.series.{0,60}(?:generat|representation)|(?:generat|representation).{0,60}time.series'),
 ('probabilistic','hypothesis_testing','Hypothesis Testing & Selection / 假设检验与统计选择',r'hypothesis test|goodness.of.fit|false discovery|multiple testing|selective inference|signal detection|significance test'),
 ('linguistics','fact_verification','Fact Verification & Semantic Matching / 事实核验与语义匹配',r'fact verif|claim verif|semantic matching|presupposition|semantic similarity'),
 ('continual_transfer','model_merging','Model Merging & Reuse / 模型合并与复用',r'model merg|merging.{0,25}models|model fusion|model reuse|heterogeneous models'),
 ('science','mathematics','Mathematics & Symbolic Computation / 数学与符号计算',r'mathematical discover|discovery in mathematics|Gr[oö]bner|symbolic computation|computational algebra'),
 ('architectures','network_design','Network Design & Regularization / 网络设计与正则化',r'capsule network|network normalization|normalization layer|dropout|equivariant architecture|equilibrium model|neural network architecture'),
 ('optimization','bilevel','Bilevel & Hyperparameter Optimization / 双层与超参数优化',r'bilevel optimi|hyperparameter optimi|homotopy optimi|algorithm configuration|loss landscape|learning rate sched'),
 ('reinforcement','gflownets_world','GFlowNets & World Models / 生成式流网络与世界模型',r'GFlowNets?|world model|reward hypothesis'),
 ('recommendation','personalization','Personalized Recommendation / 个性化推荐',r'news recommendation|personalized recommendation|recommendation agents?'),
]
COMPILED=[(p,i,l,re.compile(rx,re.I)) for p,i,l,rx in RULES]
PRIORITY=['datasets_evaluation','security_privacy','fairness_explainability','alignment','translation','retrieval',
 'question_answering','information_extraction','text_generation','speech_audio','linguistics','code','robotics',
 'multimodal','vision','health','science','time_series','tabular','recommendation','social_human','federated','agents','reasoning',
 'generative','graphs','clustering','active_weak','continual_transfer','efficiency_systems','causal','robustness',
 'optimization','learning_theory','reinforcement','probabilistic','representations','language_models','architectures','supervised','finance','other']
assert set(PRIORITY)==set(TOPIC_MAP)

def compact(s):return re.sub(r'\s+',' ',str(s or '')).strip()

def classify(p,fin=None,override=None):
    source=[('title',compact(p['title']),100),('abstract',compact(p.get('abstract')),40)]
    scores={};evidence=[];subtopics=[]
    for parent,ident,label,rx in COMPILED:
        for where,text,score in source:
            m=rx.search(text)
            if m:
                if parent=='datasets_evaluation' and where=='abstract':score=25
                scores[parent]=max(scores.get(parent,0),score)
                subtopics.append(ident)
                evidence.append(dict(topic_id=parent,subtopic_id=ident,source=where,matched=m.group(),
                    excerpt=text[max(0,m.start()-90):m.end()+150],score=score))
                break
    # Explicit resource terms in a title establish a resource-oriented paper.
    title=source[0][1]
    resource=re.search(r'^(?:benchmarking|evaluating|evaluation of)|\b(?:a|an|new|novel|comprehensive|large.scale)\b.{0,45}\b(?:dataset|benchmark|corpus)\b|^\S*(?:Bench|Benchmark):',title,re.I)
    if resource:
        scores['datasets_evaluation']=115
        if 'benchmarks' not in subtopics:subtopics.append('benchmarks')
        evidence.append(dict(topic_id='datasets_evaluation',subtopic_id='benchmarks',source='title',
            matched=resource.group(),excerpt=title,score=115))
    if fin:
        scores['finance']=150 if fin['scope']=='core' else 20
        evidence.append(dict(topic_id='finance',subtopic_id=None,source='confirmed_finance_review',
            matched=fin['scope'],excerpt=compact(fin.get('evidence_excerpt'))[:400],score=scores['finance']))
        if 'time_series' in fin.get('topic_ids',[]) and 'time_series' not in scores:
            scores['time_series']=70;subtopics.append('ts_modeling')
            evidence.append(dict(topic_id='time_series',subtopic_id='ts_modeling',source='reviewed_finance_taxonomy',
                matched='time_series',excerpt=compact(fin.get('evidence_excerpt'))[:400],score=70))
    if not scores and p.get('venue') in {'ACL','EMNLP'}:
        m=re.search(r'natural language|\bNLP\b|\b(?:texts?|sentences?|words?|linguistic|discourse)\b',source[1][1],re.I)
        if m:
            scores['linguistics']=20;subtopics.append('language_tasks')
            evidence.append(dict(topic_id='linguistics',subtopic_id='language_tasks',source='abstract',
                matched=m.group(),excerpt=source[1][1][max(0,m.start()-70):m.end()+160],score=20))
    if not scores:
        scores['other']=0
        evidence.append(dict(topic_id='other',subtopic_id=None,source='title',matched='needs finer classification',excerpt=title,score=0))
    primary=max(scores,key=lambda x:(scores[x],-PRIORITY.index(x)))
    out=dict(primary_topic_id=primary,topic_ids=[i for i,l,d in TOPICS if i in scores],
        subtopic_ids=list(dict.fromkeys(subtopics)),evidence=evidence,
        basis='title_and_official_abstract_rules',review_status='needs_review' if primary=='other' or not p.get('abstract') else 'metadata_classified')
    if override:
        for field in ['primary_topic_id','topic_ids','subtopic_ids']:
            if field in override:out[field]=override[field]
        if 'topic_ids' in override and 'subtopic_ids' not in override:
            parents={i:parent for parent,i,l,rx in RULES}
            out['subtopic_ids']=[i for i in out['subtopic_ids'] if parents[i] in out['topic_ids']]
        out['evidence']=[e for e in out['evidence'] if e['topic_id'] in out['topic_ids']]
        for i in out['topic_ids']:
            if not any(e['topic_id']==i for e in out['evidence']):
                out['evidence'].append(dict(topic_id=i,subtopic_id=None,source='manual_metadata_review',
                    matched=override['reason'],excerpt=override.get('evidence_excerpt') or title,score=120))
        out['manual_override']=override;out['review_status']='manually_reviewed_metadata'
    # A research-label correction cannot alter independently verified finance admission.
    if fin:
        if 'finance' not in out['topic_ids']:out['topic_ids'].append('finance')
        if not any(e['topic_id']=='finance' for e in out['evidence']):
            out['evidence'].append(dict(topic_id='finance',subtopic_id=None,source='confirmed_finance_review',
                matched=fin['scope'],excerpt=compact(fin.get('evidence_excerpt'))[:400],score=20))
        if fin['scope']=='core':out['primary_topic_id']='finance'
    else:assert 'finance' not in out['topic_ids']
    assert out['primary_topic_id'] in out['topic_ids']
    return out

def apply_research_taxonomy(papers,finance):
    DEST.mkdir(exist_ok=True)
    path=DEST/'manual_overrides.json'
    overrides=json.loads(path.read_text()) if path.exists() else {}
    code_hash=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    input_hash=hashlib.sha256(json.dumps(dict(papers=[(p['id'],p['venue'],p['title'],p.get('abstract',''),
        finance.get(p['id'],{}).get('scope'),finance.get(p['id'],{}).get('topic_ids'),
        finance.get(p['id'],{}).get('evidence_excerpt')) for p in papers],overrides=overrides),
        ensure_ascii=False,sort_keys=True).encode()).hexdigest()
    cached_summary=DEST/'summary.json';cached_assignments=DEST/'assignments.json'
    if cached_summary.exists() and cached_assignments.exists():
        old=json.loads(cached_summary.read_text())
        if old.get('source_code_sha256')==code_hash and old.get('input_sha256')==input_hash:
            assignments=json.loads(cached_assignments.read_text())
            assert set(assignments)=={p['id'] for p in papers}
            print('Reused research classifications for identical metadata, rules and manual corrections.',flush=True)
            return assignments
    assignments={}
    for n,p in enumerate(papers,1):
        assignments[p['id']]=classify(p,finance.get(p['id']),overrides.get(p['id']))
        if n%1000==0:print('Research papers classified',n,'/',len(papers),flush=True)
    schema=dict(version=VERSION,topics=list(TOPIC_MAP.values()),
        subtopics=[dict(parent_id=p,id=i,label=l,pattern=rx) for p,i,l,rx in RULES],
        scope='Selected catalog records only, including Best/Oral/confirmed Finance and explicitly marked candidates.',
        basis='Metadata rule classification with evidence passages and ID-based manual corrections; not official conference area labels.')
    summary=dict(version=VERSION,papers=len(papers),abstracts_available=sum(bool(p.get('abstract')) for p in papers),
        topic_counts=dict(Counter(t for a in assignments.values() for t in a['topic_ids'])),
        primary_counts=dict(Counter(a['primary_topic_id'] for a in assignments.values())),
        subtopic_counts=dict(Counter(t for a in assignments.values() for t in a['subtopic_ids'])),
        manual_overrides=sum('manual_override' in a for a in assignments.values()),
        needs_review=sum(a['review_status']=='needs_review' for a in assignments.values()),
        source_code_sha256=code_hash,input_sha256=input_hash)
    for name,obj in [('schema.json',schema),('assignments.json',assignments),('summary.json',summary)]:
        (DEST/name).write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
    return assignments

if __name__=='__main__':
    papers=[json.loads(l) for l in (ROOT/'catalog.jsonl').read_text().splitlines()]
    finance=json.loads((ROOT/'checks/finance_review.json').read_text())['included']
    assignments=apply_research_taxonomy(papers,finance)
    print((DEST/'summary.json').read_text())
