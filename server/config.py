from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS

from models import db, bcrypt

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "super-secret-dev-key"

CORS(app, supports_credentials=True)

db.init_app(app)
bcrypt.init_app(app)

migrate = Migrate(app, db)