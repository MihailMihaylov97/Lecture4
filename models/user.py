from ext import db

class UserModel(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String, unique=True)
    password=db.Column(db.String)
    