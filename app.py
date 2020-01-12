import sys, os
sys.path.append(os.path.abspath(os.path.join('.')))
from flask import Flask
from blueprints.hotel import hotelapi

app = Flask(__name__)
app.config.from_object('config')
app.config.from_pyfile('./instance/config.py')

app.register_blueprint(hotelapi)