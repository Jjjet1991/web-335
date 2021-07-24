#
#=====================================================
# Title: Assignment 9.3 Updating and Deleting Documents
# Author: Professor Krasso
# Date: 25 July 2021
# Modified By: Jourdan Neal
# Description: Updating and deleting documents from a collection with Python.
#=====================================================
#

# Import Statements
import pymongo
import pprint
import datetime

# Connect to MongoDB
from pymongo import MongoClient
client = MongoClient('localhost', 27017)
print(client)
db = client.web335

# Update Captain Hook employee_id 123457, email to Bellevue email address
db.users.update_one(
    {"employee_id" : "1234567"},
    {
        "$set":{
            "email": "janeal@my65@bellevue.edu"
        }
    }
)
# Print updated document.
pprint.pprint(db.users.find_one({"employee_id": "1234567"}))

result = db.users.delete_one({
    "employee_id": "765321"
})
print(result)
pprint.pprint(db.users.find_one({"employee_id": "765321"}))
pprint.pprint(db.users.find_one({"email": "janeal@my65@bellevue.edu"}))
#pprint.pprint(db.users.find_one({"first_name": "Maleficent"}))
#pprint.pprint(db.users.find_one({"lastName": "Hook"}))