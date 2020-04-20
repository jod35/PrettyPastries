from . import db,login_manager
from flask_login import UserMixin


class User(db.Model,UserMixin):
    __tablename__="app_users"
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(255),nullable=False)
    email=db.Column(db.String(80),nullable=False)
    password=db.Column(db.Text(),nullable=False)

    def __repr__(self):
        return f"user {self.id}"
        

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))