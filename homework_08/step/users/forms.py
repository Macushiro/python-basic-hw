from django.contrib.auth.forms import UserCreationForm
# from users.models import Student      - for future functional extending
from django.contrib.auth.models import User

from django import forms


class RegistrationForm(UserCreationForm):

    username = forms.CharField(help_text='Придумайте логин', label='Логин/Login:')
    email = forms.CharField(help_text='Введите Вашу почту', label='Email:')
    password1 = forms.CharField(help_text='Придумайте пароль', label='Пароль/Password:', widget=forms.PasswordInput())
    password2 = forms.CharField(help_text='Введите повторно пароль', label='Пароль/Password:', widget=forms.PasswordInput())

    class Meta:
        model = User
        # model = Student   - for future functional extending
        fields = ('username', 'email', 'password1', 'password2')