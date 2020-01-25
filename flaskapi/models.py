from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), index=True, unique=False)
    datetime = db.Column(db.DateTime(), index=False, unique=False)
    birthday = db.Column(db.Boolean(), index=False, unique=False)
    poem = db.column(db.Text(), index=False, unique=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)