from typing import Any
from app import db
from .brand import brands_manufacturers

class Manufacturer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    country = db.Column(db.String(100))
    certificates = db.Column(db.Text)
    internal_id = db.Column(db.String(50), unique=True)
    brands = db.relationship('Brand', secondary=brands_manufacturers, 
                             back_populates='manufacturers', lazy='joined')

    def to_dict(self) -> dict[str, Any]:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'country': self.country,
            'certificates': self.certificates,
            'internal_id': self.internal_id,
            'brands': [{'id': b.id, 'name': b.name} for b in self.brands]
        }
