import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("USER_DB_URI", "sqlite:///user_fallback.db")

    SQLALCHEMY_BINDS = {
        'articles': os.getenv("NEWS_DB_URI", "sqlite:///news_fallback.db")
    }

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "defaultsecret")