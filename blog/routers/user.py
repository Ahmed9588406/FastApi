from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas,database,models,hashing
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

get_db = database.get_db


@router.post("/")
def create_user(request:schemas.User,db:Session = Depends(get_db)):
    new_user = models.User(name = request.name, email = request.email,password = hashing.Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get("/",response_model=List[schemas.ShowUser])
def get_users(db:Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

@router.get("/{id}",response_model=schemas.ShowUser)
def get_user(id, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {id} not found")
    return user