from django.db import models
# from users.models import Student  - for future functional extending
from django.contrib.auth.models import User


class Course(models.Model):
    course_name = models.CharField(verbose_name="Наименование курса/Course name", max_length=256, blank=False, editable=False)
    description = models.TextField(verbose_name="О курсе/Description", blank=True, null=True)


class Result(models.Model):
    percent = models.DecimalField(verbose_name="Процент прохождения/Completion percent", decimal_places=1, max_digits=100, editable=False)
    test_result = models.BooleanField(verbose_name="Статус теста/Test status", editable=False, default=False)
    # student = models.OneToOneField(Student, on_delete=models.PROTECT)     - for future functional extending
    student = models.OneToOneField(User, on_delete=models.PROTECT)
    course = models.OneToOneField(Course, on_delete=models.PROTECT)