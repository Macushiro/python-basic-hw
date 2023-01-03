"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
import asyncio

import aiohttp


USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"

URLS = [USERS_DATA_URL, POSTS_DATA_URL]     # for next step for near OOP style


async def fetch_json(url: str) -> list[dict]:
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        data = await response.json()
        # print(data)
        # for el in data:
        #     print(el["name"])
        return data


async def main():
    tasks = {asyncio.create_task(fetch_json(el)) for el in URLS}
    await asyncio.wait(tasks)