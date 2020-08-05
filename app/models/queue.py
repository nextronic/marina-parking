from app import db


class Queue(db.Model):
    __tablename__ = 'queue'
    id_queue = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    color = db.Column(db.String(7), nullable=False, default='#1919FF')
    index = db.Column(db.Integer, unique=True, nullable=False)
    p1_x = db.Column(db.Integer, nullable=False)
    p1_y = db.Column(db.Integer, nullable=False)
    p2_x = db.Column(db.Integer, nullable=False)
    p2_y = db.Column(db.Integer, nullable=False)
    p3_x = db.Column(db.Integer, nullable=False)
    p3_y = db.Column(db.Integer, nullable=False)
    p4_x = db.Column(db.Integer, nullable=False)
    p4_y = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, default=1)

    display = db.relationship('Display', backref='queue', lazy=True)
    detector = db.relationship('Detector', backref='queue', lazy=True)

    def __repr__(self):
        return f'<Queue {self.name} , N° {self.index}>'
