from main import db, login_manager
from flask_login import UserMixin
from .ClearanceEnum import ClearanceEnum
from sqlalchemy.sql import func


USERNAME_MIN_LENGTH = 4
USERNAME_MAX_LENGTH = 32

EMAIL_MIN_LENGTH = 2
EMAIL_MAX_LENGTH = 64


@login_manager.user_loader
def load_user(user_id):
    return Account.query.get(int(user_id))


class Account(db.Model, UserMixin):

    account_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(USERNAME_MAX_LENGTH), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    clearance = db.Column(db.Integer, default=ClearanceEnum.NORMAL, nullable=False)
    email = db.Column(db.String(EMAIL_MAX_LENGTH), unique=True, nullable=False)
    join_date = db.Column(db.DateTime, server_default=func.now(), nullable=False)
    last_login = db.Column(db.DateTime, nullable=True)

    cart = db.relationship("Cart", back_populates="account", cascade="all, delete", uselist=False)

    def __repr__(self):
        return f"<Account: {self.account_id}, {self.username}>"

    def get_id(self):
        return self.account_id


