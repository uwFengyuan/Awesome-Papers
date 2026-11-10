"""Human-reviewed taxonomy corrections for boundary cases; never change admission."""
import json
from common import load_json, finance_text_cache
import re
import gzip
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'checks/finance_taxonomy'
papers={p['id']:p for p in load_json('sources/resolved_universe.json.gz')}
finance=json.loads((ROOT/'checks/finance_review.json').read_text())['included']
queue=json.loads((DEST/'remaining_general_queue.json').read_text())
out={}

def decision(pid,primary,topics,subtopics,reason,excerpt=None):
    out[pid]=dict(primary_topic_id=primary,topic_ids=topics,subtopic_ids=subtopics,reason=reason,
        evidence_excerpt=excerpt or papers[pid].get('abstract') or finance[pid]['evidence_excerpt'])

general={
 0:('time_series',['time_series','market_prediction'],['ts_foundation','stock_prediction'],'Time-dependent multimodal stock data and representations, not an unspecified financial application.'),
 1:('financial_agents',['financial_agents','financial_models'],['agent_decisions','financial_reasoning_eval'],'Financial-domain evaluation of agentic temporal memory.'),
 2:('portfolio',['portfolio'],['financial_planning'],'Explicit financial portfolio constraints; generic satisfiability is the method.'),
 3:('portfolio',['portfolio'],['investment_evaluation'],'Financial investment application; the Partial Credit Model is a psychometric model, not a credit-scoring task.'),
 4:('financial_safety',['financial_safety'],['robustness_attacks'],'Backdoor attacks on finance datasets are a security application.'),
 7:('trading',['trading'],['trading_execution'],'FinRL benchmark evaluates financial trading control, not generic financial planning.'),
 8:('financial_models',['financial_models'],['financial_benchmarks'],'Financial-domain test-time evaluation; no narrower task established in the reviewed passage.'),
 13:('financial_qa',['financial_qa','financial_safety'],['knowledge_qa','trust_compliance'],'Financial questions in a factuality benchmark.'),
 16:('fraud_aml',['fraud_aml'],['financial_fraud'],'Fraud-resistant revenue division on subscription platforms.'),
 17:('financial_safety',['financial_safety'],['privacy_security'],'Private-data synthesis includes financial data; retain the privacy application label.'),
 19:('banking',['banking'],['bank_data'],'Reviewed Bank dataset experiment; avoid guessing a finer banking task.'),
 20:('financial_safety',['financial_safety'],['trust_compliance'],'Finance-category truthfulness behavior under model steering.'),
 21:('banking',['banking'],['personal_finance'],'Observed saving and investment advice interactions across socioeconomic groups.'),
 22:('financial_nlp',['financial_nlp'],['nlp_datasets'],'Language embedding evaluations include financial language data; not automatically a retrieval task.'),
 23:('banking',['banking'],['personal_finance'],'Finance-related dialogue about budgets, stocks and retirement.'),
 24:('financial_nlp',['financial_nlp'],['financial_translation'],'Finance-domain application of personalized machine translation.'),
 25:('financial_nlp',['financial_nlp'],['nlp_datasets'],'Procedural language understanding includes finance-domain instructions.'),
 26:('financial_qa',['financial_qa'],['qa_tasks'],'Financial-domain examples in contextual question generation.'),
 28:('financial_nlp',['financial_nlp'],['nlp_datasets'],'Finance-category language classification evaluations.'),
 30:('financial_nlp',['financial_nlp'],['information_extraction'],'Structured extraction from unstructured financial text.'),
 31:('financial_ir',['financial_ir'],['retrieval'],'Financial currency-converter query is an actual generative-search case study.'),
 38:('time_series',['time_series','market_prediction'],['ts_forecasting','fx_crypto'],'Exchange benchmark is the currency time-series forecasting experiment.'),
}
for index,args in general.items():decision(queue[index]['id'],*args)

