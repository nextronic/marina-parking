from app import db
from .display import Display
from .detector import Detector
from .company import Company


class Queue(db.Model):
    __tablename__ = 'queue'
    id_queue = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    color = db.Column(db.String(7), nullable=False, default='#1919FF')
    order = db.Column(db.Integer, nullable=False, default=0)
    p1_x = db.Column(db.Integer, nullable=False)
    p1_y = db.Column(db.Integer, nullable=False)
    p2_x = db.Column(db.Integer, nullable=False)
    p2_y = db.Column(db.Integer, nullable=False)
    p3_x = db.Column(db.Integer, nullable=False)
    p3_y = db.Column(db.Integer, nullable=False)
    p4_x = db.Column(db.Integer, nullable=False)
    p4_y = db.Column(db.Integer, nullable=False)
    id_company = db.Column(db.Integer, db.ForeignKey('company.id_company'), nullable=False)
    status = db.Column(db.Integer, default=1)

    display = db.relationship('Display', backref='queue', lazy=True)
    detector = db.relationship('Detector', backref='queue', lazy=True)
    company = db.relationship("Company", back_populates="queue")

    def __repr__(self):
        return f'<Queue {self.name} , N° {self.index}>'

    @property
    def serialize(self):
        return {
            "id": self.id_queue,
            "name": self.name,
            "p1_x": self.p1_x,
            "p1_y": self.p1_y,
            "p2_x": self.p2_x,
            "p2_y": self.p2_y,
            "p3_x": self.p3_x,
            "p3_y": self.p3_y,
            "p4_x": self.p4_x,
            "p4_y": self.p4_y,
            "company": self.company.name
        }