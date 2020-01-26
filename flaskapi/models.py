from . import db

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), index=True, unique=False)
    lastname = db.Column(db.String(80), index=True, unique=False)
    date = db.Column(db.Date(), index=False, unique=False)
    age = db.Column(db.String(2), index=False, unique=False)
    daystobirthday = db.Column(db.String(5), index=False, unique=False)
    birthday = db.Column(db.Boolean(), index=False, unique=False)
    poem = db.Column(db.Text())

    def __repr__(self):
        return '<Person {}>'.format(self.firstname)