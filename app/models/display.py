from app import db


class Display(db.Model):
    __tablename__ = 'display'

    id_display = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    serial = db.Column(db.String(15), unique=True, nullable=False)
    status = db.Column(db.Integer, default=1)
    index = db.Column(db.Integer, default=1, nullable=False)
    id_queue = db.Column(db.Integer, db.ForeignKey('queue.id_queue'), nullable=False)

    def __repr__(self):
        return f'<Display {self.name} , N° {self.serial}>'
