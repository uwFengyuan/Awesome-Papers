"""Evidence-based, multi-label research topics, subtopics and independent methods.

This module only classifies already admitted finance papers. It never decides
whether a paper belongs in the collection. Rules and manual overrides are saved
with matching source passages so classifications can be reviewed and revised.
"""
import re
import json
from common import load_json
import hashlib
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT/'checks/finance_taxonomy'
VERSION = '2.0'

# id, bilingual label, spreadsheet name, inclusion boundary
TOPICS = [
 ('alpha_mining','Alpha Mining / 量化因子挖掘','Alpha Mining','因子表达式搜索、自动化 alpha 发现与因子评价；不把一般 alpha 超参数或资产定价混入。'),
 ('time_series','Time Series / 时间序列','Time Series','有金融应用证据的序列预测、生成、表征、异常、缺失及动态建模。'),
 ('asset_pricing','Asset Pricing / 资产定价','Asset Pricing','收益横截面、风险溢价、随机折现因子与资产定价模型。'),
 ('derivatives','Derivatives & Hedging / 衍生品定价与对冲','Derivatives','期权、隐含波动率曲面、衍生品定价与对冲。'),
 ('portfolio','Portfolio & Investment / 投资组合与投资管理','Portfolio','资产配置、组合选择、投资评价与有效前沿；通用模型组合不据此归类。'),
 ('trading','Trading & Microstructure / 交易与市场微观结构','Trading','交易策略、执行、做市、订单簿、市场仿真与预测市场。'),
 ('market_prediction','Market Prediction / 股价、收益与波动率预测','Market Prediction','股票方向与收益、波动率、汇率或加密资产市场预测。'),
 ('credit_risk','Credit & Financial Risk / 信贷与金融风险','Credit and Risk','授信、违约、信用风险、运营风险和尾部风险。'),
 ('insurance','Insurance & Actuarial / 保险与精算','Insurance','承保、保费、理赔、保险业务数据与精算应用。'),
 ('fraud_aml','Fraud & AML / 欺诈检测与反洗钱','Fraud and AML','支付和金融交易欺诈、反洗钱、金融诈骗。'),
 ('financial_nlp','Financial NLP / 金融文本、情感与事件','Financial NLP','金融文本情感、立场、信息抽取、生成和摘要。'),
 ('financial_qa','Financial QA & Reasoning / 金融问答与数值推理','Financial QA','金融知识问答、财报表格计算、数学和多跳推理。'),
 ('financial_ir','Financial IR & RAG / 金融检索与RAG','Financial IR and RAG','金融信息检索、FiQA 检索评测、嵌入、重排与金融 RAG。'),
 ('document_ai','Document AI / 票据、财报与图表理解','Document AI','票据发票、OCR、文档版面、财务表格与金融图表；普通表格分类另标技术方法。'),
 ('financial_agents','Financial Agents / 金融Agent与决策','Financial Agents','金融研究、投资分析、金融工具使用和金融决策 Agent。'),
 ('macro_economics','Macro & Economic Forecasting / 宏观经济与预测','Macro and Economics','宏观指标、货币政策、经济预测、经济活动仿真。'),
 ('corporate_finance','Corporate Finance & Accounting / 公司金融与会计','Corporate and Accounting','盈利、披露、并购、财务报告、会计审计与税务。'),
 ('esg','ESG & Sustainable Finance / ESG与可持续金融','ESG','企业可持续披露、绿色投资、ESG 分析和合规审计。'),
 ('banking','Banking & Customer Service / 银行业务与客户服务','Banking','银行营销、客户意图、客服对话、债务催收及金融服务。'),
 ('blockchain','Blockchain & Digital Assets / 区块链与数字资产','Blockchain','比特币、以太坊、链上交易、智能合约及加密资产数据。'),
 ('financial_safety','Financial Safety & Compliance / 金融安全与合规','Safety and Compliance','金融隐私、金融 LLM 安全、投资建议风险、监管及可信评测。'),
 ('financial_models','Financial Models & Benchmarks / 金融模型与评测资源','Models and Benchmarks','金融领域预训练、领域适配、跨任务金融评测与综合金融资源。'),
 ('other_finance','Other Financial Applications / 其他金融应用','Other Finance','金融相关性已确认，但当前证据未支持更具体的上述任务分类。'),
]
TOPIC_BY_ID={x[0]:dict(id=x[0],label=x[1],sheet=x[2],description=x[3]) for x in TOPICS}

