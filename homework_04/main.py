"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""

import asyncio
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from models import (
    Base,
    User,
    Post,
    Session,
    engine,
)
from jsonplaceholder_requests import (
    fetch_json,
    POSTS_DATA_URL,
    USERS_DATA_URL,
)

async def recreate_tables():
    print("Recreating tables has started")
    async with engine.begin() as db_connect:
        await db_connect.run_sync(Base.metadata.drop_all)
        await db_connect.run_sync(Base.metadata.create_all)
    print("Recreating tables has finished")


async def fetch_users_data(url: str) -> list[dict]:
    data = await fetch_json(url)
    return data


async def fetch_post_data(url: str) -> list[dict]:
    data = await fetch_json(url)
    return data


async def create_users(session:AsyncSession, user_data: list[dict]) -> list[User]:
    print("Start creating users")
    users = [
        User(username=el["username"], name=el["name"], email=el["email"])
        for el in user_data
    ]
    session.add_all(users)
    print(users)

    await session.commit()
    print("Finish creating users")
    return users


async def create_posts(session:AsyncSession, posts_data: list[dict]) -> list[Post]:
    print("Start creating posts")
    posts = [
        Post(user_id=el["userId"], title=el["title"], body=el["body"])
        for el in posts_data
    ]
    session.add_all(posts)

    await session.commit()
    print("Finish creating posts")
    return posts


async def async_main():
    await recreate_tables()

    async with Session() as session:
        users_data: List[dict]
        posts_data: List[dict]
        user_data, posts_data = await asyncio.gather(
            fetch_users_data(USERS_DATA_URL),
            fetch_post_data(POSTS_DATA_URL),
        )
        await create_users(session=session, user_data=user_data)
        await create_posts(session=session, posts_data=posts_data)


async def main():
    await async_main()


if __name__ == "__main__":
    asyncio.run(main())