for index,primary,topics,subtopics,pattern,reason in [
 (6,'credit_risk',['credit_risk'],['financial_risk'],r'Real data Exchange rates','Joint return distributions for financial risk; no temporal forecasting model is asserted.'),
 (9,'asset_pricing',['asset_pricing'],['risk_factors'],r'Stock data factor analysis','Latent stock-risk factor analysis, separate from formulaic alpha discovery.'),
 (11,'market_prediction',['market_prediction'],['stock_prediction'],r'Stock prediction using financial data','The actual financial experiment is stock prediction.'),
 (12,'derivatives',['derivatives'],['option_pricing'],r'financial data application \(predicting equity option values\)','The financial application prices equity options.'),
 (36,'portfolio',['portfolio'],['financial_planning'],r'namely energy planning, financial planning','Financial planning is one of the actual multistage optimization experiments.'),
]:
    x=queue[index];path=finance_text_cache(x['id'])
    text=re.sub(r'\s+',' ',gzip.decompress(path.read_bytes()).decode());m=re.search(pattern,text,re.I);assert m,(index,pattern)
    decision(x['id'],primary,topics,subtopics,reason,text[max(0,m.start()-80):m.end()+450])

core={
 'P17-1126':('financial_nlp',['financial_nlp'],['text_generation'],'Task generates market comments from prices; it does not forecast stock prices.'),
 'P19-1034':('market_prediction',['market_prediction','financial_nlp'],['stock_prediction','volatility_prediction','sentiment_stance'],'Sentiment dictionaries predict excess returns and volatility; this is not LLM pretraining.'),
 'P19-1047':('corporate_finance',['corporate_finance','financial_nlp'],['earnings_disclosure','nlp_datasets'],'Human analysts and earnings calls; not an autonomous financial-agent study.'),
 '2023.acl-long.800':('financial_nlp',['financial_nlp','corporate_finance'],['information_extraction','earnings_disclosure'],'Highlights financial signals and relations in narrative reports; not formulaic alpha mining.'),
 '2022.acl-short.12':('financial_models',['financial_models','financial_nlp'],['financial_benchmarks','sentiment_stance'],'Evaluates stock preferences of pretrained language models; no trading-agent system.'),
 '2024.emnlp-main.601':('financial_nlp',['financial_nlp','document_ai','corporate_finance'],['text_generation','financial_tables','earnings_disclosure'],'Financial report narration is a generation task.'),
 'icml-2026-x6nNQBumUQ':('financial_agents',['financial_agents','financial_models'],['agent_decisions','tools_research','financial_benchmarks'],'Financial agent benchmarking, tooling and structured decision workflows.'),
 'iclr-2026-8AJbbbe2ni':('financial_ir',['financial_ir','financial_agents'],['retrieval','tools_research'],'Financial search and expert information seeking are the central evaluated task.'),
 'iclr-2026-eC4ygDs02R':('financial_agents',['financial_agents','financial_models'],['agent_decisions','domain_models'],'Agent-context adaptation with a financial-domain evaluation.'),
 'iclr-2026-RzT2sombPD':('time_series',['time_series','blockchain'],['ts_generation','crypto_transactions'],'Cryptocurrency time-series generation is the actual task; trading is motivation.'),
 'neurips-2024-94090':('blockchain',['blockchain','financial_safety'],['smart_contracts','privacy_security'],'Financially consequential smart-contract bugs are blockchain/security tasks.'),
 'neurips-2021-w1FvEPcwTnI':('asset_pricing',['asset_pricing','blockchain'],['risk_factors','crypto_transactions'],'Graphical dependence structure of S&P 500, FX and crypto returns; no alpha-expression search.'),
 '2026.acl-long.499':('financial_qa',['financial_qa','document_ai','corporate_finance'],['qa_tasks','financial_tables','real_estate'],'Tabular clarification QA includes real-estate finance; document format is a secondary label.'),
 '2023.emnlp-main.234':('financial_ir',['financial_ir','banking'],['retrieval','customer_intents'],'Financial FAQ retrieval, not loan-default prediction.'),
 '2026.emnlp-main.1329':('corporate_finance',['corporate_finance','time_series'],['earnings_disclosure','ts_forecasting'],'Quarter-ahead company revenue forecasting, not a numerical QA benchmark.'),
 'icml-2026-BZfkxSasd3':('time_series',['time_series','asset_pricing'],['ts_foundation','risk_factors'],'Learns temporal market-state representations and factor structure rather than a stock-direction trading signal.'),
}
for pid,args in core.items():decision(pid,*args)
decision('icml-2026-EKmiOtjZjI','time_series',['time_series'],['ts_uncertainty'],
    'Online conformal prediction on finance and energy series; portfolio selection is the source algorithm, not the evaluated financial investment task.',
    finance['icml-2026-EKmiOtjZjI']['evidence_excerpt'])
assert all(pid in finance for pid in out)
(DEST/'manual_overrides.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('Reviewed taxonomy corrections',len(out))
