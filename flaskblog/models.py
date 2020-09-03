from datetime import datetime
from flaskblog import db, login_manager, app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    liked_posts = db.Column(db.Text, default="No,posts,liked")

    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return F"[USER] {self.id} {self.username} --- {self.email} --- {self.image_file} "


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    is_verified = db.Column(db.Boolean, default=False)
    views = db.Column(db.Integer, default=0)
    font = db.Column(db.String(30), default="Poppins")
    font_color = db.Column(db.String(20), default="#fff")
    likes = db.Column(db.Integer, default=0)

    # replies = db.relationship('Reply', backref="main_post", lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return F"[POST] {self.id} posted {self.title} on {self.date_posted}\t VALIDATED={self.is_verified}"


class Reply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
                     nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'),
                        nullable=False)

    def __repr__(self):
        return f"[REPLY] {self.id}) | {self.title}"
