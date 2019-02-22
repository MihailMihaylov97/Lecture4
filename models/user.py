from ext import db

class UserModel(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String, unique=True)
    password=db.Column(db.String)
    

    def create_new(self):
        db.session.add(self)
        db.session.commit()

    def get_user(self, username):
        db.session.filter_by(username=username).first()