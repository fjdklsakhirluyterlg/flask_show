from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user, LoginManager, UserMixin
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        password2 = request.form["password2"]

        if password != password2:
            return render_template("signup.html", msg="pasword does not match")

        news = User(name=name, email=email, password=generate_password_hash(password, method='sha256'))
        db.session.add(news)
        db.session.commit()
        login_user(news, remember=True)

        return redirect('/dashboard')

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        name = request.form["name"]
        password = request.form["password"]
        usern = db.session.query(User).filter(User.name == name).first_or_404()
        eid = usern.id
        if not usern:
            return redirect(url_for("signup"))
        elif check_password_hash(usern.password, password):
            login_user(usern, remember=True)
            return redirect(f"/dashboard")
        else:
            return render_template("login.html", msg="password is incorrect")
    else:
        return render_template("login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/login")