from typing import Literal

from flask import Blueprint, Response, jsonify

from app.services import brand_service, manufacturer_service
from app.services.errors import NotFoundError

bp = Blueprint('api', __name__, url_prefix='/api/v1')

@bp.route('/brands')
def get_brands() -> Response:
    brands = brand_service.list_brands()
    return jsonify([brand.to_dict() for brand in brands])

@bp.route('/brands/<int:id>')
def get_brand(id) -> Response | tuple[Response, Literal[404]]:
    try:
        brand = brand_service.get_brand(id)
    except NotFoundError:
        return jsonify({'error': 'Brand not found'}), 404
    return jsonify(brand.to_dict())

@bp.route('/manufacturers')
def get_manufacturers() -> Response:
    manufacturers = manufacturer_service.list_manufacturers()
    return jsonify([manufacturer.to_dict() for manufacturer in manufacturers])

@bp.route('/manufacturers/<int:id>')
def get_manufacturer(id) -> Response | tuple[Response, Literal[404]]:
    try:
        manufacturer = manufacturer_service.get_manufacturer(id)
    except NotFoundError:
        return jsonify({'error': 'Manufacturer not found'}), 404
    return jsonify(manufacturer.to_dict())
