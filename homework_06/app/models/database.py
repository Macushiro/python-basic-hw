"""
    Файл приложения для взаимодействия с БД.
"""

__all__ = (
    "db",
)

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()