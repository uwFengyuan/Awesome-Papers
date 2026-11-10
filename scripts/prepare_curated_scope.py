"""Merge auditable metadata, reuse local finance evidence, and enforce long-paper scope."""
from common import *
import csv
import io
import re
import subprocess
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from bs4 import BeautifulSoup
import openpyxl
from urllib.parse import urlparse, parse_qs, urljoin
from paper_attributes import award_types, paper_length, publication_track
from paper_deduplication import deduplicate

REFERENCE = pathlib.Path('/home/qi/aiagent/Awesome-AI4Finance-Papers')
REFERENCE_MAIN = REFERENCE if (REFERENCE/'finance_catalog.jsonl').exists() else REFERENCE/'main'
DEST = ROOT/'checks/scope_revision'
ALLOWED = {'main', 'datasets_benchmarks', 'evaluations'}
FIN = re.compile(r'financ(?:e|ial)|stock[- ](?:market|price|movement|predict)|earnings|credit[- ](?:risk|scor|default)|money[- ]launder|insurance|banking|investment|cryptocurr|\bESG\b|\b(?:FinQA|ConvFinQA|TAT-QA|FinBERT|FinTextQA|FinanceBench|FinMTEB|FinRAG|FinCon|FinSearchComp|FinanceMATH|FOMC|XBRL)\b', re.I)
DATA = re.compile(r'\b(?:FinQA|ConvFinQA|TAT-QA|MultiHiertt|FiQA|FinancialPhraseBank|FinanceBench|FinMTEB|EDGAR|FOMC|StockNet|FinTextQA)\b', re.I)


def cached(key):
    path=RAW/(key+'.gz')
    return gzip.decompress(path.read_bytes()) if path.exists() else None


def url(key):
    path=RAW/(key+'.meta.json')
    return json.loads(path.read_text())['url'] if path.exists() else ''


def length_evidence():
    labels={}
    key='emnlp-2023-oral-tsv'
    for row in csv.DictReader(io.StringIO((cached(key) or b'').decode()), delimiter='\t'):
        value=row.get('Length','').lower()
        if value.startswith(('long','short')):
            labels[('EMNLP',2023,norm(row['Title']))]=(value.split()[0],url(key))
    key='emnlp-2025-program-xlsx'
    if cached(key):
        wb=openpyxl.load_workbook(io.BytesIO(cached(key)),read_only=True,data_only=True)
        for sheet in wb:
            for row in sheet.values:
                if len(row)>8 and str(row[8]).lower() in {'long','short'}:
                    labels[('EMNLP',2025,norm(str(row[2])))]=(str(row[8]).lower(),url(key))
        wb.close()
    return labels


