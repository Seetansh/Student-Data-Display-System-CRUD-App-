from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def __repr__(self):
        return f'<User {self.username}>'

    @staticmethod
    def hash_text(text):
        hashed_text = generate_password_hash(text)
        return hashed_text

    @staticmethod
    def check_hash(hashed_text, text):
        return check_password_hash(hashed_text, text)

    
