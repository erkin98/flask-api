from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class ManufacturerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    country = StringField('Country')
    certificates = TextAreaField('Certificates')
    internal_id = StringField('Internal ID', validators=[DataRequired()])
