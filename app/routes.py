from flask import render_template

from app import app
from app.forms import LoginForm


user = {"username": "Roman Reigns"}

posts: list[dict[str, str | dict[str, str]]] = [
    {
        "author": {"username": "John Cena"},
        "body": "Beautiful day in Portland!",
    },
    {
        "author": {"username": "Brock Lesnar"},
        "body": "The Avengers movie was so cool!",
    },
]


@app.route("/")
@app.route("/index")
def index():
    return render_template(
        "index.html",
        title="Home",
        user=user,
        posts=posts,
    )


@app.route("/login")
def login():
    form = LoginForm()
    return render_template(
        "login.html",
        title="Sign In Page",
        form=form,
    )
