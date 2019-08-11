from pymongo import MongoClient

conn = MongoClient("mongo.db://localhost:")

def add_new_faculty():
    f=add({
        "name":"Boi",
        "qualification":"M.tech",
        "subjects":[{
        }],
        "exp":12
    }
    col_name = db["faculty"]

    })

def add_subject_to_faculty():
    add =  faculty.updateOne(
        {"subject":1"}

    })  

    }
def remove_subject_from_faculty():
    d = db.facutly.remove({"subject":})

def increment_exp_by_one_year():
    c_name = db
    inc = db.faculty.updateMany({},{$inc:{"age":1}})

def update_qualification():
    c_name = db["faculty"]
    x = collection.updateOne({"name":f_name},{"$set":{"qualification":}})
    print(f"{qualification}")

def total_duration_by_faculty():
    dur = collection.updateOne({})

def subject_with_faclty_name():
    c_name = db["faculty"]
    x = collection.

def delete_faculty():
    c_name = db["faculty"]
    x = collection.remove({},{"name":f_name})
    print(f"{f_name}s data has been deleted")

def show_faculty_t_duration():
    c_name = db["faculty"]
    query = [
    ]