from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug import Response
from app.forms.brand_form import BrandForm
from app.forms.manufacturer_form import ManufacturerForm
from app.controllers import brand_controller, manufacturer_controller

bp = Blueprint('admin', __name__, url_prefix='/client')

@bp.route('/brands', methods=['GET', 'POST'])
def brands() -> Response | str:
    form = BrandForm()
    if form.validate_on_submit():
        brand_data = {
            'logo': form.logo.data,
            'name': form.name.data,
            'description': form.description.data,
            'internal_id': form.internal_id.data
        }
        brand = brand_controller.create_brand(brand_data)
        flash('Brand added successfully!', 'success')
        return redirect(url_for('admin.brands'))
    brands = brand_controller.get_all_brands()
    return render_template('brands.html', brands=brands, form=form)

@bp.route('/manufacturers', methods=['GET', 'POST'])
def manufacturers() -> Response | str:
    form = ManufacturerForm()
    if form.validate_on_submit():
        manufacturer_data = {
            'name': form.name.data,
            'description': form.description.data,
            'country': form.country.data,
            'certificates': form.certificates.data,
            'internal_id': form.internal_id.data
        }
        manufacturer = manufacturer_controller.create_manufacturer(manufacturer_data)
        flash('Manufacturer added successfully!', 'success')
        return redirect(url_for('admin.manufacturers'))
    manufacturers = manufacturer_controller.get_all_manufacturers()
    return render_template('manufacturers.html', manufacturers=manufacturers, form=form)
