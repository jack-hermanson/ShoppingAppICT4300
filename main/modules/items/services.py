from .models import Item
from ..carts.models import CartItem
from main import db


def get_all_items():
    return Item.query.order_by(Item.name).all()


def get_items_in_stock():
    # todo - add sorting, filtering?
    return Item.query.filter(Item.current_inventory > 0) \
        .order_by(Item.name).all()


def remove_item_from_all_carts(item):
    cart_items = CartItem.query.filter(CartItem.item == item).all()
    for cart_item in cart_items:
        db.session.delete(cart_item)
    db.session.commit()
