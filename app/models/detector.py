from app import db


class Detector(db.Model):
    __tablename__ = 'detector'
    id_detector = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    serial = db.Column(db.String(15), unique=True, nullable=False)
    index = db.Column(db.Integer, nullable=False, default=1)
    x = db.Column(db.Integer, nullable=False)
    y = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, default=1)
    id_queue = db.Column(db.Integer, db.ForeignKey('queue.id_queue'), nullable=False)

    def __repr__(self):
        return f'<Detector {self.name} , N° {self.serial}>'
