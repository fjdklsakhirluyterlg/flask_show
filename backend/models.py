from flask_login import UserMixin
from datetime import datetime
from . import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(50))
    points = db.Column(db.Integer, default=1)
    timestamp = db.Column(db.DateTime(), default=datetime.utcnow, index=True)