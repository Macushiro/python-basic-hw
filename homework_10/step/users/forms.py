"""
    Описание форм для вывода/получения данных.
"""

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# from users.models import Student      - for future functional extending
from django.contrib.auth.models import User

from django import forms


class RegistrationForm(UserCreationForm):
    """
    Custom form for User model object registration
    """
    username = forms.CharField(help_text="Введите логин", label="Логин/Login:")
    email = forms.CharField(help_text="Введите Вашу почту", label="Почта/Email:")
    first_name = forms.CharField(help_text="Введите Ваше имя", label="Имя/Name:")
    last_name = forms.CharField(
        help_text="Введите Вашу фамилию", label="Фамилия/Last Name:"
    )
    password1 = forms.CharField(
        help_text="Введите пароль",
        label="Пароль/Password:",
        widget=forms.PasswordInput(),
    )
    password2 = forms.CharField(
        help_text="Введите повторно пароль",
        label="Пароль/Password:",
        widget=forms.PasswordInput(),
    )

    class Meta:
        """
        Meta for User custom model form
        """
        model = User
        # model = Student   - for future functional extending
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )


class UserUpdateForm(UserChangeForm):
    """
    Custom form for User model object updating
    """
    username = forms.CharField(help_text="Введите логин", label="Логин/Login:")
    email = forms.CharField(help_text="Введите Вашу почту", label="Почта/Email:")
    first_name = forms.CharField(help_text="Введите Ваше имя", label="Имя/Name:")
    last_name = forms.CharField(
        help_text="Введите Вашу фамилию", label="Фамилия/Last Name:"
    )
    password1 = forms.CharField(
        help_text="Введите пароль",
        label="Пароль/Password:",
        widget=forms.PasswordInput(),
    )
    password2 = forms.CharField(
        help_text="Введите повторно пароль",
        label="Пароль/Password:",
        widget=forms.PasswordInput(),
    )

    class Meta:
        """
        Meta for User custom model form
        """
        model = User
        # model = Student   - for future functional extending
        fields = (
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        )
