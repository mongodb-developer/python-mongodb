# Get the database using the method we defined in pymongo_test_insert file 
from pandas import DataFrame
from pymongo_get_database import get_database
dbname = get_database()

# Create a new collection
collection_name = dbname["user_1_items"]

item_details = collection_name.find()

# List items without formatting
for item in item_details:
	print(item)

# This will give readable output, but KeyError
for item in item_details:
	print(item['item_name'], item['category'])

# Use pandas for formatting
# Convert the dictionary objects to dataframe
items_df = DataFrame(item_details)

# View all items
print(items_df)	

