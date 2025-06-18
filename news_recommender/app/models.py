from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.dialects.postgresql import ARRAY, TIMESTAMP

class User(db.Model):
    __tablename__ = "users"
    id        = db.Column(db.Integer, primary_key=True)
    username  = db.Column(db.String(80), unique=True, nullable=False)
    email     = db.Column(db.String(120), unique=True, nullable=False)
    pw_hash   = db.Column(db.String(1024), nullable=False)

    def set_password(self, pwd):
        self.pw_hash = generate_password_hash(pwd)

    def check_password(self, pwd):
        return check_password_hash(self.pw_hash, pwd)

class Like(db.Model):
    __tablename__ = 'likes'
    id      = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    news_id = db.Column(db.Integer)

class News(db.Model):
    __tablename__ = 'articles'
    id           = db.Column(db.Integer, primary_key=True)
    title        = db.Column(db.String, nullable=False)
    description  = db.Column(db.Text, nullable=False)
    published_at = db.Column(TIMESTAMP)
    category     = db.Column(db.String, nullable=False)
