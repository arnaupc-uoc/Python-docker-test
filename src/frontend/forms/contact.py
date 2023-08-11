from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email(granular_message=True)])
    message = StringField(label='Message')
