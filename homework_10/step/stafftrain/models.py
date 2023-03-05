"""
    Файл моделей приложения.
"""

from django.db import models

# from users.models import Student  - for future functional extending
from django.contrib.auth.models import User


class Course(models.Model):
    """
    Course model description
    """
    name = models.CharField(
        verbose_name="Наименование курса/Course name",
        max_length=256,
        blank=False,
        editable=True,
    )
    description = models.TextField(
        verbose_name="О курсе/Description", blank=True, null=True
    )
    is_available = models.BooleanField(
        verbose_name="Доступен/Available", blank=True, null=True
    )
    student = models.ForeignKey(User, on_delete=models.PROTECT, null=True)


class Result(models.Model):
    """
    Result model description
    """
    percent = models.DecimalField(
        verbose_name="Процент прохождения/Completion percent",
        decimal_places=1,
        max_digits=100,
        editable=True,
    )
    test_result = models.BooleanField(
        verbose_name="Статус теста/Test status", editable=True, default=False
    )
    # student = models.OneToOneField(Student, on_delete=models.PROTECT)
    # - for future functional extending
    student = models.OneToOneField(User, on_delete=models.PROTECT)
    course = models.OneToOneField(Course, on_delete=models.PROTECT)
