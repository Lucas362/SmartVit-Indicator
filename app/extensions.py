from flask_pymongo import PyMongo, MongoClient

client = MongoClient('mongodb://indicators-mongodb:27017/', username='admin', password='password')
db = client.smartDevApiService