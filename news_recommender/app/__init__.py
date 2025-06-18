from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    CORS(app)

    with app.app_context():
        from .models import User, Like, News  # register models
        db.create_all()

        from .routes import auth_bp
        app.register_blueprint(auth_bp)

    return app