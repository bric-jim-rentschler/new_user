To get the project up and running...

Install python 3.4, venv, and pip, if not already

Create the virtualenv in the root of the project: python -m venv flask

Install the requirements (Windows):
    * flask\Scripts\pip install -r requirements.txt
MacOs/Linux/Similar:
    * flask/bin/pip3 install -r requirements.txt
Activate the virtual environment:
    * venv\Scripts\activate
Set the environment variable to the initialization file:
    * set FLASK_APP=newuserform.py
    * Run 'flask run'
Should be debugging on localhost:5000/
