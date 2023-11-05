from sqlalchemy import func
from .models import Account, EMAIL_MIN_LENGTH, EMAIL_MAX_LENGTH, USERNAME_MIN_LENGTH, USERNAME_MAX_LENGTH
from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField, PasswordField, BooleanField, EmailField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Email, Length


username_length = Length(min=USERNAME_MIN_LENGTH, max=USERNAME_MAX_LENGTH)
password_length = Length(max=100)
email_length = Length(min=EMAIL_MIN_LENGTH, max=EMAIL_MAX_LENGTH)


class Login(FlaskForm):
    username = StringField("Username", validators=[DataRequired(), username_length], render_kw={
        "autofocus": "true"
    })
    password = PasswordField("Password", validators=[DataRequired(), password_length])
    remember = BooleanField("Remember Me", default=False)
    submit = SubmitField("Log In")

    @staticmethod
    def validate_username(_, username):
        account_exists = Account.query.filter(func.lower(Account.username) == func.lower(username.data)).count()
        if not account_exists:
            raise ValidationError(f"The username {username.data} does not exist.")


class Create(FlaskForm):
    username = StringField(
        "Username",
        validators=[DataRequired(), username_length],
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
