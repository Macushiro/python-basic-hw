"""
    Модуль обработки запросов по пользователям.
"""
import requests
import random
from flask import (
    Blueprint,
    render_template,
)
from sqlalchemy import func

# Тут не пойму что сломалось. Приложение видит, но PyCharm подчеркнул красным,
# а при импорте через "..models" - не подчеркивает, но зато выдаёт:
# "ImportError: attempted relative import beyond top-level package"
from models import db, User, Bill
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest

users_app = Blueprint(
    "users_app",
    __name__,
)

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"


@users_app.get("/list/", endpoint="user_list")
def get_user_list():
    user_list = User.query.all()
    return render_template("user_list.html", user_list=user_list)


@users_app.get("/<int:user_id>/", endpoint="user_info")
def get_user_bills_by_id(user_id: int):
    user = User.query.get(user_id)
    bills_list = Bill.query.filter_by(user_id=user_id).order_by(Bill.bill_number)
    return render_template("user_info.html", user=user, bills_list=bills_list)


@users_app.get("/reload/", endpoint="reload_users")
def upload_users_info():
    with requests.session() as session:
        response = session.get(USERS_DATA_URL)
        data = response.json()
        users = [
            User(name=el["name"], email=el["email"])
            for el in data
        ]
        Bill.query.delete()
        User.query.delete()
        db.session.commit()
        db.session.add_all(users)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            raise BadRequest(f"Couldn't add new users to Database.")
        min_user_id = db.session.query(func.min(User.id)).scalar()
        max_user_id = db.session.query(func.max(User.id)).scalar()
        r = random
        user_list = range(min_user_id, max_user_id+1)
        nums = range(1, r.randrange(1, 1000))
        bills = [
            Bill(user_id=el, bill_number=el, total=r.uniform(1.0, 1000.0), description=f"Check #{el} for {r.choice(['food', 'fuel', 'water'])}")
            # for num in nums
            for el in user_list
        ]
        print(min_user_id, max_user_id)
        db.session.add_all(bills)
        db.session.commit()
    return data