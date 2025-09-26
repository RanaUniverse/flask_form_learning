from flask import render_template, flash, redirect, url_for

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


@app.route("/login_old")
def login_old():
    form = LoginForm()
    return render_template(
        "login.html",
        title="Sign In Page",
        form=form,
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    print("is this validate on submit?", form.validate_on_submit())
    if form.validate_on_submit():
        flash(
            "Login requested for user {}; remember_me={}".format(
                form.username.data,
                form.remember_me.data,
            )
        )
        return redirect(url_for("index"))

    return render_template(
        "login.html",
        title="Sign In Page",
        form=form,
    )
