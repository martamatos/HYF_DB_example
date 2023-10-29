from datetime import datetime
from hashlib import md5
from app import current_app, db
from werkzeug.security import generate_password_hash, check_password_hash
from time import time
import jwt
import enum



class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(140), nullable=False)
    email = db.Column(db.String(140), nullable=False)
    phone = db.Column(db.String(140))

    tasks = db.relationship('Task', back_populates='user')

    def __repr__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)


class Status(db.Model):
    __tablename__ = 'status'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(140), nullable=False)

    def __repr__(self):
        return str(self.name)

    def __str__(self):
        return str(self.name)


class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(140), nullable=False)
    description = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    due_date = db.Column(db.DateTime)
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    user = db.relationship('User', back_populates='tasks')
    status = db.relationship('Status')

    def __repr__(self):
        return str(self.title)
