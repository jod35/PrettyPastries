from . import db


class User(db.Model):
    __tablename__="app_users"
    id=db.Column(db.Integer(),primary_key=True)
    username=db.Column(db.String(255),nullable=False)
    email=db.Column(db.String(80),nullable=False)
    password=db.Column(db.Text(),nullable=False)

    def __repr__(self):
        return f"user {self.id}"
        