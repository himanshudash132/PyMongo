import pymongo


if __name__ == "__main__":
    print("welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    # Create a new or switch databases 
    db = client["himanshu"]
    collection = db["mySamplecollectionforhimanshu"]
    # Update one 
    prev = {"Name":"Himanshu"}
    nextt = {"$set":{"Location":"Mumbai"}}
    collection.update_one(prev,nextt)
    # Update many
    up = collection.update_many(prev,nextt) 
    print(up.modified_count) # count the update
