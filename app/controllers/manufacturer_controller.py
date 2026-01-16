from __future__ import annotations

from typing import Optional

from app.extensions import db
from app.models.manufacturer import Manufacturer

def get_all_manufacturers() -> list[Manufacturer]:
    return list(Manufacturer.query.all())

def get_manufacturer_by_id(manufacturer_id: int) -> Optional[Manufacturer]:
    return db.session.get(Manufacturer, manufacturer_id)

def create_manufacturer(data: dict) -> Manufacturer:
    manufacturer = Manufacturer(**data)
    db.session.add(manufacturer)
    db.session.commit()
    return manufacturer
