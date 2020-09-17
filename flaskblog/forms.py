from flask_wtf import FlaskForm, RecaptchaField
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import (
    StringField, PasswordField, SubmitField,
    BooleanField, SelectField, RadioField,
    TextAreaField,
)
from wtforms.validators import (
    DataRequired,
    Length, Email,
    EqualTo, ValidationError,
    InputRequired,
)
from flaskblog.models import User, Post

SPECIAL_CHARACTERS = "/\\-+!@#$%^&()~`><=*_\{\}[]';:\"?.,|"


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[
                             DataRequired(), Length(min=8)])
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("This username already exists.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("This email already exists.")

    def validate_password(self, password):
        validated_ = False
        for character in SPECIAL_CHARACTERS:
            if character in password.data:
                validated_ = True
        if not validated_:
            raise ValidationError(
                "Your password should have at least on special character.")


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember Me")
    recaptcha = RecaptchaField()
    submit = SubmitField("Login")


class UpdateAccountForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    picture = FileField(
        "Update Profile Picture", validators=[FileAllowed(["jpg", "png", "jpeg"])]
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


class PostForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    content = TextAreaField("Content", validators=[DataRequired()])
    font = SelectField(
        "Font",
        choices=[
            ("Poppins", "Default"),
            ("Didot", "Didot"),
            ("Quicksand", "Quicksand"),
            ('"Roboto Mono"', "Monospace"),
            ("Caveat", "Cursive"),
            ("Roboto", "Roboto"),
            ("Montserrat", "Montserrat"),
            ('"Balsamiq Sans", sans-serif', "Balsamiq Sans"),
            ("Lobster", "Lobster"),
        ],
    )
    font_color = SelectField(
        "Font Colour",
        choices=[
            ("#ffffff", "Default"),
            ("rgb(255, 2, 2)", "Red"),
            ("#3197ff", "Blue"),
            ("rgb(255, 209, 2)", "Yellow"),
            ("rgb(45, 126, 7)", "Green"),
        ],
    )
    submit = SubmitField("Post")


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


class VerifyPostForm(FlaskForm):
    verify = BooleanField("Verify this post?")
    save_changes = SubmitField("Save Changes")


class ConfirmDeleteForm(FlaskForm):
    confirmation_text = StringField(
        "Type in some text longer that 3 characters to confirm\
        the deletion of this post",
        validators=[InputRequired(), Length(
            min=4, message="Enter text more than 3 characters.")],
    )
    submit = SubmitField("I am sure I want to delete this post.")
