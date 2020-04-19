from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from flask import flash,redirect,url_for
from . import db

def create_user_account(username,email,password):
    pass_hash=generate_password_hash(password)
    new_user=User(username=username,email=email,password=pass_hash)

    db.session.add(new_user)
    db.session.commit()

def check_user(prompt):
    user=(User.query.filter_by(username=prompt).first() or 
        User.query.filter_by(email=prompt).first())
    
    if not user:
        flash("User doesnot exist")
        return redirect('login')

    return user

    



    
