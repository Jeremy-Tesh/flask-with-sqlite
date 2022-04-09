from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from market.model import User


class RegisterForm(FlaskForm):
    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("Usename already exists!")

    def validate_email(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()
        if email:
            raise ValidationError("Email aaddress already exist!")

    username = StringField(
        label="User Name", validators=[Length(min=2, max=30), DataRequired()]
    )
    email = StringField(label="Email", validators=[Email(), DataRequired()])
    password1 = PasswordField(
        label="Password", validators=[Length(min=6), DataRequired()]
    )
    password2 = PasswordField(
        label="Confirm Password", validators=[EqualTo("password1"), DataRequired()]
    )
    submit = SubmitField(label="Create Account")


class LoginForm(FlaskForm):
    username = StringField(
        label="User Name", validators=[Length(min=2, max=30), DataRequired()]
    )
    password1 = PasswordField(
        label="Password", validators=[Length(min=6), DataRequired()]
    )
    submit = SubmitField(label="Login")
