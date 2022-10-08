from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from db.session import get_db
from typing import List 
from db.schemas import CustomerShow
from db.repository import list_customers

router = APIRouter()


@router.get("/all", response_model=List[CustomerShow])
def get_all_customers(db:Session = Depends(get_db)):
    customers = list_customers(db=db)
    return customers