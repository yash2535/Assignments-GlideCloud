# FastAPI Student Management CRUD API

A **Student Management System API** built using **FastAPI** that performs full **CRUD operations** with **MongoDB** as the database.  
The project follows a **modular folder structure**, uses **environment variables** for configuration, and includes **automated API testing with pytest**.

---

##  Tech Stack
- FastAPI
- Python
- MongoDB
- PyMongo
- Pydantic
- pytest

---

## Features
- Create, Read, Update, Delete students
- RESTful APIs with Swagger documentation
- MongoDB database integration
- `.env` file for secure configuration
- Modular and scalable project structure
- API testing using pytest

---

##  Student Schema
- **PRN**: int  
- **Name**: string  
- **Age**: int  
- **Contact**: int  

---

## How to Run

uvicorn main:app --reload
