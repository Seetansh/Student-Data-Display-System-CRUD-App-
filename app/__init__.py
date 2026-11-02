from flask import Flask
from config import DevelopmentConfig, ProductionConfig
from app.routes import main_bp, auth_bp, user_bp
from app.extensions import db, migrate

def create_app():
    app = Flask(__name__)

    # loading configurations
    app.config.from_object(DevelopmentConfig)
    db.init_app(app)

    from app.models import Students, Subjects, Classes, StudentSubjects
    migrate.init_app(app, db)

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(user_bp, url_prefix="/user")
    
    return app