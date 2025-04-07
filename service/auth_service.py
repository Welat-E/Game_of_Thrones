from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token
from flask sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config[ 'SQLALCHEMY _DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/game_of_thrones'
app.config[ 'JWT_SECRET_KEY'] = 'Knfasduf3425881f!?jasdf'
db = SQLAlchemy (app)
jwt = JWTManager (app)


class User (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String (50), unique=True, nullable=False)
    password = db. Column (db.String(80), nullable=False)