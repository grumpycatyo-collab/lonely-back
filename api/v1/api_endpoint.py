import json
import logging as log
from sqlalchemy.orm import Session
from fastapi import APIRouter, HTTPException, Body, status, Depends, Query
from ..crud import crud, schemas
from models import models
from dependencies.database import SessionLocal, engine
from typing import List

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


log.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level='INFO')

router = APIRouter()

@router.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # db_user = crud.get_user_by_email(db, email=user.email)
    # if db_user:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)



@router.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.get("/users/", response_model=List[schemas.User])
def get_users_by_hobby_or_all(
    hobby: str = Query(None, alias="by_hobby"),  # Optional query parameter
    db: Session = Depends(get_db)
):
    if hobby:
        # If hobby query parameter is provided, fetch users by hobby
        return crud.get_users_by_hobby(db=db, hobby=hobby)
    else:
        # If no hobby query parameter is provided, fetch all users
        return crud.get_users(db=db)


# Endpoint to create an activity
@router.post("/activities/", response_model=schemas.Activity)
def create_activity(activity: schemas.ActivityCreate, db: Session = Depends(get_db)):
    return crud.create_activity(db=db, activity=activity)


# Endpoint to get all activities
@router.get("/activities/", response_model=List[schemas.Activity])
def read_activities(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    activities = crud.get_activities(db=db, skip=skip, limit=limit)
    return activities


# Endpoint to get an activity by ID
@router.get("/activities/{activity_id}", response_model=schemas.Activity)
def read_activity(activity_id: int, db: Session = Depends(get_db)):
    db_activity = crud.get_activity_by_id(db=db, activity_id=activity_id)
    if db_activity is None:
        raise HTTPException(status_code=404, detail="Activity not found")
    return db_activity


# Endpoint to get recent activities (within one week)
@router.get("/recent_activities/", response_model=List[schemas.Activity])
def read_recent_activities(db: Session = Depends(get_db)):
    recent_activities = crud.get_recent_activities(db=db)
    return recent_activities