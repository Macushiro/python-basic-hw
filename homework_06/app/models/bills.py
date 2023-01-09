"""
    Файл модели счетов пользователей.
    Изначально пытался сделать базовый класс (который создавался на базе db.Model, с общей частью для моделей)
    и от него наследоваться, но встроенные магические методы во Flask всё ломали, смешивая метаданные,
    а переписывать я их не готов :)
"""

from typing import TYPE_CHECKING
from sqlalchemy.orm import relationship
from pydantic import confloat
from sqlalchemy import (
    Column,
    Integer,
    String,
    FLOAT,
    ForeignKey,
)

from .database import db


if TYPE_CHECKING:
    from flask_sqlalchemy.query import Query


class Bill(db.Model):
    id = Column(Integer, primary_key=True)
    bill_number = Column(Integer, unique=True, nullable=False)
    total = Column(FLOAT, nullable=False)
    description = Column(String(200), nullable=False)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)

    user = relationship("User", back_populates="bills", uselist=True)

    if TYPE_CHECKING:
        query: Query