from pydantic import BaseModel
from typing import Optional, Dict

class Address(BaseModel):
    city: Optional[str] = None
    country: Optional[str] = None

class Student(BaseModel):
    name: str
    age: int
    address: Address

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    address: Optional[Address] = None