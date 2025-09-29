from flask import Flask,redirect,request,render_template, session, url_for
from extensions import db, migrate


app = Flask(__name__, template_folder="templates")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///auth.sqlite3"

# init extensions
db.init_app(app)
migrate.init_app(app,db)

# make app aware of models
# from models import User,Profile


@app.route("/") 
def home():
    if 'username' in session:
        return render_template('Dashboard/dashbaord.html')
    return render_template('landing_page.html')

# Lecturer Auth End-points
@app.route("/lecturer_register", methods=["GET","POST"]) 
def lecturer_register():
    if request.method == "GET":
        return render_template('auth/lecturer_auth.html')

    valid_lecturer_id = ["L1001","L1002","L1003","L1004","L1005"]

    # extract auth credentials

    auth_creds =  request.form

    lecture_id = auth_creds.get("lecturerid","").strip()
    password = auth_creds.get("password","").strip()

    # check if auth credentials was submitted 
    if not lecture_id and not password :
        return render_template('auth/lecturer_auth.html', error="Lecturer ID and password are required!"), 400
    

    # check for individual missing fields
    missing_fields = []
    
     # handle missing or empty lecturerid
    if not auth_creds["lecturerid"] and auth_creds["lecturerid"].strip() == "":
        missing_fields.append("lecturer id is a required!")

    # handle missing or empty password
    if not auth_creds["password"] and auth_creds["password"].strip() == "":
        missing_fields.append("password id is a required!")    


    if missing_fields:
        return render_template('auth/lecturer_auth.html', missing_fields=missing_fields), 400

    return "registered as lecturer"


@app.route("/lecturer_login") 
def lecturer_login():
    return "logged as lecturer"



# Student Auth End-points
@app.route("/student_register") 
def student_register():
    return "registered as student"



@app.route("/student_login") 
def student_login():
    return "registered as student"


# Logout Enpoint
@app.route("/logout") 
def  logout():
    return "logged out"


# Dashboard
@app.route("/dashboard") 
def dasboard():
    if "username" in session:
        return render_template('Dashboard/dashbaord.html')
    return redirect(url_for(''))
