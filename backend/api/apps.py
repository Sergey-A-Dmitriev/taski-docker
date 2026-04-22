"""Модуль приложений."""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Класс конфиг приложений."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
