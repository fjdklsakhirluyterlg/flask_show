from flask import Flask, render_template, url_for, request, redirect, send_from_directory, send_file, flash, jsonify, Blueprint, Response, abort
from flask_login import login_user, login_required, logout_user, current_user, LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy

DB_NAME = "database.db"
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] =f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    db.create_all(app=app)