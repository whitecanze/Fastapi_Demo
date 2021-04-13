from hashing import Hash
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, status, Response, HTTPException
import schemas, database, models


def create_user(request: schemas.User, db: Session):
    new_user = models.User(name=request.name,email=request.email,password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def all(db: Session):
    users = db.query(models.User).all()
    return users

def get_user(id:int ,db:Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {id} not available")
    return user

def destroyAll(db:Session):
    user = db.query(models.User)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Not found user in list")
    user.delete(synchronize_session=False)
    db.commit()
    return 'done'