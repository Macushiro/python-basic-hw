"""
    Файл тестирования контролеров (view).
"""

from django.test import TestCase
from .models import Course
from django.contrib.auth.models import User


class TestCourseListView(TestCase):

    def test_response_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/courses/list/')
        self.assertEqual(response.status_code, 200)


    def test_course_detail(self):
        user = User.objects.create_user(username='Frank', email='Frank@email.com', password='Frank1234567')
        self.client.login(username='Frank', password='Frank1234567')

        response = self.client.get('/courses/detail/88888888/')
        self.assertEqual(response.status_code, 404)

        course = Course.objects.create(name='SQL', student=user)
        response = self.client.get(f'/courses/detail/{course.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_response_context(self):
        course = Course.objects.create(name='SQL')
        response = self.client.get('/courses/list/')
        self.assertEqual(response.context['courses'][0].name, 'SQL')

    def test_response_content(self):
        response = self.client.get('/courses/list/')
        button = '<a class="btn btn-outline-primary my-3"\n       href="/"\n    >Back to main page</a>'
        self.assertIn(button, response.content.decode(encoding='utf-8'))

    def test_permissions(self):
        # For unauthorized user
        response = self.client.get('/students/list/')
        self.assertEqual(response.status_code, 302)

        # For authorized user
        user = User.objects.create_user(username='Frank', email='Frank@email.com', password='Frank1234567')
        self.client.login(username='Frank', password='Frank1234567')
        self.assertEqual(response.status_code, 302)

        response = self.client.get('/users/info/')
        self.assertEqual(response.status_code, 200)

        # For just logout user
        self.client.logout()
        response = self.client.get('/users/info/')
        self.assertEqual(response.status_code, 302)

        # Check superuser permissions
        response = self.client.get('/students/list/')
        self.assertEqual(response.status_code, 302)
        user = User.objects.create_superuser(username='test_admin', email='test_admin@email.com', password='test_admin1234567')
        self.client.login(username='test_admin', password='test_admin1234567')
        response = self.client.get('/students/list/')
        self.assertEqual(response.status_code, 200)
