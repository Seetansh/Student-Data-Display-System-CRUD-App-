from app.extensions import db

class Subjects(db.Model):
    __tablename__ = 'subjects'
    sub_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sub_name = db.Column(db.String(100), nullable=False)
    student_enrollments = db.relationship(
        'StudentSubjects',
        back_populates='subject',
        cascade='all, delete-orphan',
    )

    def __init__(self, sub_name):
        self.sub_name = sub_name

    def __repr__(self):
        return f'<Subject {self.sub_name}>'
