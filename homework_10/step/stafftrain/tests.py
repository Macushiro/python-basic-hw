"""
    Файл тестирования моделей.
"""

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Course, Result


# Create your tests here.
class TestUser(TestCase):

    def test_str(self):
        user = User.objects.create(username='Frank', email='frank@sinatra.com')
        self.assertEqual(str(user.username), 'Frank')
        self.assertEqual(str(user.email), 'frank@sinatra.com')


class TestCourse(TestCase):

    def setUp(self) -> None:
        print('......Created user for test......')
        self.user = User.objects.create(username='Frank', email='frank@sinatra.com')

    def tearDown(self) -> None:
        self.user.delete()
        print('....Test user has been deleted....')

    def test_str_method(self):
        course = Course.objects.create(name='SQL')
        self.assertEqual(str(course.name), 'SQL')

    def test_create_with_student(self):
        course = Course.objects.create(name='SQL', student=self.user)
        self.assertTrue(course.student, self.user)
        Course.objects.filter(pk=course.pk).update(student='')

    def test_update(self):
        course = Course.objects.create(name='SQL', student=self.user)
        Course.objects.filter(pk=course.pk).update(name='Python')
        course.refresh_from_db()
        self.assertEqual(str(course.name), 'Python')
        Course.objects.filter(pk=course.pk).update(student='')

    def test_wrong(self):
        course = Course.objects.create(name=00000000000, description=111111111)
        with self.assertRaises(AssertionError):
            self.assertEqual(course.name, '00000000000')
            self.assertEqual(course.description, '111111111')
            print('Get expected error')


class TestResult(TestCase):

    def test_result_init(self):
        user = User.objects.create(username='Frank', email='frank@sinatra.com')
        course = Course.objects.create(name='SQL', student=user)
        result = Result.objects.create(student=user, course=course, percent=10.1, test_result=True)
        self.assertEqual(result.percent, 10.1)
        self.assertEqual(result.test_result, True)