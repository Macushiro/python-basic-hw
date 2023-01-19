"""
    Файл основной программы.
"""

from os import getenv

from flask import Flask, render_template
from flask_migrate import Migrate

from views.users import users_app
from views.bills import bills_app
from models import db

app = Flask(
    __name__,
)
app.register_blueprint(users_app, url_prefix="/user")
app.register_blueprint(bills_app, url_prefix="/bills")

CONFIG_OBJECT = getenv("CONFIG", "DevelopmentConfig")
app.config.from_object(f"config.{CONFIG_OBJECT}")


db.init_app(app)
migrate = Migrate(app, db)

@app.get("/", endpoint="index_page")
def get_root():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)