from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired

class BrandForm(FlaskForm):
    logo = StringField('Logo URL')
    name = StringField('Name', validators=[DataRequired()])
    description = TextAreaField('Description')
    internal_id = StringField('Internal ID', validators=[DataRequired()])
