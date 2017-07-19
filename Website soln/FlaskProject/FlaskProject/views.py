"""
Routes and views for the bucketbook application.
"""

from flask import render_template, session, request, url_for, redirect
from FlaskProject import app

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/<username>/my_buckets')
def mybuckets(username):
    """Renders the my buckets page."""
    return render_template('my buckets.html')

@app.route('/login', methods=["POST", "GET"])
def login():
    """Renders the login page."""
    return render_template('login.html')

@app.route('/', methods=["POST", "GET"])
def home():
    """Renders the home/create account page."""
    if request.method == "POST":
        session["firstname"] = request.form["firstname"]
        session["email"] = request.form["emailaddress"]
        session["password"] = request.form["password"]
        return redirect('/login')
    else:
        return render_template( 'create-account.html' )




