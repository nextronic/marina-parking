from flask_login import login_required
from app import db
from ..middleware.device import DeviceMiddleware
from ..models import Company, Queue
from ..utils.mqtt import SendItem
from ..forms.device import DeviceForm
from flask import render_template, jsonify


class DeviceController(DeviceMiddleware):
    route_base = '/device'
    decorators = [login_required]

    def index(self):
        queues = Queue.query.all()
        return render_template('devices.jinja2', queues=queues, companies=self.companies, form=self.form)

    def post(self):
        self.queue.order = self.form.order.data
        self.queue.status = self.form.direction.data
        print(self.queue.status)
        if self.form.company.data == -1:
            tmp = Company()
            tmp.name = self.form.name.data
            db.session.add(tmp)
            db.session.commit()
            self.queue.id_company = tmp.id_company
        else:
            self.queue.id_company = self.form.company.data
        db.session.commit()
        SendItem(self.queue)
        return jsonify(queue={"id": self.queue.id_queue, "company": self.queue.company.name, "direction": self.queue.status, "order": self.queue.order}), 201

    def list(self):
        queues = Queue.query.all()
        return jsonify(queues=[{"id": queue.id_queue, "company": queue.company.name, "name": queue.name, "color": queue.color, "index": queue.index, "points": [(queue.p1_x, queue.p1_y), (queue.p2_x, queue.p2_y), (queue.p3_x, queue.p3_y), (queue.p4_x, queue.p4_y)]} for queue in queues])
