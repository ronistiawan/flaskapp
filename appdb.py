import pymongo
from bson.objectid import ObjectId
from instance.config import MONGODB_CONNECTION_STRING

db = pymongo.MongoClient(MONGODB_CONNECTION_STRING).flaskapp
