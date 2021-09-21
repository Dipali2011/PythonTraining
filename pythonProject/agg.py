from pymongo import MongoClient
myclient =MongoClient()
mydata = myclient["database"]
mycollection = mydata["mytable2"]

profiles = [
    {"x":1,"title":["dog","cat"]},
    {"x":2,"title":["cow","dog"]},
    {"x":2,"title":["mouse","cat","dog"]},
    {"x":3,"title":[]}
]

result = mycollection.insert_many(profiles)
from bson.son import SON

pipeline = [
    {
        "$unwind":"$title"
    },
    {
        "$group":{"_id":"$title","count":{"$sum":1}}
    },
    {
        "$sort":SON([("count",-1),("_id",-1)])
    }
]

import pprint
pprint.pprint((list(mycollection.aggregate(pipeline))))