from concurrent import futures
from typing import List

from github_sequential import get_owners_ids, get_repos_data, main, save_stats

MAX_WORKERS = 2

def save_one(query: str):
    data = get_repos_data(query)
    repo_owners = get_owners_ids(data)
    save_stats(repo_owners, query)
    print(query, end='', flush=True)
    return repo_owners

def save_many(queries: list) -> int:
    with futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:  # ProcessPoolExecutor
        res = executor.map(save_one, queries)  # futures

    return len(list(res))

def save_many_explicit(queries: list) -> int:
    with futures.ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:  # ProcessPoolExecutor
        to_do : List[futures.Future] = []
        for q in queries:
            future = executor.submit(save_one, q)
            to_do.append(future)
            print(f'Awaiting execution for {q}: {future}')
        
        for count, future in enumerate(futures.as_completed(to_do), 1):
            res : str = future.result()
            print(f'{future} result: {res!r}')
    
    return count

if __name__ == '__main__':
    # main(save_many)
    main(save_many_explicit)
