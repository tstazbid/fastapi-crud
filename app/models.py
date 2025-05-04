from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    email = Column(String(100), unique=True)
    
    tasks = relationship("Task", back_populates="owner", cascade="all, delete")

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    description = Column(Text)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    
    owner = relationship("User", back_populates="tasks")