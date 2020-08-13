from flask_login import UserMixin
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    passwd = db.Column(db.String(250))
    status = db.Column(db.Boolean, default=True)
    type = db.Column(db.Integer, default=1)
    username = db.Column(db.String, nullable=False, unique=True)

    @property
    def password(self):
        return self.passwd

    @password.setter
    def password(self, val):
        self.passwd = generate_password_hash(val)

    def checkPasswd(self, password):
        return check_password_hash(self.passwd, password)

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'
