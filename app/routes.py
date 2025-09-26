from flask import render_template

from app import app


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
