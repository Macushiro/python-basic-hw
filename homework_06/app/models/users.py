"""
    Файл модели пользователей.
    Изначально пытался сделать базовый класс (который создавался на базе db.Model, с общей частью для моделей)
    и от него наследоваться, но встроенные магические методы во Flask всё ломали, смешивая метаданные,
    а переписывать я их не готов :)
"""

from typing import TYPE_CHECKING
from sqlalchemy.orm import relationship
from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
)

from .database import db


if TYPE_CHECKING:
    from flask_sqlalchemy.query import Query


class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, default="", server_default="")
    email = Column(String(200), nullable=False, default="", server_default="")
    # age = Column(Integer, nullable=False, default=1, server_default=1)

    bills = relationship("Bill", back_populates="user", uselist=False)

    if TYPE_CHECKING:
        query: Query