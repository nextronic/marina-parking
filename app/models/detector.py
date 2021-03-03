from app import db


class Detector(db.Model):
    __tablename__ = 'detector'
    id_detector = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    serial = db.Column(db.String(15), unique=True, nullable=False)
    x = db.Column(db.Integer, nullable=False)
    y = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, default=1)
    last_event = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Detector {self.name} , N° {self.serial}>'
