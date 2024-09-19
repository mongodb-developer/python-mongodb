# Notice: Repository Deprecation
This repository is deprecated and no longer actively maintained. It contains outdated code examples or practices that do not align with current MongoDB best practices. While the repository remains accessible for reference purposes, we strongly discourage its use in production environments.
Users should be aware that this repository will not receive any further updates, bug fixes, or security patches. This code may expose you to security vulnerabilities, compatibility issues with current MongoDB versions, and potential performance problems. Any implementation based on this repository is at the user's own risk.
For up-to-date resources, please refer to the [MongoDB Developer Center](https://mongodb.com/developer).

# python-mongodb
Contains details on how we use pymongo to connect python with mongodb

# Prerequisites
Download and install Python on your machine (in this example: Windows). To confirm if your installation is right, type ‘python’ in your command line window. You should get:
```bash
Python 3.9.0 (tags/v3.9.0:9cf6752, Oct  5 2020, 15:34:40) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

We recommend that you set up a **MongoDB Atlas free tier cluster** for this tutorial. 

# Connecting Python and MongoDB Atlas
PyMongo has a set of packages for Python MongoDB interaction.
To install PyMongo, open command line and type:
```bash
python -m pip install pymongo
```

###### Tip: If you are getting “ModuleNotFoundError: No module named 'pymongo'” error, uninstall pymongo. 
Use 
```bash
pip uninstall pymongo 
```
command. Then, re-install using the installation command.
For this python mongodb tutorial, we use mongodb srv URI, so let’s install dnspython:
```bash
python -m pip install dnspython
```

Now, we can use pymongo as a python mongodb library in our code with an import statement.

# Creating a database in Python MongoDB
First, get the client using the connection string. Then, create the database from the client using the database name.
```python
from pymongo import MongoClient
import pymongo

# Provide the mongodb atlas url to connect python to mongodb using pymongo
CONNECTION_STRING = 'mongodb+srv://m001-student:m001-mongodb-basics@sandbox.qurli.mongodb.net/myFirstDatabase'

# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
from pymongo import MongoClient
client = MongoClient(CONNECTION_STRING)

# Create the database for our example (we will use the same database throughout the tutorial
return client['user_shopping_list']

dbname = get_database()
```

# Creating a collection in Python MongoDB

To create a collection, pass the collection name to the database. Make sure to have the right indentation while copying the code to your .py file.
```python
collection_name = dbname["user_1_items"]
```

# Inserting documents in Python MongoDB
For inserting many documents at once, use the pymongo insert_many() method.
```python
item_1 = {
"_id" : "U1IT00001",
"item_name" : "Blender",
"max_discount" : "10%",
"batch_number" : "RR450020FRG",
"price" : 340,
"category" : "kitchen appliance"
}

item_2 = {
"_id" : "U1IT00002",
"item_name" : "Egg",
"category" : "food",
"quantity" : 12,
"price" : 36,
"item_description" : "brown country eggs"
}
collection_name.insert_many([item_1,item_2])
```

Let us insert a third document without specifying the _id field. This time we add a field of data type ‘date’. To add date using pymongo, use the python dateutil package. ISODate will not work with Python, as it is a Mongo shell function. 
Install the package using the following command: 
```bash
python -m pip install python-dateutil
```
Add the following to pymongo_test.py:
```python
from dateutil import parser
expiry_date = '2021-07-13T00:00:00.000Z'
expiry = parser.parse(expiry_date)
item_3 = {
"item_name" : "Bread",
"quantity" : 2,
"ingredients" : "all-purpose flour",
"expiry_date" : expiry
}
collection_name.insert_one(item_3)
```

We use the insert_one() method to insert a single document.
Open the command line and navigate to the folder where you have saved pymongo_test_insert.py. Execute the file using the  python pymongo_test_insert.py command.

# Querying in Python MongoDB 
To query, we use the find() method.
```python
dbname = get_database()

# Create a new collection
collection_name = dbname["user_1_items"]

item_details = collection_name.find()
for item in item_details:
	# This does not give a very readable output
	print(item)
```	
	
# Indexing in Python MongoDB
Let us create a single index on the ‘category’ field. 
```python
category_index = collection_name.create_index("category")
```
# Disclaimer
This software is not supported by MongoDB, Inc under any of their commercial support subscriptions or otherwise. Any usage is at your own risk.
