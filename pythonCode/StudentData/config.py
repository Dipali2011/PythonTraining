from pymongo import MongoClient

"""
DEBUG = True
client = MongoClient()
DATABASE =client['restfulapi'] # DB_NAME
"""
client = MongoClient("mongodb://localhost:27017/")
DATABASE = client["mydatabase"]


