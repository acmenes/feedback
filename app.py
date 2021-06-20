from flask import Flask, render_template, redirect, session, flash

from models import connect_db, db, User

from forms import RegisterForm, LoginForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///flask_feedback"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "MissMillieIsGood"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
db.create_all()

@app.route('/')
def home_page():
    return redirect('/register')

@app.route('/register', methods=["GET", "POST"])
def reg_user():

    if "username" in session:
        return redirect(f"/users/{session['username']}")

    form = RegisterForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        email = form.email.data
        first_name = form.first_name.data
        last_name = form.last_name.data
        new_user = User.register(
            username, password, email, first_name, last_name)
        db.session.add(new_user)
        db.session.commit()
        session['username'] = new_user.username
        return redirect('/secret')

    return render_template('register.html', form=form)

@app.route('/users/<username>')
def user_page(username):

    if "username" in session:
        user = User.query.get_or_404(username.id)
        return render_template('user.html', user=user)


@app.route('/login')
def login_user():

    if "username" in session:
        return redirect(f"/users/{session['username']}")

    form = LoginForm()

    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
    
        user = User.authenticate(username, password)

        if user:
            session['username'] = user.username
            return redirect(f'/users/{user.username}')
    
        else:
            flash("Invalid username/password")
            return render_template('login.html', form=form)

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_user():
    session.pop('username')
    return redirect('/login')

@app.route('/secret')
def its_secret():

    if "username" in session:
        return redirect(f"/users/{session['username']}")
    else:
        return render_template('secret.html')