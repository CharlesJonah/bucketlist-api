from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import sys
sys.path.append('..')
import config

app = Flask(__name__)

app.config.from_object('config.Config')

db = SQLAlchemy(app)

from app import models, views

db.create_all()
db.session.commit()
