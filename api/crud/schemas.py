from pydantic import BaseModel
from typing import List


class ActivityBase(BaseModel):
    title: str
    description: str


class ActivityCreate(ActivityBase):
    pass


class Activity(ActivityBase):
    id: int
    user_id: int

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
        orm_mode = True
