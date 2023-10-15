from .models import Item


def get_all_items():
    return Item.query.order_by(Item.name).all()


def get_items_in_stock():
    # todo - add sorting, filtering?
    return Item.query.filter(Item.current_inventory > 0) \
        .order_by(Item.name).all()
