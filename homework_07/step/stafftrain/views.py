from django.shortcuts import render
from django.views.generic import ListView
# from users.models import Student  - for future functional extending
from django.contrib.auth.models import User

class MainPage(ListView):
    # model = Student   - for future functional extending
    model = User
    context_object_name = 'students'
    template_name = 'index.html'