from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False) 
    sex = db.Column(db.String(1), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    id_faculty = db.Column(db.Integer, db.ForeignKey('faculty.id'),nullable=False)

    def __repr__(self):
        return f'Student({self.name}, {self.last_name}, {self.sex}, {self.group}, {self.id_faculty})'


class Faculty(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    faculty_name = db.Column(db.String(100), nullable=False)


    def __repr__(self):
        return f'Student({self.faculty_name})'