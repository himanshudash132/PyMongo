import pymongo


if __name__ == "__main__":
    print("welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    # Create a new or switch databases 
    db = client["himanshu"]
    collection = db["mySamplecollectionforhimanshu"]
    # Inset one 
    # dictionary = {"name":"himanshu","marks":90}
    # collection.insert_one(dictionary)
    # list of dictionaries

    # Inset Many
    insertthese = [
        {"_id":"1","Name":"Himanshu","Location":"Delhi","Marks":90},
        {"_id":"2","Name":"Sohan","Location":"bhubaneswar","Marks":90},
        {"_id":"3","Name":"Swati","Location":"Ahmedabad","Marks":90},
        {"_id":"4","Name":"chai","Location":"Banglore","Marks":100}
    ]
    collection.insert_many(insertthese)
    