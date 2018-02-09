from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class CreateAccountForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email_address = StringField('Email Address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired()])
    phone_number = StringField('Phone Number')
    security_questions = SelectField('Security Question', choices=[(
        'wsdylo', "What Street did you live on in 6th grade?"), ("test", "test")])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')