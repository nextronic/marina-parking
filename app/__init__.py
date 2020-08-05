from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
login = LoginManager()
db = SQLAlchemy()


def create_app():
    app.config.from_object('config.Config')
    db.init_app(app)
    login.init_app(app)
    with app.app_context():
        from app.models.company import Company
        from app.models.display import Display
        from app.models.detector import Detector
        from app.models.queue import Queue
        from app.models.map import Map
        db.create_all()