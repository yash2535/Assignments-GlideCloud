from fastapi import APIRouter, HTTPException
from schema.student_schema import Student
from crud.student_crud import (
    create_student,
    get_all_students,
    get_student,
    update_student,
    delete_student
)

student_router = APIRouter()

# CREATE
@student_router.post("/")
def add_student(student: Student):
    return create_student(student.model_dump())


# READ ALL
@student_router.get("/")
def fetch_students():
    return get_all_students()

# READ ONE
@student_router.get("/{prn}")
def fetch_student(prn: int):
    student = get_student(prn)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# UPDATE
@student_router.put("/{prn}")
def modify_student(prn: int, student: Student):
    return update_student(prn, student.model_dump())

# DELETE
@student_router.delete("/{prn}")
def remove_student(prn: int):
    return delete_student(prn)
