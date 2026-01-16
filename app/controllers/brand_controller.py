from __future__ import annotations

from typing import Optional

from app.extensions import db
from app.models.brand import Brand

def get_all_brands() -> list[Brand]:
    return list(Brand.query.all())

def get_brand_by_id(brand_id: int) -> Optional[Brand]:
    # Prefer SQLAlchemy 2.x style access through the session.
    return db.session.get(Brand, brand_id)

def create_brand(data: dict) -> Brand:
    brand = Brand(**data)
    db.session.add(brand)
    db.session.commit()
    return brand
