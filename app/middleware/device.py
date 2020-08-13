from flask_classful import FlaskView
from ..forms.device import DeviceForm
from ..models.company import Company
from ..models.queue import Queue
from flask import jsonify, request


class DeviceMiddleware(FlaskView):
    def __init__(self):
        self.form = None
        self.companies = None
        self.queue = None

    def before_request(self, name):
        self.companies = Company.query.all()
        self.form = DeviceForm(_companies=self.companies)

    def before_post(self):
        self.form = DeviceForm(request.form, _companies=self.companies)
        if not self.form.validate_on_submit():
            return jsonify(self.form.errors), 400
        queue = Queue.query.filter_by(id_queue=self.form.iid.data).first()
        if queue is None:
            return '', 404
        self.queue = queue

    def before_get(self):
        pass
