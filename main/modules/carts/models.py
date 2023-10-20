from main import db


cart_item = db.Table(
    "cart_item",
    db.Column("cart_id", db.Integer, db.ForeignKey("cart.cart_id")),
    db.Column("item_id", db.Integer, db.ForeignKey("item.item_id"))
)


class Cart(db.Model):
    cart_id = db.Column(db.Integer, primary_key=True)
    account_id = db.mapped_column(db.ForeignKey("account.account_id"), nullable=True)
    account = db.relationship("Account", back_populates="cart", single_parent=True, uselist=False)
    items = db.relationship("Item", secondary=cart_item)
