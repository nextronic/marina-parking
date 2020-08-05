from app import db


class Display(db.Model):
    __tablename__ = 'display'
    id_display = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    serial = db.Column(db.String(15), unique=True, nullable=False)
    ip = db.Column(db.String(15), unique=True, nullable=False)
    x = db.Column(db.Integer, nullable=False)
    y = db.Column(db.Integer, nullable=False)
    status = db.Column(db.Integer, default=1)
    id_queue = db.Column(db.Integer, db.ForeignKey('queue.id_queue'), nullable=False)

    def __repr__(self):
        return f'<Display {self.name} , N° {self.serial}>'
