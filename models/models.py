import datetime
from dependencies.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_type = Column(String) 
    hobby = Column(String)
    age = Column(Integer)
    location = Column(String)
    location_type = Column(String) 
    availability = Column(Boolean, default=True)

class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    activity_type = Column(String)  
    location = Column(String)
    time = Column(DateTime, default=datetime.datetime.utcnow)
    # user = relationship("User", back_populates="activities")