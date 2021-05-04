import os
import json
import requests
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "cocktails"
COLLECTION = "ingredients"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]
count = 600

for i in range(616):
        response = requests.get(
        "https://www.thecocktaildb.com/api/json/v1/1/lookup.php?iid={}"
                .format(count))
        count += 1
        drink_list = response.json()
        for g in drink_list["ingredients"]:
            print(g)
            coll.insert_one(g)