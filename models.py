from app import db


class Contact(db.Model):
    __tablename__ = 'contact'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    gender = db.Column(db.String(3))
    address = db.Column(db.Text())
    email = db.Column(db.String(100), unique=True)
    age = db.Column(db.Integer())
    language = db.Column(db.String(10))