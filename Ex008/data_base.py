from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Base(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False) 
    password = db.Column(db.String(1000), nullable=False)
