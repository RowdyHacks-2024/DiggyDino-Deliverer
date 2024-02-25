from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv, getcwd

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{getcwd()}/{getenv("SQLITE_DB")}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

@app.route('/')
def hello():
    return 'hello'
