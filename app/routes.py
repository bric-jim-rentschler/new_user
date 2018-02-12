from flask import render_template, flash, redirect
from app import app
from app.forms import CreateAccountForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/createaccount', methods=['GET', 'POST'])
def newuser():
    form = CreateAccountForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}, e {}, p {}, cp {}, pn {}, sa {}'.format(
            form.first_name.data, form.last_name.data, form.email_address.data
            , form.password.data, form.confirm_password.data, form.phone_number.data
            , form.security_answers.data))
        return redirect('/index')
    return render_template('create_account.html', title='Create Account', form=form)