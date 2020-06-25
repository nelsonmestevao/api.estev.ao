import os

from flask import Flask
from flask_cors import CORS

from app.extensions.admin import admin
from app.extensions.database import db
from app.routes.shortener import short
import app.routes.admin


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
    admin.init_app(app)

    app.register_blueprint(short)

    return app
