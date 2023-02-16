from django.shortcuts import render
from django.views.generic import ListView, DetailView
# from users.models import Student  - for future functional extending
from django.contrib.auth.models import User
from .models import Course

class MainPage(ListView):
    # model = Student   - for future functional extending
    model = Course
    context_object_name = 'courses'
    template_name = 'index.html'

    def get_queryset(self):
        return Course.objects.all()


class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'courses_list.html'

    def get_queryset(self):
        return Course.objects.all()


class CourseDetail(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'course_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.filter(is_staff=False)
        return context