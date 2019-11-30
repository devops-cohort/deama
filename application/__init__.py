from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://"+os.getenv("MYSQL_USER")+":"+os.getenv("MYSQL_PASSWORD")+"@"+os.getenv("MYSQL_HOST")+"/"+os.getenv("MYSQL_DB")
db = SQLAlchemy(app)

app.config["SECRET_KEY"] = "qqwertyuiop[asdfghjklzxcvbnn4567"

from application import routes
