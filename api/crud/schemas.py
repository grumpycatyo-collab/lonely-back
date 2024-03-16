from pydantic import BaseModel
from typing import List
from datetime import datetime


class ActivityBase(BaseModel):
    title: str
    description: str
    location: str  # Make sure this line is included
    activity_type: str

class ActivityCreate(ActivityBase):
    pass


class Activity(ActivityBase):
    id: int
    location: str
    activity_type: str
    time: datetime

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    name: str
    user_type: str
    hobby: str
    age: int
    location: str
    location_type: str
    availability: bool


class UserCreate(BaseModel):
    name: str
    user_type: str
    hobby: str
    age: int
    location: str
    location_type: str
    availability: bool = True


class User(UserBase):
    id: int

    class Config:
        from_orm = True
