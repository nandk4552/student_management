from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI") 
client = MongoClient(MONGO_URI)
db = client["student_management"]  
students_collection = db["students"]