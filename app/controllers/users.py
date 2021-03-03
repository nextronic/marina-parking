from flask_login import login_required
from app import db
from ..middleware.users import UsersMiddleware
from ..models import User
from flask import render_template, jsonify


class UsersController(UsersMiddleware):
    route_base = '/user'
    decorators = [login_required]

    def index(self):
        return render_template('users.jinja2')