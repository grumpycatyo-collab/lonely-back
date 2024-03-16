from sqlalchemy.orm import Session

from . import schemas
from models import models

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users_by_hobby(db: Session, hobby: str):
    return db.query(models.User).filter(models.User.hobby == hobby).all()   

def get_users(db: Session, skip: int = 0, limit: int = 100): #not tested
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Activity

def create_activity(db: Session, activity: schemas.ActivityCreate):
    db_activity = models.Activity(
        title=activity.title,
        description=activity.description,
        location=activity.location,
        activity_type=activity.activity_type
    )
    db.add(db_activity)
    db.commit()
    db.refresh(db_activity)
    return db_activity


def get_activities(db: Session, skip: int = 0, limit: int = 100): # not tested
    return db.query(models.Activity).offset(skip).limit(limit).all()


def get_activity_by_id(db: Session, activity_id: int): # not tested
    return db.query(models.Activity).filter(models.Activity.id == activity_id).first()


def get_recent_activities(db: Session, days: int = 7): # not tested
    import datetime
    week_ago = datetime.datetime.now() - datetime.timedelta(days=days)
    return db.query(models.Activity).filter(models.Activity.time >= week_ago).all()


