from . import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), index=True, unique=False)
    date = db.Column(db.Date(), index=False, unique=False)
    birthday = db.Column(db.Boolean(), index=False, unique=False)
    poem = db.Column(db.Text())

    def __repr__(self):
        return '<Person {}>'.format(self.username)