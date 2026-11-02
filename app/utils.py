



def save_to_db(instance):
    from app import db
    db.session.add(instance)
    db.session.commit()
