# install the mongodb on local
# # checked cli by using mongo --host
#
# # 1. Database up and running
# # python,  + mongo ===> pymongo
#
# # 1. connect to mongodb using python
#
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# def main():
#     try:
#         myclient = MongoClient("mongodb://%s:%s@127.0.0.1" %('admin', 'admin'))
#         print("connection successful", myclient)
#
#         # list down the databases
#         list_of_db = myclient.list_database_names()
#         print("databases available in mongodb", list_of_db)
#
#         # create new database in mongodb
#         mydb = myclient['test']
#         print("Database created...", mydb)
#         # #create collection
#         # collection = mydb['student']
#         # record = {
#         #     "_id":0,
#         #     "name": "raj",
#         #     "roll_number": 101,
#         #     "branch": "cse",
#         #     "marks": 40
#         #
#         # }
#         # record_1 = collection.insert_one(record)
#         # print("records", record_1)
#         #
#         # # list down the databases
#         # list_of_db = myclient.list_database_names()
#         # print("databases available in mongodb after creation", list_of_db)
#
#         records = {
#             "record1":{
#                             "_id": 17,
#                             "name": "rohan",
#                             "roll_number": 103,
#                             "branch": "cse",
#                             "marks": 45
#                         },
#         "record2":{
#                         "_id": 18,
#                         "name": "ram",
#                         "roll_number": 104,
#                         "branch": "cse",
#                         "marks": 55
#                     }
#         }
#         # #create collection
#         # collection = mydb['student']
#         # for record in records.values():
#         #     collection.insert_one(record)
#         mylist = [
#            {
#                           "_id": 19,
#                           "name": "john",
#                           "roll_number": 103,
#                           "branch": "cse",
#                           "marks": 45
#                       },
#            {
#             "_id": 20,
#             "name": "jenny",
#             "roll_number": 108,
#             "branch": "cse",
#             "marks": 55
#         },
#             {
#                 "_id": 21,
#                 "name": "joe",
#                 "roll_number": 105,
#                 "branch": "cse",
#                 "marks": 55
#             }
#
#         ]
#
#         collection = mydb['student']
#         #collection.insert_many(mylist)
#
#         # 3 find the  document display document or retreive
#         x = collection.find_one()
#         #print("record", x)
#
#         # all_document = collection.find()
#         # for each_record in all_document:
#         #     print("doc", each_record)
#
#         # for x in collection.find({}, {"_id":0, "name":1, "branch":1}):
#         #     print("Only fields with 1", x)
#
#         # curson = collection.find({"marks":{"$lt":45}})
#         # print("Marks greter than 45 are")
#         # for i in curson:
#         #     print(i)
#
#         curson = collection.find({"marks": {"$lt": 45}})
#
#         mydoc = collection.find().sort("marks",-1)
#         for x in mydoc:
#             print(x)
#     except ConnectionFailure as e:
#         print("error", e)
#
# if __name__ == '__main__':
#     main()
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

myclient = MongoClient("mongodb://%s:%s@127.0.0.1" % ('admin', 'admin'))
print("connection successful", myclient)

# list down the databases
list_of_db = myclient.list_database_names()
print("databases available in mongodb", list_of_db)

# create new database in mongodb
mydb = myclient['test']
print("Database created...", mydb)
collection = mydb['student']
curson = collection.find({"marks": {"$gt": 45}})
print("The records greater than 45")
# for record in curson:
#   print("records:%s" % record)

cursor = collection.find({"marks": {"$lt": 45}})
print("The records less than 45")
# for record in cursor:
#    print("records:%s" % record)

# search or display records in between

# ob = collection.find({"$and":[{"marks":{"$gt":40}}, {"marks":{"$lt":50}}]})
# print("And conditions records")
# for record in ob:
#    print("records", record)

ob = collection.find({"$and":[{"marks":{"$gt":40}}, {"marks":{"$lt":50}}]})
print("And conditions records")
for record in ob:
   print("records", record)

# sorting
mydoc = collection.find().sort("name")
for x in mydoc:
   print("sorting..", x)
mydoc = collection.find().sort("name", -1)
for x in mydoc:
     print("sorting..", x)

# 1. connectivity to mongodb
# 2. create database in mongodb
# 3. create collections in mongodb
# 4. insert - insert_one, insert_many
# 5. find - find_one, find
# 6. find- display particular attributes records
# 7. find -- conditional formating using and or gt, lt
# home work explore operator in pymongo
# 8. Sorting how to sort on fields of the documents
