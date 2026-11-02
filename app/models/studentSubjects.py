
from app.extensions import db

# enrollment table to link students and subjects
class StudentSubjects(db.Model):
    __tablename__ = 'student_subjects'
    # this prevents duplicate entries for the same student and subject combination
    __table_args__ = (
        db.UniqueConstraint('student_id', 'subject_id', name='uq_student_subject'),
    )

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, db.ForeignKey('students.std_id'), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.sub_id'), nullable=False)
    student = db.relationship('Students', back_populates='std_subjects')
    subject = db.relationship('Subjects', back_populates='student_enrollments')

    def __init__(self, student_id, subject_id):
        self.student_id = student_id
        self.subject_id = subject_id

    def __repr__(self):
        return f'<StudentSubjects {self.student_id} - {self.subject_id}>'