from pymongo import MongoClient # import mongo client to connect
client = MongoClient("mongodb://%s:%s@127.0.0.1" %('admin', 'admin'))

# Creating database
db = client.exam
employee = {"id": "10",
"name": "Peter",
"profession": "Software Engineer",
}
# Creating document
employees = db.employees
# Inserting data
employees.insert_one(employee)
# Fetching data
print(employees.find_one())
