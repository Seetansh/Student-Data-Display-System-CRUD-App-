from flask import Flask
from config import DevelopmentConfig, ProductionConfig

def create_app():
    app = Flask(__name__)

    # loading configurations
    app.config.from_object(DevelopmentConfig)

    return app