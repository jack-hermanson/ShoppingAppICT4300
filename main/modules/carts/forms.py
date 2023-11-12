from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, IntegerField, URLField, TextAreaField, DecimalField, SelectField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Email, Length, NumberRange, Regexp

states = ["", 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
          'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
          'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
          'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
          'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']


class CheckoutForm(FlaskForm):
    # https://stackoverflow.com/questions/59650010/regularexpression-for-16-digits-virtual-visa-cards-with-dash
    credit_card_number = StringField("Credit/Debit Card Number",
                                     render_kw={"placeholder": "XXXX-XXXX-XXXX-XXXX"},
                                     validators=[DataRequired(),
                                                 Regexp("^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$",
                                                        message="Please enter a valid credit card number.")])
    expiration_date = StringField("Expiration",
                                  render_kw={"placeholder": "MM/YY"},
                                  validators=[DataRequired(),
                                              Regexp("^(0[1-9]|10|11|12)/[2-9][0-9]$",
                                                     message="Please enter a valid expiration date in MM/YY format.")])
    name = StringField("Name", validators=[DataRequired()])
    street_address = StringField("Street Address", validators=[DataRequired()])
    city = StringField("City", validators=[DataRequired()])
    state = SelectField("State", validators=[DataRequired(), Length(2)], choices=states)
    zip_code = StringField("ZIP Code", validators=[DataRequired(), Length(min=5, max=5)],
                           description="Enter your ZIP code, and the city and state will be filled in automatically.")

    submit = SubmitField("Submit")
