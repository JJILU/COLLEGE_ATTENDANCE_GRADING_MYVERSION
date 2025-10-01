from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# --- Association Tables ---
date_class = db.Table(
    "date_class",
    db.Column("date_id", db.Integer, db.ForeignKey("date.id")),
    db.Column("class_id", db.Integer, db.ForeignKey("class.id"))
)

student_class = db.Table(
    "student_class",
    db.Column("student_id", db.Integer, db.ForeignKey("student.id")),
    db.Column("class_id", db.Integer, db.ForeignKey("class.id"))
)

exam_grade = db.Table(
    "exam_grade",
    db.Column("exam_id", db.Integer, db.ForeignKey("exam.id")),
    db.Column("grade_id", db.Integer, db.ForeignKey("student_grades.id"))
)


# --- MODELS ---
class Date(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    month = db.Column(db.String(20))
    year = db.Column(db.Integer)
    classes = db.relationship("Class", secondary=date_class, backref="dates")


class Class(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    lecturer = db.Column(db.String(50))
    class_start_time = db.Column(db.Time)
    class_end_time = db.Column(db.Time)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(20), unique=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    semester = db.Column(db.Integer)

    # relation with course
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"))

    classes = db.relationship("Class", secondary=student_class, backref="students")
    attendances = db.relationship("StudentAttendance", backref="student")
    grades = db.relationship("StudentGrades", backref="student")


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    duration = db.Column(db.Integer)
    present_year = db.Column(db.Integer, default=datetime.now().year)

    students = db.relationship("Student", backref="course")


class StudentAttendance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    student_attendance = db.Column(db.Boolean)


class StudentGrades(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey("student.id"))
    student_grade = db.Column(db.Boolean)

    exams = db.relationship("Exam", secondary=exam_grade, backref="grades")


class Exam(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    exam_name = db.Column(db.String(50))
    exam_start_time = db.Column(db.Time)
    exam_end_time = db.Column(db.Time)
    passing_mark = db.Column(db.Integer)

    # one-to-many with Date
    date_id = db.Column(db.Integer, db.ForeignKey("date.id"))
    date = db.relationship("Date", backref="exams")
