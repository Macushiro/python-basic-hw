# как оказалось без подобной обёртки данный образ не запускал приложение
from main import app


if __name__ == "__main__":
    app.run(debug=False)