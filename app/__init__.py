"""A short and simple redirecting service"""
import os

from flask import Flask
from flask_cors import CORS

from app.extensions.admin import admin
from app.extensions.database import db
from app.extensions.database import migrate
from app.extensions.login import login_manager
from app.routes.auth import auth
from app.routes.shortener import short

import app.routes.admin
import app.routes.auth
import app.models.user

VERSION = "0.1.0"
DESCRIPTION = __doc__

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    migrate.init_app(app, db)

    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']
    admin.init_app(app)

    login_manager.init_app(app)

    app.register_blueprint(short)
    app.register_blueprint(auth)

    return app
