from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models import Base
from app.database import engine, get_db
from app.schemas import UserCreate, User, TaskCreate, Task
from app.crud import create_user, create_task, get_tasks, update_task, delete_task

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
async def root():
    return {
        "message": "Welcome to FastAPI CRUD Application",
        "docs": "Visit /docs for API documentation"
    }

@app.post("/users/", response_model=User)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)

@app.post("/users/{user_id}/tasks/", response_model=Task)
def create_user_task(user_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db=db, task=task, user_id=user_id)

@app.get("/tasks/", response_model=list[Task])
def read_tasks(db: Session = Depends(get_db)):
    tasks = get_tasks(db)
    return tasks

@app.put("/tasks/{task_id}", response_model=Task)
def update_existing_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    return update_task(db=db, task_id=task_id, task=task)

@app.delete("/tasks/{task_id}", response_model=Task)
def delete_existing_task(task_id: int, db: Session = Depends(get_db)):
    return delete_task(db=db, task_id=task_id)