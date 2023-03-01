"""step URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from stafftrain.views import (
    MainPageView,
    CourseListView,
    CourseDetailView,
    CourseCreateView,
    CourseUpdateView,
    CourseDeleteView,
)
from users.views import (
    UserRegistrationView,
    UserLoginView,
    UserLogoutView,
    UserDetailView,
    UserUpdateView,
    UserDeleteView,
    StudentsListView,
    generate_data,
)

urlpatterns = [
    # base URLs
    path("", MainPageView.as_view(), name="main_page"),
    path("admin/", admin.site.urls),
    path("generate_data/", generate_data, name="generate"),
    # users
    path("users/create/", UserRegistrationView.as_view(), name="registration"),
    path("users/login/", UserLoginView.as_view(), name="login"),
    path("users/logout/", UserLogoutView.as_view(), name="logout"),
    path("users/info/", UserDetailView.as_view(), name="user_info"),
    path("users/update/<int:pk>/", UserUpdateView.as_view(), name="user_update"),
    path("users/delete/<int:pk>/", UserDeleteView.as_view(), name="user_delete"),
    # students
    path("students/list/", StudentsListView.as_view(), name="students_list"),
    # courses
    path("courses/list/", CourseListView.as_view(), name="courses_list"),
    path("courses/detail/<int:pk>/", CourseDetailView.as_view(), name="course_detail"),
    path("courses/create/", CourseCreateView.as_view(), name="course_create"),
    path("courses/update/<int:pk>/", CourseUpdateView.as_view(), name="course_update"),
    path("courses/delete/<int:pk>/", CourseDeleteView.as_view(), name="course_delete"),
    # results
    # path('results/list/', ResultListView.as_view(), name='results'),
]
