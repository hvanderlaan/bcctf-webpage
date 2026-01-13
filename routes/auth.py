from flask import Blueprint, render_template, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from extensions import db
from forms import LoginForm, RegisterForm

auth = Blueprint("auth", __name__)

@auth.route("/login", methods=["GET", "POST"])
def login() -> render_template:
    '''
    login route for flask (/login)
    
    :return: login page
    :rtype: render_template
    '''
    form: LoginForm = LoginForm()
    if form.validate_on_submit():
        user: User = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            session["user_id"] = user.id
            return redirect(url_for("main.profile"))
        flash("Invalid credentials")
    return render_template("login.html", form=form)

@auth.route("/register", methods=["GET", "POST"])
def register() -> render_template:
    '''
    register route for flask (/register)
    
    :return: register page
    :rtype: render_template
    '''
    form: RegisterForm = RegisterForm()
    if form.validate_on_submit():
        user: User = User(
            username=form.username.data,
            password=generate_password_hash(form.password.data)
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("auth.login"))
    return render_template("register.html", form=form)

@auth.route("/logout")
def logout() -> redirect:
    '''
    logout route for flask (/logout)
    
    :return: logout user
    :rtype: redirect
    '''
    session.clear()
    return redirect(url_for("main.index"))
