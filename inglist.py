import os
import json
import requests
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "cocktails"
COLLECTION = "drinks"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]


response = requests.get(
    "https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=Tequila")
drink_list = response.json()
new_list = []
full_ing = []
ctr = 0

for i in drink_list['drinks']:
    new_list.append(i)

for j in new_list:
    for k in j:
        x = j.get("idDrink")
        drink_id = requests.get(
            "https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={}"
            .format(x))
        drink_id_list = drink_id.json()
        for h in drink_id_list["drinks"]:
            ctr += 1
            cat = {"category_name": "Tequila"}
            if ctr % 3 == 0:
                full_ing.append(h)
                h["category_name"] = "Vodka"
                coll.insert_one(h)
