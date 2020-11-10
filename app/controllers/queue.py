from flask_login import login_required
from ..middleware.queue import QueueMiddleware
from ..models import Queue, Display
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
        in_token = request.json.get("in", "")
        out_token = request.json.get("out", "")
        print(name)
        print(out_token)
        print(in_token)
        if len(positions) == 0 or name == "" or in_token == "" or out_token == "":
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
        tmp_in = Display()
        tmp_in.id_queue = tmp.id_queue
        tmp_in.serial = in_token
        tmp_in.name = f"{name} In"
        tmp_in.index = 1
        db.session.add(tmp_in)
        tmp_out = Display()
        tmp_out.id_queue = tmp.id_queue
        tmp_out.serial = out_token
        tmp_out.name = f"{name} Out"
        tmp_out.index = 2
        db.session.add(tmp_out)
        db.session.commit()
        return "ok", 200

    def delete(self, id):
        print(id)
        displays = Display.query.filter_by(id_queue=id).all()
        for display in displays:
            db.session.delete(display)
        tmp = Queue.query.filter_by(id_queue=id).first()
        db.session.delete(tmp)
        db.session.commit()
        return id, 204