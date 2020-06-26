from flask import Blueprint, request, render_template, redirect
from flask_login import login_user, logout_user, login_required

from app.extensions.login import login_manager
from app.models.user import User

auth = Blueprint('auth', __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form["username"]).first()
        if user.validate(request.form["password"]):
            login_user(user)
            return redirect("/admin/link")
        else:
            return render_template('login.html', error="Wrong password")

    return render_template('login.html')


@auth.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect("/")