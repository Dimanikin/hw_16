import os.path

from flask import Flask
from setup_db import db
from utils import GetData

app = Flask(__name__,instance_path=os.path.dirname(os.path.abspath(__file__)))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII']
db.init_app(app)

data = GetData()

with app.app_context():
    data.create_db()
