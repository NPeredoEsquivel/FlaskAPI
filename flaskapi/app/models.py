from . import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), index=True, unique=False)
    datetime = db.Column(db.DateTime(), index=False, unique=False)
    birthday = db.Column(db.Boolean(), index=False, unique=False)
    poem = db.Column(db.Text())

    def __repr__(self):
        return '<Person {}>'.format(self.username)