from flask import Blueprint

carts = Blueprint("carts", __name__, url_prefix="/carts")


@carts.route("/")
def temp():
    # todo - remove
    return "it works"
