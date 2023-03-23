import pymongo
import certifi
from dotenv import load_dotenv
import os


load_dotenv()
ca = certifi.where()

def get_mongo_client():
    # Access environment variables
    mongoURI = os.getenv('MONGOURI')
    client = pymongo.MongoClient(mongoURI, tlsCAFile=ca)
    return client

