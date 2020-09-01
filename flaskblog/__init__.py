import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

# Configurations
app = Flask(__name__)
app.config['SECRET_KEY'] = '352afd99251a17dd386ccab7410aa6684431b46cdfa98ba6a25cb24a4cd3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('EMAIL_ID')
app.config["MAIL_PASSWORD"] = os.environ.get('EMAIL_PWD')

app.config['RECAPTCHA_PUBLIC_KEY'] = '6Leki68ZAAAAAAblHuBeK2IdglQvnK8aVuWSqc9x'
app.config['RECAPTCHA_PRIVATE_KEY'] = '6Leki68ZAAAAAL2YM69Aby_XaSj3REMsxJxo0sv7'
app.config["RECAPTCHA_DATA_ATTRS"] = {'theme': 'dark'}
app.config["TESTING"] = True

# Instances
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
mail = Mail(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'danger'

from flaskblog import routes
