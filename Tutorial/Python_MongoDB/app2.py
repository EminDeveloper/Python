import pymongo

# Establish a connection to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB connection string

# Create or access a database
db = client["mydatabase"]  # Replace "mydatabase" with your database name

# Create or access a collection
collection = db["logs"]  # Replace "logs" with your collection name

# Data to be logged
log_data = {
    "timestamp": "2024-01-01 12:00:00",
    "message": "Logging this message into MongoDB!"
}

# Insert the log data into the collection
insert_result = collection.insert_one(log_data)

# Check if the insertion was successful
if insert_result.acknowledged:
    print("Log inserted successfully. ObjectId:", insert_result.inserted_id)
else:
    print("Log insertion failed.")
