from __future__ import annotations

from dataclasses import dataclass

from sqlalchemy.exc import IntegrityError

from app.extensions import db
from app.models.brand import Brand
from app.services.errors import ConflictError, NotFoundError, ValidationError


@dataclass(frozen=True, slots=True)
class BrandCreate:
    name: str
    internal_id: str
    logo: str | None = None
    description: str | None = None


def list_brands() -> list[Brand]:
    return list(Brand.query.all())


def get_brand(brand_id: int) -> Brand:
    brand = db.session.get(Brand, brand_id)
    if brand is None:
        raise NotFoundError("Brand not found")
    return brand


def create_brand(payload: BrandCreate) -> Brand:
    if not payload.name.strip():
        raise ValidationError("Brand name is required")
    if not payload.internal_id.strip():
        raise ValidationError("Brand internal_id is required")

    brand = Brand(
        logo=payload.logo,
        name=payload.name.strip(),
        description=payload.description,
        internal_id=payload.internal_id.strip(),
    )
    db.session.add(brand)
    try:
        db.session.commit()
    except IntegrityError as exc:
        db.session.rollback()
        # Most likely unique constraint violation (internal_id).
        raise ConflictError("Brand with this internal_id already exists") from exc
    return brand

