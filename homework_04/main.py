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

from sqlalchemy.ext.asyncio import AsyncSession

from models import Base, Session, engine


async def create_tables():
    print("Recreating tables has started")
    async with engine.begin() as db_connect:
        print("Begin")
        await db_connect.run_sync(Base.metadata.drop_all)
        await db_connect.run_sync(Base.metadata.create_all)
    print("Recreating tables has finished")


async def create_user(session:AsyncSession, name: str):
    print(f"User {name} has created")


async def create_post(session:AsyncSession, title: str):
    print(f"Post with title {title} has created")


async def async_main():
    await create_tables()

    async with Session() as session:
        await asyncio.gather(
            create_user(session=session, name="Bob"),
            create_post(session=session, title="Bob's days")
        )


async def main():
    await async_main()


if __name__ == "__main__":
    asyncio.run(main())
