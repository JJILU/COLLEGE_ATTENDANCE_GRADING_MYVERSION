from extensions import db

class Lecturer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Lecturer_id = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(50), nullable=False)
   


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(50), nullable=False)


# class ValidLecturer(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     Lecturer_id = db.Column(db.String(10), nullable=False)
#     password = db.Column(db.String(50), nullable=False)       

# class ValidStudent(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     Lecturer_id = db.Column(db.String(10), nullable=False)
#     password = db.Column(db.String(50), nullable=False)           