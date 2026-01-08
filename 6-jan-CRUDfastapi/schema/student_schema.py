from pydantic import BaseModel

class Student(BaseModel):
    prn: int
    name: str
    age: int
    contact: int
