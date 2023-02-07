from django.shortcuts import render
from django.views.generic import ListView
from users.models import Student


class MainPage(ListView):
    model = Student
    context_object_name = 'students'