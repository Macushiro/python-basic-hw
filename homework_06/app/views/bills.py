"""
    Модуль обработки запросов по счетам.
"""

from flask import (
    Blueprint,
    render_template,
    request,
    url_for,
    redirect,
)

# Тут не пойму что было с PyCharm, он подчеркнул красным "models",
# и не видел обращения к методам и свойствам импортированных объектов,
# а при импорте через "..models" - не подчеркивал, но зато выдавал:
# "ImportError: attempted relative import beyond top-level package"
from models import User, Bill, db
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import BadRequest

from .forms.add_bill import BillForm

bills_app = Blueprint(
    "bills_app",
    __name__,
)


# Add new bill manually
@bills_app.route(
    "/<int:user_id>/add_bill/",
    methods=["GET", "POST"],
    endpoint="add_bill"
)
def add_bill_for_user(user_id: int):
    user = User.query.get_or_404(
        user_id,
        description=f"User #{user_id} not found!"
    )

    if request.method == "GET":
        form = BillForm(user_name=user.name)
        return render_template("add.html", form=form, user=user)

    form = BillForm()
    if not form.validate_on_submit():
        return render_template("add.html", form=form, user=user), 400

    bill_number = form.number.data
    bill_total = form.total.data
    bill_description = form.description.data
    bill = Bill(bill_number=bill_number, total=bill_total, description=bill_description, user_id=user_id)
    db.session.add(bill)
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise BadRequest(f"Could not add bill with #{bill_number!r},"
                         f" bill with that number already exists.")

    url = url_for("users_app.user_info", user_id=user_id)
    return redirect(url)