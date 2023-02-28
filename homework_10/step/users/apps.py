"""
    Файл конфигурации приложения.
"""

from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    UsersConfig
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "users"
