from flask import Flask
import json
import random

app = Flask(__name__)


@app.route("/")
def get_characters():
    while True:
        try:
            limit = input("How many Characters do you wanna see? ")
            skip = input("Where should the List of Characters start? ")
            if limit == "" and skip == "":
                limit = int(20)
                skip = int(0)
                break
            elif limit != "" and skip != "":
                limit = int(limit)
                skip = int(skip)
                break
            else:
                raise Exception
        except:
            print("Both must be filled with integer or should be empty.")
    with open("data/characters.json", "r") as file:
        data = json.load(file)  # loading the json file in a object
        if limit == int(20) and skip == int(0):
            random.shuffle(data)
        for character in data[skip : limit + skip]:  # we iterate over the list and go,
            print()  # in each selected dict. and print each key and value inside.
            for key, value in character.items():
                print(f"{key.title()}: {value}")


get_characters()
