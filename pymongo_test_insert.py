def get_database():
	from pymongo import MongoClient
	import pymongo

	# Provide the mongodb atlas url to connect python to mongodb using pymongo
	CONNECTION_STRING = 'mongodb+srv://<username>:<password>@<cluster-name>.mongodb.net/myFirstDatabase'

	# Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
	from pymongo import MongoClient
	client = MongoClient(CONNECTION_STRING)

	# Create the database for our example (we will use the same database throughout the tutorial
	return client['user_shopping_list']
	
# Add this to execute only the called functions from other files
if __name__ == "__main__":	
	
	# Get the database
	dbname = get_database()

	# Create a new collection
	collection_name = dbname["user_1_items"]

	# Create the first document
	item_1 = {
	"_id" : "U1IT00001",
	"item_name" : "Blender",
	"max_discount" : "10%",
	"batch_number" : "RR450020FRG",
	"price" : 340,
	"category" : "kitchen appliance"
	}

	# Create the second document
	item_2 = {
	"_id" : "U1IT00002",
	"item_name" : "Egg",
	"category" : "food",
	"quantity" : 12,
	"price" : 36,
	"item_description" : "brown country eggs"
	}

	# Insert both the documents at once using insert_many()
	collection_name.insert_many([item_1,item_2])

	# Parsing date for the third document
	from dateutil import parser
	expiry_date = '2021-07-13T00:00:00.000Z'
	expiry = parser.parse(expiry_date)

	# Create document 3
	item_3 = {
	"item_name" : "Bread",
	"quantity" : 2,
	"ingredients" : "all-purpose flour",
	"expiry_date" : expiry
	}

	# Insert single document
	collection_name.insert_one(item_3)
