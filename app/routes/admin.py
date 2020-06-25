from flask_admin.contrib.sqla import ModelView
from flask_login import current_user

from app.extensions.admin import admin
from app.extensions.database import db
from app.models.link import Link
from app.models.user import User


class AdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


admin.add_view(AdminModelView(Link, db.session))
admin.add_view(AdminModelView(User, db.session))
