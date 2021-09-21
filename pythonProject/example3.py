from pymongo import MongoClient
# from bson.son import SON
# import pprint
#
# myclient = MongoClient("mongodb://%s:%s@127.0.0.1" % ('admin', 'admin'))
# mydb = myclient['db']
# collection = mydb['test5']
#
# data = [
#     # {"x": 1, "animal": {"tags":["dog", "cat"]}},
#     # {"x": 2, "tags": ["cat"]},
#     # {"x": 2, "tags": ["mouse", "dog", "cat"]},
#     # {"x": 3, "tags": []},
#     {"fridge": {"india": {"MH": ["pune", "mumbai"]}}}
# ]
#
# result = collection.insert_many(data)
# pipeline = [
#     {
#         "$unwind": "$fridge.india.MH",
#     },
#     {"$group": {"_id": "$fridge.india.MH", "count": {"$sum": 1}}
#      },
#     {"$sort": SON([("count", 1), ("_id", 1)])
#      }
# ]
# for i in collection.aggregate(pipeline):
#     print(i)
# # res = collection.aggregate(
# #     [
# #         {
# #             "$group" :
# #                 {
# #                     "_id" : "$branch",
# #                     "num_lang" : {"$sum" : 1}
# #                 }
# #         }
# #     ]
# # )
# # for i in res:
# #     print(i)
# def get_numbers(n):
#     for i in range(1,n+1):
#         print(i)
#
# n = int(input())
# get_numbers(n)
# def o(b):
#     def i(*args,**kwargs):
#         print("args",args)
#         print("kwargs",kwargs)
#         b(*args)
#     return i
# @o
# def f():
#     print("No args")
#
# f()

# def count_digits(number):
#     count = 0
#     for i in str(number):
#         count += 1
#     return count
#
# print(count_digits(1234))

# def decor1(func):
#     def inner():
#         x = func()
#         print("X in decor2", x)
#         return x * x  # logic doing mul
#
#     return inner
#
#
# def decor(func):
#     def inner():
#         x = func()
#         print("X in decor 1st...", x)
#         return 2 * x  # multiplu with 2
#
#     return inner
#
#
# @decor1
# @decor
# def num():
#     return 10
#
# num()
# import pickle
#
#
# def storeData():
#     # intializing the data
#     pickel_dataset_1 = {"key": "john", "name": "fred", "age": 21, "pay": 400000}
#     pickel_dataset_2 = {"key": "jay", "name": "jay", "age": 50, "pay": 500000}
#
#     db = {}
#     db['john'] = pickel_dataset_1
#     db['jay'] = pickel_dataset_2
#     dbfile = open("examplepickle", "wb")
#     pickle.dump(db, dbfile)
#     dbfile.close()
#
#
# def loadData():
#     # for reading
#
#     dbfile = open("examplepickle", "rb")
#     db = pickle.load(dbfile)
#     for key in db:
#         print(key, "==>", db[key])
#     dbfile.close()
#
#
# if __name__ == '__main__':
#     storeData()
#     loadData()

# import json
# data = {
#     "name":"pradip",
#     "price":100
# }
# js = json.dumps(data)
# data1 = json.loads(js)
# print(type(js))
# print(type(data1))

# import xml.etree.ElementTree as ET
# mytree = ET.parse("sample.xml")
# myroot = mytree.getroot()
# print(myroot)
# print(myroot[0].tag)
#
# for x in myroot[0]:
#     print(x.tag, x.attrib)
#
# for x in myroot.findall("food"):
#     description = x.find('description').text
#     calories = x.find('calories').text
#     print(description,calories)

# XMLexample_stored_in_a_string ='''<?xml version ="1.0"?>
# <States>
#     <state name ="TELANGANA">
#         <rank>1</rank>
#         <neighbor name ="ANDHRA" language ="Telugu"/>
#         <neighbor name ="KARNATAKA" language ="Kannada"/>
#     </state>
#     <state name ="GUJARAT">
#         <rank>2</rank>
#         <neighbor name ="RAJASTHAN" direction ="N"/>
#         <neighbor name ="MADHYA PRADESH" direction ="E"/>
#     </state>
#     <state name ="KERALA">
#         <rank>3</rank>
#         <neighbor name ="TAMILNADU" direction ="S" language ="Tamil"/>
#     </state>
# </States>
# '''
#
# root = ET.fromstring(XMLexample_stored_in_a_string)
# for x in root.iter('neighbor'):
#     print(x.attrib)
#
# import xml.etree.ElementTree as ET
# mytree = ET.parse("x1.xml")
# myroot = mytree.getroot()
# for prices in myroot.iter('price'):
#     prices.text = str(float(prices.text)+10)
#     prices.set('newprices', 'yes')
# ET.SubElement(myroot[0], "tasty")
# for temp in myroot.iter('tasty'):
#     temp.text = str("YES")
# # poping the element
# print(myroot[2][0].attrib.pop('name'))
# # Delete
# print(myroot.remove(myroot[2]))
# mytree.write('modified.xml')
