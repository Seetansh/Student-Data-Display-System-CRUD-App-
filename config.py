import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    HOST = os.getenv("HOST", "localhost")

    PORT = int(os.getenv("PORT", 5000))

    DEBUG = os.getenv("DEBUG", "True") == "True"

    SECRET_KEY = os.getenv("SECRET_KEY", "your secret_key_here")

    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI", "default_database_uri_here")

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

class TestingConfig(Config):
    DEBUG = True
    TESTING = True