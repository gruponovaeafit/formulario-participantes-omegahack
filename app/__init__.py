from flask import Flask
from config import Config
import os
import urllib.parse 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pymssql://novaeafit:q8Hb6itCChKjRnkWHMOV@novaeafit.database.windows.net:1433/hackaton-2024'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes
