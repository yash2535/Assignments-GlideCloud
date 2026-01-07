from pymongo import MongoClient
from dotenv import load_dotenv
import os

# load .env file
load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

# 🔒 SAFETY CHECK (VERY IMPORTANT)
if not DB_NAME:
    raise ValueError("DB_NAME is not set in .env file")

if not MONGO_URI:
    raise ValueError("MONGO_URI is not set in .env file")

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

student_collection = db.students
