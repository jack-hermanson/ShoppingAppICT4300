from flask_login import current_user
from .models import Cart
from main import db
from datetime import datetime


def get_or_initialize_cart():
    if current_user.is_authenticated:
        # should always be logged in
        if current_user.cart:
            current_user.cart.last_updated = datetime.now()
            db.session.commit()
            return current_user.cart
        else:
            new_cart = Cart()
            new_cart.account = current_user
            new_cart.last_updated = datetime.now()
            db.session.add(new_cart)
            db.session.commit()
            return new_cart
