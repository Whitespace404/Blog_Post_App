import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
mail = Mail()


login_manager.login_view = "user.login"
login_manager.login_message_category = "danger"


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.main.routes import main
    from flaskblog.posts.routes import posts
    from flaskblog.user.routes import user

    app.register_blueprint(user)
    app.register_blueprint(posts)
    app.register_blueprint(main)

    return app
