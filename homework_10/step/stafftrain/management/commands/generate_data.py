"""
    Файл наполнения БД.
"""

from django.core.exceptions import BadRequest
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.db import IntegrityError
import random
import requests

from stafftrain.models import Course, Result
import env

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
course_list = ['SQL', 'Python', 'Java', 'Kotlin', 'JS', 'HTML/CSS', 'JQuery', 'C++']
course_level = ['starter', 'base', 'advanced', 'professional', 'for architects', 'optimization']

class Command(BaseCommand):
    help = 'Generate data'

    def handle(self, *args, **options):
        print('DB populating has started')

        # 1. Clearing
        print('Erasing previous data')
        Result.objects.all().delete()
        Course.objects.all().delete()
        User.objects.all().delete()

        # 2. Generate base data
        print('Generating base data')
        su = User.objects.create_superuser(
            username='macushiro',
            email='macushiro@newbie.com',
            password=env.su_password,
        )

        # 2.1 Getting data from external service
        with requests.session() as session:
            response = session.get(USERS_DATA_URL)
            data = response.json()
            r = random
            for el in data:
                try:
                    user = User.objects.create(
                        username=el['username'],
                        first_name=el['name'],
                        email=el['email']
                    )
                    # 2.2 Generate courses data
                    print(user.id, user.username, user.first_name)
                    course_name = r.choice(course_list)
                    course = Course.objects.create(
                        name=course_name,
                        description=f"{course_name} {r.choice(course_level)} course",
                        is_available=True, student=user
                    )
                    print(course.name, course.description)
                except IntegrityError:
                    raise BadRequest(f"Couldn't delete previous data from Database.")

        # 3. Generate results data  -  for feature working
        # min_user_id = User.objects.order_by('id').first()
        # max_user_id = User.objects.order_by('id').last()
        # user_list = range(min_user_id, max_user_id + 1)
        # left_bord = 1
        # for el in user_list:
        #     right_bord = left_bord + r.randrange(1, 10)
        #     while left_bord < right_bord:
        #         result = Result.objects.create(
        #             student=el,
        #             course=f"Result #{left_bord} for {r.choice(['normal', 'good', 'great'])}",
        #             percent=r.uniform(1.0, 100.0),
        #             test_result=left_bord,
        #         )
        #         left_bord += 1
        #     left_bord = right_bord

