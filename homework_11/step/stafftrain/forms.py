"""
    Описание форм для вывода/получения данных.
"""

from django import forms
from django.contrib.auth.models import User
from .models import Course, Result


class CourseModelForm(forms.ModelForm):
    """
    Custom form for Course model
    """
    name = forms.CharField(
        label="Наименование курса/Course name",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    description = forms.CharField(
        label="О курсе/Description",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    is_available = forms.BooleanField(
        label="Доступен/Available",
        initial=True,
        widget=forms.CheckboxInput(attrs={"checked": True}),
    )

    student = forms.ModelChoiceField(
        queryset=User.objects.filter(is_staff=False),
        required=False,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    class Meta:
        """
        Meta for Course custom model form
        """
        model = Course
        fields = ("name", "description", "is_available", "student")


class ResultModelForm(forms.ModelForm):
    """
    Custom form for Result model
    """

    student = forms.ModelChoiceField(
        queryset=User.objects.filter(is_staff=False),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    course = forms.ModelChoiceField(
        queryset=Course.objects.filter(is_available=True),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    percent = forms.DecimalField(
        label="Процент прохождения/Completion percent",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    test_result = forms.BooleanField(
        label="Статус теста/Test status", initial=True, widget=forms.BooleanField()
    )

    class Meta:
        """
        Meta for Result custom model form
        """
        model = Result
        fields = ("student", "course", "percent", "test_result")
