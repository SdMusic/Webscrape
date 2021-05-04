import os
import json
import requests
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "cocktails"
COLLECTION = "cat_whiskey"

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
    "https://www.thecocktaildb.com/api/json/v1/1/filter.php?i=blended%20whiskey")
drink_list = response.json()

for i in drink_list['drinks']:
    i["category_name"] = "Whiskey"
    coll.insert_one(i)