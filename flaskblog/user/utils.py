import os
from secrets import token_hex
from PIL import Image
from flask import url_for
from flask_mail import Message
from flaskblog import mail
from flask import current_app


def save_picture(form_picture):
    random_hex = token_hex(16)
    _, f_extn = os.path.splitext(form_picture.filename)
    picture_filename = random_hex + f_extn
    picture_path = os.path.join(
        current_app.root_path, "static/profile_pics", picture_filename)

    final_size = (200, 200)
    image = Image.open(form_picture)
    image.thumbnail(final_size)
    image.save(picture_path)

    return picture_filename


def send_reset_confirmation(user):
    msg = Message(
        "Password Reset Confirmation", sender="noreply@demo.com", recipients=[user.email]
    )

    msg.html = """
    <h1 style="font-family: Poppins;text-align: center; ">
Password Reset | FlaskBlog </h1>
<p style="text-align: center; font-family: Poppins;
font-size: larger;">
    You have reset your FlaskBlog password successfully.
</p>
"""
    mail.send(msg)


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message(
        "Password Reset Request", sender="noreply@demo.com", recipients=[user.email]
    )

    msg.html = f"""
    <h1 style="font-family: Poppins;text-align: center; ">
Password Reset | FlaskBlog </h1>
<p style="text-align: center; font-family: Poppins;
font-size: larger;">
Looks like you've forgotten your password.
Don't worry! It happens to everyone.
Reset it by clicking on the link below.
If you did not request for this reset,
simply ignorethis email and no changes
will be made to your FlaskBlog account.
</p>

<div class="wrapper" style="text-align: center;">
<a href="{url_for('user.reset_token', token=token, _external=True)}
" style="
text-decoration: none; font-family: Poppins;
padding: 20px; background: rgb(255, 206, 92);
margin: 50px; display: block; color: black;
font-size: 1.8em;
">
Reset my Password
</a>
</div>
"""
    mail.send(msg)
