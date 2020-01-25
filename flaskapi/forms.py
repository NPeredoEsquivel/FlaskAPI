from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.fields.html5 import DateField

class UserInfoForm(FlaskForm):
    """Contact form."""
    fullname = StringField('Name', [
        DataRequired()])
    date = DateField('Date', format='%d-%m-%y')
    submit = SubmitField('Submit')