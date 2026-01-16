from __future__ import annotations

from app.models.manufacturer import Manufacturer
from app.services import manufacturer_service
from app.services.errors import NotFoundError


def get_all_manufacturers() -> list[Manufacturer]:
    return manufacturer_service.list_manufacturers()

def get_manufacturer_by_id(manufacturer_id: int) -> Manufacturer | None:
    try:
        return manufacturer_service.get_manufacturer(manufacturer_id)
    except NotFoundError:
        return None

def create_manufacturer(data: dict) -> Manufacturer:
    return manufacturer_service.create_manufacturer(
        manufacturer_service.ManufacturerCreate(
            name=data['name'],
            description=data.get('description'),
            country=data.get('country'),
            certificates=data.get('certificates'),
            internal_id=data['internal_id'],
        )
    )
