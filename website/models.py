from email.policy import default
from enum import unique
from time import timezone
from sqlalchemy import null
from . import db
from flask_login import UserMixin
from sql_alchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    email = db.Column(db.String(150))
    date_created = db.Column(db.Date(timezone=True), default=func.now())
    