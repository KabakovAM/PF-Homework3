from flask import Flask, render_template
from students import db, Student, Faculty

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
db.init_app(app)


@app.cli.command("init-db")
def init_db():
    db.create_all()
    print("OK")


@app.cli.command("fill-db")
def fill_tables():
    count = 5
    for faculty in range(1, count + 1):
        new_faculty = Faculty(faculty_name=f"faculty_name{faculty}")
        db.session.add(new_faculty)
    db.session.commit()
    for student in range(1, count**2):
        new_student = Student(
            name=f"name{student}",
            last_name=f"lastname{student}",
            age=student,
            sex="M/F",
            group=f"group{student}",
            id_faculty=student % count + 1,
        )
        db.session.add(new_student)
    db.session.commit()

@app.route('/students/')
def all_students():
    students = Student.query.all()
    context = {'students':students}
    return render_template('students.html', **context)

if __name__ == "__main__":
    app.run(debug=True)
