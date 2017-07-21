"""
Routes and views for the bucketbook application.
"""

from flask import render_template, session, request, url_for, redirect
from FlaskProject import app

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/mybuckets/<firstname>', methods=["POST", "GET"])
def mybuckets(firstname):
    """Renders the my buckets page."""
    if request.method=="POST": 
        session["newbucket"] = request.form["newbucket"]
        session["bucketitems"] = []
        return redirect(url_for("bucketlist", firstname=session["firstname"], newbucket=session["newbucket"]))
    else:
        return render_template('my buckets.html')

@app.route('/<firstname>/<newbucket>', methods=["POST", "GET"])
def bucketlist(firstname, newbucket):
    """ Renders a bucketlists page"""
    if request.method=="POST":
        newitem = request.form["newlist"]
        session["bucketitems"].append(newitem)
        session.modified = True
        return render_template("samplebucketlist1.html")
    return render_template("samplebucketlist1.html")

@app.route('/login', methods=["POST", "GET"])
def login():
    """Renders the login page."""
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if email==session["email"] and password==session["password"]:
            return redirect(url_for("mybuckets", firstname=session["firstname"]))
        else:
            render_template('login.html')
    else:
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
