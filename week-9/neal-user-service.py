#
#=====================================================
# Title: Assignment 9.2 Querying and Creating Documents
# Author: Professor Krasso
# Date: 25 July 2021
# Modified By: Jourdan Neal
# Description: Creating documents and querying documents using Python.
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

# Creating new user.
user = {
    "first_name": "Maleficent",
    "last_name": "DarkQueen",
    "email": "sleepyspindle@evil.net",
    "employee_id": "6789101",
    "date_created": datetime.datetime.utcnow()
}

# Inserting users to the users collection.
user_id = db.users.insert_one(user).inserted_id

# Print user info. 
print(user_id)

# Print all 3 added documents from the find_one query, querying documents by employee-id.
pprint.pprint(db.users.find_one({"employee_id": "1234567"}))
pprint.pprint(db.users.find_one({"employee_id": "7654321"}))
pprint.pprint(db.users.find_one({"employee_id": "6789101"}))

