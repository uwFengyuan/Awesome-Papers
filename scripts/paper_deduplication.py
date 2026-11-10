"""Merge duplicate NeurIPS dataset-track programme events into paper records."""
import re
from collections import defaultdict
from common import norm
from paper_attributes import award_types


def deduplicate(papers):
    groups=defaultdict(list)
    for paper in papers:
        key=(paper['venue'],paper['year'],paper['track'],norm(paper['title']))
        groups[key].append(paper)
    output=[];aliases=[]
    for group in groups.values():
        if len(group)==1:
            output.extend(group);continue
        assert all(p['venue']=='NeurIPS' and p['track'] in {'datasets_benchmarks','evaluations'} for p in group)
        names=[{norm(a) for a in p['authors']} for p in group if p['authors']]
        assert names and set.intersection(*names),[p['id'] for p in group]
        def priority(p):
            return ('proceedings.neurips.cc' in p['paper_url'],'openreview.net' in p['paper_url'],len(p.get('abstract','')))
        main=max(group,key=priority).copy()
        for field in ['awards','award_evidence','oral_evidence','metadata_sources','presentation_original','code_urls']:
            main[field]=list(dict.fromkeys(value for p in group for value in p.get(field,[])))
        main['oral']=any(p.get('oral') for p in group)
        main['alias_ids']=[p['id'] for p in group if p['id']!=main['id']]
        main['alternate_paper_urls']=list(dict.fromkeys(p['paper_url'] for p in group if p['paper_url']!=main['paper_url']))
        main['award_types']=award_types(main)
        if 'proceedings.neurips.cc' in main['paper_url'] and '-Abstract-' in main['paper_url']:
            main['pdf_url']=main['paper_url'].replace('/hash/','/file/').replace('-Abstract-','-Paper-').replace('.html','.pdf')
        elif not main.get('pdf_url'):
            main['pdf_url']=next((p['pdf_url'] for p in group if p.get('pdf_url')),'')
        aliases.append(dict(canonical_id=main['id'],alias_ids=main['alias_ids'],title=main['title'],
            reason='Same NeurIPS venue, year, dataset track, normalized title and overlapping authors; multiple programme events.'))
        output.append(main)
    output.sort(key=lambda p:(p['venue'],p['year'],p['title'].casefold()))
    return output,aliases
