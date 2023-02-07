from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from users.models import Student
from django import forms


class RegistrationForm(UserCreationForm):

    username = forms.CharField(help_text='Придумайте логин', label='Пароль/Password')
    password1 = forms.CharField(help_text='Придумайте пароль', label='Пароль/Password', widget=forms.PasswordInput())

    class Meta:
        # model = User
        model = Student
        fields = ('username', 'password1', 'password2')