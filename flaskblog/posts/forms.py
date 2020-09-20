from wtforms.validators import DataRequired, Length, InputRequired
from flask_wtf import FlaskForm
from wtforms import (
    StringField, SubmitField, BooleanField,
    SelectField, RadioField, TextAreaField)


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
