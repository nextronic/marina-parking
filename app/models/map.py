from app import db


class Map(db.Model):
    __tablename__ = 'map'
    id_map = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    width = db.Column(db.Integer, nullable=False)
    height = db.Column(db.Integer, nullable=False)
    path = db.Column(db.String(255), nullable=False)
