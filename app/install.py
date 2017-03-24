from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app_install = Flask(__name__)
app_install.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db_install = SQLAlchemy(app_install)


class User(db_install.Model):
    id = db_install.Column(db_install.Integer, primary_key=True)
    username = db_install.Column(db_install.String(80), unique=True)
    email = db_install.Column(db_install.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username