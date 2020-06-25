from flask_admin.contrib.sqla import ModelView

from app.extensions.admin import admin
from app.extensions.database import db
from app.models.link import Link

admin.add_view(ModelView(Link, db.session))
