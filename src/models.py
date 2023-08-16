from .extensions import db
from sqlalchemy.orm import validates
from flask_login import UserMixin

class Urls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    short_url = db.Column(db.String, unique=True, nullable=False)
    long_url = db.Column(db.String, nullable=False)
    description = db.Column(db.String, unique=False, nullable=True)
    created_by = db.Column(db.String)
    edited_by = db.Column(db.String)
    updated_on = db.Column(db.Date)
    last_used = db.Column(db.Date)

    @validates('short_url')
    def convert_lower(self, key, value):
        return value.lower()
    

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String)
