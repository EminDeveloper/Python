from pymongo import MongoClient

# Provide the connection details
hostname = 'localhost'
port = 27017  # Default MongoDB port
username = 'rootuser'  # If authentication is required
password = 'rootpass'  # If authentication is required

# Create a MongoClient instance
client = MongoClient(hostname, port, username=username, password=password)
# Create or access a database
db = client["applogdb"]  # Replace "mydatabase" with your database name

# Create or access a collection
collection = db["allLogCollection"]  # Replace "logs" with your collection name

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

client.close()