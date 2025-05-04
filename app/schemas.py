from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class UserBase(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, example="John Doe")
    email: EmailStr = Field(..., example="john@example.com")

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=2, max_length=50, example="John Smith")
    email: Optional[EmailStr] = Field(None, example="john.smith@example.com")

class User(UserBase):
    id: int
    
    class Config:
        from_attributes = True 
        json_schema_extra = {
            "example": {
                "id": 1,
                "name": "John Doe",
                "email": "john@example.com"
            }
        }

class TaskBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=100, example="Complete project")
    description: str = Field(..., example="Finish the FastAPI CRUD implementation")

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=100)
    description: Optional[str] = None
    user_id: Optional[int] = None

class Task(TaskBase):
    id: int
    user_id: int
    owner: User 
    
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "Complete project",
                "description": "Finish the FastAPI CRUD implementation",
                "user_id": 1,
                "owner": {
                    "id": 1,
                    "name": "John Doe",
                    "email": "john@example.com"
                }
            }
        }