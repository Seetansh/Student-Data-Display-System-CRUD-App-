from werkzeug.security import generate_password_hash, check_password_hash

def hash_text(text):
    hashed_text = generate_password_hash(text)
    return hashed_text

def check_hash(text, hashed_text):
    return check_password_hash(hashed_text, text)