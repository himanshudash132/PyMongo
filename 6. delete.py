import pymongo


if __name__ == "__main__":
    print("welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    # Create a new or switch databases 
    db = client["himanshu"]
    collection = db["mySamplecollectionforhimanshu"]
    # delete one 
    prev = {"Name":"Himanshu"}
    collection.delete_one(prev)
    # delete many
    de =collection.delete_many(prev) 
    print(de.deleted_count) # count the delete
