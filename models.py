from enum import unique

from sqlalchemy.orm import backref
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()

db = SQLAlchemy()

def connect_db(app):
    '''Connect to database'''

    db.app = app
    db.init_app(app)

class User(db.Model):

    __tablename__ = 'users'

    # id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    username = db.Column(db.String(20), primary_key=True, unique=True)

    password = db.Column(db.Text, nullable=False)

    email = db.Column(db.String(50), nullable=False, unique=True)

    first_name = db.Column(db.String(30), nullable=False)

    last_name = db.Column(db.String(30), nullable=False)

    @classmethod
    def register(cls, username, pwd):
        '''Reg a user w/hashed pwd & return user'''

        # hashed = bcrypt.generate_password_hash(pwd)
        hashed = bcrypt.generate_password_hash(pwd)
        hashed_utf8 = hashed.decode("utf8")

        return cls(username=username, password=hashed_utf8)
    
    @classmethod
    def authenticate(cls, username, pwd):
        '''Authenticate a user'''

        u = User.query.filter_by(username=username).first()

        if u and bcrypt.check_password_hash(u.password, pwd):
            return u
        else:
            return False 

class Feedback(db.Model):

    __tablename__ = 'feedback'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    title = db.Column(db.String(100), nullable=False)

    content = db.Column(db.Text, nullable=False)

    username = db.relationship('User', backref="feedback")