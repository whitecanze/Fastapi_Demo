from fastapi import APIRouter, Depends, status, Response, HTTPException
import schemas, database, oauth2
from sqlalchemy.orm import Session
from repository import user

router = APIRouter(
    prefix='/user',
    tags=['users']
)

get_db = database.get_db


@router.post('', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user.create_user(request, db)


@router.get('')
def all(db: Session = Depends(get_db)):
    return user.all(db)


@router.get('/{id}')
def get_user(id: int, db: Session = Depends(get_db)):
    return user.get_user(id,db)


@router.delete('', status_code=status.HTTP_204_NO_CONTENT)
def destroyAll(db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    return user.destroyAll(db)