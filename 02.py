import random

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/user/<name>")
def hello(name):
    return render_template("hello.html", name=name)


@app.route("/omikuji")
def omikuji():
    omikuji_list = ["大吉", "中吉", "凶"]
    result = random.choice(omikuji_list)
    return render_template("omikuji.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
