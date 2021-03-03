from flask_classful import route
from flask_login import login_required
from app import db
from ..middleware.detector import DetectorMiddleware
from ..models import Detector
from ..utils.mqtt import SendItem
from ..forms.detector import DetectorForm
from flask import jsonify, request


class DetectorController(DetectorMiddleware):
    route_base = '/detector'

    def post(self):
        name = request.json.get('name', '')
        serial = request.json.get('serial', '')
        x = request.json.get('x', '')
        y = request.json.get('y', '')

        if name == "" or serial == '' or x == '' or y == '':
            return jsonify(msg='error load data '), 400
        else:
            tmp = Detector()
            tmp.name = name
            tmp.serial = serial
            tmp.x = x
            tmp.y = y
            db.session.add(tmp)
            db.session.commit()
            return jsonify(detector={"id": tmp.id_detector, "name": name, "serial": serial}), 201

    def list(self):
        detectors = Detector.query.all()
        return jsonify(detectors=[{"id": detector.id_detector, "name": detector.name, "serial": detector.serial, "status": detector.status, "x": detector.x, "y": detector.y} for detector in detectors])

    def delete(self, serial):
        Detector.query.filter(Detector.serial == serial).delete()
        db.session.commit()
        return 'ok', 204

    @route('/status', methods=['post'])
    def status(self):
        print(request.json)
        return 'ok'