# Stable subtopic identifiers. All patterns use word/phrase semantics, not a
# generic "finance", "risk", "alpha", "tabular" or "portfolio" substring.
RULES = [
 ('alpha_mining','factor_discovery','Alpha Discovery / Alpha与因子发现',r'\balpha (?:factor|mining|discovery)|formulaic alpha|alpha(?:bench|sage|probe|pareto|qcm)\b|quantitative factor (?:mining|discovery)|financial factor (?:mining|discovery)|Cognitive Alpha'),
 ('alpha_mining','factor_evaluation','Factor Evaluation / 因子评价与回测',r'factor (?:evaluat|screen|select)|alpha (?:evaluat|benchmark)|backtesting.*alpha|alpha.*backtesting'),
 ('time_series','ts_forecasting','Forecasting / 序列预测',r'time[- ]?series.{0,75}forecast|forecast.{0,65}time[- ]?series|\b(?:exchange[- ]?rate|fred-md|M4[- ](?:Yearly|Quarterly|Monthly|Daily|Weekly))\b|\b(?:TimeGrad|FEDformer|Autoformer|iTransformer|TimesNet|TimeMixer|N-BEATS)\b'),
 ('time_series','ts_foundation','Representation & Foundation Models / 表征与基础模型',r'time[- ]?series.{0,65}(?:foundation|pretrain|pre-train|representation|embedding)|(?:foundation|pretrain|pre-train|representation).{0,65}time[- ]?series|\b(?:Moirai|Time-LLM|Chronos|Time-MoE)\b'),
 ('time_series','ts_generation','Generation & Simulation / 序列生成与仿真',r'time[- ]?series.{0,65}(?:generat|synthes|simulat)|(?:generat|synthes|simulat).{0,65}time[- ]?series|\b(?:CTBench|SigDiffusions|Diffusion-TS|TimeTok)\b'),
 ('time_series','ts_anomaly','Anomaly Detection / 序列异常检测',r'time[- ]?series.{0,65}(?:anomal|outlier)|(?:anomal|outlier).{0,65}time[- ]?series|\bNIPS-TS-CREDITCARD\b'),
 ('time_series','ts_imputation','Imputation & Irregular Series / 缺失与不规则序列',r'time[- ]?series.{0,80}(?:imput|irregular|missing)|(?:imput|irregular|missing).{0,80}time[- ]?series'),
 ('time_series','ts_dynamics','Causality & Dynamics / 序列因果与动力学',r'(?:causal|differential equation|dynamics|point process).{0,75}(?:time[- ]?series|stochastic process|stock|financ)|time[- ]?series.{0,75}(?:causal|dynamics)|temporal point process|stochastic differential equation|\bNeural MJD\b'),
 ('time_series','ts_uncertainty','Probabilistic Forecasting & Calibration / 概率预测与校准',r'(?:probabilistic|conformal|uncertainty).{0,65}(?:forecast|time[- ]?series)|(?:forecast|time[- ]?series).{0,65}(?:probabilistic|conformal|uncertainty)'),
 ('time_series','ts_general','General Time-Series Methods / 综合序列方法',r'time[- ]?series|\b(?:NASDAQ|NYSE|SP500|S&P 500)\b.{0,50}(?:dataset|forecast|stock data)'),
 ('asset_pricing','pricing_models','Pricing Models & Risk Premia / 定价模型与风险溢价',r'asset pricing|risk premi(?:um|a)|stochastic discount factor|cross[- ]sectional.{0,25}(?:asset|return)|lookahead factor models|factor models for quantitative investing'),
 ('derivatives','option_pricing','Option Pricing & PDEs / 期权定价与PDE',r'option pric|Black[- ]Scholes|American option|derivative pric|pricing.{0,20}derivatives'),
 ('derivatives','hedging','Hedging / 对冲',r'\bhedging\b|hedge.{0,25}(?:option|derivative|asset|financial)|(?:option|financial).{0,25}hedge'),
 ('derivatives','volatility_surface','Implied Volatility / 隐含波动率曲面',r'implied volatility|volatility surface'),
 ('portfolio','allocation','Asset Allocation / 资产配置',r'asset allocation|asset allocat|Black[- ]Litterman|investment polic|sustainable investment'),
 ('portfolio','selection','Portfolio Selection & Optimization / 组合选择与优化',r'portfolio[- ](?:optimi|alloc|select|manag|invest|return|value|benchmark)|efficient frontier|Sharpe ratio|stochastic discount factor portfolios'),
 ('trading','trading_execution','Trading & Execution / 交易策略与执行',r'\btrading\b|trade execution|optimal execution|\bCryptoTrade\b|\bTrade in Minutes\b|arbitrage|financial backtest'),
 ('trading','microstructure','Order Books & Market Impact / 订单簿与市场冲击',r'order book|market impact|market microstructure|market making|market maker|trading.volume|\bLOB[- ]Bench\b'),
 ('trading','market_simulation','Market Simulation / 金融市场仿真',r'(?:financial|stock) market simulat|simulat.{0,30}(?:stock|financial) market|\b(?:MarketSim|TwinMarket|MarS:)\b|financial world model'),
 ('trading','prediction_markets','Prediction Markets / 预测市场',r'prediction markets?'),
 ('market_prediction','stock_prediction','Stock Movement & Returns / 股价方向与收益预测',r'(?:stock|equity|equities).{0,60}(?:predict|forecast)|(?:predict|forecast).{0,60}(?:stock|equity|equities)|financial forecast|stocknet|causalstock|market comments from stock'),
 ('market_prediction','volatility_prediction','Volatility & Tail Forecasts / 波动率与尾部预测',r'volatility (?:predict|forecast)|(?:predict|forecast).{0,55}volatility|financial asset tail dynamics|asset.{0,30}tail dynamics|extremal dependence.{0,30}financial assets'),
 ('market_prediction','fx_crypto','FX & Crypto Forecasts / 汇率与加密资产预测',r'exchange[- ]?rate|(?:crypto|bitcoin).{0,65}(?:forecast|predict)|(?:forecast|predict).{0,65}(?:crypto|bitcoin)'),
 ('credit_risk','credit_default','Credit Scoring & Default / 信用评分与违约',r'credit[- _](?:risk|scor|default|approval|screen|g\b|reg\b)|German[- ]?Credit|Australian[- ]Credit|\b(?:HELOC|FICO|GiveMeSomeCredit|HomeCredit)\b|home[- ]credit|loan[- ](?:default|approv|predict|decision|data)|default.of.credit|Taiwan(?:ese)? credit|loan problem|credit dataset|credit card clients'),
 ('credit_risk','financial_risk','Financial Risk / 金融风险管理',r'financial risk|operational risk|financial.{0,25}stress test|financial asset tail|creditworthiness|credit[- ](?:card|payment).{0,35}default'),
 ('insurance','insurance_business','Insurance & Claims / 承保与理赔',r'insurance|actuarial|allstate|healthcare claims|health claims|inslogic|Insur(?:ance)?QA|homesite|insurance claims'),
 ('fraud_aml','financial_fraud','Payment & Transaction Fraud / 支付与交易欺诈',r'(?:credit[- ]?card|financial|insurance|payment|transaction).{0,65}(?:fraud|anomal)|(?:fraud|anomal).{0,65}(?:credit[- ]?card|financial|insurance|payment|transaction)|\b(?:PaySim|BankSim|T-Finance)\b|innovative image fraud|identity fraud via dialogue|financial scam|procurement fraud'),
 ('fraud_aml','aml','Anti-Money Laundering / 反洗钱',r'money[- ]launder|anti[- ]money|\b(?:AMLSim|Elliptic dataset)\b|illicit bitcoin|bitcoin.{0,55}illicit'),
 ('fraud_aml','scam','Scams & Financial Misinformation / 诈骗与金融虚假信息',r'\bscam|fraud detection|financial misinformation|counterfactual financial misinformation|financial.{0,35}misinformation'),
 ('financial_nlp','sentiment_stance','Sentiment & Stance / 情感与立场',r'financial[- ]?phrase[- ]?bank|financialphrasebank|financial sentiment|sentiment.{0,60}(?:financ|stock|market)|(?:financ|stock|market).{0,60}(?:sentiment|stance)|\bFinEntity\b|\bEFSA\b'),
 ('financial_nlp','information_extraction','Entities, Events & Causality / 实体、事件与关系抽取',r'financial.{0,70}(?:event extract|entity|relation|causal)|(?:entity|event|relation).{0,45}financial|\b(?:(?-i:FiNER)|FinCausal|FinRE|ChFinAnn|DuEE-Fin|Doc2EDAG|FinKario)\b'),
 ('financial_nlp','text_generation','Generation & Summarization / 金融文本生成与摘要',r'\bECTSum\b|earnings? call.{0,65}summari|summari.{0,65}(?:financ|earnings?|report)|financial report generation|market comments|financial text generation|accounting audit procedures generation'),
 ('financial_qa','numerical_reasoning','Numerical & Table Reasoning / 数值与表格推理',r'\b(?:FinQA|ConvFinQA|TAT[- ]?QA|TAT[- ]?DQA|MultiHiertt|FinanceMATH|BizBench|DocFinQA|FinChain|FinanceReasoning|FinMME|CFMME)\b|financial (?:numerical |mathematical |multi-hop |table[- ]text )?reasoning|(?:numerical|math).{0,65}financ'),
 ('financial_qa','knowledge_qa','Knowledge & Conversational QA / 知识与对话问答',r'\b(?:FinTextQA|FinanceBench|PACIFIC|SustainableQA|SAHM)\b|financial.{0,50}question answer|question answer.{0,55}financ|financial.{0,35}multi-hop'),
 ('financial_ir','retrieval','Retrieval, Embedding & Reranking / 检索、嵌入与重排',r'\bF\s*I\s*QA\b|\bFinMTEB\b|financial.{0,65}\b(?:retriev\w*|search|text embedding|rerank\w*)|\b(?:retriev\w*|search|text embedding).{0,65}\bfinanc\w*|\bFinSearchComp\b'),
 ('financial_ir','rag','Financial RAG & Long Documents / 金融RAG与长文档',r'\b(?:FinRAGBench|FinRAGBench-V|REAL-MM-RAG|OmniEval)\b|financial.{0,65}(?:RAG|retrieval.augmented)|(?:RAG|retrieval.augmented).{0,65}financ'),
 ('document_ai','receipts_invoices','Receipts, Invoices & OCR / 票据发票与OCR',r'\b(?:SROIE|CORD|Kleister|Chargrid)\b|receipts?|invoices?|financial.{0,30}(?:OCR|document pars)'),
 ('document_ai','financial_charts','Charts & Visual Understanding / 金融图表与视觉理解',r'financial.{0,55}(?:chart|visual)|(?:chart|visual).{0,55}financ|\b(?:FinChart|FinMME|CFMME|VisFinEval|FCMR|FinRAGBench-V|ChartVA)\b'),
 ('document_ai','reports_tables','Report Layout & Structured Extraction / 财报版面与结构提取',r'\b(?:XBRL|EDINET-Bench)\b|table of contents.{0,60}(?:financial|ESG)|(?:financial|report).{0,50}(?:layout|table extraction|document understanding|parsing)|document understanding.{0,60}(?:report|financial)'),
 ('financial_agents','agent_decisions','Investment & Financial Research Agents / 投研与金融决策Agent',r'(?:financial|invest(?:ment|or)|trading|quantitative|ESG).{0,60}\bagent|\bagent.{0,65}(?:financial|investment|trading)|\b(?:FinCon|FinSight|CryptoTrade|SocioDojo|INVESTORBENCH|FinDeepForecast|MoCA-Agent)\b'),
 ('financial_agents','tools_research','Financial Tools & Deep Research / 金融工具与深度研究',r'financial.{0,45}(?:deep research|tool|search and reasoning)|FinSearchComp|MoCA-Agent|financial report generation'),
 ('macro_economics','macro_forecasting','Macro Indicators & Policy / 宏观指标与政策',r'macroeconomic|\b(?:FRED[- ]MD|FOMC)\b|monetary polic|fiscal polic|economic (?:growth|indicator|forecast)|unemployment rate|Trillion Dollar Words|country.level socio.economic indicators'),
 ('macro_economics','economic_simulation','Economic Behavior & Simulation / 经济行为与仿真',r'EconAgent|economic risk preferences|simulat.{0,40}(?:economic|economy)|economic.{0,35}(?:simulat|interactions)|economy of minds'),
 ('corporate_finance','earnings_disclosure','Earnings & Corporate Disclosures / 盈利与公司披露',r'earnings? call|earning surprise|earnings? forecast|company.{0,20}(?:earnings|revenue)|revenue forecast|corporate.{0,30}(?:disclosure|financial)|financial disclosure|\b(?:EDGAR|EDINET|ECTSum|FinCall-Surprise|(?-i:CAME))\b|SEC filings|financial statements?|annual reports?'),
 ('corporate_finance','ma','Mergers & Acquisitions / 并购与公司事件',r'merger|acquisition.{0,35}financial|M&A|merger.arbitrage'),
 ('corporate_finance','accounting_tax','Accounting, Audit & Tax / 会计、审计与税务',r'\btax(?:ation|payer| returns?| practice| planning| compliance)|TaxPraBen|accounting (?:audit|report|standard|practice|procedure)|audit procedures|bookkeeping|tax and financial education'),
 ('esg','esg_disclosure','ESG Disclosure & Greenwashing / ESG披露与漂绿',r'\bESG\b|sustainability|greenwashing|environmental claim|corporate promise|sustainableqa|ESGenius|ESGPT'),
 ('esg','sustainable_investment','Sustainable Investment / 可持续投资',r'sustainable investment|climate investment|InvestESG|green financ|sustainable financ|environmental development projects'),
 ('banking','customer_intents','Banking Dialogue & Intent / 银行对话与意图',r'\bBANKING77\b|banking|debt collection|bank.{0,30}(?:customer|dialogue|intent|service)|\bBQ Corpus\b|personal finance'),
 ('banking','bank_marketing','Bank Marketing & Churn / 银行营销与客户流失',r'bank[- _]marketing|bank marketing|bank_customer_churn|bank customer churn|term[- ]deposit'),
 ('blockchain','crypto_transactions','Crypto & Blockchain Transactions / 加密资产与链上交易',r'bitcoin|ethereum|cryptocurrenc|blockchain|\b(?:CTBench|CryptoTrade|EX-Graph|BlockScan)\b'),
 ('blockchain','smart_contracts','Smart Contracts & DeFi / 智能合约与DeFi',r'smart contract|\b(?:EVMbench|EVM-QuestBench|DeFi)\b|sandwich equilibria|sandwich attack'),
 ('financial_safety','privacy_security','Financial Privacy & Security / 金融隐私与信息安全',r'financial.{0,65}(?:privacy|security|red.team|harm|safety)|(?:privacy|security|red.team|harm).{0,65}financ|deanonymization.{0,40}bitcoin|credit card (?:numbers?|details|information)|bank card.{0,30}password|wrong credit card|incorrect credit card'),
 ('financial_safety','trust_compliance','Trust, Compliance & Bias / 可信、合规与偏差审计',r'\bFinTrust\b|Shari|financial.{0,65}(?:compliance|trustworthiness|look.ahead|bias|abstention)|(?:look.ahead|temporal leakage|memory biases|risk.adjusted harm).{0,70}(?:financial|finance)|financial backtesting'),
 ('financial_models','domain_models','Financial Pretraining & Adaptation / 金融预训练与领域适配',r'\b(?:FinBERT|FLANG|FLUE|ESGPT|Plutus)\b|financial.{0,65}(?:pretrain|pre-train|language model|LLMs?|domain adapt)|(?:pretrain|pre-train|domain adapt).{0,65}financial'),
 ('financial_models','financial_benchmarks','Cross-Task Financial Evaluation / 跨任务金融综合评测',r'\b(?:FinBen|MultiFinBen|FinMME|CFMME|BizFinBench|VisFinEval|FinTrust)\b|financial.{0,40}(?:multimodal evaluation|application benchmark)|benchmarking.{0,50}(?:Greek Finance|finance domain)'),
 ('credit_risk','credit_data','Lending & Credit Data / 借贷与信贷数据应用',r'\bloans?\b|\blending\b|mortgage|credit (?:graph|network|loan|agreement|line|card|balance)|\bcreditcard\b|default credit|consumer finance|assessment of credit|\bCredit[- ]Card\b|\bcredit8\b'),
 ('fraud_aml','banknote_authentication','Banknote Authentication / 钞票真伪识别',r'banknote'),
 ('banking','bank_data','Banking Data Applications / 银行业务数据应用',r'\bBank dataset\b|\bBank\b.{0,12}\d?\.\d{3}|bank accounts?|Bank of America'),
 ('financial_nlp','nlp_datasets','Financial Language Tasks & Corpora / 金融语言任务与语料',r'financial NLP|financial domain RE|financial event types|Earnings-21|financial numeric entity|finance news|金融\(Finance\)|财务\(Finance\)'),
 ('portfolio','investment_evaluation','Investment Evaluation & Decisions / 投资评价与决策',r'sequential investment|financial rebalancing|mean.field portfolio|mean.variance portfolio|optimal consumption and investment|investment decisions|low quality funds|portfolio (?:study|problem|game|risk management)|machine learning portfolio'),
 ('financial_qa','qa_tasks','Financial Reasoning Tasks / 金融推理任务',r'financial QA|financial credit agreements|financial (?:and scientific|or scientific).{0,40}numeric|numeric.{0,45}financial|Finance Formula|TheoremQA|financial laws|finance reports'),
 ('document_ai','financial_tables','Financial Tables & Spreadsheets / 财务表格与电子表格',r'FinTabNet|spreadsheets for finance|financial reports paired|tables.{0,90}finance|finance.{0,50}tables'),
 ('time_series','financial_processes','Financial Stochastic Processes / 金融随机过程',r'stochastic volatility|financial data prediction|stock market models|\bNASDAQ series\b|stock market data|finance and weather forecasting|30 P ORTFOLIOS|Financial Trans.{0,5}actions'),
 ('financial_models','numerical_finance','Numerical Finance / 计算金融与数值方法',r'financial integral|financial operations|finance on point clouds|financial.{0,20}PDE'),
 ('financial_safety','financial_regulation','Financial Regulation / 金融监管与业务规则',r'financial regulations|financial laws|financial.{0,40}regulatory|FinLLM-Eval'),
 ('financial_nlp','claim_verification','Financial Claim Verification / 金融声明核验',r'FinDVer|financial.{0,30}(?:claim verification|fact.verification)|(?:claim verification|fact.verification).{0,40}financ'),
 ('portfolio','financial_planning','Financial Planning / 财务规划',r'financial planning|financial portfolios'),
 ('corporate_finance','real_estate','Real Estate & Business Finance / 房地产与企业财务应用',r'real estate|real-estate|realty|housing.{0,30}(?:financial|investment)|financial properties of the housings'),
 ('financial_models','financial_reasoning_eval','Professional Financial Evaluation / 金融专业能力评测',r'ProfBench|PRBench|Finance MBA|FinTMMBench'),
 ('financial_safety','robustness_attacks','Adversarial Robustness in Finance / 金融应用中的攻击与防御',r'finance.{0,20}backdoor|backdoor.{0,30}finance'),
 ('asset_pricing','risk_factors','Risk Factor Models / 市场风险因子建模',r'stock data factor analysis|financial factor model|lookahead factor model|factor models for quantitative investing'),
 ('financial_nlp','financial_translation','Financial Translation / 金融翻译',r'translat.{0,60}(?:financial|finance|tax)|financial.{0,60}translat'),
 ('banking','personal_finance','Personal Finance Interaction / 个人理财交互',r'personal finance|finance.{0,15}(?:budgets|budgeting)|financial advice'),
]

