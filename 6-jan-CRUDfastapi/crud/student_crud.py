from database.connection import student_collection
from models.student_models import student_model

# CREATE
def create_student(student: dict):
    student_collection.insert_one(student_model(student))
    return {"message": "Student created successfully"}

# READ ALL
def get_all_students():
    return list(student_collection.find({}, {"_id": 0}))

# READ ONE
def get_student(prn: int):
    return student_collection.find_one({"prn": prn}, {"_id": 0})

# UPDATE
def update_student(prn: int, data: dict):
    student_collection.update_one(
        {"prn": prn},
        {"$set": data}
    )
    return {"message": "Student updated successfully"}

# DELETE
def delete_student(prn: int):
    student_collection.delete_one({"prn": prn})
    return {"message": "Student deleted successfully"}
