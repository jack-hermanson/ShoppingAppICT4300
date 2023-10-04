from flask import Blueprint, render_template, abort

from .forms import Login, Create

accounts = Blueprint("accounts", __name__, url_prefix="/accounts")


@accounts.route("/log-in")
def login():
    form = Login()
    return render_template("accounts/log-in.html",
                           form=form)


@accounts.route("/register", methods=["GET", "POST"])
def register():
    form = Create()
    return render_template("accounts/register.html",
                           form=form)


@accounts.route("/log-out")
def logout():
    return None, 418


@accounts.route("/me")
def me():
    return None, 418
