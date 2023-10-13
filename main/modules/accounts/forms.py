from sqlalchemy import func
from .models import Account
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField, BooleanField, EmailField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Email, Length


name_length = Length(min=2, max=15)
password_length = Length(max=100)


class Login(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), name_length], render_kw={
        "autofocus": "true"
    })
    password = PasswordField("Password", validators=[DataRequired(), password_length])
    remember = BooleanField("Remember Me", default=False)
    submit = SubmitField("Log In")

    @staticmethod
    def validate_name(_, username):
        if not Account.query.filter(func.lower(Account.username) == func.lower(username.data)).count():
            raise ValidationError("That username does not exist.")


class Create(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(), name_length],
        render_kw={
            "autofocus": "true"
        }
    )
    email = EmailField(
        "Email",
        validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), password_length])
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(),
            EqualTo("password", "Your passwords must match.")
        ]
    )
    submit = SubmitField("Create Account")

    @staticmethod
    def validate_username(_, username):
        if Account.query.filter(func.lower(Account.username) == func.lower(username.data.strip())).all():
            raise ValidationError("That username has already been taken.")

    @staticmethod
    def validate_email(_, email):
        if Account.query.filter(func.lower(Account.email) == func.lower(email.data.strip())).all():
            raise ValidationError("That email has already been taken.")
