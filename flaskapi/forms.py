from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import DateField
from datetime import datetime
from wtforms.validators import ValidationError

class PersonInfoForm(FlaskForm):
    """Contact form."""
    fullname = StringField('Primer nombre y apellido', [
        DataRequired("Favor ingresa tu nombre completo.")])
    date = DateField('Fecha de nacimiento', format='%Y-%m-%d',validators=[DataRequired("Favor ingresa tu fecha de nacimiento.")])
    submit = SubmitField('Ingresar')

    def validate_date(form, field):
        # datetime_object = datetime.strptime(field.data, '%Y-%m-%d').date()
        today = datetime.now().date()
        if field.data > today:
            raise ValidationError("La fecha debe ser menor a la fecha actual.")