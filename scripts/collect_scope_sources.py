"""Cache official sources needed by the long-paper scope revision."""
from common import *


def main():
    jobs = [(f'findings-{year}-anthology',
             f'https://raw.githubusercontent.com/acl-org/acl-anthology/master/data/xml/{year}.findings.xml')
            for year in range(2020, 2027)]
    jobs.extend([
        ('aaai-awards-history', 'https://aaai.org/about-aaai/aaai-awards/aaai-conference-paper-awards-and-recognition/'),
        ('aaai-awards-legacy', 'https://new.aaai.org/Awards/paper.php'),
        ('aaai-2025-oral-program', 'https://aaai.org/wp-content/uploads/2025/01/AAAI-25-Oral-Talks-Schedule.pdf'),
        ('aaai-2020-program', 'https://aaai.org/wp-content/uploads/2023/01/AAAI20-ProgramWeb.pdf'),
        ('aaai-2026-main-page', 'https://aaai.org/conference/aaai/aaai-26/main-technical-track/'),
    ])
    def job(pair):
        key, url = pair
        data, info = fetch(url, key, timeout=30, retries=1)
        print(key, len(data or b''), info.get('http_status', info.get('error')), flush=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
        list(pool.map(job, jobs))


if __name__ == '__main__':
    main()
