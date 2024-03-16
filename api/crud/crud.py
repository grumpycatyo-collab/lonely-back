from sqlalchemy.orm import Session

from . import schemas
from models import models

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_user_by_hobby(db: Session, hobby: str): #not tested
    return db.query(models.User).filter(models.User.hobby == hobby).first()

def get_users(db: Session, skip: int = 0, limit: int = 100): #not tested
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


