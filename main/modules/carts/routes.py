import logging

from flask import Blueprint, render_template, flash, redirect, url_for, request, abort

from .models import CartItem
from .services import get_or_initialize_cart
from flask_login import login_required
from main import db
from ..items.models import Item

carts = Blueprint("carts", __name__, url_prefix="/carts")


@carts.route("/")
@login_required
def my_cart():
    cart = get_or_initialize_cart()
    return render_template("carts/cart.html",
                           cart=cart)


@carts.route("/anchor-partial")
@login_required
def get_cart_anchor_partial():
    """Cart that displays in the navigation bar"""
    cart = get_or_initialize_cart()
    return render_template("carts/cart-anchor-partial.html",
                           cart=cart)


@carts.route("/add", methods=["POST"])
@login_required
def add_to_cart():

    item_id = int(request.form.get("item_id"))
    count = int(request.form.get("count"))

    cart = get_or_initialize_cart()
    item = Item.query.get_or_404(item_id)
    # todo - doesn't handle duplicates, doesn't actually handle count
    # https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#association-object
    cart_item = CartItem()
    cart_item.cart = cart
    cart_item.item = item
    cart_item.count = count
    cart.cart_items.append(cart_item)
    db.session.commit()

    return render_template("carts/add-to-cart-result.html", item=item, screen="items")


@carts.route("/remove/<int:item_id>/<string:screen>", methods=["POST"])
@login_required
def remove_from_cart(item_id: int, screen: str):
    cart = get_or_initialize_cart()
    item = Item.query.get_or_404(item_id)
    cart_item_to_remove = CartItem.query.filter(CartItem.cart == cart and CartItem.item == item).first_or_404()
    cart.cart_items.remove(cart_item_to_remove)
    db.session.commit()
    return render_template("carts/add-to-cart-result.html", item=item, screen=screen, cart=cart)