# These task-level fallbacks only apply if the specific rules above do not
# identify a topic. Their finance application is established by admission
# evidence, and the task is established independently by the title.
FALLBACK_RULES = [
 ('financial_safety','privacy_security',r'jailbreak|security|harmless|harmful|saniti|leakage|honeypot|extraction attacks|red.team|deception|ideolog|hijack|safety|refusal|policy alignment'),
 ('financial_ir','retrieval',r'retriev|rerank|re.rank|information.seek|text matching|text embedding|query.focused'),
 ('financial_qa','qa_tasks',r'question answer|\bQA\b|mathematical reasoning|number prediction|tabular reasoning|table understanding|aggregation queries|quantity extractor'),
 ('financial_nlp','information_extraction',r'named entity|\bNER\b|entity recognition|relation extraction|information extraction|word segmentation|sequence labeling'),
 ('financial_nlp','text_generation',r'summariz|summaris|text generation|writing|news comment generation|simplification|text.to.table|translating headers'),
 ('financial_nlp','sentiment_stance',r'sentiment|stance detection'),
 ('financial_nlp','nlp_datasets',r'text classifi|text categor|dialectal corpus|word sense|ChineseBERT|language translation|narrative media|news.{0,40}fake news'),
 ('document_ai','financial_charts',r'visualization|visual semantics|visual.semantic|multimodal.{0,40}comprehension|General.Bench|vision.language'),
 ('financial_agents','agent_decisions',r'\bagents?\b|negotiation|tool.call|tool.using|MCP|FutureX|ForecastBench|ForecastCompass|InsightBench|AutoDiscovery'),
 ('banking','customer_intents',r'conversational|dialog|acoustic memory'),
 ('trading','microstructure',r'clear the market|transaction costs'),
 ('credit_risk','financial_risk',r'CVaR|risk.aware|model risk management'),
 ('time_series','financial_processes',r'data streams|changepoint|score climbing|stochastic process|spatio.temporal'),
 ('financial_models','domain_models',r'domain adapt|fine.tun|model merging|models.{0,20}merg|pretrain|pre.train|distillat|domain.specific|specialized generalist|memory decoder|AMARIS|VersaTune|REEF|LLM DNA|GEPA'),
 ('financial_models','financial_benchmarks',r'benchmark|evaluation|evaluating|reasoning|LLMs?|language models?|test.time scaling'),
]

