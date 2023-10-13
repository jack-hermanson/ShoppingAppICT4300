from flask import Blueprint, render_template, abort, request, flash, redirect, url_for
from .forms import CreateEdit
from . import services
from .models import Item
from main import db

items = Blueprint("items", __name__, url_prefix="/items")


# helper function
def update_item(item_entity, form) -> Item:
    item_entity.name = form.name.data
    item_entity.description = form.description.data if len(form.description.data) else None
    item_entity.image_url = form.image_url.data if len(form.image_url.data) else None
    item_entity.current_inventory = form.current_inventory.data

    return item_entity


@items.route("/")
def index():
    items_list = services.get_all_items()
    return render_template("items/index.html",
                           items_list=items_list)


@items.route("/create", methods=["GET", "POST"])
def create():
    form = CreateEdit()

    if form.validate_on_submit():
        new_item = Item()
        update_item(new_item, form)

        db.session.add(new_item)
        db.session.commit()

        flash(f"Item '{new_item.name}' created successfully.", "success")
        return redirect(url_for("items.index"))

    elif request.method == "GET":
        return render_template("items/create-edit.html",
                               mode="create",
                               form=form)


@items.route("/edit/<int:item_id>", methods=["GET", "POST"])
def edit(item_id: int):
    item = Item.query.get_or_404(item_id)

    form = CreateEdit()

    if form.validate_on_submit():
        update_item(item, form)
        db.session.commit()

        flash(f"Item '{item.name}' edited successfully.", "success")
        return redirect(url_for("items.index"))

    elif request.method == "GET":
        form.name.data = item.name
        form.description.data = item.description
        form.image_url.data = item.image_url
        form.current_inventory.data = item.current_inventory
        return render_template("items/create-edit.html",
                               mode="edit",
                               item=item,
                               form=form)


