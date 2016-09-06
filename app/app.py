import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
if 'testing' in os.environ:
    app.config.from_object('config_test')

db = SQLAlchemy(app)

import views
