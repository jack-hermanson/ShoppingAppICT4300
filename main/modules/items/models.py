from main import db


ITEM_NAME_MAX_LENGTH = 100
ITEM_DESCRIPTION_MAX_LENGTH = 512
ITEM_IMAGE_URL_MAX_LENGTH = 100


class Item(db.Model):

    item_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(ITEM_NAME_MAX_LENGTH), nullable=False)
    description = db.Column(db.String(ITEM_DESCRIPTION_MAX_LENGTH), nullable=True)
    image_url = db.Column(db.String(ITEM_IMAGE_URL_MAX_LENGTH), nullable=True)
    current_inventory = db.Column(db.Integer, nullable=False, server_default="0")
