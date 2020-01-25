from flask_wtf import FlaskForm,
from wtforms import StringField, TextField, SubmitField, DateField
from wtforms.validators import DataRequired, Length

class UserInfoForm(FlaskForm):
    """Contact form."""
    fullname = StringField('Name', [
        DataRequired()])
    date = DateField('Date', [
        Email(message=('Not a valid email address.')),
        DataRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')