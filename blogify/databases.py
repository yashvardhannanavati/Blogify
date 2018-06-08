from pymongo import MongoClient
# Change this to Prod when deployed
from blogify.config import DevConfig

client = MongoClient(DevConfig.MONGO_URI)
