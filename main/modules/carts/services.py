
from flask_login import current_user
from .models import Cart


def create_cart_for_visitor():
    """
    todo
    When a user visits the site, we need to give them
    a cart if they don't already have one. It should persist
    between sessions by storing a GUID in local storage.
    If they're logged in, store it on the user so it'll be there
    if they open on a different device.
    """
    pass
