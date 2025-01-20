from flask import Flask
import json

app = Flask(__name__)


@app.route("/")
def get_characters():
    with open("data/characters.json", "r") as file:
        data = json.load(file)  # loading the json file in a object
        for character in data:
            print(character["name"])

get_characters()