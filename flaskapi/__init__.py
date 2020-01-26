from flask import Flask, jsonify, render_template, redirect, url_for, request
from flask_static_compress import FlaskStaticCompress
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from .config import Config
import requests, json

db = SQLAlchemy()


def create_app():
    app = Flask(__name__, static_folder="static", template_folder='templates')

    app.config.from_object(Config)
    db.init_app(app)
    migrate = Migrate(app, db)

    app.config['COMPRESSOR_DEBUG'] = app.config.get('DEBUG')
    app.config['COMPRESSOR_STATIC_PREFIX'] = 'static'
    app.config['COMPRESSOR_OUTPUT_DIR'] = 'build'
    app.static_folder = 'static'
    compress = FlaskStaticCompress(app)

    with app.app_context():
        # Imports
        from . import routes

        # Create tables for our models
        db.create_all()

        return app



