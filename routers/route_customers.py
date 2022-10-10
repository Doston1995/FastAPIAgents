from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from db.session import get_db
from typing import List 
from schemas.customer import CustomerShow, CustomerCreate
from db.repository.customer import list_customers, create_customer, retreive_customer, update_customer, delete_customer

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


@router.put("/update/{cust_code}") 
def update_customers(cust_code:str, customer: CustomerCreate, db: Session = Depends(get_db)):
    message = update_customer(cust_code=cust_code,customer=customer,db=db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Customer with id {cust_code} not found")
    return {"msg":"Successfully updated data."}


@router.delete("/delete/{cust_code}")
def delete_customers(cust_code:str, db: Session = Depends(get_db)):
    customer = retreive_customer(cust_code=cust_code,db=db)
    if not customer:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Customer with this code {cust_code} does not exist")
    if customer:
        delete_customer(cust_code=cust_code,db=db)
        return {"detail": "Successfully deleted."} 
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")