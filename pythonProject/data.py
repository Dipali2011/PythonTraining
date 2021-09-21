from pymongo import MongoClient
myclient = MongoClient("mongodb://%s:%s@127.0.0.1" %('admin', 'admin'))
mydata = myclient["database"]
mycollection = mydata["mytable1"]

profiles = [
    {"x":1,"title":["dog","cat"]},
    {"x":2,"title":["cow","dog"]},
    {"x":2,"title":["mouse","cat","dog"]},
    {"x":3,"title":[]}
]

mycollection.insert_many(profiles)

agg_result = mycollection.aggregate(
    [
        {
            "$group":
                {
                    "_id":"$x",
                     "titles":{"$sum":1}
                }
       }
   ]
)
print("result:\n")
for i in agg_result:
   print(i)