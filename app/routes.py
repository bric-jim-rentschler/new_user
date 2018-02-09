from flask import render_template
from app import app
from app.forms import CreateAccountForm

@app.route('/')
@app.route('/createaccount')
def newuser():
    form = CreateAccountForm()
    return render_template('create_account.html', title='Account Creation', form=form)