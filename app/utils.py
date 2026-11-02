from werkzeug.security import generate_password_hash, check_password_hash

def hash_text(text):
    hashed_text = generate_password_hash(text)
    return hashed_text

def check_hash(hashed_text, text):
    return check_password_hash(hashed_text, text)

def save_to_db(instance):
    from app import db
    db.session.add(instance)
    db.session.commit()
