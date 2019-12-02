from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import pymysql
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://"+os.getenv("MYSQL_USER")+":"+os.getenv("MYSQL_PASSWORD")+"@"+os.getenv("MYSQL_HOST")+"/"+os.getenv("MYSQL_DB")
db = SQLAlchemy(app)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
bcrypt = Bcrypt(app)

from application import routes
