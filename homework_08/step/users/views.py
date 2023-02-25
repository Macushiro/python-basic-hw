"""
    Файл классов-обработчиков запросов к приложению.
"""

from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# from .models import Student   - for future functional extending
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    TemplateView,
    ListView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.views import LoginView, LogoutView

from users.forms import RegistrationForm, UserUpdateForm
from stafftrain.models import Course

from django.core import management


@login_required()
def generate_data(request):
    management.call_command('generate_data')
    return render(request, 'index.html')


class UserRegistrationView(CreateView):
    # model = Student   - for future functional extending
    model = User
    form_class = RegistrationForm
    success_url = '/'
    template_name = 'user_form.html'


class UserLoginView(LoginView):
    template_name = 'login_form.html'


class UserLogoutView(LogoutView):
    pass


class StudentsListView(ListView):
    model = User
    context_object_name = 'students'
    template_name = 'students_list.html'

    def get_queryset(self):
        return User.objects.filter(is_staff=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        return context


class UserDetailView(TemplateView):
    template_name = 'user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.request.user
        return context


class UserUpdateView(UpdateView):
    model = User
    template_name = 'user_update_form.html'
    form_class = UserUpdateForm
    success_url = reverse_lazy('user_info')


class UserDeleteView(UserPassesTestMixin, DeleteView):
    model = User
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('students_list')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser