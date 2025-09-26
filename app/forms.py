from flask_wtf import FlaskForm  # type: ignore # for this has what to do i am confused.

from wtforms import StringField, PasswordField, BooleanField, SubmitField

from wtforms.validators import DataRequired


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
