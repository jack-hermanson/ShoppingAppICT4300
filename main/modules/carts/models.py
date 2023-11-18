from main import db
from sqlalchemy import func


class CartItem(db.Model):
    cart_id = db.mapped_column(db.ForeignKey("cart.cart_id"), nullable=False, primary_key=True)
    cart = db.relationship("Cart", back_populates="cart_items")

    item_id = db.mapped_column(db.ForeignKey("item.item_id"), nullable=False, primary_key=True)
    item = db.relationship("Item")

    count = db.Column(db.Integer, nullable=False, server_default="1")

    def __repr__(self):
        return f"CartItem! cart_id={self.cart_id}, item_id={self.item_id}"


class Cart(db.Model):
    cart_id = db.Column(db.Integer, primary_key=True)
    account_id = db.mapped_column(db.ForeignKey("account.account_id"), nullable=False)
    last_updated = db.Column(db.DateTime, server_default=func.now(), nullable=False)

    cart_items = db.relationship("CartItem", back_populates="cart", cascade="all, delete-orphan")
    account = db.relationship("Account", back_populates="cart", single_parent=True, uselist=False)

