import pymongo as pm
conn = pm.MongoClient("mongodb://localhost:27017")
db = conn["aggregate"]
collection = db["faculty"]

def add_new_faculty():
    data = {
        
    "name" : "Joy",
    "age" : 21.0,
    "gender" : "M",
    "exp" : 12.0,
    "address" : {
        "city" : "Bangalore",
        "state" : "Karnataka"
    },
    "subjects" : [ 
        "JAVA", 
        "DBMS"
    ],
    "type" : "Full Time",
    "qualification" : "Ph.D",
    "rating" : [ 
        5.0, 
        6.0, 
        7.0
    ],
    "deptno" : 10.0,
    "salary" : 100000.0,
    "bonus" : 5000.0


    }
    collection.insert_one(data)
    
    
def add_subject_to_faculty():
    collection.update_one({"name":"Joy"},{"$push":{"subjects":"React"}})
    
def remove_subject_from_faculty():
    collection.update_one({"name":"Joy"},{"$pull":{"subjects":"React"}})
def increment_exp_by_one_year():
    collection.update_one({"name":"Joy"},{"$inc":{"exp":1}})
def update_qualification():
    collection.update_one({"name":"Joy"},{"$set":{"qualification":"Nobel"}})

def subject_with_faclty_name():
    db.collection.aggregate([
        
       {"$project":{"name":1,"subjects":1,"_id":0}}
    ])
def delete_faculty():
    collection.remove({"name":"Joy"})