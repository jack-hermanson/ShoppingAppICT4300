from flask import Blueprint, render_template, abort, request, flash, redirect, url_for
from .forms import CreateEdit


items = Blueprint("items", __name__, url_prefix="/items")


@items.route("/")
def index():
    return render_template("items/index.html")


@items.route("/create", methods=["GET", "POST"])
def create():
    form = CreateEdit()

    return render_template("items/create-edit.html",
                           mode="create",
                           form=form)
