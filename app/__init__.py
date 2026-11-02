from flask import Flask
from config import DevelopmentConfig, ProductionConfig
from app.routes import main_bp

def create_app():
    app = Flask(__name__)

    # loading configurations
    app.config.from_object(DevelopmentConfig)

    app.register_blueprint(main_bp)

    return app