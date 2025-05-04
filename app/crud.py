from sqlalchemy.orm import Session
from app.models import User, Task

# User CRUD
def create_user(db: Session, user):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Task CRUD
def create_task(db: Session, task, user_id: int):
    db_task = Task(**task.dict(), user_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session):
    return db.query(Task).join(User).all()

def update_task(db: Session, task_id: int, task):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    for key, value in task.dict().items():
        setattr(db_task, key, value)
    db.commit()
    return db_task

def delete_task(db: Session, task_id: int):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    db.delete(db_task)
    db.commit()
    return db_task