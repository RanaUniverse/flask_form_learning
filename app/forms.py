from collections.abc import Sequence
from typing import Mapping
from flask_wtf import FlaskForm  # type: ignore # for this has what to do i am confused.

import sqlalchemy as sa

from wtforms import StringField, PasswordField, BooleanField, SubmitField

from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from wtforms.validators import DataRequired


from app import db

from app.models import User


class LoginForm(FlaskForm):
    """
    This LoginForm name i make i make myself of what to do?
    """

    username = StringField(
        label="Username",
        validators=[DataRequired()],
        description=(
            "This is where user will press his preferred username "
            "it can be seen with .description "
        ),
    )

    password = PasswordField(
        label="Password",
        validators=[DataRequired()],
    )
    remember_me = BooleanField(
        label="Remember Me",
    )
    submit = SubmitField(
        "Sign In",
    )


class RegistrationForm(FlaskForm):

    username = StringField(
        label="Username",
        validators=[DataRequired()],
    )

    email = StringField(
        label="Email",
        validators=[DataRequired(), Email()],
    )
    password = PasswordField(
        label="Password",
        validators=[DataRequired()],
    )

    password2 = PasswordField(
        label="Repeat Password",
        validators=[DataRequired(), EqualTo("password")],
    )

    submit = SubmitField("Register Now")

    def validate_username(self, username: StringField):
        user = db.session.scalar(sa.select(User).where(User.username == username.data))
        if user is not None:
            raise ValidationError("Please use a different username.")

    def validate_email(self, email: StringField):
        user = db.session.scalar(sa.select(User).where(User.email == email.data))
        if user is not None:
            raise ValidationError("Please use a different email address.")
