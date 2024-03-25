import pymongo


if __name__ == "__main__":
    print("welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    db = client["himanshu"]
    collection = db["mySamplecollectionforhimanshu"]
    # only find one
    # one = collection.find_one({"Name":"Swati"})
    # print(one)

    # find all
    # alldoc = collection.find({"Name":"Himanshu"})
    # for i in alldoc:
    #     print(i)

    # only print what i want--> 1 excude-->0
    # alldoc = collection.find({"Name":"Swati"},{"Name":1,"_id":0}).limit(1)
    # alldoc = collection.find({"Name":"Swati"},{"Name":1,"_id":0})
    alldoc = collection.find({"Name":"Swati","Marks":{"$lte":90}},)
    print(collection.count_documents({}))
    for i in alldoc:
        print(i)    

    