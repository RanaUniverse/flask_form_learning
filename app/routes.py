from urllib.parse import urlsplit

from flask import render_template, flash, redirect, url_for, request

from flask_login import current_user, login_user, logout_user, login_required
import sqlalchemy as sa

from app import app, db
from app.models import User
from app.forms import LoginForm, RegistrationForm

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
@login_required
def index():
    return render_template(
        "index.html",
        title="Home",
        # user=user,
        posts=posts,
    )


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data)
        )
        if user is None or not user.check_password(form.password.data):
            flash("Invalid username or password was pressed...")
            return redirect(url_for("login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or urlsplit(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(next_page)
    return render_template("login.html", title="Sign In", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@app.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now register as a new user")
        return redirect(url_for("login"))
    return render_template(
        "register.html",
        title="Register For New User",
        form=form,
    )


# @app.route("/login_old")
# def login_old():
#     form = LoginForm()
#     return render_template(
#         "login.html",
#         title="Sign In Page",
#         form=form,
#     )


# @app.route("/login_old2", methods=["GET", "POST"])
# def login_old2():
#     form = LoginForm()
#     print("is this validate on submit?", form.validate_on_submit())
#     if form.validate_on_submit():
#         flash(
#             "Login requested for user {}; remember_me={}".format(
#                 form.username.data,
#                 form.remember_me.data,
#             )
#         )
#         return redirect(url_for("index"))

#     return render_template(
#         "login.html",
#         title="Sign In Page",
#         form=form,
#     )
