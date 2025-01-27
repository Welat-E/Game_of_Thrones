from flask import Flask, jsonify, request
import json
import random
from operator import itemgetter

app = Flask(__name__)


@app.route("/get_all_characters", methods=["GET"])
def get_all_characters():
    get_characters_lst = []
    try:
        match = False
        limit = request.args.get("limit")
        skip = request.args.get("skip")
        if limit == "" and skip == "":
            limit = int(20)
            skip = int(0)
            match = True
        elif limit != "" and skip != "":
            limit = int(limit)
            skip = int(skip)
        else:
            raise Exception
    except:
        return jsonify("Both must be filled with integer or should be empty.")
    with open("data/characters.json", "r") as file:
        data = json.load(file)  # loading the json file in a object
        if match: #match == True means in this case that there no user entry for skip and limit because we defined it on line 16-19 
            random.shuffle(data)  #it shuffles the data
        for character in data[skip : limit + skip]:  # we iterate over the list
            get_characters_lst.append(character)
    return jsonify(get_characters_lst)

@app.route("/get_character_by_id", methods=["GET"])
def get_character_by_id():
    character_id = request.args.get("id")
    with open("data/characters.json", "r") as file:
        data = json.load(file)
        for character in data:
            if str(character["id"]) == character_id:
                return jsonify(character)

    return jsonify({"error": "Character not found"}), 404


@app.route("/filter_characters", methods=["GET"])
def filter_characters():
    filtered_character = []
    filter_dict = request.args  # postman query parameters saved as ImmutableMultiDict.
    sort_by = request.args.get("sort_by")
    sort_by_desc = request.args.get("sort_by_desc")
    with open("data/characters.json", "r") as file:
        data = json.load(file)
        for character in data:  # iterate over the List of dict.
            match = True
            for key, value in filter_dict.items():  # iterate over dict.
                try:
                    if key in character and str(character[key]).lower() == value.lower() and match: #"and match" means if match == True
                        continue
                    elif key == "age_more_than" and value: #and value means if something is inside
                        if character.get("age") is None or character["age"] < int(value):
                            match = False
                    elif key == "age_less_than" and value:
                        if character.get("age") is None or character["age"] > int(value):
                            match = False
                    elif key != "sort_by" and key != "sort_by_desc":
                        match = False
                except Exception as e:
                    return jsonify((f"{e} Please use integers."))
            if match: #if match == true than...
                filtered_character.append(character)    
        if sort_by:
            if sort_by not in data[0]:
                return jsonify({"error": f"Invalid field '{sort_by}' for sorting"}), 400
            filtered_character = sorted(filtered_character, key=lambda x: (x.get(sort_by) is not None, x.get(sort_by)))
        if sort_by_desc:
            if sort_by_desc not in data[0]:
                return jsonify({"error": f"Invalid field '{sort_by_desc}' for sorting"}), 400
            filtered_character = sorted(filtered_character, key=lambda x: (x.get(sort_by_desc) is not None, x.get(sort_by_desc)),reverse=True)

        return jsonify(filtered_character)

    return jsonify({"error": "Character list not found"}), 404


@app.route("/add_new_character", methods=["GET"])
def add_new_character():
    new_character = request.args  
    with open("data/characters.json", "r") as file:
        data = json.load(file)
        try:
            for key, value in new_character.items():
                if value == "":
                    raise Exception("You need to fill out every category.")
            if new_character not in data: # you only need one check if new_charac in data is
                data.append(new_character)
            return jsonify(data)
        except Exception as e:
            return jsonify(f"{e}")                



#Im try block versuchen wir ein code auszuführen
#in dem fall oben wenn value leer ist gebe mir ein error
#die Bedingung das ein Except Block ausgeführt wird, 
# ist ein Python Error im Try Block
#der except block wird ausgeführt wenn im try block ein python error entsteht


if __name__ == "__main__":
    app.run(debug=True)
