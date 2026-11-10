"""Record review of the frozen unclassified queue and title-only exceptions."""
import json
import hashlib
from pathlib import Path
from research_taxonomy import TOPIC_MAP,RULES

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'checks/research_taxonomy'
path=DEST/'remaining_review_queue.json'
queue=json.loads(path.read_text())
groups={
 ('question_answering','qa_reading'):[0,12],
 ('linguistics','semantics'):[1],
 ('linguistics','fact_verification'):[13],
 ('social_human','social_content'):[2,7],
 ('social_human','human_interaction'):[52,140,186],
 ('social_human','social_economics'):[157,163,170,184,195],
 ('information_extraction','ie_knowledge'):[3],
 ('text_generation','dialogue'):[4,11],
 ('speech_audio','speech_synthesis'):[5,32,37,40,103],
 ('recommendation','personalization'):[6,9],
 ('fairness_explainability','interpretability'):[8,39,44,61,125,166,188],
 ('datasets_evaluation','evaluation'):[10,77,124],
 ('datasets_evaluation','reproducibility'):[86],
 ('efficiency_systems','efficient_algorithms'):[14,15,16,83,90,134,143,177],
 ('language_models','lm_pretraining'):[17],
 ('robustness','distribution_shift'):[18,20,21,42,133],
 ('text_generation','generation_tasks'):[19,22],
 ('security_privacy','privacy'):[23,49],
 ('continual_transfer','model_merging'):[24,27,109,128,139],
 ('agents','agent_tools'):[25,30],
 ('retrieval','retrieval_ranking'):[26],
 ('retrieval','retrieval_dense'):[28],
 ('security_privacy','attack_methods'):[29,41,138,171],
 ('graphs','graph_tasks'):[31,36,102,132,137,154,168,191],
 ('generative','energy_models'):[33],
 ('architectures','sequence_models'):[34],
 ('architectures','network_design'):[35,64,67,114,126,141,146,152,175,198],
 ('probabilistic','probabilistic_models'):[38,70,112,150],
 ('optimization','blackbox_bayes_opt'):[43,53,127],
 ('vision','vision_recognition'):[46,176],
 ('optimization','gradient'):[47,62,68,73,75,80,89,105,123,135,160,161,196,199],
 ('optimization','convex'):[48,87],
 ('optimization','combinatorial'):[50,56,59,113,181],
 ('efficiency_systems','systems'):[54],
 ('health','neuroscience'):[51,129],
 ('science','mathematics'):[55,182],
 ('learning_theory','neural_theory'):[57,60,65,72,79,88,94,115,117,120,130,148,151,159,200],
 ('learning_theory','statistical_theory'):[76,116,203,204],
 ('probabilistic','statistical_estimation'):[58,69,84,93,100,136,145,147,162,169],
 ('efficiency_systems','compression'):[63,155,190],
 ('clustering','dimension'):[66,95,106,110,122,197],
 ('supervised','classification_regression'):[71,78,81,121,153,165,179],
 ('reinforcement','sequential_decisions'):[74,91,98,167,193],
 ('causal','causal_discovery'):[82,183],
 ('probabilistic','sampling'):[92],
 ('robotics','control'):[96,104,144],
 ('time_series','ts_dynamics'):[97],
 ('federated','distributed'):[99],
 ('continual_transfer','meta_fewshot'):[101,108],
 ('supervised','structured_prediction'):[107],
 ('probabilistic','hypothesis_testing'):[111,185,192],
 ('code','program_analysis'):[119,149],
 ('representations','embeddings'):[131,142,156],
 ('vision','vision_video'):[158],
 ('science','scientific_computing'):[164],
 ('fairness_explainability','fairness'):[180],
 ('architectures','neural_architecture'):[187],
 ('science','scientific_tasks'):[189,202],
 ('vision','vision_3d'):[194],
 ('robotics','robotics'):[201],
 ('reinforcement','gflownets_world'):[45,178],
 ('science','physics_chemistry'):[85],
 ('supervised','kernel_regression'):[118],
 ('optimization','bilevel'):[172,174],
 ('reinforcement','rl'):[173],
}
parents={i:p for p,i,l,rx in RULES}
out={};seen=set()
for (parent,child),indices in groups.items():
    assert parent in TOPIC_MAP and parents[child]==parent
    for index in indices:
        assert index not in seen,index
        seen.add(index);p=queue[index]
        out[p['id']]=dict(primary_topic_id=parent,topic_ids=[parent],subtopic_ids=[child],
            reason='Human metadata review of the research task or method stated in the title; ambiguous cases checked against the official abstract.',
            evidence_excerpt=p['title']+' | '+p.get('abstract','')[:1300],frozen_queue='remaining_review_queue.json',queue_index=index)
assert seen==set(range(len(queue))),('Unreviewed indices',sorted(set(range(len(queue)))-seen))

# Explicit cross-topic cases whose abstracts clarify the methodological boundary.
for index,extra,extra_child in [(12,'linguistics','semantics'),(44,'multimodal','vision_language'),
    (59,'graphs','graph_tasks'),(63,'architectures','network_design'),(68,'learning_theory','neural_theory'),
    (129,'science','physics_chemistry'),(134,'federated','distributed'),(144,'reinforcement','rl_control'),
    (150,'speech_audio','audio_tasks'),(175,'learning_theory','neural_theory'),
    (180,'datasets_evaluation','data_quality'),(182,'reasoning','reason_math'),
    (190,'vision','image_video_tasks'),(193,'social_human','social_economics'),(201,'continual_transfer','transfer')]:
    d=out[queue[index]['id']];d['topic_ids'].append(extra);d['subtopic_ids'].append(extra_child)
out['2024.emnlp-main.419']=dict(primary_topic_id='information_extraction',
    topic_ids=['information_extraction','language_models'],subtopic_ids=['ie_knowledge','lm_pretraining'],
    reason='Official abstract unavailable; title explicitly identifies information extraction and language models.',
    evidence_excerpt='ADELIE: Aligning Large Language Models on Information Extraction')
out['2024.emnlp-main.122']=dict(primary_topic_id='health',topic_ids=['health','vision'],
    subtopic_ids=['neuroscience','vision_recognition'],
    reason='Official abstract unavailable; title explicitly identifies decoding visual information from fMRI.',
    evidence_excerpt='Decoding the Echoes of Vision from fMRI: Memory Disentangling for Past Semantic Information')
(DEST/'manual_overrides.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
(DEST/'manual_review_manifest.json').write_text(json.dumps(dict(queue_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
    reviewed_queue_records=len(queue),title_only_exceptions=2,manual_overrides=len(out)),indent=2)+'\n')
print('Manual research classifications',len(out))
