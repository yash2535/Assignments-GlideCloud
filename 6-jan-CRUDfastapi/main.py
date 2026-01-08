from fastapi import FastAPI
from routes.student import student_router

app = FastAPI(title="Student Management System")

app.include_router(
    student_router,
    prefix="/students",
    tags=["Students"]
)
