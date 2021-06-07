import flask
from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
import os

app = Flask(__name__)

SECRET_KEY = os.environ.get('SECRET_KEY')
app.config['SECRET_KEY'] = SECRET_KEY

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app=app)


# CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __repr__(self):
        return '<User %r>' % self.name


# Line below only required once, when creating DB.
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user_db = User.query.filter_by(email=email).first()
        if user_db:
            # User exists in db
            flash("You've already signed up with that email. \nLog in instead.")
            return redirect(url_for('login'))

        # User not in db
        password_hash_salt = generate_password_hash(password=password,
                                                    method='pbkdf2:sha256',
                                                    salt_length=8)
        new_user = User(
            email=request.form.get("email"),
            password=password_hash_salt,
            name=request.form.get("name")
        )
        # print(new_user)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("secrets"))

    return render_template("register.html")


@login_manager.user_loader
def load_user(user_id):
    # print(user_id)
    return User.query.get(int(user_id))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        # Get user with matching email from database
        # user_in_db = db.session.query(User).filter(User.email == email).first()
        user_in_db = User.query.filter_by(email=email).first()
        if not user_in_db:
            # User not in db
            flash("The email does not exist. \nPlease try again.")
            return redirect(url_for("login"))

        else:
            password_match = check_password_hash(pwhash=user_in_db.password,
                                                 password=password)
            if not password_match:
                # Password does not match
                flash("Password incorrect. \nPlease try again.")
                return redirect(url_for("login"))

            else:
                # print(user_db)
                login_user(user=user_in_db)
                # flash("Logged in successfully.")
                return redirect(url_for('secrets'))

    return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    # The 'current_user' proxy is available in this and ALL the HTML templates.
    # So after authentication, we don't need to pass the user object
    # to this function/route nor to the return function or HTML.
    print(current_user.name)
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(directory="static/files/", path="cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
