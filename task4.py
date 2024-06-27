from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb_url')
db = client['database_name']
collection = db['collection_name']

document = {
    'data': 'some_data',
    'createdAt': datetime.now()
}

collection.insert_one(document)


collection.create_index('createdAt', expireAfterSeconds=86400)
