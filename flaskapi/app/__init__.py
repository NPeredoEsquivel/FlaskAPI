from flask import Flask, jsonify, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
import requests, json



db = SQLAlchemy()


def create_app():
    app = Flask(__name__, template_folder='templates')
    db.init_app(app)
    app.config.from_object('config.Config')

    with app.app_context():
        # Imports
        from . import routes
        from forms import PersonInfoForm

        # Create tables for our models
        db.create_all()

        return app



