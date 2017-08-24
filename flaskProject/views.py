"""
Routes and views for the bucketbook application.
"""

from flask import render_template, session, request, url_for, redirect
from flaskProject import app
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Email, Length
from wtforms import StringField, BooleanField, PasswordField

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

class Loginform(FlaskForm):
    email = StringField("email", validators=[InputRequired()])
    password = PasswordField("password", validators=[InputRequired()])
    remember = BooleanField("rememberme")


@app.route('/mybuckets/<firstname>', methods=["POST", "GET"])
def mybuckets(firstname):
    """Renders the my buckets page."""
    if request.method=="POST": 
        newbucket = request.form["newbucket"]
        if newbucket not in session["buckets"]:
            session["buckets"].append(newbucket)
            session["bucketitems"][newbucket] = []
            session.modified = True
        #return redirect(url_for("bucketlist", firstname=session["firstname"], newbucket=session["newbucket"]))
        return render_template('my buckets.html')
    else:
        return render_template('my buckets.html')

@app.route('/<firstname>/<newbucket>', methods=["POST", "GET"])
def bucketlist(firstname, newbucket):
    """ Renders a bucketlists page"""
    session["currentbucket"] = newbucket
    session.modified = True
    if request.method=="POST":
        newitem = request.form["newlist"]
        session["bucketitems"][session["currentbucket"]].append(newitem)
        session.modified = True
        return render_template("samplebucketlist1.html")
    return render_template("samplebucketlist1.html")

@app.route('/login', methods=["POST", "GET"])
def login():
    """Renders the login page."""
    myform = Loginform()
    if myform.validate_on_submit():
        email = myform.email.data
        password = myform.password.data
        if email==session["email"] and password==session["password"]:
            # session storages
            session["buckets"] = []  # stores the buckets created
            session["bucketitems"] = {} # has buckets as keys and a listof bucket items as the value
            return redirect(url_for("mybuckets", firstname=session["firstname"]))
        else:
            render_template('login.html')
    else:
        print(myform.errors)
        return render_template('login.html', form=myform)

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
