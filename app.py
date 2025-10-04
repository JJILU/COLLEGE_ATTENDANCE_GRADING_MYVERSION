from flask import Flask, redirect, request, render_template, session, url_for
from extensions import db, migrate
# make app aware of models
from models import Lecturer,Student
from config import Config


app = Flask(__name__, template_folder="templates")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///auth.sqlite3"
app.config["SECRET_KEY"] = Config.SECRET_KEY

# init extensions
db.init_app(app)
migrate.init_app(app, db)




@app.route("/")
def home():
    if 'lecturer_id' in session:
        return redirect(url_for('dasboard'))
    return render_template('landing_page.html')

# Lecturer Auth End-points


@app.route("/lecturer_register", methods=["GET", "POST"])
def lecturer_register():
    if request.method == "GET":
        return render_template('auth/lecturer_auth.html')

    valid_lecturer_id = ["L1001", "L1002", "L1003", "L1004", "L1005"]

    # extract auth credentials

    auth_creds = request.form

    lecture_id = auth_creds.get("lecturerid", "").strip()
    password = auth_creds.get("password", "").strip()

    # check if auth credentials was submitted
    if not lecture_id and not password:
        return render_template('auth/lecturer_auth.html', error="Lecturer ID and password are required!"), 400

    # check for individual missing fields
    missing_fields = []

    # handle missing or empty lecturerid
    if not auth_creds["lecturerid"] or auth_creds["lecturerid"].strip() == "":
        missing_fields.append("lecturer id is a required!")

    # handle missing or empty password
    if not auth_creds["password"] or auth_creds["password"].strip() == "":
        missing_fields.append("password id is a required!")

    if missing_fields:
        return render_template('auth/lecturer_auth.html', missing_fields=missing_fields), 400
    
    # check if lecturer id is valid
    if lecture_id not in valid_lecturer_id:
        return render_template('auth/lecturer_auth.html', error="Invalid Lecturer id"), 400
    
    # check is lecturer already has an account
    new_lecturer = Lecturer.query.filter_by(lecturer_id=lecture_id).first()

    if new_lecturer:
        return render_template('auth/lecturer_auth.html', error=f"Lecturer with id {lecture_id} already exists"), 400

    # lecturer does not exist, attempet create account and redirect to dashboard
    try:
       # create new lecturer account 
        new_lecturer  = Lecturer(lecturer_id=lecture_id)
        new_lecturer.hash_password(password)

        # save lecturer to table
        new_lecturer.save()    

        # create new session for the lecturer
        session["lecturer_id"] = lecture_id

        # redirect user to dashboard
        return redirect(url_for('dasboard'))
    except Exception as e:
        db.session.rollback()
        print("Lecturer account could not be created due to following error: ", e)
        return render_template('auth/lecturer_auth.html', error=f"An error occured,account could not be created"), 500


    


@app.route("/lecturer_login", methods=["GET", "POST"])
def lecturer_login():
    return "logged as lecturer"


# Student Auth End-points
@app.route("/student_register", methods=["GET", "POST"])
def student_register():
    return render_template("auth/student_auth.html")


@app.route("/student_login", methods=["GET", "POST"])
def student_login():
    return render_template("auth/student_auth.html")


# Logout Enpoint
@app.route("/logout", methods=["GET"])
def logout():
    session.pop("lecturer_id",None)
    return redirect(url_for('home'))


# Dashboard
@app.route("/dashboard")
def dasboard():
    if "lecturer_id" in session:
        return render_template('Dashboard/dashbaord.html', username=session["lecturer_id"])
    return redirect(url_for('home'))
