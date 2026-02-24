from pymongo import MongoClient
from Config import MONGO_URL, DB_NAME

client = MongoClient(MONGO_URL)
db = client[DB_NAME]

users_col = db["users"]
history_col = db["history"]
watchlater_col = db["watchlater"]
