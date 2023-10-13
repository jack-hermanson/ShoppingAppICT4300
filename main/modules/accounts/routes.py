from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user
from datetime import datetime
from .forms import Login, Create
from main import db, bcrypt
from .models import Account

accounts = Blueprint("accounts", __name__, url_prefix="/accounts")


@accounts.route("/log-in", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        flash("You are already logged in.", "warning")
        return redirect(url_for("home.index"))

    form = Login()
    if form.validate_on_submit():
        account = Account.query.filter(Account.username == form.username.data).first_or_404()
        if account and bcrypt.check_password_hash(account.password, form.password.data):
            login_user(account, remember=form.remember.data)
            next_page = request.args.get("next")
            last_login = account.last_login.strftime('%a %d %b %Y, %I:%M%p') \
                if account.last_login is not None else "never"
            flash(f"Welcome back, {account.username}. Your last login was {last_login}.", "info")
            account.last_login = datetime.now()
            db.session.commit()

            return redirect(next_page) if next_page else redirect(url_for("home.index"))
        else:
            flash("Incorrect login credentials.", "danger")

    return render_template("accounts/log-in.html",
                           form=form)


@accounts.route("/register", methods=["GET", "POST"])
def register():
    form = Create()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        new_account = Account()
        new_account.username = form.username.data.strip()
        new_account.password = hashed_password
        new_account.email = form.email.data.lower().strip()
        db.session.add(new_account)
        db.session.commit()
        flash(f"Your account has been created. Please log in.", "success")
    return render_template("accounts/register.html",
                           form=form)


@accounts.route("/log-out")
def logout():
    if not current_user.is_authenticated:
        flash("You are not logged in, so you cannot log out.", "danger")
        return redirect(url_for("accounts.login"))

    logout_user()
    flash("You have logged out successfully.", "success")
    return redirect(url_for("home.index"))


@accounts.route("/me")
def me():
    return render_template("accounts/me.html")
