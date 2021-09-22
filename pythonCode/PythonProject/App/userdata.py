from App import app
from config import client
from flask import Flask,request,jsonify
from pymongo import MongoClient
from bson.json_util import dumps

#db = client.mydatabase
#collection = db.students
print("connection successfull")
mydabase= client['student']
collection = mydabase['student_info']

@app.route('/add', methods=['POST'])
def get_user():
    _json = request.get_json()
    print(_json)
    id=_json['_id']
    name =_json['name']
    _class = _json['class']
    #language = _json['language']
    if request.method =='POST':
        record = {
            "_id":id,
            "name":name,
            "class":_class
        }
        insert_record = collection.insert_one(record)
        return "value added",200
    else:
        return "value not added",500

@app.route("/retrive")
def get_display():
    user = collection.find()
    return dumps(user),200

@app.route("/retrive_single/<id>")
def get_single_retrive(id):
    user = collection.find({"_id":id})
    dict ={}
    for x in user:
        dict.update(x)
    return dumps(dict),200

@app.route("/delete/<id>",methods=['DELETE'])
def delete(id):
    user = collection.find({"_id":id})
    _json = request.get_json()
    if user != "" and request.method == 'DELETE':
        collection.delete_one({"_id":id})
        return "user delete successfull"
    else :
        return "unable delete"

@app.route("/update/<id>",methods=['PUT'])
def update(id):
    _json = request.get_json()
    filter = {'_id':id}
    for x in _json:
        collection.update_one(filter,{"$set":{x:_json[x]}})
    return "value updated",200
