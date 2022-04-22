import asyncio
import aiohttp
from aiohttp import ClientSession

from github_sequential import URL, main, save_stats, get_owners_ids

async def get_repos_data(session: ClientSession, query: str) -> dict:
    query_url = f'{URL}?q={query}+language:python'
    async with session.get(query_url) as response:
        return await response.json()


async def save_one(session: ClientSession, query: str):
    data = await get_repos_data(session, query)
    ids = get_owners_ids(data)
    save_stats(ids, query)

def save_many(queries: list) -> int:
    return asyncio.run(supervisor(queries))

async def supervisor(queries: list) -> int:
    async with ClientSession() as session:
        to_do = [save_one(session, q) for q in queries]
        res = await asyncio.gather(*to_do)

    return len(res)

if __name__ == '__main__':
    main(save_many)
