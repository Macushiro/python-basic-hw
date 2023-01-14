from flask_wtf import FlaskForm
from wtforms import (
    IntegerField,
    DecimalField,
    StringField,
)
from wtforms.validators import (
    DataRequired,
    Length,
    NumberRange
)


class BillForm(FlaskForm):
    user_name = StringField(
        label="User name",
        name="user_name",
        validators=[DataRequired()],
    )
    number = IntegerField(
        label="Bill number",
        name="bill_number",
        validators=[
            DataRequired(),
            NumberRange(min=0),
        ],
    )
    total = DecimalField(
        label="Total",
        name="total",
        validators=[
            DataRequired(),
            NumberRange(min=0),
        ],
    )
    description = StringField(
        label="Description",
        name="description",
        validators=[
            DataRequired(),
            Length(min=3, max=200),
        ],
    )