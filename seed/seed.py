from models.attendance_grading import *

def seed_data():
    fake = Faker()

    # create some courses first
    for _ in range(5):
        course = Course(
            name=fake.word().title(),
            duration=random.randint(1, 4)  # duration in years
        )
        db.session.add(course)
    db.session.commit()

    courses = Course.query.all()

    # add registered students
    for _ in range(10):
        student = RegisteredStudents(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            student_id=fake.unique.bothify(text="STU####"),
            course_id=random.choice(courses).id
        )
        db.session.add(student)

    # add employed lecturers
    for _ in range(5):
        lecturer = EmployedLecturers(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            nrc_number=fake.unique.numerify(text="######"),
            lecturer_id=fake.unique.bothify(text="LEC###")
        )
        # attach lecturer to 1–3 random courses
        lecturer.courses = random.sample(courses, k=random.randint(1, 3))
        db.session.add(lecturer)

    db.session.commit()
    print("✅ Fake data seeded!")
