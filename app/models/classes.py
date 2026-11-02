from app.extensions import db

class Classes(db.Model):
    __tablename__ = 'classes'
    class_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    class_name = db.Column(db.String(100), unique=True, nullable=False)
    students = db.relationship('Students', back_populates='student_class', lazy=True)

    def __init__(self, class_name):
        self.class_name = class_name

    def __repr__(self):
        return f'<Class {self.class_name}>'