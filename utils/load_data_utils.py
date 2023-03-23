import os
import json
from datetime import datetime
from pymongo import MongoClient
from providers_utils import get_mongo_client
from id_utils import *

# Get the path to the JSON file one level above the current directory
dirname = os.path.dirname(os.path.abspath(__file__))
json_path = os.path.join(dirname, '..', 'resources', 'courses.json')

# Load the JSON file
with open(json_path) as f:
    data = json.load(f)

# Add the three attributes to each item
for item in data:
    item['_id'] = get_course_id()
    item['is_active'] = True
    item['created_at'] = datetime.now()
    item['modified_at'] = datetime.now()
    for chapter in item['chapters']:
        chapter['_id'] = get_chapter_id(item['_id'])

# Connect to MongoDB and insert the items
client = get_mongo_client()
db = client['courseMDb']
collection = db['courses']
# Adding index
course_collection.create_index([("chapters._id", pymongo.ASCENDING)])
collection.insert_many(data)

# Close the MongoDB connection
client.close()