def aaai_records():
    rules=json.loads((REFERENCE_MAIN/'checks/aaai_expansion/track_rules.json').read_text())
    records={}
    for path in sorted((REFERENCE_MAIN/'sources/aaai').glob('crossref_*.json.gz')):
        for item in json.loads(gzip.decompress(path.read_bytes()))['message']['items']:
            volume=item.get('volume','')
            if not str(volume).isdigit() or not 31<=int(volume)<=40:continue
            year=int(volume)+1986
            issue=str(item.get('issue',''))
            if year>=2020 and (not issue.isdigit() or not 1<=int(issue)<=rules[str(year)]['last_main_issue']):continue
            page=item.get('resource',{}).get('primary',{}).get('URL','')
            ident=page.rstrip('/').split('/')[-1]
            if not ident.isdigit():continue
            doi=item['DOI']
            clean=lambda text:BeautifulSoup(str(text),'lxml').get_text(' ',strip=True)
            paper=dict(id=f'aaai-{year}-{ident}',venue='AAAI',year=year,
                title=clean(' '.join(item.get('title',[]))),abstract=clean(item.get('abstract','')),
                authors=[' '.join(filter(None,[a.get('given'),a.get('family')])) for a in item.get('author',[])],
                paper_url=page,doi=doi,volume=volume,issue=issue,track='main',
                pdf_url=next((x['URL'] for x in item.get('link',[]) if x.get('content-type')=='application/pdf'),''),
                metadata_sources=['https://api.crossref.org/works/'+doi],abstract_source='https://api.crossref.org/works/'+doi,
                booktitle='Proceedings of the AAAI Conference on Artificial Intelligence',
                awards=[],award_evidence=[],oral=False,oral_evidence=[],presentation_original=[],code_urls=[])
            records[paper['id']]=paper
    # Only explicitly outstanding MAIN awards; special/student/distinguished sections stop admission.
    chunks=defaultdict(list);year=None;active=False
    soup=BeautifulSoup(cached('aaai-awards-history') or b'','lxml')
    main=soup.find('main') or soup
    for line in main.get_text('\n',strip=True).splitlines():
        if re.fullmatch(r'20\d{2}',line):year=int(line);active=False
        if re.search(r'AAAI.\d\d.*(?:Paper Award|Paper Recognition)',line,re.I):
            active=bool(re.search('Outstanding Paper Award',line,re.I)) and not re.search(r'student|social|alignment|demonstration',line,re.I)
        if re.search(r'^Honorable Mention|^Distinguished|Student Abstract|Demonstration Award',line,re.I):active=False
        if active and year:chunks[year].append(line)
    award_text={y:norm(' '.join(lines)) for y,lines in chunks.items()}
    for p in records.values():
        if len(norm(p['title']))>20 and norm(p['title']) in award_text.get(p['year'],''):
            p['awards']=['Outstanding Paper Award'];p['award_evidence']=[url('aaai-awards-history')]
    oral_text={}
    key='aaai-2026-oral-program'
    if cached(key):
        raw=cached(key)
        if raw.startswith(b'%PDF'):
            path=pathlib.Path('/tmp/awesome-aaai-2026-oral.pdf');path.write_bytes(raw)
            text=subprocess.check_output(['pdftotext','-x','191','-y','0','-W','190','-H','2000',str(path),'-']).decode(errors='replace')
        else:text=BeautifulSoup(raw,'lxml').get_text(' ',strip=True)
        oral_text[2026]=(norm(text),url(key))
    key='aaai-2025-oral-program'
    if cached(key):
        path=pathlib.Path('/tmp/awesome-aaai-2025-oral.pdf');path.write_bytes(cached(key))
        # Crop the official table's title column so wrapped titles are not interleaved with authors.
        text=subprocess.check_output(['pdftotext','-x','262','-y','0','-W','220','-H','2000',str(path),'-']).decode(errors='replace')
        oral_text[2025]=(norm(text),url(key))
    key='aaai-2020-program'
    if cached(key):
        path=pathlib.Path('/tmp/awesome-aaai-2020-program.pdf');path.write_bytes(cached(key))
        text=subprocess.check_output(['pdftotext',str(path),'-']).decode(errors='replace')
        # Technical-session paper talks are distinct from the program's explicitly named poster spotlights.
        sections=re.split(r'(?i)poster spotlight',text)
        # Keep this source for coverage review, without automatically treating spotlight titles as Oral.
        (DEST/'aaai2020_program_for_review.txt').write_text(text)
    for p in records.values():
        if p['year'] in oral_text:
            text,evidence=oral_text[p['year']]
            if len(norm(p['title']))>22 and norm(p['title']) in text:
                p.update(oral=True,oral_evidence=[evidence],presentation_original=['Oral'])
    return [p for p in records.values() if p['oral'] or p['awards']]


