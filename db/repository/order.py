from sqlalchemy.orm import Session
from db.models import ORDER
from schemas.order import OrderCreate, OrderShow
import datetime, uuid


def list_orders(db : Session):
    orders = db.query(ORDER).all()
    return orders


def create_order(order: OrderCreate, db: Session):
    ord_date = str(datetime.datetime.now())
    order_object = ORDER(
                        ORD_NUM = order.ORD_NUM,
                        ORD_AMOUNT = order.ORD_AMOUNT,
                        ADVANCE_AMOUNT = order.ADVANCE_AMOUNT,
                        ORD_DATE = ord_date,
                        CUST_CODE = order.CUST_CODE,
                        AGENT_CODE = order.AGENT_CODE,
                        ORD_DESCRIPTION = order.ORD_DESCRIPTION
    )
    db.add(order_object)
    db.commit()
    db.refresh(order_object)
    return order_object
    

def retreive_order(ord_num:str, db:Session):
    order = db.query(ORDER).filter(ORDER.ORD_NUM == ord_num).first()
    return order


def update_order(ord_num:str, order: OrderShow, db: Session):
    existing_order = db.query(ORDER).filter(ORDER.ORD_NUM == ord_num)
    if not existing_order.first():
        return 0
    existing_order.update(order.__dict__)
    db.commit()
    return 1


def delete_order(ord_num:str, db: Session):
    existing_order = db.query(ORDER).filter(ORDER.ORD_NUM == ord_num)
    if not existing_order.first():
        return 0
    existing_order.delete(synchronize_session=False)
    db.commit()
    return 1