METHODS = [
 ('llm','Language Models & LLM / 语言模型与LLM',r'\bLLMs?\b|language models?|instruction.tuning|GPT[- ]?\d|\b(?:Llama|Qwen|BERT)\b'),
 ('reinforcement_learning','Reinforcement Learning / 强化学习',r'reinforcement learning|\bRL\b|bandit|GFlowNet|Q.learning'),
 ('graph_learning','Graph Learning / 图学习',r'graph neural|graph learning|graph convolution|graph attention|\bGNNs?\b|hypergraph|graph fraud'),
 ('diffusion_flow','Diffusion & Flow / 扩散与流模型',r'diffusion|flow matching|normalizing flows?|rectified flow'),
 ('generative','Generative Modeling / 生成建模',r'generative|synthetic data|data synthesis|\bGANs?\b|variational autoencoder|data generation'),
 ('transformer','Transformer / Transformer模型',r'transformer|self.attention'),
 ('causal','Causal Learning / 因果学习',r'causal|structural causal|causality'),
 ('fairness_recourse','Fairness & Recourse / 公平性与算法追索',r'fairness|fair learning|fair representation|counterfactual explanation|algorithmic recourse|strategic classification'),
 ('uncertainty_robustness','Uncertainty & Robustness / 不确定性与鲁棒性',r'uncertainty|conformal|robust|distribution shift|adversarial|calibration'),
 ('privacy','Privacy & Federated Learning / 隐私与联邦学习',r'differential privacy|differentially private|privacy.preserving|federated learning|private learning|unlearning'),
 ('tabular','Tabular Learning / 表格学习',r'tabular|decision tree|random forest|gradient boost|TabPFN|TabM\b|TabDPT'),
 ('multimodal','Multimodal Learning / 多模态学习',r'multi.modal|cross.modal|vision.language|visual.language|audio.text|text.audio'),
 ('retrieval','Retrieval & RAG / 检索与RAG',r'\bRAG\b|retrieval|re-rank|rerank|search engine'),
 ('optimization','Optimization & Numerical Methods / 优化与数值方法',r'optimization|optimisation|optimal control|differential equations?|convex|gradient descent|subgradient|PDE|branch.and.bound'),
 ('representation','Representation Learning / 表征学习',r'representation learning|contrastive learning|embeddings?|pre.training|pretraining'),
]

