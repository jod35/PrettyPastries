from . import app,db
from flask import render_template,redirect,flash,url_for,request
from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import login_user,logout_user,current_user
from .auth import create_user_account,check_user

#home page
@app.route('/')
def home_page():
   return render_template('index.html')

@app.route('/login',methods=['POST','GET'])
def login_page():
    prompt=request.form.get('prompt')
    password=request.form.get('password')
    user=(User.query.filter_by(username=prompt).first() or 
        User.query.filter_by(email=prompt).first())
    
    if user and check_password_hash(user.password,password):
        login_user(user)
        return "Logged In"
    return render_template('login.html')

@app.route('/signup',methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password =request.form.get('password')

        print(username,email,password)

        user_exists=(User.query.filter_by(username=username).first() or 
            User.query.filter_by(email=email).first())

        if user_exists:
            flash("The user already exists!! \nTry using another email or username")
            return redirect(url_for('register'))
        else:
            create_user_account(username,email,password)
            flash("Account Created Successfully!!")
            return redirect(url_for('login_page'))
    return render_template('register.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home_page'))
   

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')
