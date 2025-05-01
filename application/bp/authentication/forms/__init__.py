from flask_wtf import FlaskForm
from wtforms import validators
from wtforms.fields import *


class LoginForm(FlaskForm):
    email = EmailField('Email Address', [
        validators.DataRequired(),
        validators.Email()
    ])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.length(min=6, max=35)
    ])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    email = EmailField('Email Address', [
        validators.DataRequired(),
        validators.Email()
    ])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.length(min=6, max=35)
    ])
    confirm = PasswordField('Confirm Password', [
        validators.DataRequired(),
        validators.EqualTo('password', message='Passwords must match')
    ])
    submit = SubmitField('Register')