from typing import Any
from app.extensions import db

brands_manufacturers = db.Table('brands_manufacturers',
    # `internal_id` is a String on both tables; the join table must match.
    db.Column(
        'brand_internal_id',
        db.String(50),
        db.ForeignKey('brand.internal_id'),
        primary_key=True,
    ),
    db.Column(
        'manufacturer_internal_id',
        db.String(50),
        db.ForeignKey('manufacturer.internal_id'),
        primary_key=True,
    ),
)

class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    logo = db.Column(db.String(200))
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    internal_id = db.Column(db.String(50), unique=True)
    manufacturers = db.relationship('Manufacturer', secondary=brands_manufacturers, 
                                    back_populates='brands', lazy='joined')

    def to_dict(self) -> dict[str, Any]:
        return {
            'id': self.id,
            'logo': self.logo,
            'name': self.name,
            'description': self.description,
            'internal_id': self.internal_id,
            'manufacturers': [{'id': m.id, 'name': m.name} for m in self.manufacturers]
        }

    def __repr__(self) -> str:
        return f"<Brand id={self.id} internal_id={self.internal_id!r} name={self.name!r}>"
