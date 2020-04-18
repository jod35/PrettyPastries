from .models import User
from werkzeug.security import generate_password_hash,check_password_hash
from flask import flash
from . import db

def create_user_account(username,email,password):
    pass_hash=generate_password_hash(password)
    new_user=User(username=username,email=email,password=pass_hash)

    db.session.add(new_user)
    db.session.commit()