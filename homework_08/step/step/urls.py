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
    MainPage,
    CourseListView,
    CourseDetail,
)
from users.views import (
    UserRegistrationView,
    UserLoginView,
    UserLogoutView,
    UserDetailView,
    StudentsListView,
)

urlpatterns = [
    path('', MainPage.as_view(), name='main_page'),
    path('admin/', admin.site.urls),
    # users
    path('users/create/', UserRegistrationView.as_view(), name='registration'),
    path('users/login/', UserLoginView.as_view(), name='login'),
    path('users/logout/', UserLogoutView.as_view(), name='logout'),
    path('users/info/', UserDetailView.as_view(), name='user_info'),
    # students
    path('students/list/', StudentsListView.as_view(), name='students_list'),
    # courses
    path('courses/detail/<int:pk>/', CourseDetail.as_view(), name='course_detail'),
    path('courses/list/', CourseListView.as_view(), name='courses_list'),
]
