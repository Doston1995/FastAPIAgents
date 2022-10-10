from sqlalchemy.orm import Session
from db.models import CUSTOMER
from schemas.customer import CustomerCreate, CustomerShow


def list_customers(db : Session):
    customers = db.query(CUSTOMER).all()
    return customers


def create_customer(customer: CustomerCreate, db: Session):
    customer_object = CUSTOMER(**customer.dict())
    db.add(customer_object)
    db.commit()
    db.refresh(customer_object)
    return customer_object
    

def retreive_customer(cust_code:str, db:Session):
    customer = db.query(CUSTOMER).filter(CUSTOMER.CUST_CODE == cust_code).first()
    return customer


def update_customer(cust_code:str, customer: CustomerShow, db: Session):
    existing_customer = db.query(CUSTOMER).filter(CUSTOMER.CUST_CODE == cust_code)
    if not existing_customer.first():
        return 0
    existing_customer.update(customer.__dict__)
    db.commit()
    return 1


def delete_customer(cust_code:str, db: Session):
    existing_customer = db.query(CUSTOMER).filter(CUSTOMER.CUST_CODE == cust_code)
    if not existing_customer.first():
        return 0
    existing_customer.delete(synchronize_session=False)
    db.commit()
    return 1