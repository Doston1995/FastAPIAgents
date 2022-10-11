from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from db.session import get_db
from typing import List 
from schemas.users import UserCreate, UserShow, UserUpdate, UserDelete
from db.repository.users import list_users, create_user, retreive_user, update_user, delete_user


router = APIRouter()


@router.get("/all", response_model=List[UserShow])
def get_all_users(db:Session = Depends(get_db)):
    users = list_users(db=db)
    return users


@router.post("/create/",response_model=UserShow)
def create_users(user: UserCreate, db: Session = Depends(get_db)):
    user = create_user(user=user, db=db)
    return user


@router.get("/user/{user_id}",response_model=UserShow)
def read_user(user_id:str, db:Session = Depends(get_db)):
    user = retreive_user(user_id=user_id, db=db)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with this id {user_id} does not exist")
    return user


@router.put("/update/{user_id}") 
def update_users(user_id:str, user: UserUpdate, db: Session = Depends(get_db)):
    message = update_user(user_id=user_id, user=user, db=db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {user_id} not found")
    return {"msg":"Successfully updated data."}


@router.delete("/delete/{user_id}")
def delete_users(user_id:str, db: Session = Depends(get_db)):
    user = retreive_user(user_id=user_id,db=db)
    if not user:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"User with this id {user_id} does not exist")
    if user:
        delete_user(user_id=user_id,db=db)
        return {"detail": "Successfully deleted."} 
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")