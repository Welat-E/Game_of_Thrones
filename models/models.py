import sys
import os
from dotenv import load_dotenv
import json
from flask import Flask

load_dotenv()#loading env file for db using

#add the project root directory to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_root)

from app import app
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialisiere SQLAlchemy direkt mit der App
db = SQLAlchemy(app)
session = Session()

class Characters(db.Model):
    __tablename__ = "characters"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=True)
    house = db.Column(db.String, nullable=True)
    animal = db.Column(db.String, nullable=True)
    symbol = db.Column(db.String, nullable=True)
    nickname = db.Column(db.String, nullable=True)
    role = db.Column(db.String, nullable=True)
    age = db.Column(db.Integer, nullable=True)
    death = db.Column(db.Integer, nullable=True)
    strength = db.Column(db.String, nullable=True)


with app.app_context():
    db.create_all()

def import_json_to_db(json_file):
    with open(json_file, "r") as file:
        data = json.load(file)  #load json file

    with app.app_context():
        for chars in data:
            character = Characters(
                name=chars.get("name"),
                house=chars.get("house"),
                animal=chars.get("animal"),
                symbol=chars.get("symbol"),
                nickname=chars.get("nickname"),
                role=chars.get("role"),
                age=chars.get("age"),
                death=chars.get("death"),
                strength=chars.get("strength")
            )
            db.session.add(character)  # add data to session

        db.session.commit() #save changes

import_json_to_db("data/characters.json") #call the function



