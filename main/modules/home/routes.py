from flask import Blueprint, render_template
from ..items import services as item_services


home = Blueprint("home", __name__, url_prefix="")


@home.route("/")
def index():
    items = item_services.get_items_in_stock()
    return render_template("home/index.html",
                           items=items)
