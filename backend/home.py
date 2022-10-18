from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from flask_login import login_user, login_required, logout_user, current_user, LoginManager, UserMixin

home = Blueprint(__name__, "home")

@login_required
@home.route("/dashboard")
def dashboard():
    return f"<h1>hi {current_user.name}</h1><a href='/logout'><button>logout</button></a>"
