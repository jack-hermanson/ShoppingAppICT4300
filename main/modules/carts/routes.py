from flask import Blueprint, request
from flask_login import current_user
from uuid import uuid4

carts = Blueprint("carts", __name__, url_prefix="/carts")


@carts.route("/")
def temp():
    # todo - remove
    return "it works"


@carts.route("/initialize")
def initialize_cart():
    if current_user.is_authenticated:
        # User is authenticated.
        # See if user already has a cart.
        # todo
        return "ok"

    # User is not authenticated, do we need a new cart?
    elif request.args.get("cart_guid"):
        # We are told by the browser that there is already a cart.
        # Try to find it. todo
        return "temp"

    # User is not authenticated and browser isn't aware of any cart.
    # Create a new one.
    guid = uuid4()
    return guid.__str__()



