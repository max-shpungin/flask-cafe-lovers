import os
from dotenv import load_dotenv

from flask import Flask, render_template

load_dotenv()

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ['SECRET_KEY']


################################################################################
# Anon / Signup / Login / Dashboard

@app.route('/')
def home():
    """ Will show cafes and listings"""
    return render_template('home.html')

@app.route('/signup')
def signup():
    """ redirects to dashboard on signup """
    ...

@app.route('/login')
def login():
    """ redirects to dashboard on login"""
    ...

@app.route('/users/<username>')
def dashboard():
    ...

################################################################################
# Add/remove cafes and view user and cafe listings

@app.route('/cafes')
def cafes():
    """ Cafe Listings """
    ...

@app.route('/cafes/<int:cafe_id>')
def cafe():
    """ Individual Cafe """
    ...

@app.route('/users')
def users():
    """ User listings """
    ...



