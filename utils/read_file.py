import json
import os

def get_ingredients():
    path = os.path.dirname(os.path.abspath(__file__)) + "/../data/ingredients.json"
    with open(path, "r", encoding="utf-8") as f:
        ingredients = json.load(f)
    return ingredients