def findings_records():
    result=[]
    for year in range(2020,2027):
        key=f'findings-{year}-anthology'
        raw=cached(key)
        if not raw:continue
        root=ET.fromstring(raw)
        for volume in root.findall('volume'):
            if volume.get('id') not in {'acl','emnlp'}:continue
            for node in volume.findall('paper'):
                ident=f"{year}.findings-{volume.get('id')}.{node.get('id')}"
                text=lambda tag:' '.join(''.join(e.itertext()) for e in node.findall(tag)).strip()
                title,abstract=text('title'),text('abstract')
                if not FIN.search(title+' '+abstract):continue
                page='https://aclanthology.org/'+ident+'/'
                p=dict(id=ident,venue=volume.get('id').upper(),year=year,title=title,abstract=abstract,
                    authors=[' '.join(filter(None,[''.join(a.find('first').itertext()) if a.find('first') is not None else '',
                                                  ''.join(a.find('last').itertext()) if a.find('last') is not None else ''])) for a in node.findall('author')],
                    track='findings',paper_url=page,pdf_url=page[:-1]+'.pdf',doi=text('doi'),
                    booktitle=''.join(volume.find('meta/booktitle').itertext()),
                    abstract_source=page,metadata_sources=[url(key)],awards=[],award_evidence=[],oral=False,
                    oral_evidence=[],presentation_original=[],code_urls=[])
                title_match=FIN.search(title)
                dataset_match=DATA.search(abstract)
                if title_match or dataset_match:
                    sentences=[s for s in re.split(r'(?<=[.!?])\s+',abstract) if FIN.search(s) or DATA.search(s)]
                    p['finance']=dict(scope='core' if title_match else 'application',
                        relevance_zh='金融任务或金融数据在官方题名／摘要中明确出现。',
                        evidence_type='publisher_title_abstract_screen',evidence_excerpt=title+' | '+' '.join(sentences)[:1800],
                        evidence_url=page,review_basis='Explicit financial task in title, or named financial benchmark in official abstract.')
                result.append(p)
    return result


def dataset_track_records():
    awards=load_json('sources/award_candidates.json')
    result=[]
    for year in range(2022,2027):
        key=f'neurips-{year}-events'
        if not cached(key):continue
        for event in json.loads(cached(key)).get('results',[]):
            source=event.get('sourceurl') or ''
            if not any(word in source.lower() for word in ['datasets','evaluations']):continue
            if event.get('eventtype') not in {'Poster','Oral','Spotlight'}:continue
            title=event['name'];decision=event.get('decision') or ''
            oral=event.get('eventtype')=='Oral' or bool(re.search(r'\boral\b',decision,re.I))
            paper_url=event.get('paper_url') or next((r['uri'] for r in event.get('eventmedia',[]) if r.get('name')=='OpenReview'),'')
            uid=parse_qs(urlparse(paper_url).query).get('id',[str(event['id'])])[0]
            page=urljoin('https://neurips.cc',event.get('virtualsite_url') or f'/virtual/{year}/poster/{event["id"]}')
            pdf=event.get('paper_pdf_url') or ('https://openreview.net/pdf?id='+uid if 'openreview.net' in paper_url else '')
            names=[];evidence=[]
            for award in awards:
                if award['venue']=='NeurIPS' and award['year']==year and norm(award['title'])==norm(title):
                    for raw in RAW.glob(f'neurips-{year}-*awards*.gz'):
                        if norm(title) in norm(BeautifulSoup(gzip.decompress(raw.read_bytes()),'lxml').get_text(' ',strip=True)):
                            names.append(award['award']);evidence.append(url(raw.name[:-3]));break
            if not oral and not names:continue
            result.append(dict(id=f'neurips-{year}-{uid}',title=title,venue='NeurIPS',year=year,
                authors=[a.get('fullname','') for a in event.get('authors',[])],
                abstract=event.get('abstract') or '',abstract_source=page,paper_url=paper_url or page,
                pdf_url=pdf,track='evaluations' if 'evaluations' in source.lower() else 'datasets_benchmarks',
                metadata_sources=[url(key),source],awards=list(dict.fromkeys(names)),award_evidence=list(dict.fromkeys(evidence)),
                oral=oral,oral_evidence=[url(key),page] if oral else [],presentation_original=[decision,event.get('eventtype')],code_urls=[]))
    return result


