from .models import Item


def get_all_items():
    return Item.query.order_by(Item.name).all()
