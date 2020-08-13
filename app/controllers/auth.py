from flask import render_template, jsonify, request, redirect , url_for
from flask_login import current_user, login_user, login_required, logout_user

from ..middleware.auth import AuthMiddleware
from ..forms.auth import LoginForm
from app import login, db
from ..models.user import User


class AuthController(AuthMiddleware):
    route_base = "/auth"

    def index(self):
        form = LoginForm()
        return render_template('login.jinja2', form=form)

    def post(self):
        if current_user.is_authenticated:
            return redirect(url_for('index'))

        user = User.query.filter_by(username=self.form.username.data).first()
        if user is None or not user.checkPasswd(self.form.passwd.data):
            return redirect(url_for('login'))
        login_user(user, remember=self.form.remember.data)
        next_page = request.args.get('next')
        return redirect(next_page or url_for('index'))

    @login_required
    def logout(self):
        """User log-out logic."""
        logout_user()
        return redirect(url_for('AuthController:index'))

    def init(self):
        u = User()
        u.first_name = 'yassine'
        u.last_name = 'ouarrak'
        u.password = 'admin'
        u.username = 'admin'
        db.session.add(u)
        db.session.commit()
        return 'ok'


@login.user_loader
def load_user(user_id):
    if user_id is not None:
        return User.query.get(user_id)
    return None
