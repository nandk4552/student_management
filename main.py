from typing import Optional
from fastapi import FastAPI, HTTPException, Query, Path
from models import Student, UpdateStudent
from crud import create_student, get_student, update_student, delete_student
from config import students_collection

app = FastAPI()

# Convert MongoDB documents to JSON serializable format
def serialize_student(student):
    if "_id" not in student:
        raise KeyError("The document does not contain '_id'")
    
    return {
        "id": str(student["_id"]),  # Convert `_id` to `id`
        "name": student.get("name", ""),
        "age": student.get("age", 0),
        "address": student.get("address", {}),
    }

# CREATE STUDENT || POST || http://localhost:8000/students/
@app.post("/students", status_code=201)
async def create_students(student: Student):
    # Use `model_dump()` to convert Pydantic model to a dictionary
    student_data = student.model_dump()
    student_id = create_student(students_collection, student_data)
    return {"id": student_id}



# LIST OF STUDENTS DETAILS BY PARAMS || GET || http://localhost:8000/students?country=India&age=20
@app.get("/students")
async def list_students(country: Optional[str] = Query(None), age: Optional[int] = Query(None)):
    query = {}

    if country:
        query["address.country"] = country
    if age is not None:
        query["age"] = {"$gte": age}

    # Fetch matching students from MongoDB
    students = students_collection.find(query)

    # Serialize MongoDB documents
    serialized_students = [serialize_student(student) for student in students]

    return {"data": serialized_students}

# GET STUDENT DETAILS BY ID || GET || http://localhost:8000/students/:id
@app.get("/students/{id}")
async def fetch_student(id: str = Path(...)):
    student = get_student(students_collection, id)
    print(student)
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    
    # Ensure `_id` is present before serialization
    serialized_student = serialize_student(student)
    return serialized_student

# UPDATE STUDENT BY ID || PATCH || http://localhost:8000/students/:id
@app.patch("/students/{id}", status_code=204)
async def update_students(id: str, updates: UpdateStudent):
    # Use `model_dump()` to get the dictionary of updates
    update_data = updates.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(status_code=400, detail="No fields to update")
    update_success = update_student(students_collection, id, update_data)
    if not update_success:
        raise HTTPException(status_code=404, detail="Student not found")
    return

# DELETE STUDENT BY ID || DELETE || http://localhost:8000/students/:id
@app.delete("/students/{id}", status_code=200)
async def delete_students(id: str):
    delete_success = delete_student(students_collection, id)
    if not delete_success:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)