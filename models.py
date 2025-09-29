from extensions import db
from werkzeug.security import generate_password_hash,check_password_hash

class Lecturer(db.Model):

    __tablename__ = "lecturer"


    id = db.Column(db.Integer, primary_key=True)
    lecturer_id = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(50))

    # method to hash password when user registers
    def hash_password(self,password):
        self.password = generate_password_hash(password)

    # check if password matches hashed password
    def check_password(self,password):
        return check_password_hash(self.password,password)
    
    # save lecturer to table
    def save(self):
        db.session.add(self)
        db.session.commit()






class Student(db.Model):

    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(10), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    
    # method to hash student password when registering 
    def hash_password(self,password):
        self.password = generate_password_hash(password)

    # check if password matches hashed password
    def check_password(self,password):
        return check_password_hash(self.password,password)
    
    # save student to table
    def save(self):
        db.session.add(self)
        db.session.commit()



# class ValidLecturer(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     Lecturer_id = db.Column(db.String(10), nullable=False)
#     password = db.Column(db.String(50), nullable=False)       

# class ValidStudent(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     Lecturer_id = db.Column(db.String(10), nullable=False)
#     password = db.Column(db.String(50), nullable=False)           