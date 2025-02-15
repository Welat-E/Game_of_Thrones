import sys
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String


# database configs
SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False


# Add the project root directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_root)

load_dotenv()

class Users(db.Model):
    __tablename__ = "Characters"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=True)
    house = db.Column(db.String, nullable=True)
    animal = db.Column(db.String, default=True)
    symbol = db.Column(db.String, nullable=True)
    nickname = db.String(db.String, nullable=True)
    role = db.Column(db.String, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    death = db.Column(db.Integer, nullable=True)
    strength = db.Column(db.String, nullable=True)


with app.app_context():
    db.create_all()
