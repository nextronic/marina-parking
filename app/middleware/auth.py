from flask_classful import FlaskView
from ..forms.auth import LoginForm
from flask import redirect, render_template


class AuthMiddleware(FlaskView):
    def __init__(self):
        self.form = None

    def before_post(self):
        self.form = LoginForm()
        if not self.form.validate_on_submit():
            return render_template('login.jinja2', title='Sign In', form=self.form)

    def before_get(self):
        pass
