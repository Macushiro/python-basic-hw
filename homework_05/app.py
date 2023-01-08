"""
Домашнее задание №5
Первое веб-приложение

создайте базовое приложение на Flask
создайте index view /
добавьте страницу /about/, добавьте туда текст
создайте базовый шаблон (используйте https://getbootstrap.com/docs/5.0/getting-started/introduction/#starter-template)
в базовый шаблон подключите статику Bootstrap 5 и добавьте стили, примените их
в базовый шаблон добавьте навигационную панель nav (https://getbootstrap.com/docs/5.0/components/navbar/)
в навигационную панель добавьте ссылки на главную страницу / и на страницу /about/ при помощи url_for
"""
from flask import Flask, render_template


app = Flask(
    __name__,
)

app.config.update(
    ENV="development",
    SECRET_KEY="homework_05_TKV_Zzzz",
)

greeting_info = "Hello there! Nice to meet You on our service main page!"
about = "This is info about our very useful service... ^^,"

@app.get("/", endpoint="index_page")
def get_index_page():
    return render_template("index.html", page_text=greeting_info)


@app.get("/about/", endpoint="about_page")
def get_info():
    return render_template("about.html", page_text=about)


if __name__ == "__main__":
    app.run(debug=True)