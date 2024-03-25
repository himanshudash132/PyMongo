import pymongo


connectionString = "mongodb+srv://username:password@cluster0.gbfcu.mongodb.net/test"


def insertDocument():
    studentInfo = {
        "name": "Drake",
        "section": 2,
        "maths_marks": 35,
        "sst_marks": 79
    }
    student_id = collection.insert_one(studentInfo).inserted_id
    print(f"Student with id {student_id} has been created")


def readDocuments():
    # Inserting a Document
    # Reading a Collection
    # Using find function 
    myStudents = collection.find({"section": 1, "name": "Harry"})
    # print(myStudents)
    for student in myStudents:
        print(student)
    # Using findOne function 
    myStudent = collection.find_one({"section": 1})
    print(myStudent) 


def updateDocuments():
    collection.update_one({"section": 1}, {'$inc': {'section': 100}})
    collection.update_many({}, {'$inc': {'section': 100}})


def deleteDocuments():
    r = collection.delete_one({"section": 101})
    print(r.deleted_count)
    r = collection.delete_many({})
    print(r.deleted_count)
    collection.update_many({})



if __name__ == '__main__':
    client = pymongo.MongoClient(connectionString)
    # Creating a Database for a School
    db = client['wisdom-academy'] 

    # Creating a Collection
    collection = db.class1
    
    # CRUD: Create, Read, Update, Delete
    # 1. Create
    # insertDocument()

    # 2. Read
    # readDocuments()

    # 3. Update 
    # updateDocuments()

    # 4. Delete 
    # deleteDocuments()