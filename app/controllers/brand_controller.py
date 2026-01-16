from __future__ import annotations

from app.models.brand import Brand
from app.services import brand_service
from app.services.errors import NotFoundError


def get_all_brands() -> list[Brand]:
    return brand_service.list_brands()

def get_brand_by_id(brand_id: int) -> Brand | None:
    try:
        return brand_service.get_brand(brand_id)
    except NotFoundError:
        return None

def create_brand(data: dict) -> Brand:
    return brand_service.create_brand(
        brand_service.BrandCreate(
            logo=data.get('logo'),
            name=data['name'],
            description=data.get('description'),
            internal_id=data['internal_id'],
        )
    )
