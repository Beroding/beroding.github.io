from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_Session import Session
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__, template_folder='views')
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
APP.CONFIG["SQLALCHEMY_DATABASE_URI"] = os.getenv("DB_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["SESSION_PERMANENT"] = False

db = SQLAlchemy(app)

from application import routes
from application.models import *