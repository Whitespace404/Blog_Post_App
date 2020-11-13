from flask_login import current_user
from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    EqualTo,
    ValidationError,
    NoneOf,
)
from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Length(
                min=3,
                max=20,
                message="A username should atleast\
                                            have three characters.",
            ),
        ],
    )
    email = StringField("Email", validators=[DataRequired(), Email()])

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=8),
            NoneOf(
                values=[
                    "password",
                    "adminatflaskblog",
                    "__FLASKBLOG_ADMIN__" "thisisadifficultpassword",
                    "qwertyuiop",
                    "password",
                    "password!",
                    "password1",
                    "1234567890",
                    "abcdefghijkl",
                    "123456789",
                    "dirtyadmin",
                    "dirtywebsite",
                    "0123456789",
                    "flaskblog1",
                    "everpost1",
                    "EverPost0",
                    "abcdefghijk",
                    "abcdefghijk",
                    "abcdefghij",
                    "abcdefghi",
                    "abcdefgh",
                    "0987654321",
                    "zxcvbnm",
                    "asdfghjkl",
                    "thehardestpassword",
                    "YouCan'tHackMyPassword",
                    "UnbeatablePassword",
                ],
                message="Your password appears in a \
                                         list of previously hacked passwords.",
            ),
        ],
    )
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Create Account")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("This username already exists.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("This email already exists.")

    def validate_password(self, password):
        NUMBERS = "1234567890"
        validated_ = False
        for character in NUMBERS:
            if character in password.data:
                validated_ = True
        if not validated_:
            raise ValidationError("Your password should have a number in it.")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    recaptcha = RecaptchaField()
    submit = SubmitField("Continue")


class UpdateAccountForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    picture = FileField(
        "Update Profile Picture", validators=[FileAllowed(["jpg", "png", "jpeg", ""])]
    )
    submit = SubmitField("Update")

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError("This username already exists.")

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    "This email already exists. Please choose a different one. How about "
                )


class RequestResetForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    recaptcha = RecaptchaField()
    submit = SubmitField("Request a Password Reset.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is None:
            raise ValidationError(
                "There is no account with that email. Please enter a valid email adress."
            )


class ChangePasswordForm(FlaskForm):
    new_password = PasswordField(
        "New Password", validators=[DataRequired(), Length(min=8)]
    )
    confirm_password = PasswordField(
        "Confirm New Password", validators=[DataRequired(), Length(min=8)]
    )
    submit = SubmitField("Change my Password.")
