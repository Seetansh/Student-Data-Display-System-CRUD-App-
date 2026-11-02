from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from app.extensions import db

# create a registerForm class containing the fields for the registration form
class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[validators.DataRequired(), validators.Length(min=4, max=25)])
    email = StringField('Email Address', validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField('New Password', validators=[validators.DataRequired(), validators.Length(min=6)])
    confirm_password = PasswordField('Repeat Password', validators=[validators.DataRequired(), validators.EqualTo('password')])
    submit = SubmitField('Register')

    # custom validation method to check if the username already exists in the database
    # def validate_username(self, username):
    #     user = db.session.execute(db.select(User).filter_by(username=username.data)).scalar()
    #     if user:
    #         raise ValidationError('Username already exists. Please choose a different one.')

    # # custom validation method to check if the email already exists in the database
    # def validate_email(self, email):
    #     user = db.session.execute(db.select(User).filter_by(email=email.data)).scalar()
    #     if user:
    #         raise ValidationError('Email already exists. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', validators=[validators.DataRequired()])
    submit = SubmitField('Login')

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[validators.DataRequired()])
    email = StringField('Email', validators=[validators.DataRequired(), validators.Email()])
    message = StringField('Message', validators=[validators.DataRequired()])
    submit = SubmitField('Send')