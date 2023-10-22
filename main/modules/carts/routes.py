from flask import Blueprint, request
from flask_login import current_user
from uuid import uuid4

from main.modules.carts import services

carts = Blueprint("carts", __name__, url_prefix="/carts")


@carts.route("/")
def temp():
    # todo - remove
    return "it works"


@carts.route("/initialize")
def initialize_cart():
    """
    Initialize a cart and return its guid.
    This route should be accessed via JavaScript.
    """
    cart = services.get_or_initialize_cart(request.args.get("cart_guid"))
    if not cart:
        return "", 404
    return cart.cart_guid




