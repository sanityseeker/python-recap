import time
from typing import Callable
import requests

import os

BASE_DIR = 'github_downloads'
URL = 'https://api.github.com/search/repositories'
KEYWORDS = ['search', 'torch', 'tensorflow',
            'requests', 'alice', 'data', 'deep', 'ML']

def get_repos_data(query: str) -> dict:
    response = requests.get(
        URL,
        params={'q': f'{query}+language:python'},
    )
    if response.ok:
        return response.json()
    else:
        return {}


def get_owners_ids(resp: dict) -> list:
    owners = []
    for item in resp.get('items', []):
        owners.append(item['owner']['id'])
    return owners


def save_stats(ids: list, query_name: str):
    os.makedirs(BASE_DIR, exist_ok=True)
    with open(os.path.join(BASE_DIR, query_name), 'w') as f:
        f.write(str(ids))


def get_many_stats(queries: list) -> int:
    for query in queries:
        data = get_repos_data(query)
        repo_owners = get_owners_ids(data)
        save_stats(repo_owners, query)
    return len(queries)

def main(downloader: Callable[[list], dict]):
    t_start = time.perf_counter()
    count = downloader(KEYWORDS)
    elapsed = time.perf_counter() - t_start
    print(f'\n{count} searches done in {elapsed:.2f}s')

if __name__ == '__main__':
    main(get_many_stats)