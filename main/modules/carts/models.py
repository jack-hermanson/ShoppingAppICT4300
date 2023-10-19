from main import db


class Cart(db.Model):
    cart_id = db.Column(db.Integer, primary_key=True)
    account_id = db.mapped_column(db.ForeignKey("account.account_id"), nullable=True)
    account = db.relationship("Account", back_populates="cart", single_parent=True, uselist=False)
