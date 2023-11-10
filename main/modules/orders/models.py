from main import db
from sqlalchemy import func


class OrderItem(db.Model):
    order_id = db.mapped_column(db.ForeignKey("order.order_id"), nullable=False, primary_key=True)
    order = db.relationship("Order", back_populates="order_items")

    item_id = db.mapped_column(db.ForeignKey("item.item_id"), nullable=False, primary_key=True)
    item = db.relationship("Item")

    count = db.Column(db.Integer, nullable=False, server_default="1")
    price_per_item = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"OrderItem: order_id={self.order_id}, item_id={self.item_id}"


class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    account_id = db.mapped_column(db.ForeignKey("account.account_id"), nullable=False)
    date_submitted = db.Column(db.DateTime, server_default=func.now(), nullable=False)

    order_items = db.relationship("OrderItem", back_populates="order")
    account = db.relationship("Account", back_populates="orders")


