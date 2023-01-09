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
from models import User, Bill

bills_app = Blueprint(
    "bills_app",
    __name__,
)

@bills_app.get("/<int:user_id>", endpoint="bill_list")
def get_user_bills(user_id: int):
    user = User.query.get(user_id)
    bills = Bill.query.all()
    #     get_or_404(
    #     user.id,
    #     description=f"Bills for user {user.first_name!r} not founded."
    # )
    return render_template("bills.html", user=user, bills_list=bills)