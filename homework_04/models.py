"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Text,
    ForeignKey,
)
from sqlalchemy.orm import (
    declarative_base,
    sessionmaker,
    declared_attr,
    relationship,
)
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
    AsyncSession,
)

# PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"
DB_URL = "postgresql+pg8000://username:passwd!@localhost/blog"
DB_ASYNC_URL = "postgresql+asyncpg://username:passwd!@localhost/blog"


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)


engine: AsyncEngine = create_async_engine(url=DB_ASYNC_URL, echo=False)
sync_engine = create_engine(url=DB_URL, echo=False)
Base = declarative_base(bind=sync_engine, cls=Base)

Session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class User(Base):
    name = Column(String(30), nullable=False, default="")
    username = Column(String(100), nullable=False, default="")
    email = Column(String(150), nullable=False, default="")

    posts = relationship("Post", back_populates="users", uselist=True)


class Post(Base):
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    title = Column(String(100), nullable=False, default="")
    body = Column(Text, nullable=False, default="")

    user = relationship("User", back_populates="posts", uselist=False)


def main():
    Base.metadata.create_all()

if __name__ == '__main__':
    main()