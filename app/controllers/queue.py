from flask_login import login_required
from ..middleware.queue import QueueMiddleware
from ..models.queue import Queue
from app import db
from flask import jsonify, request


class QueueController(QueueMiddleware):
    route_base = '/queue'
    trailing_slash = False
    decorators = [login_required]

    def index(self):
        tmp = Queue.query.all()
        return jsonify(queues=[i.serialize for i in tmp])

    def post(self):
        positions = request.json.get("infos", [])
        name = request.json.get("name", "")
        if len(positions) == 0 or name == "":
            return "", 401
        tmp = Queue()
        tmp.name = name
        tmp.p1_x = positions[0][0]["lat"]
        tmp.p1_y = positions[0][0]["lng"]
        tmp.p2_x = positions[0][1]["lat"]
        tmp.p2_y = positions[0][1]["lng"]
        tmp.p3_x = positions[0][2]["lat"]
        tmp.p3_y = positions[0][2]["lng"]
        tmp.p4_x = positions[0][3]["lat"]
        tmp.p4_y = positions[0][3]["lng"]
        tmp.index = 1
        tmp.id_company = 0
        db.session.add(tmp)
        db.session.commit()

        return "ok", 200

    def delete(self, id):
        tmp = Queue.query.filter_by(id_queue=id).first()
        db.session.delete(tmp)
        db.session.commit()
        return id, 204