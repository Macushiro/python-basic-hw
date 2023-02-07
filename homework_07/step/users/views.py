from django.shortcuts import render
# from django.contrib.auth.models import User
from .models import Student
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView

from users.forms import RegistrationForm


class UserRegistrationView(CreateView):
    model = Student
    form_class = RegistrationForm
    success_url = '/'
    template_name = 'user_form.html'


class UserLoginView(LoginView):
    template_name = 'login_form.html'


class UserLogoutView(LogoutView):
    pass