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


@app.route("/add_new_character", methods=["POST"])
def add_new_character():
    try:
        new_character = request.get_json() #check if json data is in Postman request
        if not new_character:
            return jsonify({"error": "No data provided"}), 400
        with open("data/characters.json", "r") as file: #loads existing data from the json file
            data = json.load(file)

        for key, value in new_character.items():
            if key == "id" and (value == "" or value is None):
                continue
        if not value:  # if fields are empty
            return jsonify({"error": "You need to fill out every category."}), 400

        if new_character in data:
            return jsonify({"error": "Character already exists."}), 400

        new_id = data[-1]["id"] + 1 if data else 1 #creating new ID for new character
        new_character["id"] = new_id
        data.append(new_character)
        return jsonify({"message": "Character added successfully.", "data": new_character}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/edit_character", methods=["POST"])
def edit_character():
    



#Im try block versuchen wir ein code auszuführen
#in dem fall oben wenn value leer ist gebe mir ein error
#die Bedingung das ein Except Block ausgeführt wird, 
# ist ein Python Error im Try Block
#der except block wird ausgeführt wenn im try block ein python error entsteht


if __name__ == "__main__":
    app.run(debug=True)
