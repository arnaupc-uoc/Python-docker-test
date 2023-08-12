from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Length, Email


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[InputRequired(), Email(granular_message=True)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=4)])
    remember = BooleanField(label='Remember me')
