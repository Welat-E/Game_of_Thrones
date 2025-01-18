from flask import Flask

app = Flask(__name__)

@app.route("/")
def get_characters():
    with open(data/characters.json, 'r') as file:
        for character in file:
            print(character["name"])

