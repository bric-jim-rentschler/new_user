from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, ValidationError
from wtforms.validators import DataRequired, Length, Regexp, EqualTo
from wtforms.fields.html5 import EmailField
from validate_email import validate_email


def validate_password(form, password):
    password = str(password)
    if not any(ch.isupper() for ch in password):
        if not any(c.islower() for c in password):
            if not any(n.isalnum() for n in password):
                raise ValidationError('Please enter a password that has at least 7 characters including at least 1 '
                                      'uppercase character, 1 lowercase character, and 1 special character or number.')

def valid_email(form, email):
    email = str(email)
    if (validate_email(email, verify=True)):
        raise ValidationError('This email address is already in use. If '
                              'you’ve forgotten your password click here to retrieve it.')


class CreateAccountForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired(message="First name is required"), Length(max=30)])
    last_name = StringField('Last Name', validators=[DataRequired(message="Last name is required"), Length(max=30)])
    email_address = EmailField('Email Address'
                                , validators=[DataRequired(message="Email address is required"),
                                              Length(max=100),
                                              Regexp('[_\-a-zA-Z0-9\.\+]+@[a-zA-Z0-9](\.?[\-a-zA-Z0-9]*[a-zA-Z0-9])*',
                                                     message="Please enter a valid email address."),
                                              valid_email])
    password = PasswordField('Password', validators=[DataRequired(message="Password is required"),
                                                     Length(min=7),
                                                     validate_password])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(message="Confirm password is required"),
                                                 Length(min=7), EqualTo(fieldname='password'),
                                                 validate_password])
    phone_number = StringField('Phone Number',
                                    validators=[DataRequired(message="Phone number is required"),
                                                Length(max=17),
                                                Regexp(r'(((\+[1-9]\d{0,2})[\-\s.](\d{1,3})|(((1\s)?)\(\d{3}\)))[\-\s.])'
                                                        r'?(\d{1,8})([\-\s.](\d{1,8})){1,'r'4}(\sext\.\s\d{1,10})?')])
    security_questions = SelectField('Security Question', choices=[
        ("", "")
        , ("wsdylo", "What Street did you live on in 6th grade?")
        , ("wwycn", "What was your childhood nickname?")
        , ("iwcdymafm", "In what city did your mother and father meet?")
        , ("wwtlnoytgt", "What was the last name of your third grade teacher?")
        , ("wwtnoyfsa", "What was the name of your first stuffed animal?")])
    security_answers = PasswordField('Security Answer',
                                     validators=[DataRequired(message="Security answers are required"),
                                                 Length(max=100)])
    sweepstakes = BooleanField('Yes, I would like to be enrolled in the Sweepstakes.', default="checked")
    promotions = BooleanField('Yes, I would like to receive emails about special promotions or sales.',
                              default="checked")
    submit = SubmitField('Submit')
