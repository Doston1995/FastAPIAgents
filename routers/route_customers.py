from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from db.session import get_db
from typing import List 
from db.schemas import CustomerShow, CustomerCreate
from db.repository import list_customers, create_customer, retreive_customer

router = APIRouter()


@router.get("/all", response_model=List[CustomerShow])
def get_all_customers(db:Session = Depends(get_db)):
    customers = list_customers(db=db)
    return customers


@router.post("/create/",response_model=CustomerShow)
def create_customers(customer: CustomerCreate, db: Session = Depends(get_db)):
    customer = create_customer(customer=customer, db=db)
    return customer


@router.get("/customer/{cust_code}",response_model=CustomerShow)
def read_customer(cust_code:str, db:Session = Depends(get_db)):
    customer = retreive_customer(cust_code=cust_code, db=db)
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Customer with this code {cust_code} does not exist")
    return customer