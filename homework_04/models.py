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

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)


engine: AsyncEngine = create_async_engine(url=PG_CONN_URI, echo=False)
Base = declarative_base(bind=engine, cls=Base)

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