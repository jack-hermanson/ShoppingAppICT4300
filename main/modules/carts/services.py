import logging
from uuid import uuid4
from flask_login import current_user
from .models import Cart
from main import db


def get_or_initialize_cart(existing_cart_guid: str | None) -> Cart | None:
    """
    When a user visits the site, we need to give them
    a cart if they don't already have one. It should persist
    between sessions by storing a GUID in local storage.
    If they're logged in, store it on the user so it'll be there
    if they open on a different device.
    """


    if existing_cart_guid:
        # apparently there is already a cart, go get it
        existing_cart = Cart.query.filter(Cart.cart_guid == existing_cart_guid).first()

        if not existing_cart:
            logging.error("Failed to find existing cart with GUID", existing_cart_guid)
            return None

        # okay, we have a cart
        # it's possible that it was created before user logged in, so let's make sure that's okay
        if current_user.is_authenticated and existing_cart.account is None:
            existing_cart.account = current_user
            db.session.commit()
            return existing_cart
        if not current_user.is_authenticated and existing_cart.account is None:
            # not authenticated and cart has no account, it's fine
            return existing_cart

        if current_user.is_authenticated and existing_cart.account != current_user:
            logging.error("Someone is trying to steal this cart!", existing_cart_guid)
            return None
        elif not current_user.is_authenticated and existing_cart.account:
            # user is not authenticated but cart belongs to a user
            # not good
            logging.error("Current user is not authenticated but has the GUID for a cart that belongs to a user")
            # go ahead and move on to creating a new cart

    if current_user.is_authenticated and current_user.cart:
        # logged in, has cart, so just return it
        return current_user.cart

    # If we make it here, there is no existing cart, so we have to create it
    new_cart = Cart()
    new_cart.cart_guid = uuid4().__str__()

    if current_user.is_authenticated:
        new_cart.account = current_user

    db.session.add(new_cart)
    db.session.commit()

    return new_cart

