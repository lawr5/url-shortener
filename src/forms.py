from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField
from wtforms.validators import InputRequired, Email, Length, EqualTo


class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email')])
    password = PasswordField('password', validators=[InputRequired(), Length(min=6, message='Password must be at least six characters long')])
    confirm_password = PasswordField('confirm password', validators=[InputRequired(), EqualTo('password', message='Passwords must match')])

class LoginForm(FlaskForm):
    email = StringField('username', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
