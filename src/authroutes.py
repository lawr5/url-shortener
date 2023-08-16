from flask import render_template, request, redirect, url_for, Blueprint, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from .extensions import db
from .models import *
from .forms import *

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=["GET","POST"])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = db.session.query(Users).filter_by(email=form.email.data).first()
        if user:
            flash('This user already exists.')
        
        else:
            hashed_password = generate_password_hash(form.password.data, method='sha256')
            new_user = Users(email=form.email.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
        flash('You have been sucessfully registered.')
        
    return render_template("register.html", form=form)

@auth.route("/login", methods=["GET","POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user  = db.session.query(Users).filter_by(email=form.email.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for("main.index"))
        flash('Invalid username or password. Please register if you don\'t have an account.')
    return render_template("login.html", form=form)

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
