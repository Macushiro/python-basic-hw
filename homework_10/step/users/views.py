"""
    Файл классов-обработчиков запросов к приложению.
"""

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
# from .models import Student   - for future functional extending
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.core import management
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    TemplateView,
    ListView,
    UpdateView,
    DeleteView,
)

from stafftrain.models import Course
from users.forms import RegistrationForm, UserUpdateForm


@login_required()
def generate_data(request):
    """
    The function for test data generation
    :param request:
    :return:
    """
    management.call_command("generate_data")
    return render(request, "index.html")


class UserRegistrationView(CreateView):
    """
    User registration controller
    """
    # model = Student   - for future functional extending
    model = User
    form_class = RegistrationForm
    success_url = "/"
    template_name = "user_form.html"


class UserLoginView(LoginView):
    """
    User login controller
    """
    template_name = "login_form.html"


class UserLogoutView(LoginRequiredMixin, LogoutView):
    """
    User logout controller
    """
    pass


class StudentsListView(UserPassesTestMixin, ListView):
    """
    Students list controller
    """
    model = User
    context_object_name = "students"
    template_name = "students_list.html"

    def test_func(self):
        """
        Function for users privileges checking
        :return:
        """
        return self.request.user.is_staff or self.request.user.is_superuser

    def get_queryset(self):
        """
        The function of obtaining objects of the User model
        :return:
        """
        return User.objects.filter(is_staff=False)

    def get_context_data(self, **kwargs):
        """
        Function for context extension
        :return:
        """
        context = super().get_context_data(**kwargs)
        context["courses"] = Course.objects.all()
        return context


class UserDetailView(LoginRequiredMixin, TemplateView):
    """
    User detail info controller
    """
    template_name = "user_detail.html"

    def get_context_data(self, **kwargs):
        """
        Function for context extension
        :return:
        """
        context = super().get_context_data(**kwargs)
        context["object"] = self.request.user
        return context


class UserUpdateView(LoginRequiredMixin, UpdateView):
    """
    User info updating controller
    """
    model = User
    template_name = "user_update_form.html"
    form_class = UserUpdateForm
    success_url = reverse_lazy("user_info")


class UserDeleteView(UserPassesTestMixin, DeleteView):
    """
    User deleting controller
    """
    model = User
    template_name = "user_confirm_delete.html"
    success_url = reverse_lazy("students_list")

    def test_func(self):
        """
        Function for users privileges checking
        :return:
        """
        return self.request.user.is_staff or self.request.user.is_superuser
