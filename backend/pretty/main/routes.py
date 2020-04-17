from . import app,db
from flask import render_template,redirect,flash,url_for


#home page
@app.route('/')
def home_page():
   return render_template('index.html')