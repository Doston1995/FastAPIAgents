from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from db.session import get_db
from typing import List 
from schemas.order import OrderShow, OrderCreate
from db.repository.order import list_orders, create_order, retreive_order, update_order, delete_order


router = APIRouter()


@router.get("/all", response_model=List[OrderShow])
def get_all_orders(db:Session = Depends(get_db)):
    orders = list_orders(db=db)
    return orders


@router.post("/create/",response_model=OrderShow)
def create_orders(order: OrderCreate, db: Session = Depends(get_db)):
    order = create_order(order=order, db=db)
    return order


@router.get("/customer/{ord_num}",response_model=OrderShow)
def read_customer(ord_num:str, db:Session = Depends(get_db)):
    order = retreive_order(ord_num=ord_num, db=db)
    if not order:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Order with this number {ord_num} does not exist")
    return order


@router.put("/update/{ord_num}") 
def update_orders(ord_num:str, order: OrderCreate, db: Session = Depends(get_db)):
    message = update_order(ord_num=ord_num,order=order,db=db)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Order with number {ord_num} not found")
    return {"msg":"Successfully updated data."}


@router.delete("/delete/{ord_num}")
def delete_orders(ord_num:str, db: Session = Depends(get_db)):
    order = retreive_order(ord_num=ord_num,db=db)
    if not order:
        return HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"Order with this number {ord_num} does not exist")
    if order:
        delete_order(ord_num=ord_num,db=db)
        return {"detail": "Successfully deleted."} 
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=f"You are not permitted!!!!")