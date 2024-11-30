from bson import ObjectId  # type: ignore
from pymongo.collection import Collection  # type: ignore
from typing import List, Dict, Union, Optional

def create_student(collection: Collection, student: Dict) -> str:
    """Creates a student record in the collection."""
    result = collection.insert_one(student)
    return str(result.inserted_id)

def list_students(collection: Collection, filters: Dict) -> List[Dict]:
    """Lists students from the collection with optional filters."""
    query = {}
    if "country" in filters:
        query["address.country"] = filters["country"]
    if "age" in filters:
        query["age"] = {"$gte": filters["age"]}
    
    # Retrieve and serialize documents
    students = collection.find(query)
    return [
        {
            "id": str(student["_id"]),
            "name": student["name"],
            "age": student["age"],
            "address": student["address"],
        }
        for student in students
    ]

def get_student(collection: Collection, student_id: str) -> Optional[Dict]:
    """Fetches a student by ID. Returns None if not found."""
    if not ObjectId.is_valid(student_id):
        return None
    student = collection.find_one({"_id": ObjectId(student_id)})
    # if student:
    #     student["id"] = str(student.pop("_id"))  # Convert ObjectId to string
    return student

def update_student(collection: Collection, student_id: str, updates: Dict) -> bool:
    """Updates a student by ID with the provided fields."""
    if not ObjectId.is_valid(student_id):
        return False
    result = collection.update_one({"_id": ObjectId(student_id)}, {"$set": updates})
    return result.matched_count > 0

def delete_student(collection: Collection, student_id: str) -> bool:
    """Deletes a student by ID. Returns True if deletion was successful."""
    if not ObjectId.is_valid(student_id):
        return False
    result = collection.delete_one({"_id": ObjectId(student_id)})
    return result.deleted_count > 0