from typing import Any, List
from app import db
from app.models.manufacturer import Manufacturer

def get_all_manufacturers() -> List:
    return Manufacturer.query.all()

def get_manufacturer_by_id(id) -> Any | None:
    return Manufacturer.query.get(id)

def create_manufacturer(data) -> Manufacturer:
    manufacturer = Manufacturer(**data)
    db.session.add(manufacturer)
    db.session.commit()
    return manufacturer
