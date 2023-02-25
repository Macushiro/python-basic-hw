from django.shortcuts import render
# from .models import Student   - for future functional extending
from django.contrib.auth.models import User
from django.views.generic import CreateView, TemplateView, DetailView, ListView
from django.contrib.auth.views import LoginView, LogoutView

from users.forms import RegistrationForm


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


class UserDetailView(TemplateView):
    template_name = 'user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.request.user
        return context