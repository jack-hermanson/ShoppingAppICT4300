from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, IntegerField, URLField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Email, Length, NumberRange
from .models import ITEM_NAME_MAX_LENGTH, ITEM_DESCRIPTION_MAX_LENGTH, ITEM_IMAGE_URL_MAX_LENGTH


name_length = Length(min=1, max=ITEM_NAME_MAX_LENGTH)
description_length = Length(max=ITEM_DESCRIPTION_MAX_LENGTH)
image_url_length = Length(max=ITEM_IMAGE_URL_MAX_LENGTH)
inventory_range = NumberRange(min=0, max=2048)


class CreateEdit(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), name_length])
    description = TextAreaField("Description", validators=[description_length])
    image_url = URLField("Image URL", validators=[image_url_length])
    current_inventory = IntegerField("Current Inventory", validators=[inventory_range])
    submit = SubmitField("Submit")
