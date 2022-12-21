"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio

import aiohttp


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

URLS = [USERS_DATA_URL, POSTS_DATA_URL]     # for next step for near OOP style


async def fetch_json(url):
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        data = await response.json()
        print(data)
        return data


async def main():
    # tasks = set()
    tasks = {asyncio.create_task(fetch_json(el)) for el in URLS}
    # tasks.add(asyncio.create_task(fetch_json(urls[0])))
    # tasks.add(asyncio.create_task(fetch_json(POSTS_DATA_URL)))
    # for el in urls:
    #     tasks.add(asyncio.create_task(fetch_json(el)))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    # asyncio.run(fetch_json(USERS_DATA_URL))
    # asyncio.run(fetch_json(POSTS_DATA_URL))
    asyncio.run(main())