def compact(text):
    return re.sub(r'\s+',' ',re.sub(r'[\x00-\x08\x0b-\x1f]',' ',str(text or ''))).strip()

def classify(paper, info, override=None):
    sources=[('title',compact(paper['title']),100),
             ('finance_evidence',compact(info.get('evidence_excerpt')),65),
             ('abstract',compact(paper.get('abstract')),40)]
    evidence=[];scores={};subtopics=[]
    for parent,ident,label,pattern in RULES:
        matches=[]
        for source,text,score in sources:
            match=re.search(pattern,text,re.I)
            if match:
                matches.append(dict(topic_id=parent,subtopic_id=ident,label=label,source=source,
                    matched=match.group(),excerpt=text[max(0,match.start()-100):match.end()+180],score=score))
        if matches:
            best=max(matches,key=lambda x:x['score'])
            evidence.append(best);subtopics.append(ident)
            scores[parent]=max(scores.get(parent,0),best['score'])
    if not scores:
        for parent,ident,pattern in FALLBACK_RULES:
            m=re.search(pattern,sources[0][1],re.I)
            if m:
                label=next(r[2] for r in RULES if r[1]==ident)
                scores[parent]=25;subtopics.append(ident)
                evidence.append(dict(topic_id=parent,subtopic_id=ident,label=label,
                    source='title_and_confirmed_finance_evidence',matched=m.group(),
                    excerpt='Title: '+sources[0][1]+' | Financial application: '+sources[1][1][:350],score=25))
                break
    if not scores:
        scores['other_finance']=0
        evidence.append(dict(topic_id='other_finance',subtopic_id=None,source='finance_evidence',
            matched='confirmed finance inclusion',excerpt=compact(info.get('evidence_excerpt'))[:350],score=0))
    # Prefer the actual financial task when a title is equally specific about a
    # model or resource. Keep time-series as an additional independent label.
    priority=['alpha_mining','derivatives','asset_pricing','portfolio','trading','credit_risk','fraud_aml','insurance',
        'market_prediction','financial_qa','financial_ir','document_ai','esg','macro_economics',
        'corporate_finance','banking','financial_safety','financial_agents','time_series','blockchain',
        'financial_nlp','financial_models','other_finance']
    primary=max(scores,key=lambda k:(scores[k],-priority.index(k)))
    topic_ids=[x[0] for x in TOPICS if x[0] in scores]
    methods=[];method_evidence=[]
    for ident,label,pattern in METHODS:
        for source,text,_ in [sources[0],sources[2]]:
            m=re.search(pattern,text,re.I)
            if m:
                methods.append(ident);method_evidence.append(dict(method_id=ident,source=source,matched=m.group(),
                    excerpt=text[max(0,m.start()-65):m.end()+100]));break
    result=dict(primary_topic_id=primary,topic_ids=topic_ids,subtopic_ids=subtopics,method_ids=methods,
        topic_evidence=evidence,method_evidence=method_evidence)
    if override:
        for key in ['primary_topic_id','topic_ids','subtopic_ids','method_ids']:
            if key in override:result[key]=override[key]
        assert result['primary_topic_id'] in result['topic_ids']
        if 'topic_ids' in override and 'subtopic_ids' not in override:
            parents={r[1]:r[0] for r in RULES}
            result['subtopic_ids']=[s for s in result['subtopic_ids'] if parents[s] in result['topic_ids']]
        result['topic_evidence']=[e for e in result['topic_evidence'] if e['topic_id'] in result['topic_ids']]
        if override.get('evidence_excerpt'):
            for topic_id in result['topic_ids']:
                if not any(e['topic_id']==topic_id for e in result['topic_evidence']):
                    result['topic_evidence'].append(dict(topic_id=topic_id,subtopic_id=None,
                        source='manual_review',matched=override['reason'],excerpt=override['evidence_excerpt'],score=110))
        result['manual_override']=override
    # "General time series" is a fallback subtopic, not an extra redundant tag.
    ts_ids={i for parent,i,label,rx in RULES if parent=='time_series'}
    if len(ts_ids.intersection(result['subtopic_ids']))>1:
        result['subtopic_ids']=[s for s in result['subtopic_ids'] if s!='ts_general']
    return result

