from flask import (
    Blueprint,
    render_template,
)

# Тут не пойму что сломалось. Приложение видит, но PyCharm подчеркнул красным,
# а при импорте через "..models" - не подчеркивает, но зато выдаёт:
# "ImportError: attempted relative import beyond top-level package"
from models import User, Bill


users_app = Blueprint(
    "users_app",
    __name__,
)

@users_app.get("/list/", endpoint="user_list")
def get_user_list():
    user_list = User.query.all()
    return render_template("user_list.html", user_list=user_list)


@users_app.get("/<int:user_id>/", endpoint="user_info")
def get_user_bills_by_id(user_id: int):
    user = User.query.get(user_id)
    bills_list = Bill.query.filter_by(user_id=user_id).order_by(Bill.bill_number)
    return render_template("user_info.html", user=user, bills_list=bills_list)