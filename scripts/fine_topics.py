"""Optional, evidenced leaf tasks below the research and finance taxonomies."""
import re

# parent, stable leaf id, bilingual name, metadata pattern
RULES = [
 ('agents','agent_memory','Memory / 记忆',r'agent.{0,40}memor|memor.{0,40}agent'),
 ('agents','multi_agent','Multi-agent collaboration / 多Agent协作',r'multi.agent|agent collaboration'),
 ('agents','tool_use','Tool use / 工具调用',r'tool.{0,20}(?:call|use)|function.call|computer.use'),
 ('agents','agent_planning','Planning / Agent规划',r'planning|workflow|agentic search'),
 ('language_models','pretraining','Pretraining / 预训练',r'pre.train|language model pretraining'),
 ('language_models','context_learning','In-context learning / 上下文学习',r'in.context learning|few.shot prompting'),
 ('language_models','knowledge_editing','Knowledge editing / 知识编辑',r'knowledge edit|model edit|parametric knowledge'),
 ('language_models','fine_tuning','Fine-tuning / 微调',r'fine.tun|instruction.tun|low.rank adaptation'),
 ('language_models','scaling','Scaling / 缩放',r'scaling law|model scaling|compute.optimal'),
 ('language_models','architecture','Architectures / 架构',r'mixture.of.experts|state.space model|transformer architect'),
 ('alignment','preference_optimization','Preference optimization / 偏好优化',r'\bDPO\b|preference optimi|direct preference'),
 ('alignment','reward_modeling','Reward modeling / 奖励建模',r'reward model|reward learning|process reward'),
 ('alignment','rlhf','RLHF / 人类反馈强化学习',r'\bRLHF\b|reinforcement learning from human'),
 ('alignment','safety_alignment','Safety alignment / 安全对齐',r'harmless|constitutional|safety align'),
 ('reasoning','mathematics','Mathematical reasoning / 数学推理',r'mathematical reason|math problem|theorem prov'),
 ('reasoning','logical_reasoning','Logical reasoning / 逻辑推理',r'logic|deductive|symbolic reason'),
 ('reasoning','search_planning','Search and planning / 搜索与规划',r'tree.search|Monte.Carlo.tree|planning|search algorithm'),
 ('reasoning','chain_of_thought','Chain of thought / 思维链',r'chain.of.thought|reasoning traject|test.time.scal'),
 ('retrieval','dense_retrieval','Dense retrieval / 稠密检索',r'dense retriev|bi.encoder|embedding.{0,20}retriev'),
 ('retrieval','rag','Retrieval augmented generation / 检索增强生成',r'retrieval.augmented|\bRAG\b'),
 ('retrieval','reranking','Reranking / 重排',r'rerank|re.rank|cross.encoder'),
 ('translation','low_resource','Low-resource translation / 低资源翻译',r'low.resource|zero.shot|unsupervised.{0,20}translat'),
 ('translation','simultaneous','Simultaneous translation / 同声翻译',r'simultaneous|streaming translat'),
 ('translation','multilingual','Multilingual transfer / 多语言迁移',r'multilingual|cross.lingual'),
 ('translation','document_translation','Document translation / 文档翻译',r'document.level|context.aware translat'),
 ('translation','non_autoregressive','Non-autoregressive translation / 非自回归翻译',r'non.autoregress|iterative refin'),
 ('linguistics','dependency_parsing','Dependency parsing / 依存句法',r'dependency pars|dependency tree'),
 ('linguistics','constituency_parsing','Constituency parsing / 成分句法',r'constituency|constituent pars'),
 ('linguistics','sentiment','Sentiment and stance / 情感与立场',r'sentiment|stance detect'),
 ('linguistics','inference','Semantic inference / 语义推断',r'natural language inference|textual entail|semantic pars'),
 ('linguistics','morphology','Morphology and segmentation / 形态与分词',r'morpholog|word segmentation|lexical segmentation'),
 ('linguistics','discourse','Discourse and pragmatics / 篇章与语用',r'discourse|pragmatic|coreference'),
 ('text_generation','summarization','Summarization / 摘要',r'summari'),
 ('text_generation','dialogue','Dialogue / 对话',r'dialogue|conversation|chatbot'),
 ('text_generation','controlled_generation','Controlled generation / 可控生成',r'controll.{0,20}generat|constrained decoding'),
 ('information_extraction','named_entities','Named entities / 命名实体',r'named.entity|entity recogn|entity link'),
 ('information_extraction','relations','Relation extraction / 关系抽取',r'relation extract|relation classifi'),
 ('information_extraction','events','Event extraction / 事件抽取',r'event extract|event detect|event corefer'),
 ('reinforcement','offline_rl','Offline reinforcement learning / 离线强化学习',r'offline|batch reinforcement'),
 ('reinforcement','model_based_rl','Model-based reinforcement learning / 模型式强化学习',r'model.based|world model'),
 ('reinforcement','policy_optimization','Policy optimization / 策略优化',r'policy gradient|policy optimi|actor.critic'),
 ('reinforcement','exploration','Exploration / 探索',r'exploration|intrinsic reward'),
 ('reinforcement','multi_agent_rl','Multi-agent reinforcement learning / 多Agent强化学习',r'multi.agent|cooperative reinforcement'),
 ('optimization','adaptive_gradient','Adaptive gradients / 自适应梯度',r'adaptive gradient|\bAdam\b|AdaGrad'),
 ('optimization','variance_reduction','Variance reduction / 方差缩减',r'variance.reduc|SVRG|SAGA'),
 ('optimization','distributed_optimization','Distributed optimization / 分布式优化',r'distributed|decentralized|communication.efficient'),
 ('optimization','stochastic_optimization','Stochastic optimization / 随机优化',r'stochastic|SGD|mini.batch'),
 ('optimization','convex_optimization','Convex optimization / 凸优化',r'\bconvex\b|proximal|primal.dual'),
 ('optimization','nonconvex_optimization','Nonconvex optimization / 非凸优化',r'non.convex|nonconvex|saddle.point'),
 ('time_series','forecasting','Forecasting / 预测',r'forecast|time.series predict'),
 ('time_series','foundation_models','Foundation models / 基础模型',r'foundation|pre.train|pretrain|representation'),
 ('time_series','generation','Generation / 生成',r'generat|synthes|simulat'),
 ('time_series','anomaly_detection','Anomaly detection / 异常检测',r'anomal|outlier'),
 ('time_series','imputation','Imputation / 缺失处理',r'imput|missing|irregular'),
 ('alpha_mining','llm_factor_discovery','LLM factor discovery / LLM因子发现',r'language model|\bLLM\b|agent'),
 ('alpha_mining','rl_factor_discovery','RL factor discovery / 强化学习因子发现',r'reinforcement|\bRL\b'),
 ('alpha_mining','search_factor_discovery','Factor search / 因子搜索',r'tree.search|MCTS|symbolic|genetic'),
 ('alpha_mining','factor_evaluation','Factor evaluation / 因子评价',r'evaluat|backtest|benchmark'),
 ('generative','diffusion','Diffusion / 扩散',r'diffusion|score.match'),
 ('generative','flow_matching','Flow matching / 流匹配',r'flow.match|rectified.flow|normalizing.flow'),
 ('generative','variational','Variational models / 变分模型',r'variational|autoencoder|\bVAE'),
 ('efficiency_systems','quantization','Quantization / 量化',r'quanti[sz]|low.bit'),
 ('efficiency_systems','distillation','Distillation / 蒸馏',r'distill'),
 ('efficiency_systems','pruning','Pruning / 剪枝',r'prun|sparsif|sparse network'),
 ('efficiency_systems','efficient_attention','Efficient attention / 高效注意力',r'efficient.attention|flash.attention|linear.attention'),
]


def leaf(paper, parent):
    title=paper['title'];abstract=paper.get('abstract','')
    matches=[]
    for topic,ident,label,pattern in RULES:
        if topic!=parent:continue
        for source,text,score in [('title',title,100),('abstract',abstract,10)]:
            match=re.search(pattern,text,re.I)
            if match:
                matches.append((score,ident,label,dict(source=source,matched=match.group(),
                    excerpt=text[max(0,match.start()-70):match.end()+120])))
                break
    if matches:
        best=max(matches,key=lambda r:r[0])
        return best[1],best[2],best[3]
    return 'general','General / 综合',{'source':'parent_topic','matched':parent,
        'excerpt':'No more specific leaf task is established by the current metadata.'}
