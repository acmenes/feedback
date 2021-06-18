from flask import Flask, render_template, redirect, session

from models import connect_db, db, User

from forms import RegisterForm, LoginForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgres:///flask_feedback"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "MissMillieIsGood"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)

@app.route('/')
def home_page():
    return redirect('/register')

@app.route('/register')
def reg_user():
    form = RegisterForm()
    return render_template('register.html', form=form)

@app.route('/login')
def login_user():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route('/logout')
def logout_user():
    return "you have been logged out"

@app.route('/secret')
def its_secret():
    return "shhh"