from flask import Blueprint, render_template, request
from sqlalchemy import and_

from .forms import CheckoutForm
from .models import CartItem
from .services import get_or_initialize_cart, get_cart_total_cost, get_zip_info
from flask_login import login_required
from main import db
from ..items.models import Item

carts = Blueprint("carts", __name__, url_prefix="/cart")


@carts.route("/")
@login_required
def my_cart():
    cart = get_or_initialize_cart()
    cart_total = get_cart_total_cost()
    return render_template("carts/cart.html",
                           cart=cart,
                           cart_total=cart_total)


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
    cart_item_to_remove = CartItem.query.filter(and_(CartItem.cart == cart, CartItem.item == item)).first_or_404()
    cart.cart_items.remove(cart_item_to_remove)
    db.session.commit()
    cart_total = get_cart_total_cost()
    cart = get_or_initialize_cart()
    return render_template("carts/add-to-cart-result.html",
                           item=item, screen=screen, cart=cart, cart_total=cart_total)


@carts.route("/checkout", methods=["GET", "POST"])
def checkout():
    form = CheckoutForm()

    if form.validate_on_submit():
        return "ok"

    return render_template("carts/check-out.html", form=form)


# @carts.route("/zip/<int:zip_code>")
# def zip_lookup(zip_code: int):
#     api_key = "c6c50a20-9b45-11eb-bf7d-27621b3d470d"
#     base_url = "https://app.zipcodebase.com/api/v1/search"
#     url = f"{base_url}?codes={zip_code}&country=US&apikey={api_key}"
#
#     req = requests.get(url)
#     raw_data = req.json()
#     try:
#         key = list(raw_data.get("results").keys())[0]
#         data = raw_data.get("results").get(key)[0]
#         city = data.get("city")
#         state_code = data.get("state_code")
#
#         return {"city": city, "state": state_code}
#     except AttributeError:
#         logging.fatal(f"Invalid zip code or request failed for {zip_code}")
#         return abort(400)


@carts.route("/zip", methods=["POST"])
def zip_lookup():
    form = CheckoutForm()
    if form.zip_code.data:
        try:
            zip_info = get_zip_info(zip_code=form.zip_code.data)
            form.city.data = zip_info.get("city")
            form.state.data = zip_info.get("state")
        except AttributeError:
            # if the zip code is bad, handle it
            form.zip_code.errors = [f"Sorry, {form.zip_code.data} is not a valid ZIP code."]
            form.city.data = ""
            form.state.data = None

    return render_template("carts/checkout-form-partial.html", form=form)
