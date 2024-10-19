from typing import Any, List
from app import db
from app.models.brand import Brand

def get_all_brands() -> List:
    return Brand.query.all()

def get_brand_by_id(id) -> Any | None:
    return Brand.query.get(id)

def create_brand(data) -> Brand:
    brand = Brand(**data)
    db.session.add(brand)
    db.session.commit()
    return brand
