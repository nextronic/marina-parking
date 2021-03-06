from app import db


class Company(db.Model):
    __tablename__ = 'company'
    id_company = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    queue = db.relationship('Queue', back_populates='company')

    def __repr__(self):
        return f'<Company {self.name}>'
