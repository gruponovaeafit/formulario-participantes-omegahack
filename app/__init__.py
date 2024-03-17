from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv


load_dotenv()  # Take environment variables from .env.

app = Flask(__name__)
app.config.from_object(Config)

# Load the database URI from an environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'fallback-database-uri')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Extensions
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes
