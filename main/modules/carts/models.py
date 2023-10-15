from main import db


class Cart(db.Model):
    cart_id = db.Column(db.Integer, primary_key=True)

