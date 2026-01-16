from flask import Blueprint, Response, flash, redirect, render_template, url_for

from app.forms.brand_form import BrandForm
from app.forms.manufacturer_form import ManufacturerForm
from app.services import brand_service, manufacturer_service
from app.services.errors import ConflictError, ValidationError

bp = Blueprint('admin', __name__, url_prefix='/client')

@bp.route('/brands', methods=['GET', 'POST'])
def brands() -> Response | str:
    form = BrandForm()
    if form.validate_on_submit():
        try:
            brand_service.create_brand(
                brand_service.BrandCreate(
                    logo=form.logo.data,
                    name=form.name.data,
                    description=form.description.data,
                    internal_id=form.internal_id.data,
                )
            )
        except ValidationError as exc:
            flash(str(exc), 'danger')
        except ConflictError as exc:
            flash(str(exc), 'warning')
        else:
            flash('Brand added successfully!', 'success')
        return redirect(url_for('admin.brands'))
    brands = brand_service.list_brands()
    return render_template('brands.html', brands=brands, form=form)

@bp.route('/manufacturers', methods=['GET', 'POST'])
def manufacturers() -> Response | str:
    form = ManufacturerForm()
    if form.validate_on_submit():
        try:
            manufacturer_service.create_manufacturer(
                manufacturer_service.ManufacturerCreate(
                    name=form.name.data,
                    description=form.description.data,
                    country=form.country.data,
                    certificates=form.certificates.data,
                    internal_id=form.internal_id.data,
                )
            )
        except ValidationError as exc:
            flash(str(exc), 'danger')
        except ConflictError as exc:
            flash(str(exc), 'warning')
        else:
            flash('Manufacturer added successfully!', 'success')
        return redirect(url_for('admin.manufacturers'))
    manufacturers = manufacturer_service.list_manufacturers()
    return render_template('manufacturers.html', manufacturers=manufacturers, form=form)
