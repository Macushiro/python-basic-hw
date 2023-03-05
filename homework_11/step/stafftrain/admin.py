"""
    Файл регистрации моделей.
"""

from django.contrib import admin

from stafftrain.models import Course, Result

admin.site.register(Course)
admin.site.register(Result)
