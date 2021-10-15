from wtforms import Form
from wtforms.fields.core import BooleanField, StringField
from wtforms.fields.simple import PasswordField
from wtforms.validators import DataRequired


class LoginForm(Form):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', validators=[DataRequired()])