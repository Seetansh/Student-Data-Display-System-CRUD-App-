from app.extensions import db

class Students(db.Model):
    __tablename__ = 'students'

    std_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), unique=False, nullable=False)
    fees_paid = db.Column(db.Boolean, default=False)
    bio = db.Column(db.Text, nullable=True)
    interests = db.Column(db.Text, nullable=True)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.class_id'), nullable=False)
    student_class = db.relationship('Classes', back_populates='students')
    std_subjects = db.relationship(
        'StudentSubjects',
        back_populates='student',
        cascade='all, delete-orphan',
    )

    def __init__(
        self,
        name,
        email,
        phone,
        fees_paid=False,
        bio=None,
        interests=None,
        class_id=None,
    ):
        self.name = name
        self.email = email
        self.phone = phone
        self.fees_paid = fees_paid
        self.bio = bio
        self.interests = interests
        self.class_id = class_id

    def __repr__(self):
        return f'<Student {self.name}>'
    