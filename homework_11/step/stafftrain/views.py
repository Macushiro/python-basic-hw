"""
    Файл классов-обработчиков запросов к приложению.
"""

from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

# from users.models import Student  - for future functional extending
from django.contrib.auth.models import User

from .models import Course
from .forms import CourseModelForm


class MainPageView(ListView):
    """
    Main page controller
    """
    # model = Student   - for future functional extending
    model = Course
    context_object_name = "courses"
    template_name = "index.html"

    def get_queryset(self):
        """
        The function of obtaining objects of the Course model
        :return:
        """
        return Course.objects.all()


class CourseListView(ListView):
    """
    Courses list controller
    """
    model = Course
    context_object_name = "courses"
    template_name = "courses_list.html"

    def get_queryset(self):
        """
        The function of obtaining objects of the Course model
        :return:
        """
        return Course.objects.all()


class CourseDetailView(LoginRequiredMixin, DetailView):
    """
    Course detail info controller
    """
    model = Course
    context_object_name = "course"
    template_name = "course_detail.html"

    def get_context_data(self, **kwargs):
        """
        Function for context extension
        :return:
        """
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.filter(course__id=self.get_object().id)
        return context


class CourseCreateView(UserPassesTestMixin, CreateView):
    """
    Course create controller
    """
    model = Course
    template_name = "course_form.html"
    form_class = CourseModelForm
    success_url = reverse_lazy("courses_list")

    def test_func(self):
        """
        Function for users privileges checking
        :return:
        """
        return self.request.user.is_staff or self.request.user.is_superuser


class CourseUpdateView(UserPassesTestMixin, UpdateView):
    """
    Course update info controller
    """
    model = Course
    template_name = "course_form.html"
    form_class = CourseModelForm
    success_url = reverse_lazy("courses_list")

    def test_func(self):
        """
        Function for users privileges checking
        :return:
        """
        return self.request.user.is_staff or self.request.user.is_superuser


class CourseDeleteView(UserPassesTestMixin, DeleteView):
    """
    Course delete controller
    """
    model = Course
    template_name = "course_confirm_delete.html"
    success_url = reverse_lazy("courses_list")

    def test_func(self):
        """
        Function for users privileges checking
        :return:
        """
        return self.request.user.is_staff or self.request.user.is_superuser
