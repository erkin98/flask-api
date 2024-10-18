from flask import Blueprint, jsonify
from app.controllers import brand_controller, manufacturer_controller

bp = Blueprint('api', __name__, url_prefix='/api/v1')

@bp.route('/brands')
def get_brands():
    brands = brand_controller.get_all_brands()
    return jsonify([brand.to_dict() for brand in brands])

@bp.route('/brands/<int:id>')
def get_brand(id):
    brand = brand_controller.get_brand_by_id(id)
    if brand:
        return jsonify(brand.to_dict())
    return jsonify({'error': 'Brand not found'}), 404

@bp.route('/manufacturers')
def get_manufacturers():
    manufacturers = manufacturer_controller.get_all_manufacturers()
    return jsonify([manufacturer.to_dict() for manufacturer in manufacturers])

@bp.route('/manufacturers/<int:id>')
def get_manufacturer(id):
    manufacturer = manufacturer_controller.get_manufacturer_by_id(id)
    if manufacturer:
        return jsonify(manufacturer.to_dict())
    return jsonify({'error': 'Manufacturer not found'}), 404
