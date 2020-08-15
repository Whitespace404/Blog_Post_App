import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = 'opr4o0r23jk3423f04h02in2q99lzqf1gp0-0ahld23s05bdqm0oir'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config["MAIL_SERVER"] = 'smtp.gmail.com'
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "enter your email id here"
app.config["MAIL_PASSWORD"] = os.environ.get('EMAIL_PWD')


db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
mail = Mail(app)

login_manager.login_view = 'login'
login_manager.login_message_category = 'danger'

from flaskblog import routes
