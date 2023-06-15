from uuid import uuid4
from werkzeug.security import generate_password_hash,check_password_hash
from app import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    passwordhash = db.Column(db.String(128))
    todos = db.relationship('Todo', backref='user', lazy='dynamic')
    
    def __repr__(self):
        return self.email
    
    def my_genrate_password_hash(self,password_raw):
        self.passwordhash = generate_password_hash(password_raw)
        
    def check_password(self,password_raw):
        return check_password_hash(self.passwordhash,password_raw)
    
    
class UserToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(128),default=str(uuid4()))
    user = db.Column(db.Integer)