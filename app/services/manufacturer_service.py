from __future__ import annotations

from dataclasses import dataclass

from sqlalchemy.exc import IntegrityError

from app.extensions import db
from app.models.manufacturer import Manufacturer
from app.services.errors import ConflictError, NotFoundError, ValidationError


@dataclass(frozen=True, slots=True)
class ManufacturerCreate:
    name: str
    internal_id: str
    description: str | None = None
    country: str | None = None
    certificates: str | None = None


def list_manufacturers() -> list[Manufacturer]:
    return list(Manufacturer.query.all())


def get_manufacturer(manufacturer_id: int) -> Manufacturer:
    manufacturer = db.session.get(Manufacturer, manufacturer_id)
    if manufacturer is None:
        raise NotFoundError("Manufacturer not found")
    return manufacturer


def create_manufacturer(payload: ManufacturerCreate) -> Manufacturer:
    if not payload.name.strip():
        raise ValidationError("Manufacturer name is required")
    if not payload.internal_id.strip():
        raise ValidationError("Manufacturer internal_id is required")

    manufacturer = Manufacturer(
        name=payload.name.strip(),
        description=payload.description,
        country=payload.country,
        certificates=payload.certificates,
        internal_id=payload.internal_id.strip(),
    )
    db.session.add(manufacturer)
    try:
        db.session.commit()
    except IntegrityError as exc:
        db.session.rollback()
        raise ConflictError("Manufacturer with this internal_id already exists") from exc
    return manufacturer

