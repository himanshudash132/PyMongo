import pymongo


if __name__ == "__main__":
    print("welcome to pyMongo")
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    print(client)
    # View all databases
    all_databases = client.list_database_names()
    print(all_databases)
    # Show Collections
    col = client["himanshu"]
    print(col.list_collection_names())