def apply_taxonomy(papers,review):
    DEST.mkdir(exist_ok=True)
    path=DEST/'manual_overrides.json'
    overrides=json.loads(path.read_text()) if path.exists() else {}
    assignments={};sub_labels={r[1]:r[2] for r in RULES};method_labels={r[0]:r[1] for r in METHODS}
    for pid,info in review['included'].items():
        result=classify(papers[pid],info,overrides.get(pid));assignments[pid]=result
        info['primary_topic']=TOPIC_BY_ID[result['primary_topic_id']]['label']
        info['topic_ids']=result['topic_ids'];info['topics']=[TOPIC_BY_ID[x]['label'] for x in result['topic_ids']]
        info['subtopic_ids']=result['subtopic_ids'];info['subtopics']=[sub_labels[x] for x in result['subtopic_ids']]
        info['method_ids']=result['method_ids'];info['methods']=[method_labels[x] for x in result['method_ids']]
        info['taxonomy_version']=VERSION
    schema=dict(version=VERSION,topics=list(TOPIC_BY_ID.values()),
        subtopics=[dict(parent_id=p,id=i,label=l,pattern=rx) for p,i,l,rx in RULES],
        methods=[dict(id=i,label=l,pattern=rx) for i,l,rx in METHODS],
        notes=['Only already admitted finance papers are classified.',
            'Primary topic is single-valued. Topics, subtopics and methods are multi-label.',
            'Topic matches use title, reviewed financial evidence and abstract, with source passages retained.',
            'Method tags use title and abstract and do not imply a finance-specific method.',
            'Rules provide an initial classification; ID-based manual overrides are retained separately.'])
    summary=dict(version=VERSION,finance_papers=len(assignments),
        topic_counts=dict(Counter(t for a in assignments.values() for t in a['topic_ids'])),
        primary_topic_counts=dict(Counter(a['primary_topic_id'] for a in assignments.values())),
        subtopic_counts=dict(Counter(t for a in assignments.values() for t in a['subtopic_ids'])),
        method_counts=dict(Counter(t for a in assignments.values() for t in a['method_ids'])),
        manual_overrides=len(overrides),source_code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    for name,data in [('schema.json',schema),('assignments.json',assignments),('summary.json',summary)]:
        (DEST/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
    review['taxonomy']=dict(version=VERSION,schema='checks/finance_taxonomy/schema.json',
        assignments='checks/finance_taxonomy/assignments.json',manual_overrides='checks/finance_taxonomy/manual_overrides.json')
    return summary

if __name__=='__main__':
    papers={p['id']:p for p in load_json('sources/resolved_universe.json.gz')}
    review=json.loads((ROOT/'checks/finance_review.json').read_text())
    summary=apply_taxonomy(papers,review)
    (ROOT/'checks/finance_review.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(summary,ensure_ascii=False,indent=2))
