from common import *

jobs = []
for venue in ['icml', 'iclr', 'neurips']:
    for year in range(2017, 2027):
        jobs.append((f'{venue}-{year}-events', f'https://{venue}.cc/static/virtual/data/{venue}-{year}-orals-posters.json'))
for venue, old in [('acl', 'P'), ('emnlp', 'D')]:
    for year in range(2017, 2027):
        coll = f'{old}{year%100}' if year < 2020 else f'{year}.{venue}'
        jobs.append((f'{venue}-{year}-anthology', f'https://raw.githubusercontent.com/acl-org/acl-anthology/master/data/xml/{coll}.xml'))
for venue in ['icml', 'iclr', 'neurips']:
    for year in range(2017, 2027):
        jobs.append((f'{venue}-{year}-papershtml', f'https://{venue}.cc/virtual/{year}/papers.html'))
batch(jobs, 10)
