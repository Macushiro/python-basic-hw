from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    redirect,
    flash,
)

# Тут не пойму что сломалось. Приложение видит, но PyCharm подчеркнул красным,
# а при импорте через "..models" - не подчеркивает, но зато выдаёт:
# "ImportError: attempted relative import beyond top-level package"
from models import User

users_app = Blueprint(
    "users_app",
    __name__,
)

@users_app.get("/", endpoint="user_list")
def get_user_list():
    user_list = User.query.all()
    print(user_list)
    return render_template("users.html", user_list=user_list)