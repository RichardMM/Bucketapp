"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)
from flaskProject import views
