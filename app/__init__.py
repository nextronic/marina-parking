from flask import Flask, render_template, request
from flask_login import LoginManager
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from json import loads


app = Flask(__name__)
login = LoginManager()
db = SQLAlchemy()
socket = SocketIO()


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.jinja2'), 404


@app.route('/events', methods=['get', 'post'])
def events():
    print(request.json)
    return 'ok', 200



@app.route('/test', methods=['GET', 'POST'])
def test():
    data = request.json.get('objectJSON', None)
    if data is not None:
        print(data[''])
        data = loads(data) if type(data) == str else data
        socket.emit('detector', {"detector": data['id'], "status": ("1" if data['magnetic'] > 200 else "0")})

    return 'ok'


def create_app():
    app.config.from_object('config.Config')
    db.init_app(app)
    login.init_app(app)
    login.login_view = "AuthController:index"
    socket.init_app(app)
    # import Auth controller
    from app.controllers import AuthController
    AuthController.register(app)

    from app.controllers import DeviceController
    DeviceController.register(app)

    from app.controllers import MapController
    MapController.register(app)

    from app.controllers import QueueController
    QueueController.register(app)

    from app.controllers import UsersController
    UsersController.register(app)

    from app.controllers import DetectorController
    DetectorController.register(app)

    from app.utils.mqtt import loop, sender
    loop.start()
    sender.start()
    with app.app_context():
        from app.models.user import User
        db.create_all()