def main():
    DEST.mkdir(exist_ok=True)
    # Original collection is immutable provenance, retained in Git and a compact manifest.
    baseline=DEST/'baseline.json'
    if not baseline.exists():
        original=[json.loads(line) for line in (ROOT/'catalog.jsonl').open()]
        save_json('checks/scope_revision/baseline.json',dict(commit=subprocess.check_output(['git','rev-parse','HEAD'],text=True).strip(),
            papers=[dict(id=p['id'],title=p['title'],venue=p['venue'],year=p['year'],download=p.get('download')) for p in original]))
    papers={p['id']:p for p in load_json('sources/resolved_universe.json.gz')}
    reference_records=list(map(json.loads,(REFERENCE_MAIN/'finance_catalog.jsonl').read_text().splitlines()))
    frozen=REFERENCE/'checks/track_screening/finance_catalog.jsonl.baseline.gz'
    if frozen.exists():
        pool={p['id']:p for p in map(json.loads,gzip.decompress(frozen.read_bytes()).decode().splitlines())}
        pool.update({p['id']:p for p in reference_records});reference_records=list(pool.values())
    save_json('checks/scope_revision/reference_finance_snapshot.json.gz',reference_records)
    admitted_findings=REFERENCE/'findings/finance_catalog.jsonl'
    if admitted_findings.exists():
        reference_records.extend(map(json.loads,admitted_findings.read_text().splitlines()))
    finance={p['id']:p['finance'] for p in reference_records}
    reuse={}
    for p in reference_records:
        if p['id'] not in papers:papers[p['id']]={k:v for k,v in p.items() if k not in {'finance','research','download'}}
        if p.get('download',{}).get('status')=='downloaded':
            base=REFERENCE/'findings' if p.get('track')=='findings' else REFERENCE_MAIN
            reuse[p['id']]=dict(p['download'],reference_repository=str(base))
    reference_lengths={}
    for p in reference_records:
        if p.get('paper_length')=='long' and p.get('paper_length_evidence'):
            e=p['paper_length_evidence']
            reference_lengths[p['id']]=('long',json.dumps(e,ensure_ascii=False) if isinstance(e,dict) else e)
    review_path=REFERENCE/'checks/track_screening/main_length_review.json'
    if review_path.exists():
        entries=json.loads(review_path.read_text())
        save_json('checks/scope_revision/reference_main_length_review.json.gz',entries)
        for entry in entries:
            if entry.get('paper_length') in {'long','short'}:
                reference_lengths[entry['id']]=(entry['paper_length'],entry['source_url'])
    findings=findings_records()
    decisions_path=REFERENCE/'checks/track_screening/findings_review_decisions.json'
    if decisions_path.exists():
        decisions=json.loads(decisions_path.read_text())
        save_json('checks/scope_revision/reference_findings_review.json.gz',decisions)
        fulltexts={p['id']:p for p in json.loads((REFERENCE/'checks/track_screening/findings_fulltext_results.json').read_text())}
        reviewed=[]
        for p in json.loads((REFERENCE/'checks/track_screening/findings_records.json').read_text()):
            if p['id'] not in decisions:continue
            decision=decisions[p['id']]
            if decision.get('decision')!='confirmed_finance':continue
            p['finance']=dict(decision,relevance_zh='本地金融论文库已复核的金融任务、数据或案例。')
            proof=fulltexts.get(p['id'],{})
            cached_pdf=pathlib.Path('/tmp/ai4finance_findings_review')/(p['id']+'.pdf')
            if proof.get('content_exceeds_short_limit') and (proof.get('title_in_first_page') or proof.get('title_token_overlap',0)>=.95):
                reference_lengths[p['id']]=('long',proof['source_url']+' (reviewed main-text boundary; SHA-256 '+proof['sha256']+')')
            if cached_pdf.is_file() and proof.get('sha256'):
                reuse[p['id']]=dict(id=p['id'],status='downloaded',local_path=cached_pdf.name,
                    reference_repository=str(cached_pdf.parent),pdf_version='publisher_version',
                    bytes=proof['bytes'],sha256=proof['sha256'],pages=proof['pages'])
            reviewed.append(p)
        findings=reviewed
    save_json('checks/scope_revision/findings_candidates.json.gz',findings)
    additions=aaai_records()+findings+dataset_track_records()
    for p in additions:
        if p.get('finance'):finance[p['id']]=p.pop('finance')
        old=papers.get(p['id'])
        if old:
            for key in ['awards','award_evidence','oral_evidence','presentation_original']:
                old[key]=list(dict.fromkeys(old.get(key,[])+p.get(key,[])))
            old['oral']=old.get('oral',False) or p.get('oral',False)
        else:papers[p['id']]=p
    labels=length_evidence()
    pdf_types=load_json('checks/scope_revision/pdf_length_evidence.json') if (DEST/'pdf_length_evidence.json').exists() else {}
    selected=[];excluded=[]
    reconciled=ROOT/'checks/finance_reconciliation/decisions.json'
    decisions=load_json(reconciled) if reconciled.exists() else {}
    for p in papers.values():
        key=(p['venue'],int(p['year']),norm(p['title']))
        if key in labels:p['paper_length'],p['paper_length_evidence']=labels[key]
        elif p['id'] in reference_lengths:p['paper_length'],p['paper_length_evidence']=reference_lengths[p['id']]
        elif p['id'] in pdf_types:
            p['paper_length']='long';p['paper_length_evidence']=pdf_types[p['id']]['evidence']
        length,evidence=paper_length(p);p['paper_length']=length;p['paper_length_evidence']=evidence
        decision=decisions.get(p['id'],{})
        if decision.get('action')=='hold_length_unverified':
            length='unverified';evidence=decision['reason'];p['paper_length']=length;p['paper_length_evidence']=evidence
        elif decision.get('action')=='retain_verified_long':
            length='long';evidence=decision['reason']+' Publisher PDF SHA-256 '+decision['pdf_sha256']
            p['paper_length']=length;p['paper_length_evidence']=evidence
        track=publication_track(p);p['track']=track
        attributes=award_types(p)
        award=any(a['type'] in {'best','outstanding'} and a['evidence'] for a in attributes)
        oral=bool(p.get('oral') and p.get('oral_evidence'))
        fin=finance.get(p['id']) if track in {'main','findings'} else None
        candidate=bool(fin) or (track in ALLOWED and (award or oral))
        if not candidate:continue
        if length!='long':
            excluded.append(dict(id=p['id'],title=p['title'],venue=p['venue'],year=p['year'],track=track,
                                 reason='short_paper' if length=='short' else 'paper_length_unverified',evidence=evidence,
                                 is_finance=bool(fin),paper_url=p['paper_url']))
            continue
        p['finance']=fin;p['award_types']=attributes;p['is_curated']=track in ALLOWED and (award or oral)
        selected.append(p)
    selected,aliases=deduplicate(selected)
    save_json('checks/scope_revision/paper_aliases.json',aliases)
    save_json('checks/scope_revision/selected_papers.json.gz',selected)
    save_json('checks/scope_revision/reference_pdf_reuse.json',reuse)
    save_json('checks/scope_revision/length_evidence.json',{str(k):v for k,v in labels.items()})
    save_json('checks/scope_revision/excluded_or_pending.json',excluded)
    summary=dict(selected=len(selected),venues=dict(Counter(p['venue'] for p in selected)),tracks=dict(Counter(p['track'] for p in selected)),
        finance=sum(bool(p.get('finance')) for p in selected),aaai=sum(p['venue']=='AAAI' for p in selected),
        excluded_or_pending=dict(Counter(p['reason'] for p in excluded)),
        findings_candidates=sum(p['track']=='findings' for p in additions),findings_finance=sum(p['track']=='findings' for p in selected))
    save_json('checks/scope_revision/selection_summary.json',summary)
    print(json.dumps(summary,ensure_ascii=False,indent=2))


if __name__=='__main__':main()
