from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import DateField

class PersonInfoForm(FlaskForm):
    """Contact form."""
    fullname = StringField('Name', [
        DataRequired("Please enter politician public name.")])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired("Please enter the politician start Date.")])
    submit = SubmitField('Submit')