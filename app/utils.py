from app.models import Users

def check_user_exists(email):
    return Users.query.filter_by(email=email).first() is not None

def save_to_db(instance):
    from app import db
    db.session.add(instance)
    db.session.commit()
